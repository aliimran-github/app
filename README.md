# cara setup token
- buat bot baru di tele @fatherbot

  ![alt text](docs/images/image.png)
  ![alt text](docs/images/image-1.png)
- buat file .env dan masukan token bot api telegram
  ```py
  export BOT_TOKEN=<token>
  ```

# setup
## with venv pyenv
```bash
# setup
curl https://pyenv.run | bash

cat >> ~/.bashrc << 'EOF'
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
EOF

echo 'eval "\$(pyenv virtualenv-init -)' > ~/.bashrc
exec $SHELL
pyenv install 3.12.8
pyenv global 3.12.8

git clone https://github.com/ariafatah0711/bot_pentest_suggest
cd bot_pentest_suggest
# pyenv virtualenv 3.12.8 venvs
# pyenv local venv
python3 -m venv venv
pip3 install -r req.txt
chmod +x main.py

```

## with venv default
```bash
# with python3
git clone https://github.com/ariafatah0711/bot_pentest_suggest
cd bot_pentest_suggest
python3 -m venv venv
venv/bin/pip3 install -r req.txt
chmod +x main.py
```

# run
```bash
# run
./main.py

# remove __pycache__
find . -name "__pycache__" -o -name "*.pyc" | xargs rm -rf

# remove log
rm -rf log/*
```