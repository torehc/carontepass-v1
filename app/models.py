from app import db

class Group(db.Model):
    __tablename__ = 'cp_group'

    id_group = db.Column(db.Integer, primary_key=True)
    name_group = db.Column(db.String(120))
    url = db.Column(db.String(160))

    def __str__(self):
        return self.name_group

class User(db.Model):
    __tablename__ = 'cp_user'

    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    rol = db.Column(db.Enum(['adm', 'usr']), default='usr', nullable=False)
    group_id = db.ForeignKey('cp_group.id_group')
    phone = db.Column(db.String(15))
    address = db.Column(db.String(220))
    email = db.Column(db.String(180))

    def __str__(self):
        return '{}, {} ({})'.format(self.last_name, self.name, self.email)
