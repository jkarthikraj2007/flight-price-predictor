# flight-price-predictor
A Flight price predictor for Indian domestic flights built using Machine Learning 
# ✈️ Flight Price Predictor

A machine learning web app that predicts Indian domestic flight prices instantly.

🔗 **Live App:** https://flight-price-predictor-kig.streamlit.app/

## About
This app predicts flight ticket prices based on:
- Airline
- Source and destination city
- Departure and arrival time
- Number of stops
- Travel class (Economy / Business)
- Flight duration
- Days left to departure

## Tech Stack
- **Python** — core language
- **Pandas & NumPy** — data processing
- **Scikit-learn** — machine learning (Random Forest)
- **Streamlit** — web app framework
- **GitHub + Streamlit Cloud** — deployment

## Dataset
300,000+ real Indian domestic flight records from Kaggle (Shubham Bathwal).

## How to run locally
```bash
pip install -r requirements.txt
python train.py
streamlit run app.py
```

## Results
- Model: Random Forest Regressor
- Mean Absolute Error: ₹1,077