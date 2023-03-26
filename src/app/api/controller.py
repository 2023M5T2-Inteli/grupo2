from extensions import db
from models import Position

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
    # def get_highest_order(data):
    #     try:
    #         track = data["track"]
    #         positions = db.session.query(Position).filter(Position.track == track).order_by(Position.order.desc()).first()
    #         return str(positions.order)
    #     except Exception as e:
    #         return str(e)
    # def get_highest_order_track():
    #     try:
    #         positions = db.session.query(Position).order_by(Position.order.desc()).first()
    #         return str(positions.track)
    #     except Exception as e:
    #         return str(e)
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
        