# atlas200dk-cats-vs-dogs

1 - Install requirements.txt in python 3.7 or less, if you don't have this version, you can install it with pyenv running the following commands:

```bash

# Linux

curl https://pyenv.run | bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Windows

pyenv-win
```
Then, restart the terminal and then run:
```bash
pyenv install 3.7.2
pyenv global 3.7.2
```

You are now using python 3.7.2. Confirm by typing: `python --version`. To go back into your default version type: `pyenv global <your-default-python-version>`

Alternatively, you can use `virtualenv` and `virtualenvwrapper`:

```bash
pip install --user virtualenv virtualenvwrapper
mkvirtualenv -p <python3.7 path> atlas200
workon atlas200 # if it isn't already activated
```

2 - Install the dependencies running the following command:
```bash
python -m pip install -r requirements.txt
```

3 - Execute the following commands inside your project:

```bash
wget https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip
unzip -q kagglecatsanddogs_3367a.zip
```
You have now a folder named `PetImages`.

4 - Filter corrupted images: `python3 filter_corruped_images.py`

5 - Create your model using tensorflow or keras. the model must be configured to receive images with a resolution of 180x180

6 - Save your tensorflow model (1.X) as `model.h5`

7 - Make sure you have `model.h5` in the same folder as `freeze_model.py`. Execute: `python3 freeze_model.py`. You now have a new file: `model/model.pb`.

8 - Convert the `.pb` model in MindStudio to `.om`.

9 - Copy the converted model from `~/modelzoo` to `PROJECT/model/`.

10 - Copy the project to Atlas 200DK: `TODO`.

11 - Access Atlas 200DK: `TODO`.

12 - Execute: `python3 classify.py`

:)
