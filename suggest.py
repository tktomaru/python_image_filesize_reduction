import os
import shutil
from collections import defaultdict

# フォルダパス
source_folder = 'resized_images'
destination_folder = 'suggest'

# suggestフォルダが存在しない場合は作成
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# resized_imagesフォルダ内のファイルを取得
files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# プレフィックスごとにファイルを分類
file_groups = defaultdict(list)
for file in files:
    prefix = file.split('_resized')[0]  # '_resized'で分割してプレフィックスを取得
    file_groups[prefix].append(file)

# プレフィックスごとに最大サイズのファイルをコピー
for prefix, group_files in file_groups.items():
    largest_file = None
    largest_size = 0

    for file in group_files:
        file_path = os.path.join(source_folder, file)
        file_size = os.path.getsize(file_path)
        if file_size > largest_size:
            largest_file = file
            largest_size = file_size

    # 最大サイズのファイルをコピー
    if largest_file:
        source_path = os.path.join(source_folder, largest_file)
        destination_path = os.path.join(destination_folder, largest_file)
        shutil.copy2(source_path, destination_path)
        print(f"{largest_file} を {destination_folder} にコピーしました。")

# 処理完了メッセージ
print("全てのプレフィックスについて最大サイズのファイルをコピーしました。")
