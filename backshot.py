from telegram import Bot
import os
import asyncio
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tqdm import tqdm

# Your Telegram bot token
TOKEN = '5848128640:AAEgnZt4qBUX0uRqHkZpX7AElIb9SnFmo4s'

# Your chat ID (e.g., group, channel)
# chat_id = '-1002043845078'
chat_id = '-1001964591267'


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to send files to the channel
async def backup_files(bot, folder_path):
    logging.info(f"Looking for files to upload in folder: {os.path.basename(folder_path)}")
    files_to_upload = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    total_files = len(files_to_upload)
    uploaded_files = 0

    with tqdm(total=total_files, desc="Uploading files", unit="file") as pbar:
        for file_name in files_to_upload:
            file_path = os.path.join(folder_path, file_name)
            logging.info(f"Uploading: {file_name}")  # Show which file is being uploaded
            with open(file_path, 'rb') as file:
                try:
                    caption = f"From folder: {os.path.basename(folder_path)}\nFile: {file_name}"
                    await bot.send_document(chat_id=chat_id, document=file, caption=caption)
                    logging.info(f"Uploaded: {file_name}")  # Display once file upload is complete
                    pbar.update(1)
                    uploaded_files += 1
                except Exception as e:
                    logging.error(f"Error uploading {file_name}: {str(e)}")
                    pbar.update(1)

    # Check if all files have been uploaded
    if uploaded_files == total_files:
        logging.info("All files uploaded. Shutting down.")
        await asyncio.sleep(60)  # Wait for 60 seconds before shutting down
        raise SystemExit  # Gracefully exit the script

# Watchdog event handler for file changes
class FolderMonitor(FileSystemEventHandler):
    def __init__(self, bot, folder_path):
        super().__init__()
        self.bot = bot
        self.folder_path = folder_path

    async def on_created(self, event):
        if not event.is_directory:
            logging.info("File created event detected.")
            file_path = event.src_path
            with open(file_path, 'rb') as file:
                await backup_files(self.bot, self.folder_path)

async def main():
    bot = Bot(TOKEN)
    folder_path = input("Enter the folder location: ")  # Prompt user for folder location

    logging.info("Bot started.")
    await backup_files(bot, folder_path)  # Upload existing files initially

    observer = Observer()
    event_handler = FolderMonitor(bot, folder_path)
    observer.schedule(event_handler, path=folder_path)
    observer.start()

    try:
        while True:
            logging.info("Checking for changes...")
            await asyncio.sleep(60)  # Check every 60 seconds for file changes
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Bot stopped.")

    observer.join()

if __name__ == '__main__':
    asyncio.run(main())
