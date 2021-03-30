import os

def filter_images(folder='PetImages'):
    num_skipped = 0
    for folder_name in ("Cat", "Dog"):
        folder_path = os.path.join(folder, folder_name)
        for fname in os.listdir(folder_path):
            fpath = os.path.join(folder_path, fname)
            try:
                fobj = open(fpath, 'rb')
                is_jfif = b'JFIF' in fobj.peek(10)
            finally:
                fobj.close()

            if not is_jfif:
                num_skipped += 1
                os.remove(fpath)

    print('Deleted {} images'.format(num_skipped))


if __name__ == "__main__":
    filter_images()
