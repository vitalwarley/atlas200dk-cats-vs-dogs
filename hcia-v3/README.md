# Atlas 200DK -- HCIA-v3

WIP.

## Model Training and Preparation

- Download [dataset](https://drive.google.com/file/d/1srPeSkbkKSSdB97UUDLNxOFI-7Tv5MJ1/view?usp=sharing).
- Train a Keras model with it. Input shape should be `(256, 224)`.
- Save the trained model as an `.h5`.
- Convert model to `.pb` using `freeze_model.py` 
  - `python freeze_model.py <model_path>`. You must have the latest TensorFlow installed.
  - Look if you now have new directory with the frozen model: `model/model.pb`.

## VM Access

- Install tigervnc or anyother VNC Viewer.
- Create an ssh tunnel to VNC server using: `ssh -p 8035 ascend@200.17.112.26 -C -L 5901:127.0.0.1:5901`
- Start the VNC client and connect it to `localhost:5901`

## MindStudio & Project Deployment

- Open MindStudio via terminal: `./MindStudio/bin/MindStudio.sh`
- Create a new project: `File > New > Project > Ascend App > Next > Empty Acl Project > Finish.`
  - Name your project in `Ascend App`step.
- Clone this repository inside the new project.
  - You can delete all other non-IDE files.
- Download your `model.pb` and put it into `<ProjectName>/model/`
- Execute: `python3.7.5 send_project.py --to-device atlas --execute`
  - This needs the `.env` file. I will share it at the time of deployment.
- Checkout the results in `outputs`!
