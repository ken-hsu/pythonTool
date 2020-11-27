"""
Unzip file in batch
Input: 
TD = the directory contain all the .zip file
SI = the name of file for starting index

Output:
the file with ceratin name

TODO(ken): complete the document
"""
from zipfile import ZipFile # extract file
import os # rename and list the file in the directory
import fnmatch # search by wildcard

def BUZF(TD,SI=None):
   fileList = os.listdir(TD)
   fldFileList = fnmatch.filter(fileList, '*.zip')
   """
   Following is test data
   fldFileList = ['54023_108522.zip','54024_108539.zip','54023_108522.zip']
   """
   startIndex = (fldFileList.index(SI)) if SI is not None else 0
   return
   for filename in fldFileList[startIndex:]:
      filename = filename[:-4]
      try:
         with ZipFile('/usr/app/Data/coros_data/jsonload/'+filename+'.zip', 'r') as zip_ref:
            zip_ref.extractall('Data/coros_data/jsonload/extf')
         os.rename('Data/coros_data/jsonload/extf/file_data','Data/coros_data/jsonload/extf/'+filename+'.xx')
      except:
         print(filename)
         continue

if __name__ == '__main__':
   TD = 'Data/coros_data/jsonload/'
   # SI = 4023_108522.zip
   BUZF(TD)
