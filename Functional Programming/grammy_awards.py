# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]


def longer_than_5(song):
    return song[1] > 5

longer_songs = filter(longer_than_5, playlist)
print(list(longer_songs))

def convert_to_seconds(song):
    return song[1] * 60 

converted_to_seconds = map(convert_to_seconds,playlist)     
print(list(converted_to_seconds))  

