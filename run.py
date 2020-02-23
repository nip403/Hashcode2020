import os

files = ["a_example.txt","b_read_on.txt","c_incunabula.txt","d_tough_choices.txt","e_so_many_books.txt","f_libraries_of_the_world.txt"]
outputs = ["a_out.txt","b_out.txt","c_out.txt","d_out.txt","e_out.txt","f_out.txt"]

for i in range(len(files)):
    os.system("task.py " + files[i] + " " + outputs[i])