from sklearn.model_selection import train_test_split
import shutil, pathlib

src = pathlib.Path('images/aug')
train_dir = pathlib.Path('data/train/pos')
val_dir = pathlib.Path('data/validation/pos')

files = list(src.glob('*'))
train_files, val_files = train_test_split(files, test_size=0.3, random_state=42)

for f in train_files:
    shutil.copy(f, train_dir / f.name)
for f in val_files:
    shutil.copy(f, val_dir / f.name)
