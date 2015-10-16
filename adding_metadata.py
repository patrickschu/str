import codecs; import os; import collections

#enter directory to be processed here
directory="H:/07_Speaker_csv_files_normalized"
datafiles=os.listdir(directory)

print datafiles
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

#add gender
for item in filedicti:
    print item
    print len(filedicti[item])
    speakername=raw_input("gender? (male/female)\n")
    filedicti[item].append(speakername)
    print len(filedicti[item]),"\n\n------------\n\n"


#add ethnicity
for item in filedicti:
    print item
    print len(filedicti[item])
    speakername=raw_input("ethnicity? \n")
    filedicti[item].append(speakername)
    print len(filedicti[item]),"\n\n------------\n\n"


#add year born
for item in filedicti:
    print item
    print len(filedicti[item])
    speakername=raw_input("year born? \n")
    filedicti[item].append(speakername)
    print len(filedicti[item]),"\n\n------------\n\n"


    
#make speakerdicti
speakerdicti=collections.defaultdict(list)

for item in filedicti:
    speaker=filedicti[item][len(filedicti[item])-2]
    speakerdicti[speaker].append(filedicti[item])
    
#writing csv files
for item in filedicti:
	print "\n\n\nitem", item
	entry=filedicti[item]
	output=open(item+"_normalized_metadata.csv", "a")
	#for each file we nedd the column names
	columns=entry[0][0]+["region"]
	output.write(",".join(columns)+"\n")
	#iterate over the csv files that went into this
	for fili in entry:
		#for each file, we need to identify speaker and style
                bufferi=fili[len(fili)-7]
		gender=fili[len(fili)-6]
		ethnicity=fili[len(fili)-5]
		yearborn=fili[len(fili)-4]
		region=fili[len(fili)-3]
		interviewyear=fili[len(fili)-2]
		education=[len(fili)-1]
		print "buffer", bufferi
		print "gender", gender
		#in here, we take each row of the csvfiles except for the first one, which are the column names and the last two which are style and speaker info
		for row in fili[1:len(fili)-7]:
			output.write(",".join(row[0:10])+","+bufferi+","+gender+","+yearborn+","+region+","+interviewyear+","+row[13]+","+
                                     +education+","+row[15]+","+row[16]+","+region+","+ethnicity+"\n")
	output.close()


























#version 1

for item in filedicti:
	print "\n\n\nitem", item
	entry=filedicti[item]
	output=open(item.rstrip("_normalized.csv")+"_normalized_metadata.csv", "a")
	#for each file we nedd the column names
	columns=[i.rstrip("\r") for i in entry[0]]
	columns=columns+[u"region", u"ethnicity"]
	print columns
	#print entry
	output.write(",".join(columns)+"\n")
	#iterate over the csv files that went into this
	for fili in entry [1:len(entry)-7]:
		print len(fili)
		#for each file, we need to identify speaker and style
                bufferi=entry[len(entry)-7]
                #print bufferi
		gender=entry[len(entry)-7]
		#print gender
		ethnicity=entry[len(entry)-6]
		#print ethnicity
		yearborn=entry[len(entry)-5]
		#print yearborn
		region=entry[len(entry)-4]
		#print region
		interviewyear=entry[len(entry)-3]
		#print interviewyear
		education=entry[len(entry)-2]
		#print education
		#print "normal", fili[17]
		output.write(",".join(fili[0:11])+","+gender+","+yearborn+","+interviewyear+","+fili[14]+","+education+","+fili[16]+","+fili[17].rstrip("\r")+","+region+","+ethnicity+"\n")
	output.close()




#version 2
tt=['darin_normalized.csv',
'lara08_normalized.csv',
'fh10_normalized.csv',
'lara14_normalized.csv',
'sp1_normalized.csv',
'lara22_normalized.csv',
'lara10_normalized.csv',
'delilah_normalized.csv',
'fh18_normalized.csv',
'KG_normalized.csv',
'fh11_normalized.csv',
'lara19_normalized.csv',
'lv10_normalized.csv',
'lara15_normalized.csv',
'lara21_normalized.csv',
'lv11_normalized.csv',
'lara02_normalized.csv',
'lara18_normalized.csv',
'fh17_normalized.csv',
'lara13_normalized.csv']


for thing in tt:
	print "\n\n\nitem", thing
	entry=filedicti[thing]
	output=open(thing.rstrip("_normalized.csv")+"_normalized_metadata.csv", "a")
	#for each file we nedd the column names
	columns=[i.rstrip("\r") for i in entry[0]]
	columns=columns+[u"region", u"ethnicity"]
	print columns
	#print entry
	output.write(",".join(columns)+"\n")
	#iterate over the csv files that went into this
	for fili in entry [1:len(entry)-8]:
		print len(fili)
		#for each file, we need to identify speaker and style
                bufferi=entry[len(entry)-6]
                #print bufferi
		gender=entry[len(entry)-6]
		#print gender
		ethnicity=entry[len(entry)-5]
		#print ethnicity
		yearborn=entry[len(entry)-4]
		#print yearborn
		region=entry[len(entry)-3]
		#print region
		interviewyear=entry[len(entry)-2]
		#print interviewyear
		education=entry[len(entry)-1]
		print education
		#print "normal", fili[17]
		output.write(",".join(fili[0:11])+","+gender+","+yearborn+","+interviewyear+","+fili[14]+","+education+","+fili[16]+","+fili[17].rstrip("\r")+","+region+","+ethnicity+"\n")
	output.close()


version 3

for thing in ll:
	print "\n\n\nitem", thing
	entry=filedicti[thing]
	output=open(thing+"_normalized_metadata.csv", "a")
	#for each file we nedd the column names
	columns=[i.rstrip("\r") for i in entry[0]]
	columns=columns+[u"region", u"ethnicity"]
	print columns
	#print entry
	output.write(",".join(columns)+"\n")
	#iterate over the csv files that went into this
	for fili in entry [1:len(entry)-8]:
		print len(fili)
		#for each file, we need to identify speaker and style
                #for each file, we need to identify speaker and style
                bufferi=entry[len(entry)-7]
                #print bufferi
		gender=entry[len(entry)-7]
		#print gender
		ethnicity=entry[len(entry)-6]
		#print ethnicity
		yearborn=entry[len(entry)-5]
		#print yearborn
		region=entry[len(entry)-4]
		#print region
		interviewyear=entry[len(entry)-3]
		#print interviewyear
		education=entry[len(entry)-2]
		#print education
		#print "normal", fili[17]
		output.write(",".join(fili[0:11])+","+gender+","+yearborn+","+interviewyear+","+fili[14]+","+education+","+fili[16]+","+fili[17].rstrip("\r")+","+region+","+ethnicity+"\n")
	output.close()

