#!/bin/sh
# develop env initialize shell
### install pyenv
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile

# install python3.5.2 by pyenv
pyenv install 3.5.2
pyenv global 3.5.2
pip install -U pip
