import pandas as pd
import shutil
import os

def read_csv(csv_file, img_dir):
    df = pd.read_csv(csv_file)
    data_seg = csv_file.split('\\')[-1].split('.')[0]
    data_dir = os.path.join(img_dir, data_seg)
    os.makedirs(data_dir, exist_ok=True)
    return df, data_seg

def move_images(df, img_dir, data_seg):
    for label in df.label.unique():
        label_dir = os.path.join(img_dir, data_seg, str(label))
        os.makedirs(label_dir, exist_ok=True)
        result = df[df.label == label]
        for i in range(len(result)):
            img_id = result.iloc[i, 4].split('/')[-1]
            source = os.path.join(img_dir, img_id)
            shutil.copy(source, label_dir)

def main():
    train_file = r"C:\Users\srish\Hackathon\train.csv"
    test_file = r"C:\Users\srish\Hackathon\test.csv"
    img_dir = r"C:\Users\srish\Hackathon\train_test_data"
    for file in [train_file, test_file]:
        df, data_seg = read_csv(file, img_dir)
        if data_seg == 'train':
            move_images(df, img_dir, data_seg)
        else:
            dest = os.path.join(img_dir, data_seg)
            for i in range(len(df)):
                img_id = df.iloc[i, 3].split('/')[-1]
                source = os.path.join(img_dir, img_id)
                shutil.copy(source, dest)

if __name__ == '__main__':
    main()

