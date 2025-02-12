conda create -n diploma_tg_bot python=3.12
conda activate diploma_tg_bot

git clone https://github.com/damirbeybitov/stock_notifier_telegram_bot
git commit -a -m ""
git push origin main

pip freeze > requirements.txt
pip install -r requirements.txt
