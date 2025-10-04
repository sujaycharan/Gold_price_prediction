## Gold Price Prediction

## Overview

This project utilizes machine learning to predict gold prices using a **Random Forest Classifier**. By analyzing historical gold price data, the model forecasts future trends, offering valuable insights for investors and financial analysts.

## Dataset

The dataset used in this project is sourced from Kaggle:

* **Gold Price Data**: https://www.kaggle.com/datasets/altruistdelhite04/gold-price-data

This dataset includes multiple features such as SPX, GLD, USO, SLV, and EUR/USD, which are utilized to predict gold prices.

## Features

* **Data Collection**: Utilizes historical gold price data to train the model.
* **Modeling**: Implements a Random Forest Classifier for accurate predictions.
* **Evaluation**: Assesses model performance using appropriate metrics.
* **Visualization**: Provides visual representations of predictions versus actual prices.
* **Interactive UI**: Offers a simple frontend to input features and get gold price predictions.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/sujaycharan/Gold_price_prediction.git
cd Gold_price_prediction
pip install flask joblib numpy flask_cors
```

## Running the Project

1. **Start the backend Flask server**:

   ```bash
   python app.py
   ```

2. **Open the frontend** in your browser to provide input values and get gold price predictions. The frontend interacts with the backend API to display real-time predictions.

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License.

---

If you need further modifications or additions, feel free to let me know!
