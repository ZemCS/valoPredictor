from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import pandas as pd
import time
import re

options = Options()
options.add_argument("--disable-gpu")

driver = webdriver.Edge(options=options)

url = 'https://www.vlr.gg/event/2094/champions-tour-2024-emea-stage-2' 

csvName = 'stage3_2024.csv'

driver.get(url)

time.sleep(2)

matchCount = driver.find_elements(By.CLASS_NAME, "wf-nav-item-title")

matchCount = matchCount[1].text

matches = re.search(r'\((\d+)\)', matchCount)

matchCount = int(matches.group(1))

print(f'Total Number of Matches for this Event: {matchCount}')
print()

matchButton = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/div/div[1]/div[2]/a[2]')

matchButton.click()

time.sleep(1)

allStagesURL = driver.find_element(By.XPATH, "//a[text() = 'All Stages']")

allStagesURL = allStagesURL.get_attribute("href")

driver.get(allStagesURL)

time.sleep(1)

matchesContainer = driver.find_elements(By.CLASS_NAME, 'wf-card')

matches = []

data = []

for match in matchesContainer:
    children = match.find_elements(By.XPATH, './*')
    for child in children:
        if child.tag_name == 'a':
            href = child.get_attribute('href')
            matches.append(href)

for i in range (matchCount):
    print(f'Collecting Data for Match {i+1}')
    print()
    driver.get(matches[i])

    time.sleep(1)

    if(driver.find_element(By.CLASS_NAME, 'match-header-event-series').text.strip() == 'Showmatch: Showmatch'):
        continue

    score1 = driver.find_element(By.CLASS_NAME, 'match-header-vs-score-winner').text.strip()
    score2 = driver.find_element(By.CLASS_NAME, 'match-header-vs-score-loser').text.strip()

    finalScore = int(score1) + int(score2)

    patch = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/div[3]/div[1]/div[1]/div[2]/div/div[3]/div').text
    patch = patch.split(' ')
    patch = patch[1]

    teams = driver.find_elements(By.CLASS_NAME, 'wf-title-med ')
    team1 = teams[0].text
    team2 = teams[1].text

    mapData = driver.find_elements(By.CSS_SELECTOR, 'div.vm-stats-gamesnav-item.js-map-switch')

    for j in range(int(finalScore)):
        for map in mapData:
            data_href = map.get_attribute('data-href')
            data_href = data_href.split('?')
            data_href = data_href[1]
            mapValue = data_href.split('=')[1]
            if mapValue == str(j + 1):
                map.click()
                gameID = map.get_attribute('data-game-id')
                time.sleep(1)
                game = driver.find_elements(By.CLASS_NAME, 'vm-stats-game ')
                for gameNo in game:
                    mapID = gameNo.get_attribute('data-game-id')
                    if mapID == gameID:
                        mapName = map.find_element(By.CSS_SELECTOR, 'div[style="margin-bottom: 2px; text-align: center; line-height: 1.5;"]')
                        mapName = mapName.text
                        mapName = mapName.split(' ')
                        mapName = mapName[1]
                        mapScores = gameNo.find_elements(By.CSS_SELECTOR, 'div.team .score')
                        team1Score = mapScores[0].text.strip()
                        team2Score = mapScores[1].text.strip()
                        agentPicks = gameNo.find_elements(By.CSS_SELECTOR, 'span.stats-sq.mod-agent.small')
                        agentsPicked = []
                        for agentPick in agentPicks:
                            agentName = agentPick.find_element(By.TAG_NAME, 'img')
                            agentName = agentName.get_attribute('title')
                            agentsPicked.append(agentName)
                data.append([patch, team1, team2, mapName, team1Score, team2Score] + agentsPicked)
                time.sleep(1)

time.sleep(1)

driver.quit()

df = pd.DataFrame(data, columns=['patchID', 'team1_Name', 'team2_Name', 'mapName', 'team1Score', 'team2Score',
                                  'agent1', 'agent2', 'agent3','agent4', 'agent5', 
                                  'agent6', 'agent7', 'agent8', 'agent9','agent10'])

df.to_csv(csvName, index=False)