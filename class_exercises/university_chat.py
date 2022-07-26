#course = led by teacher / attended by student / assisted by TA
#module = belongs to course led by teacher / attended by student / assisted by TA
import uuid
from datetime import datetime

class Module:
    def __init__(self, name):
        self.name = name
        self.module_leader = None
        self.teaching_assistants = []
        
    def set_module_leader(self, teacher):
        self.module_leader = teacher

class Course:
    def __init__(self, name):
        self.course_leader = None
        self.modules = []
        
    def set_course_leader(self, teacher):
        self.course_leader = teacher

    def add_module(self, module):
        self.modules.append(module)

#create chat functionality : anyone can send a message to another person
#be able to retrieve conversations between any two people 
#each message sent needs to be time stamped 
#time stamp will be an attribute (not a class)
#each convo should have a unique identifier


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def send_message (self, recipient, message):
        dt = datetime.now() #to obtain date/time for UNIX timestamp below
        time_stamp = datetime.timestamp(dt)
        msg = Message(self, recipient, message, time_stamp)

    def retrieve_messages_sent(self):
        for i in Message.messages:
            if i.sender == self:
                print(f"At {i.time_stamp}, {self.name} sent to {i.recipient.name} the following message '{i.content}'. ")

    def retrieve_messages_received(self):
        for i in Message.messages:
            if i.recipient == self:
                print(f"At {i.time_stamp}, {self.name} received from {i.sender.name} the following message '{i.content}'. ")


class Message:
    messages = []
    def __init__(self, sender, recipient, content, time_stamp):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.time_stamp = time_stamp

        self.id = uuid.uuid4()

        Message.messages.append(self)


class Instructor(Person):
    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

class TeachingAssistant(Instructor):
    def __init__(self, name, gender):
        super().__init__(name, gender)

class Teacher(Instructor):
    def __init__(self, name, gender):
        super().__init__(name, gender)

    def add_ta_to_module(self, ta: TeachingAssistant, module: Module):
        print(self, module.module_leader)
        assert self == module.module_leader, f"Only module leaders can add TAs to a module."
        module.teaching_assistants.append(ta)

class Student(Person):
    def __init__(self, name, gender):
        pass  

class Staff(Person):
    def __init__(self, name, gender):
        pass     

module_1 = Module("Module 1")
module_2 = Module("Module 2")
module_3 = Module("Module 3")
module_4 = Module("Module 4")

course_1 = Course("data science")
course_2 = Course("business analytics")

course_1.add_module("module_1")
course_1.add_module("module_2")
course_2.add_module("module_3")
course_2.add_module("module_4")

print(course_1.modules)
print(course_2.modules)

teacher_1 = Teacher("Bill Nye", "male")
teacher_2 = Teacher("Jennifer Lopez", "female")

ta_1 = TeachingAssistant("Louis Alecu", "non-binary")
ta_2 = TeachingAssistant("Maria Alecu", "female")
ta_3 = TeachingAssistant("Ionel Alecu", "male")

course_1.set_course_leader(teacher_1)
module_1.set_module_leader(teacher_1)

teacher_1.add_ta_to_module(ta_1, module_1)
teacher_1.add_ta_to_module(ta_2, module_1)
teacher_1.add_ta_to_module(ta_3, module_1)

for i in module_1.teaching_assistants:
    print(i.name)

teacher_1.send_message(ta_2, "Where did Louis buy that banging cap? I want one!")
ta_1.send_message(ta_3, "I've run out of green tea.")
ta_2.send_message(teacher_1, "Not sure, but tis a very nice cap indeed.")
teacher_1.send_message(ta_2, "I really REALLY like that cap.")
teacher_1.send_message(ta_3, "Did you get Louis his cap?")
ta_3.send_message(teacher_1, "Nope, no idea. Why don't you ask him yourself?")
teacher_1.retrieve_messages_sent()
ta_2.retrieve_messages_received()
ta_3.retrieve_messages_received()



         