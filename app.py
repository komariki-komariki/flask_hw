import flask
from flask import Flask, request
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask.views import MethodView

app = Flask('app')
engine = create_engine('postgresql+psycopg2://postgres:Komar529+@localhost/db_flask')
DeclarativeBase = declarative_base()
Session = sessionmaker(bind=engine)

class Advertisement(DeclarativeBase):
    __tablename__ = 'advertisement'

    id = Column(Integer, primary_key=True)
    heading = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date_of_creation = Column(DateTime, server_default=func.now())
    owner = Column(String(64), nullable=False)

DeclarativeBase.metadata.create_all(engine)

class AdvertisementView(MethodView):

    def get(self, advertisement_id):
        with Session() as session:
            advertisement = session.query(Advertisement).get(advertisement_id)
            return {
                'id': advertisement.id,
                'heading': advertisement.heading,
                'description': advertisement.description,
                'owner': advertisement.owner,
                'date_of_creation': advertisement.date_of_creation.isoformat()
            }

    def post(self):
        advertisement_data = request.json
        with Session() as session:
            new_advertisement = Advertisement(heading=advertisement_data['heading'],
                                              description=advertisement_data['description'],
                                              owner=advertisement_data['owner']
                                              )
            session.add(new_advertisement)
            session.commit()
            return flask.jsonify({'status': 'ok', 'id': new_advertisement.id})

    def delete(self, advertisement_id):
        with Session() as session:
            advertisement = session.query(Advertisement).get(advertisement_id)
            # advertisement = session.query(Advertisement).filter(Advertisement.id == advertisement_id).first()
            session.delete(advertisement)
            session.commit()
            return flask.jsonify({'status': 'ok'})

    def patch(self,advertisement_id):
        advertisement_data = request.json
        with Session() as session:
            advertisement = session.query(Advertisement).get(advertisement_id)
            for key, value in advertisement_data.items():
                setattr(advertisement, key, value)
            session.commit()
        return flask.jsonify({'status': 'ok'})


app.add_url_rule('/advertisement', view_func=AdvertisementView.as_view('advertisement'), methods=['POST'])
app.add_url_rule('/advertisement/<int:advertisement_id>', view_func=AdvertisementView.as_view('advertisement_get'),
                 methods=['GET', 'PATCH', 'DELETE'])
app.run()