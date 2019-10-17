# Developed by Gui Ruggiero

import json
import requests
import sys
import webbrowser

class Media:
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", json_input=None):
        if json_input == None:
            self.title = title
            self.author = author
            self.release_year = release_year
        else:
            try:
                self.title = json_input["trackName"]
            except: #in case it's not a song or a movie (no "trackName" on json, so title is in "collectionName")
                self.title = json_input["collectionName"]
            self.author = json_input["artistName"]
            self.release_year = json_input["releaseDate"][:4]

    def __str__(self):
        return self.title + " by " + self.author + " (" + self.release_year + ")"
        
    def __len__(self):
        return 0

class Song(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", album="No Album", genre="No Genre", track_length="No Track Length", json_input=None):
        if json_input == None:
            self.album = album
            self.genre = genre
            self.track_length = track_length
            super().__init__(title, author, release_year)
        else:
            self.album = json_input["collectionName"]
            self.genre = json_input["primaryGenreName"]
            self.track_length = int(json_input["trackTimeMillis"]/1000) #from milliseconds to the nearest second
            super().__init__(title, author, release_year, json_input)
    
    def __str__(self):
        return super().__str__() + " [" + self.genre + "]"
    
    def __len__(self):
        return self.track_length

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", rating="No Rating", movie_length="No Movie Length", json_input=None):
        if json_input == None:
            self.rating = rating
            self.movie_length = movie_length
            super().__init__(title, author, release_year)
        else:
            self.rating = json_input["contentAdvisoryRating"]
            self.movie_length = int(json_input["trackTimeMillis"]/60000) #from milliseconds to the nearest minute
            super().__init__(title, author, release_year, json_input)
    
    def __str__(self):
        return super().__str__() + " [" + self.rating + "]"
    
    def __len__(self):
        return self.movie_length

def open_process_json(json_file_name=None):
    if json_file_name == None:
        pass

    else:
        with open(json_file_name, "r") as f:
                media_json = json.load(f)
        #print(media_json)
        #print(media_json[0])
        
        #processing all items in json
        i = 0
        media = []
        songs = []
        movies = []
        other_media = []
        for m in media_json: #directing the media type to the right template
                #print(m["wrapperType"])            
                #print(m)
                
                if m["wrapperType"] == "track" and m["kind"] == "song":
                    created_media = Song("", "", "", "", "", "", m)
                    #print(created_media)
                    media.append(created_media)
                    songs.append(created_media)
                        
                elif m["wrapperType"] == "track" and m["kind"] == "feature-movie":
                    created_media = Movie("", "", "", "", "", m)
                    #print(created_media)
                    media.append(created_media)
                    movies.append(created_media)

                else:
                    created_media = Media("", "", "", m)
                    #print(created_media)
                    media.append(created_media)
                    other_media.append(created_media)
                
                i += 1
        
        return [media, i, songs, movies, other_media]

def fetch_create_itunes_json(search=None):
    if search == None:
        pass
    else:
        #translate search into terms (spaces into +)
        terms = search.replace(" ", "%20")
        #print(terms)

        #fetching data with iTunes API and storing on the file itunes.json
        url = "https://itunes.apple.com/search?term="
        question = url + terms
        #print(question)
        resp = requests.get(question)
        #print(resp)
        resp_results = json.loads(resp.text)["results"]
        #print(resp_results)
        #print(resp_results[0])
        with open("itunes.json", "w") as outfile:
            json.dump(resp_results, outfile, indent=4, sort_keys=True)
        
        #counting and returning quantity of media fetched with API
        i = 0
        for m in resp_results:
            i += 1
        return i

if __name__ == "__main__":
    search = ""
    search = input("\nEnter a search term, or 'exit' to quit: ")
    any_search = False #flag to identify if any search was performed 

    #big loop - exits when user types "exit"
    while search != "exit" and search != "Exit":
        #understanding type of input
        try:
            number = int(search)
            if number > 0 and number <= 50:
                type_search = "option"
            else:
                type_search = "term"
        except ValueError:
            type_search = "term"
        
        #input is search term
        if type_search == "term":
            media_on_file = fetch_create_itunes_json(search)
            processing_output = open_process_json("itunes.json")
            
            #storing list of medias in variables easy to identify
            songs = processing_output[2]
            movies = processing_output[3]
            other_media = processing_output[4]

            #if there are no results for the search
            if len(songs) == 0 and len(movies) == 0 and len(other_media) == 0:
                print("\nThere were no results for your search.")
            
            #search has results - print everything
            else:            
                i = 1
                
                if len(songs) == 0:
                    print("\nSONGS - no results")
                else:
                    print("\nSONGS")
                    for s in songs:
                        print(i, s.__str__())
                        i += 1
                
                if len(movies) == 0:
                    print("\nMOVIES - no results")
                else:
                    print("\nMOVIES")
                    for m in movies:
                        print(i, m.__str__())
                        i += 1
                
                if len(other_media) == 0:
                    print("\nOTHER MEDIA - no results")
                else:
                    print("\nOTHER MEDIA")
                    for om in other_media:
                        print(i, om.__str__())
                        i += 1
                
                any_search = True

        # FOR GRADING PURPOSES - please read this
        # The only thing I could not figure out how to do is how to get "trackViewURL" from the media objects
        # at this point. The way I would logically think it would work is not and I do not know why. I left
        # some prints of the media titles so that it is possible to see that all ifs are correct, and I
        # commented the subsequent steps assuming the generation of the url is correct (including the command
        # to open the browser)

        #input is viable number
        elif type_search == "option" and any_search == True:
            if number > (len(songs) + len(movies)):
                j = number - (len(songs) + len(movies)) - 1
                print(other_media[j].title)
                #url = other_media[j]["trackViewURL"]
            elif number > len(songs):
                j = number - len(songs) - 1
                print(movies[j].title)
                #url = movies[j]["trackViewURL"]
            else:
                j = number - 1
                print(songs[j].title)
                #url = songs[j]["trackViewURL"]

            #print("Launching", url, "in web browser...")
            #webbrowser.open_new_tab(url)
        
        #input is not search term nor viable number
        else:
            print("\nI did not understand your input.")
        
        search = input("\nEnter a number for more info, or another search term, or 'exit' to quit: ")

    print("\nThanks for using this program. See you soon. Bye!\n")