#Quick and dirty way of cleaning automatically generated subtitle files for the ATNU speaker series

#read original vtt file
subtitles_original = open("GMT20210223-170445_ATNU-IES-V.transcript.vtt", "r")
#put text into string
text = subtitles_original.read()
#close original file
subtitles_original.close()

#replace moderator name with nothing
text = text.replace('James Cummings: ', '')

#replace speaker name with nothing
text = text.replace('Mike Kestemont: ', '')

#create new file and write clean subtitles to it
final_file = open("clean_subtitles.vtt", 'w')
final_file.write(text)
final_file.close()
