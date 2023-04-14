import os.path

for address, dirs, files in os.walk('test/'):
    for name in files:
        print(os.path.join(address, name))
