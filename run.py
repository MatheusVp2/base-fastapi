import os

if __name__ == '__main__':
    os.system('uvicorn src.app:app --port=3000 --host="0.0.0.0" --reload')
