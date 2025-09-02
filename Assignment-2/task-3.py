# Open a file in write mode ("w")
# If the file does not exist, it will be created
# If it already exists, its content will be overwritten

file = open("myfile.txt", "w")

# Write content to the file
file.write("Hello, this is my first text file!\n")
file.write("Python makes file handling easy.\n")
file.write("Good luck learning file operations!")

# Always close the file after writing
file.close()

print("File 'myfile.txt' created and content written successfully!")

