import glob, os

# put your own path here
dataset_path = '/dataset'

# Percentage of images to be used for the test set
percentage_val = 30;

# Create and/or truncate train.txt and validation.txt
file_train = open('train.txt', 'w')  
file_val = open('validation.txt', 'w')

# Populate train.txt and validation.txt
counter = 1  
index_val = round(100 / percentage_val)  
for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_val+1:
        counter = 1
        file_val.write(dataset_path + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(dataset_path + "/" + title + '.jpg' + "\n")
        counter = counter + 1
