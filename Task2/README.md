# Task 2 - Coffee machine
## Introduction
Your university recently installed fancy new network connected coffee machines. As we all know, computer science students run most efficiently when their diet consists of >90% caffeine, so being able to remotely choose the type of coffee, pay, and start the process of making coffee could result in some serious time savings. Good idea right? Well, we’ll see about that.

To make it easy for students to script their daily coffee intake, the coffee machines are reachable over a simple telnet connection on:

`34.90.152.198:13338`

As an example, use netcat `nc 34.90.152.198 13338` to connect to the machine and try some of the following commands:

- choose_black
- choose_cappuccino
- pay
- make_coffee

See if you can order a coffee!

Besides the questions posed in the assignment text, also include in your report your answers to the questions asked here.

## Part 1:
As often happens with IoT devices (coffee machines included), there is a bug in the firmware. In this case, a certain sequence of commands results in an unexpected outcome. Luckily, active state machine learning allows us to retrieve the state machine representing the behavior of the coffee machine in a completely black-box fashion. Once we have this state machine, spotting the bug should be easy.

- Given the possible inputs above, draw what you think the state machine representing the coffee machine looks like. How many states do you need? This number will be important for configuring the W-method in the next part. Include the state machine and number in your report.

### Make the learner talk to the coffee machine:

- Use STMLearn, subclass stmlearn.suls.SUL (See `RemoteCoffeeMachineSul.py`) and implement the abstract methods to send inputs and read outputs over telnet.

#### Hints: 
- Use python’s built in telnetlib
- reset the coffee machine by sending ‘reset’. 
- Don’t forget newlines after each message (‘\n’)
- Don’t overcomplicate things, the complete SUL implementation shouldn’t take much more than 10 lines excluding whitespace.


### Spotting bugs:
- Learn a state machine of the coffee machine. Include this in your report and indicate where the bug is. Also include how you would fix it. (e.g. what the correct state machine should look like)
#### Hints:
- Use a W-method equivalence checker with “m” set to the amount of states you think the state machine should have 
- Learning shouldn’t take much more than a minute or so

## Part 2:
After a firmware update, the bug is fixed! However, somebody at the coffee machine company forgot to disable developer mode before shipping the new version. With developer mode enabled, there is a secret code (sequence of inputs) that allows users to obtain free coffee! Using a state machine learning setup similar to the last task, learn another state machine of the new firmware and figure out what the secret code is! Include the learned state machine in your report, as well as what you think the secret code is. (Note: you could probably brute force this, but that is not the intended solution :) )

The updated machine is reachable at `34.90.152.198:13337`

#### Hints:
- The new state machine has 10 states
- If the resulting state machine is hard to read, you can always do a BFS and look for the shortest path that has an edge resulting in the output we want (free_coffee!)
- Since the W-method has a lot more searching to do, the learning process will take significantly longer than in the last assignment.

Report how you found the secret code, and what the secret code is according to you. Explain step by step how the W-method was able to find the secret code. 

