from animal_api.database import db


class Fact(db.Model):
    """
    Fact Flask-SQLAlchemy Model

    Represents objects contained in the facts table
    """

    __tablename__ = "facts"

    fact_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    animal_name = db.Column(db.String(50), nullable=False)
    source = db.Column(db.String(), nullable=False)
    text = db.Column(db.String(1000), unique=True, nullable=False)
    media_link = db.Column(db.String())
    wikipedia_link = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return (
            f"**Fact** "
            f"fact_id: {self.fact_id} "
            f"animal_name: {self.animal_name} "
            f"source: {self.source}"
            f"text: {self.text}"
            f"media_link: {self.media_link}"
            f"wikipedia_link: {self.wikipedia_link}"
            f"**Fact** "
        )

    def __str__(self):
        return (
            f"**Fact** "
            f"fact_id: {self.fact_id} "
            f"animal_name: {self.animal_name} "
            f"source: {self.source}"
            f"text: {self.text}"
            f"media_link: {self.media_link}"
            f"wikipedia_link: {self.wikipedia_link}"
            f"**Fact** "
        )
