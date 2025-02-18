


# Stock Notifier Telegram Bot

This project is a Telegram bot for stock notifications, designed to notify users about stock prices and key market changes.

## Requirements

- Python 3.12 (or compatible versions)
- Conda or a virtual environment for dependency management

## Setup Instructions

### 1. Create a Conda Environment

First, create a new Conda environment with Python 3.12:

```bash
conda create -n diploma_tg_bot python=3.12
```
### 2. Activate the Conda Environment

Activate the newly created environment:

```bash
conda activate diploma_tg_bot
```

### 3. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/damirbeybitov/stock_notifier_telegram_bot
```

### 4. Navigate to the Project Directory

Move into the project directory:

```bash
cd stock_notifier_telegram_bot
```

### 5. Install Dependencies

Once inside the project folder, install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, generate it with the following command (this is typically done after the environment is set up):

```bash
pip freeze > requirements.txt
```

### 6. Commit Changes (If Applicable)

If you've made any changes, you can commit them using:

```bash
git commit -a -m "Your commit message"
```

### 7. Push Changes to GitHub

After committing your changes, push them to the remote repository:

```bash
git push origin main
```

## Usage

Once everything is set up, follow the instructions specific to the bot to start it and configure notifications.

---

### Notes

- Ensure that you have the necessary environment variables configured, like API keys or bot credentials.
- If you need to modify the notification logic, feel free to adjust the code within the bot's core files.

## License

This project is licensed under the MIT License.
