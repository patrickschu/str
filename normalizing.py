import codecs; import os; import collections

#enter directory to be processed here
directory="H:\cogfiles_new"
datafiles=os.listdir(directory)


os.chdir("H://str//files")


#readings csvs
def csvreader(filename):
    f=codecs.open(str(filename), "r", "utf-8")
    spreadsheet=[]
    for line in f:
        #note that we need to restrip differently depending on mac or windows
        spreadsheet.append(line.rstrip("\n").split(","))
    #print "number of rows: ", len(spreadsheet)
    return spreadsheet

#MAIN 
#read them in
filedicti={}
for item in datafiles:
    #plan: we put all the files in a dict and associate with list of contents
    filedicti[item]=csvreader(os.path.join(directory,item))

#consolidate by speaker
for item in filedicti:
    print item
    print len(filedicti[item])
    speakername=raw_input("speaker name?\n")
    filedicti[item].append(speakername)
    print len(filedicti[item]),"\n\n------------\n\n"

#consolidate by style
for item in filedicti:
    print item
    print len(filedicti[item])
    style=raw_input("style?\ninterview=iv, reading=r, lara=lara, wordlist=wl")
    filedicti[item].append(style)
    print len(filedicti[item]),"\n\n------------\n\n"
    
    
#make speakerdicti
speakerdicti=collections.defaultdict(list)

for item in filedicti:
    speaker=filedicti[item][len(filedicti[item])-2]
    speakerdicti[speaker].append(filedicti[item])


for item in speakerdicti:
	print "\n\n\nitem", item
	entry=speakerdicti[item]
	output=open(item+".csv", "a")
	#for each file we nedd the column names
	columns=entry[0][0]
	output.write(",".join(columns)+"\n")
	#iterate over the csv files that went into this
	for fili in entry:
		#for each file, we need to identify speaker and style
		speaker=fili[len(fili)-2]
		style=fili[len(fili)-1]
		print "speaker", speaker
		print "style", style
		#in here, we take each row of the csvfiles except for the first one, which are the column names and the last two which are style and speaker info
		for row in fili[1:len(fili)-2]:
			output.write(speaker+","+",".join(row[1:14])+","+style+","+row[15]+"\n")
	output.close()
