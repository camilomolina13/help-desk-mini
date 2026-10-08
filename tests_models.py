import unittest

from app import create_app
from models import db, User, Ticket


class TicketTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app("config.TestConfig")
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    # PRUEBA 1
    def test_create_ticket_associated_with_user(self):

        with self.app.app_context():

            user = User(
                username="camilo321",
                password="123456"
            )

            db.session.add(user)
            db.session.commit()

            ticket_db = Ticket(
                title="Título",
                description="Descripción",
                user_id=user.id
            )

            db.session.add(ticket_db)
            db.session.commit()

            self.assertEqual(ticket_db.user_id, user.id)

    # PRUEBA 2
    def test_tickets_without_session_redirects_to_login(self):

        response = self.client.get("/")

        self.assertEqual(response.status_code, 302)

    # PRUEBA 3
    def test_short_title_does_not_create_ticket(self):

        with self.app.app_context():

            user = User.query.filter_by(
                username="camilo321"
            ).first()

            tickets_before = Ticket.query.count()

            with self.client.session_transaction() as session:
                session["user_id"] = user.id

            response = self.client.post(
                "/create",
                data={
                    "title": "abc",
                    "description": "Esta es una descripción suficientemente larga para superar la validación."
                }
            )   

        with self.app.app_context():

            tickets_after = Ticket.query.count()

            self.assertEqual(tickets_after, tickets_before)