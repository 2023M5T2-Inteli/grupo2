from extensions import db
from models import Position

class DobotController:

    #get all positions in a track       
    def get_track(data):
        try:
            track = data["track"]
            positions = db.session.query(Position).filter(Position.track == track).order_by(Position.order.asc()).all()
            return [position.return_json() for position in positions]
        except Exception as e:
            return str(e)
        
    #   get all tracks
    def get_tracks():
        try:
            positions = db.session.query(Position).all()
            return [position.track for position in positions]
        except Exception as e:
            return str(e)
        
    # adds position to track
    def add_position(self,data):
        try:
            track = data["track"]
            x = data["x"]
            y = data["y"]
            z = data["z"]
            r = data["r"]
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
            position = Position(x=x, y=y, z=z,r=r, track=track,order=order,magnet=magnet)
            db.session.add(position)
            db.session.commit()
            return f"Position {x},{y},{z},{r} added to track {track} with order {order} "
        except Exception as e:
            return str(e)
    #turns on the magnet
    def magnet_on():
        import serial
        import time
        try:
            tempo_espera = 2
            taxa_transmissao = 115200
            comunicacao_serial = serial.Serial("COM8", taxa_transmissao, timeout = tempo_espera)
            comunicacao_serial.write(b"on\n") # Escreve "on" na serial
            time.sleep(1)
            return "on"
        except Exception as e:
            return str(e)
    #turns off the magnet   
    def magnet_off():
        import serial
        import time
        try:
            tempo_espera = 2
            taxa_transmissao = 115200
            comunicacao_serial = serial.Serial("COM8", taxa_transmissao, timeout = tempo_espera)
            comunicacao_serial.write(b"off\n") # Escreve "on" na serial
            time.sleep(1)
            return "off"
        except Exception as e:
            return str(e)
    #runs a track
    def run_track(data):
        import pydobot
        import datetime
        device = pydobot.Dobot(port="COM5", verbose=False)
        if not device:
            raise Exception("unable to connect to dobot")
        try:
            track = data["track"]
            cycles = data["cycles"]
            aceleration = data["aceleration"]
            t1 = datetime.datetime.now()
            try:
                dict_aceleration = {
                    1:100,
                    2:200,
                    3:300,
                    4:400
                }
                aceleration = dict_aceleration[aceleration]
            except Exception as e:
                return str(e)
            device.speed(400,aceleration)
            positions = db.session.query(Position).filter(Position.track == track).order_by(Position.order.asc()).all()
            for i in range(int(cycles)-1) :
                print(i)
                for position in positions:
                    if position.magnet == "on":
                        DobotController.magnet_on()
                    else:
                        DobotController.magnet_off()
                    device.move_to(position.x,position.y,position.z,position.r,wait =True)
            return str((datetime.datetime.now() -t1).total_seconds())
        except Exception as e:
            return str(e)
        
    def add_position_dobot(self,data):
        import pydobot
        device = pydobot.Dobot(port="COM5", verbose=False)
        track = data["track"]
        order = data["order"]
        magnet = data["magnet"]
        if not device:
            raise Exception("unable to connect to dobot")
      
        try:
            x,y,z,r,j1,j2,j3,j4 = device.pose()
            print(x,y,z,r)
            json = {"x":x,"y":y,"z":z,"r":r,"track":track,"order":order,"magnet":magnet}
            print(json)
            return f"Position {x},{y},{z},{r} added to track {track} with order {order} "
          
        except Exception as e:
            return str(e)
    def add_position_dobot(self,data):
        import pydobot
        device = pydobot.Dobot(port="COM5", verbose=False)
        track = data["track"]
        order = data["order"]
        magnet = data["magnet"]
        if not device:
            raise Exception("unable to connect to dobot")
      
        try:
            x,y,z,r,j1,j2,j3,j4 = device.pose()
            print(x,y,z,r)
            json = {"x":x,"y":y,"z":z,"r":r,"track":track,"order":order,"magnet":magnet}
            print(json)
            return self.add_position(json)
          
        except Exception as e:
            return str(e)
        
    def delete_track(data):
       
        track = data["track"]
        try:
            positions  = db.session.query(Position).filter(Position.track == track).all()
            for position in positions:
                db.session.delete(position)
            db.session.commit()
            return f"rota {track} deletada com sucesso"
        except Exception as e:
            return str(e)
        
    def add_track(poisition_list):
            try:
                for position in poisition_list:
                    position_ = Position(x=position["x"], y=position["y"], z=position["z"],r=position["r"], track=position["track"],order=position["order"],magnet=position["magnet"])
                    db.session.add(position_)
                db.session.commit()
                return f"rota adicionada com sucesso"
            except Exception as e:
                return str(e)

       