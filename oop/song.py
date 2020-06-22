# a_string = "This is \na string split\t\t and tabbed"
# print(a_string)
#
# raw_string = r"This is \na string split\t\t and tabbed"
# print(raw_string)
#
# b_string = "This is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
# print(b_string)
#
# backslash_string = 'This is a backslash \followed by some text'
# print(backslash_string)
#
# backslash_string = 'This is a backslash \\followed by some text'
# print(backslash_string)

# error_string = 'This string end with \'
# error_string = r'This string end with \'
# error_string = 'This string end with \\'
# error_string = r'This string end with \\'
# print(error_string)

# All String in python is unicode
# Everything in python is object


class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song.
        artist (Artist): An Artist object representing the songs creator.
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year was album was released.
        artist (Artist): The artist responsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist('Various Artists')
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Add a song to the track list

        Args:
            song: A song to add.
            position (optional[int]): If specified, the song will be added to that position
                in the list - inserting it between other songs if necessary
                Otherwise, the song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """ Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums.

        Methods:
            add_album: Use to add a new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                if the album is already present, it will not added again (although this is yet to implemented).
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            # print(tuple(line.rstrip().split('\t')))
            # print(line.rstrip().split('\t'))
            # print(line.rstrip())
            # print(line.strip('\n'))
            # print(line)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)


if __name__ == '__main__':
    load_data()
