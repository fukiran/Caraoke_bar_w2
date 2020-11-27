import unittest

from src.song import Song
from src.guest import Guest
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Bongo", 3)
        self.room_2 = Room("Studio 24", 5)

        self.guest_1 = Guest("Pierre")
        self.guest_2 = Guest("Alexander")
        self.guest_3 = Guest("Pepe")
        self.guest_4 = Guest("Edi")

        self.song_1 = Song("Gotta Go", "Agnostic Front", 3.2)
        self.song_2 = Song("On My Radio", "Selecter", 3.52)
        self.song_3 = Song("Divorce a I'ltalienne", "Mungo's Hifi", 3.46)


    def test_room_has_name(self):
        self.assertEqual("Bongo",self.room_1.name)
    

    def test_room_has_capacity(self):
        self.assertEqual(True,isinstance(self.room_1.capacity,int))


    def test_guest_list_empty(self):
        self.assertEqual([],self.room_1.guest_list)


    def test_song_list_empty(self):
        self.assertEqual([],self.room_2.song_list)


    def test_add_guest_to_list(self):
        self.room_1.add_guest_to_list(self.guest_1)
        self.assertEqual(1,len(self.room_1.guest_list))

    
    def test_add_guests_to_list(self):
        self.room_1.add_guest_to_list(self.guest_1)
        self.room_1.add_guest_to_list(self.guest_2)
        self.assertEqual(2,len(self.room_1.guest_list))


    def test_remove_guest_from_list(self):
        self.room_1.add_guest_to_list(self.guest_1)
        self.room_1.remove_guest_from_list(self.guest_1)
        self.assertEqual([],self.room_1.guest_list)



    