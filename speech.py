#!/Users/UserName/speech-analysis-env/bin/python
import myspsolution as mysp
# Audio file title
p="test"
# path to audio file directory
c=r"/Users/UserName/speech/speech-files"

mysp.myspsyl(p,c)

# Gender recognition and mood of speech 
mysp.myspgend(p,c)

#pronunciation posteriori probablility score percentage
mysp.mysppron(p,c)

# detect and count number of syllables

# detect and count number of fillers and pauses
mysp.mysppaus(p,c)

# measure the rate of speech

# measure the articulation (speed). Output is syllables/sec speaking duration
mysp.myspatc(p,c)

# measure speaking time (excl. fillers and pauses)
mysp.myspst(p,c)

# measure total speaking duration (inc. fillers and pauses)
mysp.myspod(p,c)

# measure ratio between speaking duration and total speaking duration

mysp.myspf0q75(p,c)



mysp.mysptotal(p,c)
