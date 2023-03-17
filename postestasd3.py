class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if not self.head:
            self.head = new_song
        else:
            current_song = self.head
            while current_song.next:
                current_song = current_song.next
            current_song.next = new_song

    def remove_song(self, title):
        if not self.head:
            return None
        elif self.head.title == title:
            self.head = self.head.next
            return True
        else:
            current_song = self.head
            while current_song.next:
                if current_song.next.title == title:
                    current_song.next = current_song.next.next
                    return True
                current_song = current_song.next
            return False

    def display_playlist(self):
        current_song = self.head
        if not current_song:
            print("it's empty m8")
        else:
            print("my daily playlist:")
            while current_song:
                print(f"{current_song.title} - {current_song.artist}")
                current_song = current_song.next

# membuat objek playlist
daily_playlist = Playlist()

# menambahkan lagu ke dalam playlist
print("sebelum dihapus")
daily_playlist.add_song("OMG", "New Jeans")
daily_playlist.add_song("it's ok!", "Paw's Letter")
daily_playlist.add_song("Winter Poem", "KangHyeWon")
daily_playlist.add_song("Glue Song", "beabadoobee")

# menampilkan lagu yang ada di playlist
daily_playlist.display_playlist()

print(" ")
print(" ")
#menghapus lagu dari playlist
print("setelah dihapus")
daily_playlist.remove_song("OMG")
daily_playlist.display_playlist()
