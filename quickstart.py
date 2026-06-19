"""
HapTile quick start.

Downloads one task zip from the Hugging Face dataset, unzips it, opens the
first demo's trajectory.h5, and displays the front camera, wrist camera,
a tactile frame, and the action (control) curves.

Requires: huggingface_hub, h5py, opencv-python, matplotlib, numpy
"""

import zipfile
import tempfile
from pathlib import Path

import cv2
import h5py
import numpy as np
import matplotlib.pyplot as plt
from huggingface_hub import hf_hub_download
import argparse


REPO_ID = "HapTile2026/HapTile"

task_name = "fold_Tshirt.zip" # task to download from the dataset
frame_num = 150  # default frame index to visualise

parser = argparse.ArgumentParser(description="HapTile quick start")
parser.add_argument("--task", type = str, default= task_name)
parser.add_argument("--frame", type= int, default = frame_num)
args = parser.parse_args()

# 1. Download + unzip ---------------------------------------------------
zip_path = hf_hub_download(repo_id=REPO_ID, repo_type="dataset", filename=f"Data/{args.task}")
extract_dir = Path("haptile_data") / Path(args.task).stem
with zipfile.ZipFile(zip_path) as zf:
    zf.extractall(extract_dir)

# 2. Pick a demo ----------------------------------------------------------
demo_dir = sorted(d for d in extract_dir.iterdir() if d.is_dir())[0]
h5_path = demo_dir / "trajectory.h5"

# 3. Read modalities --------------------------------------------------------
def decode_frame(video_bytes: np.ndarray, frame_idx: int) -> np.ndarray:
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as tmp:
        tmp.write(video_bytes.tobytes())
        cap = cv2.VideoCapture(tmp.name)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    ok, bgr = cap.read()
    cap.release()
    return cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

with h5py.File(h5_path, "r") as f:
    front   = decode_frame(f["videos/base_camera_rgb_1"][()], args.frame)
    wrist   = decode_frame(f["videos/base_camera_rgb_0"][()], args.frame)
    tactile = decode_frame(f["videos/tactile_left_rgb"][()], args.frame)
    control = f["frames/control"][()]  # dims 0-5: 6-DOF delta pose, dim 6: gripper
    instruction = f["language_instruction"][()].decode("utf-8") if "language_instruction" in f else None
# 4. Visualise ----------------------------------------------------------
fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for ax, img, title in zip(axes, [front, wrist, tactile], ["Front camera", "Wrist camera", "Tactile (left)"]):
    ax.imshow(img)
    ax.set_title(title)
    ax.axis("off")

axes[3].plot(control[:, :6], linewidth=1.5)
axes[3].plot(control[:, 6], linewidth=2, color="black", linestyle="--", label="gripper")
axes[3].axvline(args.frame, color="red", linestyle=":")
axes[3].set_title("Action (control)")
axes[3].set_xlabel("Frame")
axes[3].legend(fontsize=7)

print(f"Language instruction: {instruction}")

fig.tight_layout()
plt.show()
