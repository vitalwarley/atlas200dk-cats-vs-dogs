# atlas200dk-cats-vs-dogs

1. Save your tensorflow model (1.X) as `model.h5`
2. Make sure you have `model.h5` in the same folder as `freeze_model.py`. Execute: `python freeze_model.py`. You now have a new file: `model/model.pb`.
3. Convert the `.pb` model in MindStudio to `.om`.
4. Copy the converted model from `~/modelzoo` to `PROJECT/model/`.
5. Copy the project to Atlas 200DK: `TODO`.
6. Access Atlas 200DK: `TODO`.
7. Execute the following commands inside your project:

```
wget https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip
unzip -q kagglecatsanddogs_3367a.zip
```
You have now a folder named `PetImages`.

8. Execute: `python classify.py`

:)

