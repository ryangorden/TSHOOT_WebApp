from app import db

# This is the database model object
class Device(db.Model):
    __tablename__ = 'devices'
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<Device {self.username}>'


if __name__ == '__main__':
    db.create_all()
    r1 = Device('user1', 'Cisco')
    r2 = Device('user2', 'Aruba')
    # db.session.add(r1)
    # db.session.add(r2)
    # db.session.commit()
    print(Device.query.all())
    # print(Device.query.filter_by(hostname='vpn-router'))
