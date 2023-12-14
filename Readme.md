# Telegram Folder Monitor & Uploader

This Python script is designed to monitor a specified folder for file changes and automatically upload new files to a Telegram channel using the Telegram Bot API. It utilizes the `watchdog` library to detect file system events and the `tqdm` library to display a progress bar during file uploads.

## Features

- Monitors a designated folder for file changes.
- Automatically uploads new files to a Telegram channel using a Telegram bot.
- Notifies the channel with file details such as file name and folder path.

## Prerequisites

Before running the script, ensure you have:

- Python 3 installed.
- Required Python packages installed:
  - `watchdog`
  - `tqdm`
  - `python-telegram-bot`

## Setup

1. Clone or download this repository to your local machine.
2. Install the necessary Python packages:

   ```bash
   pip install watchdog tqdm python-telegram-bot
   ```

3. Obtain a Telegram Bot token from the BotFather on Telegram and replace `'YOUR_BOT_TOKEN'` in the script with your token.
4. Set up a Telegram channel and obtain the channel ID (`chat_id`). Replace `'YOUR_CHANNEL_ID'` in the script with your channel ID.

## Usage

1. Run the script.
2. Enter the folder location when prompted. This folder will be monitored for changes.
3. The bot will start monitoring the specified folder and upload any new files to the designated Telegram channel.

## Important Notes

- Ensure that the bot has permission to post in the designated Telegram channel.
- Make sure to handle exceptions and errors related to file uploads or Telegram API limitations.

## Author

Your Name

## License

This project is licensed under the [MIT License](LICENSE).
