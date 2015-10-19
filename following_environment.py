import codecs; import os; import collections; import numpy
os.chdir("H:/str/files")

#enter directory to be processed here
directory="H:/"

#a message from our sponsors
"This script is brought to you by Erica B."

datafile="allspeakers_normalized_metadata_lemmas.csv"

#readings csvs
def csvreader(filename):
    f=codecs.open(str(filename), "r", "utf-8")
    spreadsheet=[]
    for line in f:
        #note that we need to restrip differently depending on mac or windows
        spreadsheet.append(line.rstrip("\r\n").split(","))
    #print "number of rows: ", len(spreadsheet)
    return spreadsheet

stressdict={"1":"prim", "0":"nprim", "2":"nprim"}

hilodict={"AA":"low", "AE":"low", "AW":"low", "AY":"low", "EH":"mid", "EY":"mid",
      "OY":"mid", "OW":"mid", "IH":"high", "IY":"high", "UH":"high", "UW":"high"}



frontbackdict = {"AA":"low", "AE":"low", "AW":"back", "AY":"back", "EH":"front", "EY":"front",
      "OY":"back", "OW":"back", "IH":"front", "IY":"front", "UH":"back", "UW":"back"}

dati=csvreader(os.path.join(directory,datafile))

print "length", len(dati)

output=open("allspeakers_normalized_metadata_lemmas_environment.csv", "a")

for row in dati[1:len(dati)]:
    foll_env=row[8]
    print foll_env
    stress=stressdict.get(foll_env[len(foll_env)-1], "NONE")
    hilo=hilodict.get(foll_env[:-1], "NONE")
    backfront=frontbackdict.get(foll_env[:-1], "NONE")
    #print stress
    #print hilo
    #print backfront
    #print hilo+backfront
    print "-----------\n\n"
    result=[stress, hilo, backfront, hilo+backfront]
    row=row+result
    #print row
    output.write(",".join(row)+"\n")

output.close()
    
    

