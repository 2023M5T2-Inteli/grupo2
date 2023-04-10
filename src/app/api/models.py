from extensions import db

#helps when recreate the databases
db.metadata.clear()

    
class Position(db.Model):
    __tablename__ = "position"

    id = db.Column(db.Integer, primary_key=True)
    j1 = db.Column(db.Float)
    j2 = db.Column(db.Float)
    j3 = db.Column(db.Float)
    j4 = db.Column(db.Float)
    order = db.Column(db.Integer)
    track = db.Column(db.String(30)) 
    magnet = db.Column(db.Boolean, default=False, nullable=False)



    def __repr__(self):
        return f"Position {self.id} {self.j1} {self.j2} {self.j3} {self.j4}  {self.order} {self.track} {self.magnet}"
    
    def return_json(self):
        return {"id":self.id,"j1":self.j1,"j2":self.j2,"j3":self.j3,"j4":self.j4 ,"order":self.order,"track":self.track ,"magnet":self.magnet}

    

if __name__ == "__main__":
    from app import app

    with app.app_context():
    
        db.create_all()