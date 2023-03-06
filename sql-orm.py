import sql_creds
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from our localhost "chinook" db

db = create_engine(
    sql_creds.DATABASE + "://"
    + sql_creds.DB_USERNAME
    + ":" + sql_creds.DB_PASSWORD
    + "@" + sql_creds.HOST
    + ":" + str(sql_creds.PORT)
    + "/" + sql_creds.DB_NAME)

base = declarative_base()


class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


class Genre(base):
    __tablename__ = "Genre"
    GenreId = Column(Integer, primary_key=True)
    Name = Column(String)


class Invoice(base):
    __tablename__ = "Invoice"
    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(Integer, primary_key=False)
    InvoiceDate = Column(String)
    BillingAddress = Column(String)
    BillingCity = Column(String)
    BillingState = Column(String)
    BillingCountry = Column(String)
    BillingPostalCode = Column(String)
    Total = Column(Float)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)


artists = session.query(Artist).all()
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep = " | ")

# for artist in artists:
#     print(artist.Name)

# albums = session.query(Album).all()
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep = " | ")

# albums = session.query(Album).filter(Album.ArtistId == 51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# genre = session.query(Genre).filter(Genre.Name == "Rock").first()
# genre = session.query(Genre).all()
# for gen in genre:
#     print(gen.GenreId, gen.Name, sep=" | ")

# tracks = session.query(Track).all()
# for track in tracks:
#     print(track.TrackId, track.Name, track.AlbumId, track.MediaTypeId,
#           track.GenreId, track.Composer, track.Milliseconds, track.Bytes,
#           track.UnitPrice, sep = " | ")

tracl = session.query(Track).filter(Track.Composer == 'Queen')
for track in tracl:
    print(track.TrackId, track.Name, track.AlbumId, track.MediaTypeId,
          track.GenreId, track.Composer, track.Milliseconds, track.Bytes,
          track.UnitPrice, sep=" | ")

# invoices = session.query(Invoice).all()
# for inv in invoices:
#     print(inv.InvoiceId, inv.CustomerId, inv.InvoiceDate, inv.BillingAddress,
#           inv.BillingCity, inv.BillingState, inv.BillingCountry,
#           inv.BillingPostalCode, inv.Total, sep=" | ")




















