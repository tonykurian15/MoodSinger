import json
from re import X
from flask import render_template


try:
    from emotions import mood
except:
    from sebin.Tensorflow.emotions import mood

def findPlaylist():
    
    print(mood)
    #return render_template('index.html',value=mood)
findPlaylist()

# with open('MyRecords.json', 'r+') as f:
#     data = json.load(f)
#     data['mood'] = '' # <--- add id value.
#     data['play'] = ''
#     f.seek(0)        # <--- should reset file position to the beginning.
#     json.dump(data, f, indent=4)
#     f.truncate()     # remove remaining part

# GET https://api.spotify.com/v1/search
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# change scope accordingly
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='82bfbdab5643413499205755c40d12c9', client_secret='e883f41216e048f39a8cb45130f7d256',
                                               redirect_uri='http://localhost:9000', scope=scope))


# results = sp.search(type="playlist", q="sad", limit=1, market="US")
# x = results["playlists"]["items"][0]["external_urls"]['spotify']
# print(x)

def getplaylist(moodi):
    results = sp.search(type="playlist", q=moodi, limit=1, market="US")
    x = results["playlists"]["items"][0]["external_urls"]['spotify']
    return x
playlist=getplaylist(mood)

print(playlist)

myRecod={'mood': mood,
        'play' : playlist
    }
j=json.dumps(myRecod)
with open('MyRecords.json','w') as f:
    f.write(j)
    f.close()



# results = sp.category_playlists(category_id="")
# results = sp.recommendations(seed_genres="happy")