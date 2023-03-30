import os
import re
from os.path import exists

#C:\Temp\NewStuff\LengthsUpdated8-5\5-7-29\8-4

folder1 = input('Path to folder you want to rename> ')

folder_input = folder1.replace("/", "//")
i = 0

for file in os.listdir(folder_input):
    
    if i == 1:
        break
    
    if ".jpg" in folder_input + "\\" + file:
        Total_files = ( (len(os.listdir(folder_input)) ) /4)
        i = 1
    else:
        Total_files = ( (len(os.listdir(folder_input)) ) /2)

#-----------------------------------------------------------------------------------------
#Moves all the length files to the correct length_folderand adds a 1, 2, ... 11, 12
if not os.path.exists(folder_input + "//" + 'Length'):
    os.makedirs(folder_input + "//" + 'Length')
    
count = 1
for file_name1 in os.listdir(folder_input):
    file_exists = exists(folder_input + "\\" + file_name1 + "\\" + "length.csv")
    print(file_name1)
    print(file_exists)
    
    source1 = folder_input + "\\" + file_name1 + "\\" + "length.csv"
    
    if file_exists == True:
       file_name1 = file_name1.replace('.csv', '')
       destination1 = folder_input + "\\" + "Length" + "\\" + "length" + str(count) + ".csv"
       os.rename(source1, destination1)
       count += 1
    elif exists(folder_input + "\\" + file_name1 + "\\" + "unclassified") == True:
        print (exists(folder_input + "\\" + file_name1 + "\\" + "unclassified"))
        count += 1
       
       
       
#---------------------------------------------------------------------------
#Either orginses the length file in acordance to thir creation date or there number added in strp 1     
       
def natural_key(string_):
   return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)] 

#----------------------------------------------------------------------------------------------
#Adds the proper naming scheme to each lenght file to know what they represent

length_folder= folder_input + "//" + 'Length'
count = 1

file_list = os.listdir(length_folder)

sorted_files = sorted(file_list, key=natural_key)



for file_name in sorted_files :
    
    
      source = length_folder+ "\\" + file_name
    
      if count <= Total_files:
              file_name = file_name.replace('.csv', '')
              destination = length_folder+ "\\" + file_name + "S" + ".csv"
              if count%2 == 0 :
                  destination = length_folder+ "\\" + file_name + "S" + "L" + ".csv"
                  
      elif count >= Total_files:
              file_name = file_name.replace('.csv', '')
              destination = length_folder+ "\\" + file_name + "R" + ".csv"
              if count%2 == 0 :
                  destination = length_folder+ "\\" + file_name + "R" + "L" + ".csv"
      os.rename(source, destination)
      count += 1            
      
      
      
      
print('All Files Renamed')
print('New Names are')
 #verify the result
res = os.listdir(length_folder)
print(res)



 #    if count <= 6:
  #       file_name = file_name.replace('.csv', '')
 #        destination = folder + "\\" + file_name + "S" + ".csv"
  #       if count%2 == 0 :
      #       destination = folder + "\\" + file_name + "S" + "L" + ".csv"
             
  #   elif count >= 6:
   #      file_name = file_name.replace('.csv', '')
     #    destination = folder + "\\" + file_name + "R" + ".csv"
     #    if count%2 == 0 :
     #        destination = folder + "\\" + file_name + "R" + "L" + ".csv"