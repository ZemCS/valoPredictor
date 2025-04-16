# ValoPredictor

ValoPredictor is a machine learning project designed to predict the winning probability of VALORANT matches between two teams based on historical and current match data. The project leverages web scraping with Selenium, multiple machine learning and deep learning models, and Power BI for exploratory data analysis and visualization.

## Project Overview

The project processes VALORANT match data, including team names, agent compositions, map names, and match outcomes, to train predictive models. The data is preprocessed, encoded, and used to train models such as Linear Regression, Logistic Regression, Random Forest, Support Vector Machine (SVM), and Artificial Neural Network (ANN). The best-performing model is used to predict match outcomes, with results visualized in Power BI.

## Features

- **Web Scraping**: Utilizes Selenium to scrape VALORANT match data from relevant sources.
- **Data Preprocessing**: Handles missing values, duplicates, and encodes categorical variables (teams, agents, maps).
- **Machine Learning Models**:
  - Multiple Linear Regression
  - Logistic Regression
  - Random Forest Classifier
  - Support Vector Machine (SVM)
  - Artificial Neural Network (ANN)
- **Model Evaluation**: Computes metrics like Mean Squared Error (MSE), accuracy, and winning probability.
- **Visualization**: Uses Power BI for exploratory data analysis and result visualization.
- **Prediction**: Predicts the winning team and probability for a given match based on year, teams, and map.

## Dataset

The dataset (`vlrDataset.csv`) contains VALORANT match data with the following key columns:
- `team1_Name`, `team2_Name`: Names of the competing teams.
- `agent1` to `agent10`: Agents used by players in the match.
- `mapName`: The map played in the match.
- `team1Score`, `team2Score`: Scores of the respective teams.
- `patchID`: Game patch version for temporal context.

The processed dataset (`processedVLRDataset.csv`) includes encoded features and additional columns like `year`, `team1Win`, `team1Agents`, and `team2Agents`.

## Requirements

To run the project, install the following Python packages:

```bash
pip install numpy pandas scikit-learn tensorflow selenium
```

Additionally, you need:
- **Selenium WebDriver**: Compatible with your browser (e.g., ChromeDriver for Google Chrome).
- **Power BI**: For data visualization and exploratory data analysis.
- **Python 3.8+**: Recommended for compatibility with all libraries.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ValoPredictor.git
   cd ValoPredictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Selenium WebDriver:
   - Download the appropriate WebDriver for your browser (e.g., [ChromeDriver](https://sites.google.com/chromium.org/driver/)).
   - Ensure the WebDriver executable is in your system PATH or specify its location in the code.

4. Download or prepare the dataset:
   - Place `vlrDataset.csv` in the `datasets/` directory.
   - Alternatively, run the web scraping script (if provided) to generate the dataset.

## Usage

1. **Data Preprocessing**:
   - Run the preprocessing script to clean and encode the dataset:
     ```bash
     python preprocess.py
     ```
   - This generates `processedVLRDataset.csv` in the `datasets/` directory.

2. **Model Training and Prediction**:
   - Run the main script to train models and predict outcomes:
     ```bash
     python main.py
     ```
   - Modify `test_year`, `test_team1`, `test_team2`, and `test_map` in the script to predict for specific matches.

3. **Visualization**:
   - Open Power BI and import the processed dataset or model outputs for exploratory data analysis.
   - Use provided Power BI templates (if available) for visualizations.

## Project Structure

```
ValoPredictor/
├── datasets/
│   ├── vlrDataset.csv
│   ├── processedVLRDataset.csv
├── preprocess.py
├── main.py
├── requirements.txt
├── README.md
```

- `datasets/`: Stores raw and processed datasets.
- `preprocess.py`: Script for data cleaning, encoding, and preprocessing.
- `main.py`: Main script for training models and making predictions.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation.

## Model Performance

The project evaluates models based on:
- **Mean Squared Error (MSE)**: For regression models.
- **Accuracy**: Percentage of correct predictions.
- **Winning Probability**: Probability of the predicted team winning (for applicable models).

Results are printed in the console and can be visualized in Power BI.

## Limitations

- **Data Dependency**: Predictions rely on the quality and completeness of the scraped dataset.
- **Feature Scope**: Current features include team names, agents, maps, and year. Additional features (e.g., player stats) could improve accuracy.
- **Model Generalization**: Models are trained on year-specific data, which may limit performance for new or unseen teams/maps.
- **Web Scraping**: Selenium-based scraping may break if the target website's structure changes.

## Future Improvements

- Incorporate player-specific statistics (e.g., KDA, economy).
- Add real-time data scraping for up-to-date predictions.
- Experiment with advanced deep learning architectures (e.g., LSTMs, Transformers).
- Enhance Power BI dashboards with interactive features.
- Deploy the model as a web application for user-friendly predictions.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

Please ensure your code follows the project's coding standards and includes appropriate documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please open an issue on GitHub or contact the project maintainer at [your-email@example.com].
