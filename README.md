# Password Calculator
Creating safe hard passwords

A module that uses a compination of two dictionaries and a second degree based incoder

input your numerical password and function enconder:

<h1>Ex:</h1> 

<h2> What u need to provide in our standards: </h2>
<strong>Your password:</strong> 123321246
<strong>Selected function:</strong> x^2 + 2x

  my_pwd = [1, 2, 3, 3, 2, 1, 2, 4, 6]
  my_function = [1, 2, 0]

<h2>Now to instantiate:</h2>

  new_pwd = HardPassword(my_pwd, my_function)
  new_pwd.create_pwd()
  
<h1> Additional Tip </h1>
Add our generated password to a phrase so its even more unique and hard to crack
