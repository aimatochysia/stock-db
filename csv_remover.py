import os

folder_path = 'data'

for filename in os.listdir(folder_path):
    if filename.endswith('.json') and filename != 'stocklist.csv':
        file_path = os.path.join(folder_path, filename)
        try:
            os.remove(file_path)
            print(f"Deleted: {filename}")
        except Exception as e:
            print(f"Failed to delete {filename}: {e}")
    elif filename == 'stocklist.csv':
        print('STOCKLIST FOUND!')