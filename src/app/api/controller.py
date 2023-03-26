from extensions import db
from models import Position
import pydobot
import serial
from sys import argv

class DobotController:

    def add(data):
        x = data["x"]
        y = data["y"]
        z = data["z"]
        r = data["r"]
        track = data["track"]
        magnet = data["magnet"]
        order = data["order"]

       
        try:
            position = Position(x=x, y=y, z=z,r=r, track=track,order=order,magnet=magnet)
            db.session.add(position)
            db.session.commit()
            return f"Added {str(data)}"
        
        except Exception as e:
            return str(e)
    def get():
        try:
            positions = db.session.query(Position).all()
            return [position.return_json() for position in positions]
        except Exception as e:
            return str(e)
        
    #get all positions in a track       
    def get_track(data):
        try:
            track = data["track"]
            positions = db.session.query(Position).filter(Position.track == track).order_by(Position.order.asc()).all()
            return [position.return_json() for position in positions]
        except Exception as e:
            return str(e)
        
    #get hightes order in a track
  
    def get_tracks():
        try:
            positions = db.session.query(Position).all()
            return [position.track for position in positions]
        except Exception as e:
            return str(e)
        
    # adds position to track
    def add_track(data):
        try:
            track = data["track"]
            x = data["x"]
            y = data["y"]
            z = data["z"]
            r = data["r"]
            order = data["order"]
            magnet = data["magnet"]
            positions = db.session.query(Position).filter(Position.track == track).all()
            if positions:
                for position in positions:
                    if position.order >= order:
                        position.order += 1
            position = Position(x=x, y=y, z=z,r=r, track=track,order=order,magnet=magnet)
            db.session.add(position)
            db.session.commit()
            return "track added"
        except Exception as e:
            return str(e)
        
    def delete_track(data):
        try:
            track = data["track"]
            positions = db.session.query(Position).filter(Position.track == track).all()
            for position in positions:
                db.session.delete(position)
            db.session.commit()
            return "track deleted"
        except Exception as e:
            return str(e)
    
    def run_track(data):
        port = argv[0]
        tempo_espera = 2
        taxa_transmissao = 115200
        comunicacao_serial = serial.Serial("COM8", taxa_transmissao, timeout = tempo_espera)


        # Connect to Dobot
        dobot = pydobot.Dobot(port=port)
        for position in data:
            if position["magnet"] == "on":
                comunicacao_serial.write(b"on\n")
            else:
                comunicacao_serial.write(b"off\n")

            dobot.move_to(position["x"],position["y"],position["z"],position["r"])
            
        return "track run"
    def run_track_dataless(data):
        port = argv[0]
        tempo_espera = 2
        taxa_transmissao = 115200
        comunicacao_serial = serial.Serial("COM8", taxa_transmissao, timeout = tempo_espera)


        # Connect to Dobot
        dobot = pydobot.Dobot(port=port)
        try:
            track = data["track"]
            positions = db.session.query(Position).filter(Position.track == track).order_by(Position.order.asc()).all()
            
        except Exception as e:
            return str(e)
        try:
            for position in positions:
                if position["magnet"] == "on":
                    comunicacao_serial.write(b"on\n")
                else:
                    comunicacao_serial.write(b"off\n")

                dobot.move_to(position["x"],position["y"],position["z"],position["r"])
        except Exception as e:
            return str(e)
        return "track run"
        
    