# HapTile

HapTile is a dataset of robot manipulation demonstrations with tactile sensing, robot actions, langauge instructions and visual demonstrations. The dataset is hosted on [Hugging Face](https://huggingface.co/datasets/HapTile2026/HapTile).

## Quickstart

### 1. Clone this repository

```bash
git clone https://github.com/HapTile-dataset/Dataset_quickstart.git
cd Dataset_quickstart
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the quickstart script

```bash
python quickstart.py --task fold_Tshirt.zip --frame 150
```

This downloads the default task (`fold_Tshirt`) from Hugging Face, extracts it to `haptile_data` folder, and displays the front camera, wrist camera, tactile frame, and action curves for a single frame.

### Options

| Argument | Default | Description |
|---|---|---|
| `--task` | `fold_Tshirt.zip` | Task zip to download from the dataset |
| `--frame` | `150` | Frame index to visualise |

`--task` can be one of the following:

- fold: `fold_Tshirt.zip`
- insert: `insert_peg.zip`
- move: `move_cable.zip`, `move_can.zip`, `move_disposable_cup.zip`, `move_mobile_box.zip`, `move_plush_toy.zip`, `move_rubiks_cube.zip`, `move_spoon.zip`, `move_toy_car.zip`, `move_water_bottle.zip`
- press: `press_Coffee_machine.zip`
- put: `put_Apple.zip`, `put_Banana.zip`, `put_baseball.zip`, `put_fork.zip`, `put_golf_ball.zip`, `put_lego.zip`, `put_Orange.zip`, `put_spatula.zip`, `put_sponge.zip`, `put_spoon.zip`, `put_spray_bottle.zip`, `put_stack_glass_cups.zip`, `put_strawberry.zip`
- remove: `remove_cloth.zip`, `remove_laundry_pod.zip`, `remove_screwdriver.zip`, `remove_sticky_note.zip`, `remove_sugar_bag.zip`, `remove_tissue.zip`
- stack: `stack_bowls.zip`, `stack_disposable_cup.zip`, `stack_glass_cups.zip`
- turn: `turn_can.zip`, `turn_cleanser_bottle.zip`, `turn_water_bottle.zip`
- wipe: `wipe_whiteboard.zip`

**Example:**
```bash
python quickstart.py --task fold_Tshirt.zip --frame 100
```

## Data

Data is downloaded automatically from Hugging Face at runtime. No manual download is required.
