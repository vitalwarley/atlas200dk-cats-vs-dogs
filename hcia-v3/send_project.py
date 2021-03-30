"""
File: send_project.py
Author: yourname
Email: yourname@email.com
Github: https://github.com/yourname
Description: this script makes it easir to update the project in Altas 200DK.
"""
import os
import argparse
from paramiko import SSHClient
from scp import SCPClient
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument(
    "--to-device",
    type=str,
    help="option to control to which device send project",
    choices=["vm", "atlas"],
    default="atlas",
)
parser.add_argument(
    "--execute",
    help="option to control if we want to send and remote execute project",
    action="store_true",
)

args = parser.parse_args()

if args.to_device == "atlas":
    DEVICE = "ATLAS"
else:
    DEVICE = "ASCEND_VM"

HOSTNAME = os.getenv(DEVICE + "_HOSTNAME")
PORT = int(os.getenv(DEVICE + "_PORT"))
USERNAME = os.getenv(DEVICE + "_USERNAME")
PASSWORD = os.getenv(DEVICE + "_PASSWORD")
SOURCES = ["src", "atlas_utils", "samples", "send_project.py", ".env", "model"]

REMOTE_PATH = "~/AscendProjects/ImageClassification"

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect(HOSTNAME, PORT, USERNAME, PASSWORD)

with SCPClient(ssh.get_transport()) as scp:
    for src in SOURCES:
        scp.put(src, remote_path=REMOTE_PATH, recursive=True)

if args.execute:
    chan = ssh.invoke_shell()
    chan.send(f"python3.6 {REMOTE_PATH}/src/main.py")

    with SCPClient(ssh.get_transport()) as scp:
        for src in SOURCES:
            scp.get(os.path.join(REMOTE_PATH, 'outputs'), recursive=True)
