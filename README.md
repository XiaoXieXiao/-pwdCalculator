# Password Calculator
Creating safe hard passwords

A module that uses a combination of two dictionaries and a second degree based encoder.


<h1>Ex</h1> 

<h2> What you need to provide in our standards: </h2>

input your numerical password and function encoder: </br>

<strong>Your password:</strong> 123321246 </br>
<strong>Selected function:</strong> x^2 + 2x </br>

  my_pwd = [1, 2, 3, 3, 2, 1, 2, 4, 6] </br>
  my_function = [1, 2, 0]

<h2>Now to instantiate</h2>

  new_pwd = HardPassword(my_pwd, my_function) </br>
  new_pwd.create_pwd() </br>
 
 <h3>Return</h3>
 3*Oo8#Hw48

<h1> Additional Tip </h1>
Add our generated password to a phrase so its even more unique and hard to crack

<h3>Ex:</h3>
MyDogName3*Oo8#Hw48
