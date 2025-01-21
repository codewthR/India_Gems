# India Gems.com

This is a proof of concept for an AI-powered Travel Guide Website. The goal of this project is to explore the use of AI for visit beautiful places in India. This project is for **educational** purposes only .

This system provides you attractive user interface and  :

1. Valuation Agent - Calculates the intrinsic value of a stock and generates trading signals
2. Sentiment Agent - Analyzes market sentiment and generates trading signals
3. Fundamentals Agent - Analyzes fundamental data and generates trading signals
4. Technical Analyst - Analyzes technical indicators and generates trading signals
5. Risk Manager - Calculates risk metrics and sets position limits
6. Portfolio Manager - Makes final trading decisions and generates orders

Note: the system simulates trading decisions, it does not actually trade.

## Disclaimer

This project is for **educational and research purposes only**.

- No warranties or guarantees provided
- Past performance does not indicate future results
- This not gives you accurate data

By using this software, you agree to use it solely for learning purposes.

## Table of Contents
- [Setup](#setup)
- [Usage](#usage)
  - [Running the Project](#running-the-hedge-fund)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Feature Requests](#feature-requests)

## Setup

Clone the repository:
```bash
git clone https://github.com/virattt/ai-hedge-fund.git
cd ai-hedge-fund
```

1. Install Poetry (if not already installed):
```bash
pip install django
```

2. Set up your environment variables:
```bash
# Create .env file for your API keys
cp .env.example .env
```
**Important**: You must to set the OpenAI API key for the hedge fund to work.

Financial data for AAPL, GOOGL, MSFT, NVDA, and TSLA is free and does not require an API key.

For any other ticker, you will need to set the `FINANCIAL_DATASETS_API_KEY` in the .env file.

## Usage

### Running the Hedge Fund
```bash
python manage.py runserver 8001 (Port address )
```

**Example Output:**
<img width="992" alt="Screenshot 2025-01-06 at 5 50 17 PM" src="https://github.com/user-attachments/assets/e8ca04bf-9989-4a7d-a8b4-34e04666663b" />

**Example Output:**
<img width="941" alt="Screenshot 2025-01-06 at 5 47 52 PM" src="https://github.com/user-attachments/assets/00e794ea-8628-44e6-9a84-8f8a31ad3b47" />

## Project Structure 
```
Ecommrce/
├── Ecommerce/
│   ├── Detils_all/                 
│   │   ├── templates
|   |       ├── datasend.html      
│   │   ├── models.py  
│   │   ├── urls.py       
│   │   ├── views.py.py        
│   │   ├── admin.py        
│   ├── Ecommerce                   
│   │   ├── settings.py
|   |   ├── urls.py
|   |   ├── Views.py        
│   ├── Media
│   ├── Static/admin
|   |   ├──Css
|   |   ├──img
|   |   ├──Java script
├   ├── Sign_up_in
|   |   ├── models.py
|   |   ├── views.py
|   |   ├── urls.py
|   ├── templates
|   |   ├── index.html
|   ├── manage.py
...
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

**Important**: Please keep your pull requests small and focused.  This will make it easier to review and merge.

## Feature Requests

If you have a feature request, please open an [issue]() and make it is tagged with `enhancement`.

