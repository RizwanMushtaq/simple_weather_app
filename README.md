# Simple Weather App

A tiny command-line Python application that fetches current weather data for a city using the OpenWeatherMap API.

## Features

- Prompt for a city name and show current conditions
- Displays temperature (°C), "feels like" temperature, and a short description

## Requirements

- Python 3.8 or newer
- See `requirements.txt` for Python dependencies (`requests`, `python-dotenv`)

## Setup

1. Create and activate a virtual environment:
   - Windows (PowerShell):

     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```

   - macOS / Linux:

     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root containing your OpenWeatherMap API key:

   ```text
   API_KEY=your_openweathermap_api_key_here
   ```

   Get a free API key at: https://openweathermap.org/api

## Usage

Run the script and follow the prompt to enter a city name:

```bash
python weather.py
```

Example:

- Input: `London`
- Output: current temperature, feels like, and weather description for London

## File(s)

- `weather.py`: main script that queries the OpenWeatherMap API and prints results

## Notes

- This project is intentionally minimal for learning purposes. Error handling is basic—improvements (input validation, better API error handling, unit tests) can be added as follow-ups.

## Contributing

Contributions are welcome — open an issue or submit a pull request.
