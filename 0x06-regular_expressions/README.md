# 0x06. Regular expression
### Background Context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:
```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```
## Tasks
#### 0. Simply matching Holberton
![Image example fot task 0](https://github.com/sfrechou/holberton-system_engineering-devops/blob/master/0x06-regular_expressions/readme_images/task0.png)
Requirements:
* The regular expression must match Holberton
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method