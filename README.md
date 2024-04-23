# Google Sheets Excel Integration Tool

This Python application automates the transfer of data from local Excel files into a Google Sheets document, creating a new sheet for each Excel file.

## Features

- Authenticate with Google using OAuth 2.0.
- Read data from local Excel files.
- Create a new sheet for each Excel file in a specified Google Sheets document.
- Automatically populate Google Sheets with data from Excel.

## Prerequisites

Before you can run this application, you will need:
- Python 3.6 or later.
- Pip for installing dependencies.
- Access to a Google account with permission to manage Google Sheets.

## Installation

1. **Clone the Repository**
   ```
   git clone https://github.com/yourusername/google-sheets-excel-integration.git
   cd google-sheets-excel-integration
   ```

2. **Install Required Libraries**
   ```
   pip install -r requirements.txt
   ```

3. **Google API Credentials**
   - You must have `credentials.json` from Google Cloud Console in the project root directory to authenticate. See the section below on obtaining or replacing this file.

## Configuration

### Setting Up Google API Credentials
To authenticate and interact with Google Sheets, you'll need credentials from Google:

1. **Create a Project in Google Cloud Console**: Visit [Google Cloud Console](https://console.developers.google.com/).
2. **Enable the Google Sheets API**: In your Google Cloud project, enable the Sheets API.
3. **Create OAuth 2.0 Credentials**: Create credentials for a Desktop application and download the `credentials.json` file.

### Using Your Own `credentials.json`
If you need to use your own `credentials.json`:

1. Obtain your `credentials.json` file by following the steps above in "Setting Up Google API Credentials".
2. Replace the existing `credentials.json` in the project root directory with your own file.

## Running the Application

To run the application, execute the following command in the terminal:
```
python main.py
```

You will be prompted to authenticate via a browser window when running the script for the first time. Once authenticated, you'll need to input the ID of the Google Sheets document where the data will be written.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
