# Smart Gen Machine Learning (CAC_23)
Smart Gen ML is a web application designed to help users reduce energy usage in thier home by informing them of their energy generation and usage.

# How it works
The app contains three pages: Dashboard, Optimization, and Comparison

* Dashboard: Users can see their daily energy usage and consumption statistics, which can inform them to make better energy usage decisions. LightGBM Gradient-boosting Decision Trees make regression predictions to help the user see predicted energy usage.
* Optimization: Users can see their energy usage breakdown by appliance to optimize consumption. The OpenAI GPT 3.5 Turbo is used to generate energy saving recommendations tailored to the user based on their energy usage distribution.
* Comparison: Users can see a prediction of how much energy they would save if following GPT recommendations and monitoring energy usage. Statistics are used to encourage the user to continue being mindful of their energy consumption.

# How to deploy application

# Task-Manager-With-Slimes

Pre-requisites:
- Git
- Python 3.x

How to import app:
- Open up terminal
- Go to the chosen directory where you want the project located
- Enter in terminal: git clone https://github.com/cranatic101/cac_23
- Open up your project in a code editor

How to set up virtual environment (in code editor):
- Enter in terminal: (Windows) python -m venv venv, (Mac) python3 -m venv venv
- Enter in terminal: (Windows) venv/Scripts/activate, (Mac) venv/bin/activate
- Make sure that your code editor has selected the venv python interpreter

How to set up .env (in code editor):
- create a file called .env
- Copy and paste the following into .env:

OPENAI_API_KEY = <<add your OpenAI GPT API Key here>>

How to install requirements:
- Enter in terminal: pip install -r requirements.txt

To run app:
- Enter in terminal: (Windows) python app.py, (Mac) python3 app.py