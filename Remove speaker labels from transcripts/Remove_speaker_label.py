#Quick and dirty way of cleaning automatically generated subtitle files for the ATNU speaker series

#NEXT STEP: Make it run from command line

def removeSpeakerLabel(fileName, *labelTuple):
    #Error control: if there is no filename, or the filename is not the first argument
    if fileName.endswith(".vtt") == False:
        raise Exception("The first argument must be a file name, ending with the .vtt extension")
    #Error control: if there is nothing to remove from the file
    if len(labelTuple) == 0:
        raise Exception("There's nothing to remove: make sure to indicate the file name and the string(s) to be removed")
    
    original = open(fileName, "r")
    text = original.read()
    original.close()
    
    for label in labelTuple:
        text = text.replace(label, "")
    return text

#Function takes the file name and at least one label to remove
text = removeSpeakerLabel("GMT20210506-160513_Recording.transcript.vtt", "James Cummings: ", "Christof Sch?ch: ")

#create new file and write clean subtitles to it
final_file = open("clean_subtitles.vtt", 'w')
final_file.write(text)
final_file.close()
