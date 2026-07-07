# ## Section 3 — File Handling

# 1. Write a program that creates a file notes.txt and writes three lines of text into it.
# 2. Open notes.txt and read the whole file, then print its contents.
# 3. Read the same file line by line and print each line with its line number.
# 4. Append a new line to notes.txt without erasing the existing content. (Hint: open mode "a".)
# 5. Always use the with open(...) as f: form so the file closes automatically. Write a one-line comment explaining why with is better than calling f.close() manually.


# 1. Write a program that creates a file notes.txt and writes three lines of text into it.


with open("notes.txt", "w") as f:
    f.write("Python is easy to learn.\n")
    f.write("Practice makes perfect.\n")
    f.write("File handling is important.\n")


with open ("notes.txt","r") as f:
    content =f.read()
print(content)

with open("notes.txt", "r") as f:
    for line_number, line in enumerate(f, start=1):
        print(line_number ,':' ,line.strip())


with open("notes.txt", "a") as f:
    f.write("This is the fourth line.\n")



# Python automatically closes the file when you leave the with block, making your code safer and cleaner.
with open("notes.txt", "r") as f: 

 content = f.read()
