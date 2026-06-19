# HapTile

HapTile is a dataset of robot manipulation demonstrations with tactile sensing. The dataset is hosted on [Hugging Face](https://huggingface.co/datasets/HapTile2026/HapTile).

## Quickstart

### 1. Clone this repository

```bash
git clone https://github.com/your-org/haptile
cd haptile
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the quickstart script

```bash
python quickstart.py
```

This downloads the default task (`fold_Tshirt`) from Hugging Face, extracts it, and displays the front camera, wrist camera, tactile frame, and action curves for a single frame.

### Options

| Argument | Default | Description |
|---|---|---|
| `--task` | `fold_Tshirt.zip` | Task zip to download from the dataset |
| `--frame` | `50` | Frame index to visualise |

**Example:**
```bash
python quickstart.py --task fold_Tshirt.zip --frame 100
```

## Data

Data is downloaded automatically from Hugging Face at runtime. No manual download is required.
