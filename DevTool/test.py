import os

ROOT_PATH = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print ROOT_PATH;
print BASE_DIR
print os.path.join(BASE_DIR, 'templates').replace('\\', '/')
print os.path.join(BASE_DIR, 'server', 'templates')