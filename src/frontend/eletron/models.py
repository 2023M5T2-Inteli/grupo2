from app import db,app

#helps when recreate the databases
db.metadata.clear()

    
class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Float)
    y = db.Column(db.Float)
    z = db.Column(db.Float)
    r = db.Column(db.Float)
    order = db.Column(db.Integer)
    track = db.Column(db.Integer)  
    time = db.Column(db.DateTime, default=db.func.now())



    def __repr__(self):
        return f"Position {self.id} {self.x} {self.y} {self.z} {self.time} {self.order} {self.track}"
    
    def return_json(self):
        return {"id":self.id,"x":self.x,"y":self.y,"z":self.z,"time":self.time,"order":self.order,"track":self.track}

    

if __name__ == "__main__":

    with app.app_context():
        db.drop_all()
        db.create_all()