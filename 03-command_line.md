# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>> change directory: `cd`  
list directory: `ls`  
remove file: `rm`
remove directory: `rmdir`  
make directory: `mkdir`  
copy file: `cp`  
move file: `mv`  
read last few lines of a large file: `tail`  
read first few lines of a large file: `head`  
looking up files that contain certain strings: `grep`  
---

###Q2.  List Files in Unix   

What do the following commands do:  
> > `ls`  list files in the current directory  
`ls -a`  list all files (including hidden ones) in the current directory  
`ls -l`  list files in the directory along with some file info for each of them such as read/write permissions, file size, date modified etc.  
`ls -lh`  same as above, but with the file size abbreviated by units  
`ls -lah`  same as -lh, but with **all** file info available listed  
`ls -t`  same as -l, but sorts the list output by modification time  
`ls -Glp`  same as -l, lists directories with '/' appended at the end to distinguish it from other files. Also color them blue  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -u`	sort by last access time  
`ls -g` list while excluding the name of the file owner   
`ls -R` display subdirectories as well  
`ls -c` display files/directories as a comma-separated list  
`ls -1` display files/directories as one vertical list rather than multiple columns/rows of file names  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > My understand is that xargs can be used to achieve a similar effect to a loop by running a command appended to the output of the previous command. For example: If we type the command `echo 1 2 3`, the output will be `1 2 3`. We can use xarg to concisely tell the program to output `Student` in front of each number by typeing `echo 1 2 3| xargs -n 1 echo Student`.

 

