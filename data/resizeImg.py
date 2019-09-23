from glob import glob
from fastai import *
from fastai.vision import *
from PIL import Image
import os

fn_paths = glob('tamil_dataset_offline/usr_*/*.tiff')
fn_paths.extend(glob('tamil_dataset_offline/usr_*/*.png'))
fn_paths_lst = list(map(Path, fn_paths))

# Average resolution of the dataset is around 140x120
# Hence 128 looks like a decent number
basewidth = 128
for i in fn_paths_lst:
    img = Image.open(str(i))
    img = img.resize((basewidth, basewidth), PIL.Image.ANTIALIAS)

    if not os.path.exists(os.path.dirname('dataset_resized_final/' + str(i))):
        try:
            os.makedirs(os.path.dirname('dataset_resized_final/' + str(i)))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    
    img.save('dataset_resized_final/' + str(i) )

# print(avg_width//len(fn_paths_lst), avg_height//len(fn_paths_lst))
