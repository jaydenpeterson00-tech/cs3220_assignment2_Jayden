from src.thingClass import Thing

class OfficeManager(Thing):
  def __init__(self):
    self.name = "Joe"
    print("I am OfficeManager Joe")

class ITStaff(Thing):
  def __init__(self):
    self.name = "Jack"
    print("I am ITStaff Jack")

class Student(Thing):
  def __init__(self):
    self.name = "Hanna"
    print("I am Student Hanna")