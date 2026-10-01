import random
from src.environmentProClass import environmentPro
from src.thingClass import Thing
from src.locations import *

from src.catFriendlyHouse_membersClass import Milk,Sausage,Mouse

from src.agentClass import Agent, proCatAgent, MouseAgent


#catFriendlyHouse_envClass
class catFriendlyHouse_env(environmentPro):
  def __init__(self):
    super().__init__()
    self.locations=[loc_A, loc_B, loc_C]
    self.direction = True

  def default_location(self, thing):
    print("The item is starting in random location...")
    return random.choice(self.locations)
  
    
  

  def percept(self, agent):
    things = self.list_things_at(agent.location)

    status = []

    for thing in things:
      if isinstance(thing, Milk):
        status.append("Milk")
      elif isinstance(thing, Sausage):
        status.append("Sausage")
      elif isinstance(thing, Mouse):
        status.append("Mouse")

    if len(status) == 0:
      status = "Empty"
    elif len(status) == 1:
      status = status[0]

    return agent.location, status
  
  def execute_action(self, agent, action):
      if action == 'Go ahead':
          current = self.locations.index(agent.location)

          if self.direction:
              if current < len(self.locations) - 1:
                  agent.location = self.locations[current + 1]
              else:
                  self.direction = False
                  agent.location = self.locations[current - 1]
          else:
              if current > 0:
                  agent.location = self.locations[current - 1]
              else:
                  agent.alive = False
                  print("The Cat finished its hunt")
                  return

          agent.performance -= 1
          print(f"The Cat moved to {agent.location}")

      elif action == 'Drink':
          items = self.list_things_at(agent.location, Milk)

          if len(items) > 0:
              agent.performance += items[0].energy
              self.delete_thing(items[0])
              print("The Cat drank the milk")

      elif action == 'Eat':
          items = self.list_things_at(agent.location, Sausage)

          if len(items) > 0:
              agent.performance += items[0].energy
              self.delete_thing(items[0])
              print("The Cat ate the sausage")

      elif action == 'Catch':
        items = self.list_things_at(agent.location, Mouse)

        if len(items) > 0:
          mouse = items[0]

          if agent.performance >= mouse.energy:
              agent.performance += mouse.energy
              self.delete_thing(mouse)
              print("The Cat caught the mouse")
          else:
            print("The Cat is too weak to catch the mouse")

  def is_done(self):
      no_agents = not any(agent.is_alive() for agent in self.agents)
      no_items = len(self.things) == 0

      return no_agents or no_items



  #catFriendlyHouse_envClass
class catFriendlyHouse2_env(environmentPro):
  def __init__(self):
    super().__init__()
    self.locations=[loc_A, loc_B, loc_C, loc_D]
    self.direction = True

  def default_location(self, thing):
    print("The item is starting in random location...")
    return random.choice(self.locations)
  
  #Return all agants exactly at a given location
  def list_agents_at(self, location, thingClass=Thing):
    return [
        agent for agent in self.agents
        if agent.location == location and isinstance(agent, thingClass)
    ]
  

  def percept(self, agent):
    things = self.list_things_at(agent.location)
    agents = self.list_agents_at(agent.location)

    return agent.location, things, agents
  

  def add_thing(self, thing, location=None): # improved  
    # perf = original one not 0 like in parent class
    #from src.agentClass import Agent
    if thing in self.agents:
      print("Can't add the same agent twice")
    else:
      if isinstance(thing, Agent):
        #thing.performance = 0
        thing.location = location if location is not None else self.default_location(thing)
        self.agents.append(thing)
        print(f"Welcome! You are added in location {thing.location}")
    if thing in self.things and thing.location==location:
      print("Can't add the same agent twice")
    else:
      if not isinstance(thing, Agent):
        thing.location = location if location is not None else self.default_location(thing)
        self.things.append(thing)
    
  def execute_action(self, agent, action):
    #changes the state of the environment based on what the agent does.
    if self.is_agent_alive(agent):
      #the current agent is Cat & Mouse is still there
      if isinstance(agent, proCatAgent) and len(self.agents+self.things)>0:
        print("Some items are still there ....")
        if action == 'Go ahead':
            current = self.locations.index(agent.location)

            if agent.direction:
                agent.location = self.locations[current + 1]
            else:
                agent.location = self.locations[current - 1]

            agent.performance -= 5
            self.update_agent_alive(agent)

            print(f"The Agent decided to Go ahead at location: {agent.location}")
          

        elif action == 'Catch':
            items = self.list_agents_at(agent.location, thingClass=MouseAgent)

            if items:
                target_mouse = items[0]

                if agent.performance > target_mouse.performance * 5:
                    self.delete_thing(target_mouse)
                    agent.performance += 10
                    self.update_agent_alive(agent)

                    print(f"The Agent did {action} {target_mouse} at location: {agent.location}")
                    print("There is nothing for Agent Cat here. Done!")
                    agent.alive = False

                else:
                    agent.performance -= 10
                    self.update_agent_alive(agent)

                    print(f"The Agent tried to {action} {target_mouse} at location: {agent.location}, but failed.")

            else:
                print(f"Agent tried to {action}, but no MouseAgent was found at {agent.location}.")
        
      elif action == 'Check direction':
          print("The Agent decided to {} at location: {}".format(action, agent.location))

          if agent.location == loc_A and not agent.direction:
              agent.changeDirection()

          if agent.location == loc_D and agent.direction:
              agent.changeDirection()

          if agent.direction == True:
              agent.location = self.locations[self.locations.index(agent.location) + 1]
          else:
              agent.location = self.locations[self.locations.index(agent.location) - 1]

          agent.performance -= 5
          self.update_agent_alive(agent)
          

      elif isinstance(agent, MouseAgent):
        print(f"the Agent Mouse is still running with a performance {agent.performance}")
        agent.location = action
        print(f"The Agent Mouse decided to move to {agent.location}")

        agent.performance -= 1
        self.update_agent_alive(agent)
      
      else:
          print("There is nothing for Agent Cat here. Done!")
          agent.alive=False
    
    
  def is_done(self):
    no_agents = not any(agent.is_alive() for agent in self.agents)
    #return no_agents or no_items
    return no_agents
    
    








  

