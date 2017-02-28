import zipfile, os

def backupTozip(folder):
    folder = os.path.abspath(folder)
    number = 0
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    print('Creating {}...'.format(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    # 遍历目录
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in {}...'.format(foldername))
        backupZip.write(foldername)
    # Add files
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()

    print('Done')


backupTozip('E:\\jj')

