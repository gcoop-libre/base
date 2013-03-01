from app import db
import datetime
from werkzeug import secure_filename

class Archivo(db.Document):
    nombre = db.StringField(max_length=200, required=True)
    date = db.DateTimeField(default=datetime.datetime.now)
    usuario = db.StringField(max_length=200, required=True)
    archivo = db.FileField()

    @classmethod
    def create_by_upload(kls, file, usuario):
        a = Archivo()
        filename = secure_filename(file.filename)
        a.nombre = filename
        a.usuario = usuario
        a.archivo.put(file, content_type=file.content_type, filename=filename)
        a.save()
