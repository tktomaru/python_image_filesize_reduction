from PIL import Image
import os

def resize_and_compress_images(input_folder, output_folder, quality_levels, resize_levels, target_size=1_048_576, max_images=5):
    """
    フォルダ内のすべての画像をリサイズおよび品質調整して1MB以下にし、画像ごとに最大指定枚数まで変換する。

    Parameters:
        input_folder (str): 入力画像フォルダのパス。
        output_folder (str): 変換後の画像を保存するフォルダ。
        quality_levels (list): 画像品質の配列 (例: [95, 85, 75, 65, ...])。
        target_size (int): ファイルサイズの目標 (バイト単位、デフォルトは1MB)。
        max_images (int): 1つの画像につき生成する最大枚数。
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 入力フォルダ内のすべてのファイルを取得
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff'))]

    for image_file in image_files:
        input_image_path = os.path.join(input_folder, image_file)
        output_count = 0  # 各画像に対する生成枚数をリセット
        
        try:
            img = Image.open(input_image_path)
            original_width, original_height = img.size  # 元画像のサイズを取得
        
            for resize in resize_levels:
                    
                width, height = original_width, original_height  # 解像度を元に戻す
                # 解像度を縮小
                width = int(width * resize)
                height = int(height * resize)

                # 最小サイズに達した場合、次の画像に進む
                if width < 10 or height < 10:
                    print(f"Resolution too small to continue resizing for quality {quality}.")
                    break
                
                for quality in quality_levels:
                    # リサイズ
                    img_resized = img.resize((width, height), Image.Resampling.LANCZOS)
                    
                    # 保存するファイルパス
                    output_file_name = f"{os.path.splitext(image_file)[0]}_resized_{output_count + 1}.jpg"
                    output_path = os.path.join(output_folder, output_file_name)
                    
                    # 保存
                    img_resized.save(output_path, "JPEG", quality=quality)
                    
                    # ファイルサイズをチェック
                    file_size = os.path.getsize(output_path)
                    
                    if file_size <= target_size:
                        print(f"Image saved: {output_path}, Size: {file_size} B, Quality: {quality}, Resize: {resize}, Resolution: {width}x{height}")
                        output_count += 1
                        break

                # 最大生成数に達したら次の画像へ
                if output_count >= max_images:
                    break

        except Exception as e:
            print(f"Error processing the image {image_file}: {e}")
            continue

# 使用例
input_folder = "input_images"  # 入力画像フォルダのパス
output_folder = "resized_images"  # 出力先フォルダ
quality_levels = [99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78]  # 品質の配列（高品質から低品質）
resize_levels = [1,0.99,0.98,0.97,0.96,0.95,0.94,0.93,0.92,0.91,0.9,0.89,0.88,0.87,0.86,0.85,0.84,0.83,0.82,0.81,0.8,0.79,0.78,0.77,0.76,0.75,0.74,0.73,0.72,0.71,0.7,0.69,0.68,0.67,0.66,0.65,0.64,0.63,0.62,0.61,0.6,0.59,0.58,0.57,0.56,0.55,0.54,0.53,0.52,0.51,0.5,0.49,0.48,0.47,0.46,0.45,0.44,0.43,0.42,0.41,0.4,0.39,0.38,0.37,0.36,0.35,0.34,0.33,0.32,0.31,0.3,0.29,0.28,0.27,0.26,0.25,0.24,0.23,0.22,0.21,0.2,0.19,0.18,0.17,0.16,0.15,0.14,0.13,0.12,0.11,0.1,0.09,0.08,0.07,0.06,0.05,0.04,0.03,0.02,0.01] # リサイズ
resize_and_compress_images(input_folder, output_folder, quality_levels, resize_levels, target_size=1_048_576, max_images=5)
