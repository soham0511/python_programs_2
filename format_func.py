users = ['rohan das', 'shubham', 'haris', 'bhai']

computer = ['raspberry pi', 'tuf', '16GB RAM vala', 'sabse mehnga vala']

for i in range(len(users)):
    var = "Computer used by "+ users[i]+ " is "+ computer[i]
    print(var)

users = ['rohan das', 'shubham', 'haris', 'bhai']
computer = ['raspberry pi', 'tuf', '16GB RAM vala', 'sabse mehnga vala']

for i in range(len(users)):
    var = "Computer used by {1} is {0}"
    print(var.format(users[i], computer[i]))

users = ['rohan das', 'shubham', 'haris', 'bhai']
computer = ['raspberry pi', 'tuf', '16GB RAM vala', 'sabse mehnga vala']
price = ['10k', '54k', 'youthoob money', 'bola na sabse mehnga']

for i in range(len(users)):
    var = "Computer used by {2} is {0} which is of {1}"
    print(var.format(users[i], computer[i], price[i]))