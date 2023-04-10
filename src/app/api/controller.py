from extensions import db
from models import Position
import pydobot

class DobotController():

    dobot = ""
    raspPort = ""

    def __init__(self, dobotPort, raspPort):
        self.dobot = pydobot.Dobot(port=dobotPort, verbose=True)
        self.raspPort = raspPort
        

    #get all positions in a track       
    def get_track(data):
        try:
            track = data["track"]
            positions = db.session.query(Position).filter(Position.track == track).order_by(Position.order.asc()).all()
            return positions
        except Exception as e:
            return str(e)
        
    #   get all tracks
    def get_tracks(self):
        try:
            #get all unique tarcks
            positions = db.session.query(Position.track).distinct().all()
            return [position.track for position in positions]
        except Exception as e:
            return str(e)
        
    # adds position to track
    def add_position(self,data):
        try:
            track = data["track"]
            j1 = data["j1"]
            j2 = data["j2"]
            j3 = data["j3"]
            j4 = data["j4"]
            order = data["order"]
            magnet = data["magnet"]
            max = -1
            positions = db.session.query(Position).filter(Position.track == track).all()
            #fixes the order in the track
            if len(positions):
                for position in positions:
                    if position.order >= order:
                        position.order += 1
                    if max < position.order:
                        max = position.order
                if order > max:
                    order = max + 1
            else:
                order = 0
            position = Position(j1=j1, j2=j2, j3=j3,j4=j4, track=track,order=order,magnet=magnet)
            db.session.add(position)
            db.session.commit()
            return f"Position {j1},{j2},{j3},{j4} added to track {track} with order {order} "
        except Exception as e:
            return str(e)
    #turns on the magnet
    def magnet_on(self):
        import serial
        import time
        try:
            tempo_espera = 2
            taxa_transmissao = 115200
            comunicacao_serial = serial.Serial(self.raspPort, taxa_transmissao, timeout = tempo_espera)
            comunicacao_serial.write(b"on\n") # Escreve "on" na serial
            print("oi")
            time.sleep(1)
            return "on"
        except Exception as e:
            return str(e)
    #turns off the magnet   
    def magnet_off(self):
        import serial
        import time
        try:
            tempo_espera = 2
            taxa_transmissao = 115200
            comunicacao_serial = serial.Serial(self.raspPort, taxa_transmissao, timeout = tempo_espera)
            comunicacao_serial.write(b"off\n") # Escreve "on" na serial
            time.sleep(1)
            return "off"
        except Exception as e:
            return str(e)
    #runs a track
    def run_track(self, data):
        import datetime
        import serial
        import time

        try:
            track = data["track"]
            cycles = data["cycles"]
            
            t1 = datetime.datetime.now()
           
            self.dobot.speed(400,200)#aceleration
            positions = db.session.query(Position).filter(Position.track == track).order_by(Position.order.asc()).all()
            # device._set_ptp_cmd(0,0,0, 0, mode=pydobot.enums.PTPMode.MOVJ_ANGLE, wait=True)
            for i in range(int(cycles)) :
               
                for position in positions:
                    if position.magnet == True:
                        self.magnet_on()
                    else:
                        self.magnet_off()
                    print(position.j1,position.j2,position.j3,position.j4)
                    # device.move_to(position.x,position.y,position.z,position.r,wait =True)
                    self.dobot._set_ptp_cmd(position.j1,position.j2,position.j3,position.j4, mode=pydobot.enums.PTPMode.MOVJ_ANGLE, wait=True)
            try:
                tempo_espera = 2
                taxa_transmissao = 115200
                comunicacao_serial = serial.Serial(self.raspPort, taxa_transmissao, timeout = tempo_espera)
                comunicacao_serial.write(b"desbomba\n") # Escreve "on" na serial
                time.sleep(1)
            
            except Exception as e:
                print("bomba não conectado")
            return str((datetime.datetime.now() -t1).total_seconds())
        except Exception as e:
            return str(e)
        
    def add_position_dobot2(self):
        try:
            x,y,z,r,j1,j2,j3,j4 = self.dobot.pose()
            
           
            json = {"j1":j1,"j2":j2,"j3":j3,"j4":j4}
            return json
          
        except Exception as e:
            return str(e)
    def add_position_dobot(self,data):
        track = data["track"]
        order = data["order"]
        magnet = data["magnet"]
        if not self.dobot:
            raise Exception("unable to connect to dobot")
      
        try:
            x,y,z,r,j1,j2,j3,j4 = self.dobot.pose()
            
            json = {"j1":j1,"j2":j2,"j3":j3,"j4":j4,"track":track,"order":order,"magnet":magnet}
            print(json)
            return self.add_position(json)
          
        except Exception as e:
            return str(e)
        
    def delete_track(self, data):
       
        track = data["track"]
        try:
            positions  = db.session.query(Position).filter(Position.track == track).all()
            for position in positions:
                db.session.delete(position)
            db.session.commit()
            return f"rota {track} deletada com sucesso"
        except Exception as e:
            return str(e)
        
    def add_track(self, poisition_list):
            try:
                for position in poisition_list:
                    position_ = Position(j1=position[0], j2=position[1], j3=position[2],j4=position[3], track=position[6],order=position[4],magnet=position[5])
                    db.session.add(position_)
                db.session.commit()
                return f"rota adicionada com sucesso"
            except Exception as e:
                return str(e)
            
    def run_home(self):
        try:
            
            self.dobot._set_ptp_cmd(0,0,0,0, mode=pydobot.enums.PTPMode.MOVJ_ANGLE, wait=True)
            
        except Exception as e:
                return str(e)
        return "return to home"
       
    def change_default_track(self,data):

        try:
            self.delete_track({"track":"default"})

            positions = self.get_track({"track":data["track"]})
            for position in positions:
                position.track = "default"
            db.session.commit()
            return "default track changed"
        except Exception as e:
            return str(e)

       