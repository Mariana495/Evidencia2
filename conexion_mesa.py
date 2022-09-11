from mesa import Agent, Model

from mesa.space import MultiGrid

from mesa.time import SimultaneousActivation

from mesa.datacollection import DataCollector

import numpy as np
import pandas as pd

import time
import datetime
import random

class Semaforo(Agent):
  def __init__(self, unique_id, model,estado):
    super().__init__(unique_id, model)
    self.sig_pos = None
    self.tipo = 'Semaforo'
    self.estado = estado
    self.nstep = 0
    self.next_estado = 0
  
  def step(self):
    self.nstep = self.nstep + 1

      # 1: verde
      # 2: rojo
      # 3: rojo con pase de peaton
    if  (self.nstep < 5):
      if (self.pos == (13,10) or self.pos == (14,10) or self.pos == (15,10)):
        self.estado = 1
      else:
        self.estado = 2
        
    elif  (self.nstep >= 10 and self.nstep < 15):
      if (self.pos == (16,13) or self.pos == (16,14) or self.pos == (16,15)):
        self.estado = 1
      else:
        self.estado = 2

    elif  (self.nstep >= 20 and  self.nstep < 25):
      if (self.pos == (11,16) or self.pos == (12, 16) or self.pos == (13,16)):
        self.estado = 1
      else:
        self.estado = 2

    elif  (self.nstep >= 30 and  self.nstep < 35):
      if (self.pos == (10,11) or self.pos == (10,12) or self.pos == (10,13)):
        self.estado = 1
      else:
        self.estado = 2

    elif  ((self.nstep >= 5 and  self.nstep < 10) or (self.nstep >= 15 and self.nstep < 20) or (self.nstep >= 25 and  self.nstep < 30) or (self.nstep >= 35 and  self.nstep < 40) or (self.nstep >= 45 and  self.nstep < 50)):
      self.estado = 2

    elif  (self.nstep >=40 and  self.nstep <45):
      self.estado = 3

    if(self.nstep == 50):
      self.nstep = 0

################################################################################

class Coche(Agent):
  def __init__(self, unique_id, model, destination, start):
    super().__init__(unique_id, model)
    self.sig_pos = None
    self.tipo = 'Coche'
    self.destination = destination
    self.start = start
    self.emergencyCouter = 0

  def step(self):
    passing = False
    vecinos = self.model.grid.get_neighbors(
        self.pos,
        moore=True,
        include_center=True)
    for vecino in vecinos:
      if isinstance(vecino,Ambulancia):
        self.emergencyCouter = 2
      elif isinstance(vecino,Semaforo):
        if vecino.estado == 1:
          passing = True
        else:
          passing = False
    
    # maquina de estados
    X = (self.pos[1]-self.destination[1])
    Y = (self.pos[0]-self.destination[0])

    if(Y > 0):
      newY = self.pos[0] - 1
    elif(Y < 0):
      newY = self.pos[0] + 1
    else:
      newY = self.pos[0]

    if(X > 0):
      newX = self.pos[1] - 1
    elif(X < 0):
      newX = self.pos[1] + 1
    else:
      newX = self.pos[1]

    self.sig_pos = (newY,newX)
    if(self.model.grid.is_cell_empty(self.sig_pos) or passing or 
        self.pos == (12,11) or self.pos == (14,11) or 
        self.pos == (11,12) or self.pos == (15,12) or
        self.pos == (11,14) or self.pos == (15,14) or 
        self.pos == (12,15) or self.pos == (14,15)):
      self.sig_pos = self.sig_pos
    else:
      self.sig_pos = self.pos
      
    if((self.destination == (14,12)) and (self.sig_pos == (14,12))):
      self.destination = random.choice([(26,12),(14,26),(0,14)])
    if((self.destination == (14,14)) and (self.sig_pos == (14,14))):
      self.destination = random.choice([(12,0),(14,26),(0,14)])
    if((self.destination == (12,14)) and (self.sig_pos == (12,14))):
      self.destination = random.choice([(26,12),(12,0),(0,14)])
    if((self.destination == (12,12)) and (self.sig_pos == (12,12))):
      self.destination = random.choice([(26,12),(12,0),(14,26)])

    if(self.emergencyCouter != 0):
      if((self.pos[0]==12 and self.pos[1]<=10) or (self.pos[1]==12 and self.pos[0]>=16) or 
         (self.pos[0]==14 and self.pos[1]>=16) or (self.pos[1]==14 and self.pos[0]<=10)):
        self.sig_pos = self.sig_pos
        self.emergencyCouter = self.emergencyCouter - 1
      else:
        self.sig_pos = self.pos
        self.emergencyCouter = self.emergencyCouter - 1

  def advance(self):
    if(self.pos != (0,0)):
      self.model.grid.move_agent(self,self.sig_pos)
      if((self.sig_pos == (12,0)) or (self.sig_pos == (26,12)) or 
        (self.sig_pos == (14,26)) or (self.sig_pos == (0,14))):
        positions = ((14,0),(26,14),(12,26),(0,12))
        new_pos = self.random.choice(positions)
        if(new_pos[0] == 14):
          self.destination = (14,12)
        elif(new_pos[0] == 26):
          self.destination = (14,14)
        elif(new_pos[0] == 12):
          self.destination = (12,14)
        elif(new_pos[0] == 0):
          self.destination = (12,12)
        self.model.grid.move_agent(self,new_pos)

################################################################################

class Ambulancia(Agent):
  def __init__(self, unique_id, model, destination, start):
    super().__init__(unique_id, model)
    self.sig_pos = None
    self.tipo = 'Ambulancia'
    self.destination = destination
    self.start = start
    self.counter = 0
    self.estado = 5

  def step(self):
    self.counter = self.counter + 1
    if self.counter == 35:
      self.counter = 0
    passing = False
    vecinos = self.model.grid.get_neighbors(
        self.pos,
        moore= False,
        include_center=True)
    for vecino in vecinos:
      if isinstance(vecino,Semaforo):
        if vecino.estado == 1:
          passing = True
        else:
          passing = False
    
    # maquina de estados
    X = (self.pos[1]-self.destination[1])
    Y = (self.pos[0]-self.destination[0])

    if(Y > 0):
      newY = self.pos[0] - 1
    elif(Y < 0):
      newY = self.pos[0] + 1
    else:
      newY = self.pos[0]

    if(X > 0):
      newX = self.pos[1] - 1
    elif(X < 0):
      newX = self.pos[1] + 1
    else:
      newX = self.pos[1]

    self.sig_pos = (newY,newX)
    if(self.model.grid.is_cell_empty(self.sig_pos) or passing or 
       self.pos == (13,11) or self.pos == (15,13) or self.pos == (13,15) or self.pos == (11,13)):
      self.sig_pos = self.sig_pos
    else:
      self.sig_pos = self.pos
    
    if((self.destination == (13,13)) and (self.pos == (13,12))):
      self.destination = random.choice([(26,13),(13,26),(0,13)])
    if((self.destination == (13,13)) and (self.pos == (14,13))):
      self.destination = random.choice([(13,0),(13,26),(0,13)])
    if((self.destination == (13,13)) and (self.pos == (13,14))):
      self.destination = random.choice([(13,0),(26,13),(0,13)])
    if((self.destination == (13,13)) and (self.pos == (12,13))):
      self.destination = random.choice([(13,0),(26,13),(13,26)])

  def advance(self):
    self.model.grid.move_agent(self,self.sig_pos)
    if((self.sig_pos == (26,13)) or (self.sig_pos == (13,0)) or (self.sig_pos == (13,26)) or (self.sig_pos == (0,13)) or (self.sig_pos == (0,0))):
      if(self.counter == 0):
        positions = ((13,0),(26,13),(13,26),(0,13))
        new_pos = self.random.choice(positions)
        self.destination = (13,13)
        self.estado = 5
        self.model.grid.move_agent(self,new_pos)
      else:
        new_pos = (0,0)
        self.destination = (0,0)
        self.estado = 0
        self.model.grid.move_agent(self,(0,0))

################################################################################

class Peaton(Agent):
  def __init__(self, unique_id, model, destination, start):
    super().__init__(unique_id, model)
    self.sig_pos = None
    self.tipo = 'Peaton'
    self.destination = destination
    self.start = start
    self.emergencyCouter = 0

  def step(self):
    passing = False
    positionsLights = ((11,10), (12,10), (13,10), (14,10), (15,10), 
                       (16,11), (16,12), (16,13), (16,14), (16,15), 
                       (11,16), (12,16), (13,16), (14,16), (15,16), 
                       (10,11), (10,12), (10,13), (10,14), (10,15))
    positionsMiddle = ((10,10), (10,16), (16,16), (16,10))
    vecinos = self.model.grid.get_neighbors(
        self.pos,
        moore=True,
        include_center=True)
    for vecino in vecinos:
      if isinstance(vecino, Semaforo):
        if vecino.estado == 3 or self.pos in positionsLights:
          passing = True
        else:
          passing = False
    
    # maquina de estados
    X = (self.pos[1]-self.destination[1])
    Y = (self.pos[0]-self.destination[0])

    if(self.emergencyCouter == 0):
      if(Y > 0):
        newY = self.pos[0] - 1
      elif(Y < 0):
        newY = self.pos[0] + 1
      else:
        newY = self.pos[0]

      if(X > 0):
        newX = self.pos[1] - 1
      elif(X < 0):
        newX = self.pos[1] + 1
      else:
        newX = self.pos[1]

      self.sig_pos = (newY,newX)
      positionsPedestrian = ((10,0), (0,16), (10,26), (16,26), (26,16), (26,10), (16,0), (10,0))

      print(" entidad", self.unique_id, "en ", self.pos, "sig pos = ", self.sig_pos, "destino: ", self.destination)
      if(self.model.grid.is_cell_empty(self.sig_pos) or passing): # poner que se mueva a la izquierda
        self.sig_pos = self.sig_pos
      else:
        if self.destination in positionsPedestrian:
          self.sig_pos = self.sig_pos
        elif self.model.grid.is_cell_empty(self.sig_pos) == False and self.destination in positionsMiddle:
          self.sig_pos = self.pos
       
      if((self.destination == (10,10)) and (self.sig_pos == (10,10))):
        self.destination = random.choice([(10,16), (16,10), (10,0), (0,10)])
      if((self.destination == (10,16)) and (self.sig_pos == (10,16))):
        self.destination = random.choice([(10,10), (16,16), (0,16), (10,26)])
      if((self.destination == (16,16)) and (self.sig_pos == (16,16))):
        self.destination = random.choice([(10,16), (16,10), (16,26), (26,16)])
      if((self.destination == (16,10)) and (self.sig_pos == (16,10))):
        self.destination = random.choice([(10,10), (16,16), (26,10), (16,0)])

    else:
      self.sig_pos = self.pos
      self.emergencyCouter = self.emergencyCouter - 1

  def advance(self):
    if(self.pos != (0,0)):
      self.model.grid.move_agent(self,self.sig_pos)
      positionsPedestrian = ((0,10), (0,16), (10,26), (16,26), (26,16), (26,10), (16,0), (10,0))

      if self.sig_pos in positionsPedestrian:
        new_pos = self.random.choice(positionsPedestrian)
        if(new_pos == (0,10) or new_pos == (10,0)):
          self.destination = (10,10)
        elif(new_pos == (0, 16) or new_pos == (10,26)):
          self.destination = (10,16)
        elif(new_pos == (16,26) or new_pos == (26,16)):
          self.destination = (16,16)
        elif(new_pos == (26,10) or new_pos == (16,0)):
          self.destination = (16,10)
        self.model.grid.move_agent(self,new_pos)

################################################################################

class Interseccion(Model):
  def __init__(self,num_agentes, num_peatones):
    self.num_agentes = num_agentes
    self.num_peatones = num_peatones
    self.grid = MultiGrid(27, 27, False)
    self.schedule = SimultaneousActivation(self)
    self.cochesList = []
    self.peatonesList = []
    self.coches = []
    self.semaforos = []
    self.ambulancias = []
    self.peatones = []   

    # Colocacion de agentes coche
    positions = ((14,0),(26,14),(12,26),(0,12))

    for id in range(num_agentes):
      new_pos = self.random.choice(positions)
      if(new_pos[0] == 14):
        destination = (14,12)
      elif(new_pos[0] == 26):
        destination = (14,14)
      elif(new_pos[0] == 12):
        destination = (12,14)
      elif(new_pos[0] == 0):
        destination = (12,12)

      r = Coche(id, self, destination, new_pos)
      self.cochesList.append(r)
      self.grid.place_agent(r,(0,0))
      self.schedule.add(r)
      self.coches.append(r)

    r = self.cochesList[0]
    del self.cochesList[0]
    self.grid.move_agent(r,r.start)

    # Colocacion de agentes semaforos
    positions1 = ((11,10), (12,10), (13,10), (14,10), (15,10), 
                  (16,11), (16,12), (16,13), (16,14), (16,15), 
                  (11,16), (12,16), (13,16), (14,16), (15,16), 
                  (10,11), (10,12), (10,13), (10,14), (10,15))
    
    idS = num_agentes + 1
    for pos in positions1:
      r = Semaforo(idS, self,0)
      self.grid.place_agent(r,pos)
      self.schedule.add(r)
      idS = idS + 1
      self.semaforos.append(r)

    # Colocacion de agentes ambulancia
    positions = ((13,0),(26,13),(13,26),(0,13))

    new_pos = self.random.choice(positions)
    destination = (13,13)

    idA = idS + 1
    r = Ambulancia(idA, self, destination,new_pos)
    self.grid.place_agent(r,r.start)
    self.schedule.add(r)
    self.ambulancias.append(r)

    # Colocacion de agentes peatones
    positionsPedestrian = ((0,10), (0,16), (10,26), (16,26), (26,16), (26,10), (16,0), (10,0))

    for id in range(idA + 1, idA + num_peatones):
      new_pos = self.random.choice(positionsPedestrian)
      if(new_pos == (0,10) or new_pos == (10,0)):
        destination = (10,10)
      elif(new_pos == (0, 16) or new_pos == (10,26)):
        destination = (10,16)
      elif(new_pos == (16,26) or new_pos == (26,16)):
        destination = (16,16)
      elif(new_pos == (26,10) or new_pos == (16,0)):
        destination = (16,10)

      r = Peaton(id, self, destination, new_pos)
      self.peatonesList.append(r)
      self.grid.place_agent(r,(0,0))
      self.schedule.add(r)
      self.peatones.append(r)

    r = self.peatonesList[0]
    del self.peatonesList[0]
    self.grid.move_agent(r,r.start)


    self.datacollector = DataCollector(
        agent_reporters={'Movimientos': lambda a: getattr(a, 'movimientos', None), 
                        "Posicion": lambda a: getattr(a, 'sig_pos', None),
                        "Tipo": lambda a: getattr(a, 'tipo', None)}
        )
    
  def status_agentes(self):
    data = []
    for r in self.coches:
      data.append({'tipo': r.tipo, 'id': r.unique_id, 'X': r.pos[1], 'Y': r.pos[0]})
    for r in self.semaforos:
      data.append({'tipo': r.tipo, 'id': r.unique_id, 'X': r.pos[1], 'Y': r.pos[0], 'estado': r.estado})
    for r in self.ambulancias:
      data.append({'tipo': r.tipo, 'id': r.unique_id, 'X': r.pos[1], 'Y': r.pos[0]})
    for r in self.peatones:
      data.append({'tipo': r.tipo, 'id': r.unique_id, 'X': r.pos[1], 'Y': r.pos[0]})
    return data

  def step(self):
    self.schedule.step()
    if(len(self.cochesList) > 0):
      r = self.cochesList[0]
      del self.cochesList[0]
      self.grid.move_agent(r,r.start)
    if(len(self.peatonesList) > 0):
      r = self.peatonesList[0]
      del self.peatonesList[0]
      self.grid.move_agent(r,r.start)