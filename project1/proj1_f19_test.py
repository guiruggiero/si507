# Developed by Gui Ruggiero

import proj1_f19 as proj1
import unittest

class TestMedia(unittest.TestCase):
    def test_part1_Media_constructor(self):
        media1 = proj1.Media()
        media2 = proj1.Media("Harry Potter and the Philosopher's Stone", "J. K. Rowling", "1997")

        #testing empty constructor
        self.assertEqual(media1.title, "No Title")
        self.assertEqual(media1.author, "No Author")
        self.assertEqual(media1.release_year, "No Release Year")

        #testing constructor with random media (book)
        self.assertEqual(media2.title, "Harry Potter and the Philosopher's Stone")
        self.assertEqual(media2.author, "J. K. Rowling")
        self.assertEqual(media2.release_year, "1997")

        #testing other methods
        self.assertEqual(media2.__str__(), "Harry Potter and the Philosopher's Stone by J. K. Rowling (1997)")
        self.assertEqual(media2.__len__(), 0)

        #testing non-existence of non-pertinent instance variables
        with self.assertRaises(AttributeError): media2.album
        with self.assertRaises(AttributeError): media2.genre
        with self.assertRaises(AttributeError): media2.track_length
        with self.assertRaises(AttributeError): media2.rating
        with self.assertRaises(AttributeError): media2.movie_length

    def test_part1_Song_constructor(self):
        song1 = proj1.Song()
        song2 = proj1.Song("Vertigo", "U2", "2004", "How to Dismantle an Atomic Bomb", "Rock", 191)

        #testing empty constructor
        self.assertEqual(song1.title, "No Title")
        self.assertEqual(song1.author, "No Author")
        self.assertEqual(song1.release_year, "No Release Year")
        self.assertEqual(song1.genre, "No Genre")
        self.assertEqual(song1.track_length, "No Track Length")

        #testing constructor with random song
        self.assertEqual(song2.title, "Vertigo")
        self.assertEqual(song2.author, "U2")
        self.assertEqual(song2.release_year, "2004")
        self.assertEqual(song2.album, "How to Dismantle an Atomic Bomb")
        self.assertEqual(song2.genre, "Rock")
        self.assertEqual(song2.track_length, 191)

        #testing other methods
        self.assertEqual(song2.__str__(), "Vertigo by U2 (2004) [Rock]")
        self.assertEqual(song2.__len__(), 191)

        #testing non-existence of non-pertinent instance variables
        with self.assertRaises(AttributeError): song2.rating
        with self.assertRaises(AttributeError): song2.movie_length
    
    def test_part1_Movie_constructor(self):
        movie1 = proj1.Movie()
        movie2 = proj1.Movie("The Matrix", "The Wachowskis", "1999", "R", 150)

        #testing empty constructor
        self.assertEqual(movie1.title, "No Title")
        self.assertEqual(movie1.author, "No Author")
        self.assertEqual(movie1.release_year, "No Release Year")
        self.assertEqual(movie1.rating, "No Rating")
        self.assertEqual(movie1.movie_length, "No Movie Length")

        #testing constructor with random movie
        self.assertEqual(movie2.title, "The Matrix")
        self.assertEqual(movie2.author, "The Wachowskis")
        self.assertEqual(movie2.release_year, "1999")
        self.assertEqual(movie2.rating, "R")
        self.assertEqual(movie2.movie_length, 150)

        #testing other methods
        self.assertEqual(movie2.__str__(), "The Matrix by The Wachowskis (1999) [R]")
        self.assertEqual(movie2.__len__(), 150)

        #testing non-existence of non-pertinent instance variables
        with self.assertRaises(AttributeError): movie2.album
        with self.assertRaises(AttributeError): movie2.genre
        with self.assertRaises(AttributeError): movie2.track_length

    def test_part2_constructors_json(self):
        processing_output = proj1.open_process_json("sample_json.json")
        #print(processing_output)
        #print(processing_output[0])
        #print(len(processing_output[0])
        #print(processing_output[0][0])
        #print(processing_output[0][0].title)

        #testing movie constructed with json data
        self.assertEqual(processing_output[0][0].title, "Jaws")
        self.assertEqual(processing_output[0][0].author, "Steven Spielberg")
        self.assertEqual(processing_output[0][0].release_year, "1975")
        self.assertEqual(processing_output[0][0].rating, "PG")
        self.assertEqual(processing_output[0][0].__str__(), "Jaws by Steven Spielberg (1975) [PG]")
        self.assertEqual(processing_output[0][0].__len__(), 124)

        #testing song constructed with json data
        self.assertEqual(processing_output[0][1].title, "Hey Jude")
        self.assertEqual(processing_output[0][1].author, "The Beatles")
        self.assertEqual(processing_output[0][1].release_year, "1968")
        self.assertEqual(processing_output[0][1].album, "TheBeatles 1967-1970 (The Blue Album)")
        self.assertEqual(processing_output[0][1].genre, "Rock")
        self.assertEqual(processing_output[0][1].__str__(), "Hey Jude by The Beatles (1968) [Rock]")
        self.assertEqual(processing_output[0][1].__len__(), 431)

        #testing media constructed with json data
        self.assertEqual(processing_output[0][2].title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(processing_output[0][2].author, "Helen Fielding")
        self.assertEqual(processing_output[0][2].release_year, "2012")
        self.assertEqual(processing_output[0][2].__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")
        self.assertEqual(processing_output[0][2].__len__(), 0)
    
    def test_part3_api(self):
        #proj1.fetch_create_itunes_json("helter skelter")
        #media_on_file = proj1.fetch_create_itunes_json("helter skelter")
        #print("\nMedia retrieved with API:", media_on_file)

        search = ["baby", "love", "moana", "helter skelter", "&@#!$", ""]
        for s in search:
            media_on_file = proj1.fetch_create_itunes_json(s)
            processing_output = proj1.open_process_json("itunes.json")
            #print(processing_output)
            #print(processing_output[0][0])
            #print("\nSearch term:", s)
            #print("Media retrieved with API:", media_on_file)
            #print("Media processed:", processing_output[1])
            #print("Songs created:", len(processing_output[2]))
            #print("Videos created:", len(processing_output[3]))
            #print("Other media created:", len(processing_output[4]))

            self.assertEqual(media_on_file, processing_output[1])
            #print(len(processing_output[2]) + len(processing_output[3]) + len(processing_output[4]))
            self.assertEqual(processing_output[1], len(processing_output[2]) + len(processing_output[3]) + len(processing_output[4]))

unittest.main(verbosity=2)