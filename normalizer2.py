import codecs; import os; import collections; import numpy
os.chdir("H:/str/files")

#our normalization formula
#
#(raw score-((mean(s)-mean(sh))/2)
#------------------------------------------
# sd(all measurements of speaker)

#enter directory to be processed here
directory="H:/05_Speaker_csv_files"
datafiles=os.listdir(directory)

#readings csvs
def csvreader(filename):
    f=codecs.open(str(filename), "r", "utf-8")
    spreadsheet=[]
    for line in f:
        #note that we need to restrip differently depending on mac or windows
        spreadsheet.append(line.rstrip("\r\n").split(","))
    #print "number of rows: ", len(spreadsheet)
    return spreadsheet


#making means and such for each spreadsheet/speaker
#takes an env (i.e. ST, STR...) and the dataset to extract it from 
def meanmachine(env, dataset):
    cogs=[]
    for row in dataset:
        #item[3] is the env, item[9] the cog2 measurement
        if row[3]==env:
           cogs.append(float(row[9]))
    #getting mean, stdev, median out of the cog measurements
    mean=numpy.mean(cogs)
    stdev=numpy.std(cogs)
    median=numpy.median(cogs)
    #print "mean", mean
    #print "standard dev", stdev
    return([mean, stdev, median, cogs])


#normalizing individual data points once we have the relevant means etc
#takes a row of data, the dictionary with means etc and the standard deviation
#we'll be owrking with
def normalizer(row, dicti, stdev):
    variable=row[3]
    cog2=float(row[9])
    #here cometh the formula
    numerator=cog2-((dicti["S"][0][0]-dicti["SH"][0][0])/2)
    denominator=stdev
    normalized_value=numerator/denominator
    return ([variable,normalized_value])
    
    


#what environment do we want to look at?
envs=["S","SH","STR", "ST", "SK", "SP"]



#MAIN
#establishing mean, median, and stdev
for fili in datafiles:
    #this dictioanry collects the means etc for each env for this speaker.
    meandicti=collections.defaultdict(list)
    print "\n\n-----\n\nfile: ",fili
    #we read in the csv files, dump all the data in the gigalist
    dati=csvreader(os.path.join(directory,fili))
    for envi in envs:
        #print envi
        #we fill the dictionary with the respective values
        meandicti[envi].append(meanmachine(envi, dati))
    # we calculate the stdev over all measurements by taking
    #the values for each env from the dictionary
    allvalues=[meandicti[envi][0][3] for envi in envs]
    #we need to flatten that
    allvalues_flat=[i for sublist in allvalues for i in sublist]
    stdev=numpy.std(allvalues_flat)
    #
    #Just a lot of printing here
    #
    print "----\n\nstandard deviation ", stdev
    print "mean and median S ", meandicti["S"][0][0], meandicti["S"][0][2]
    print "mean and median SH ", meandicti["SH"][0][0], meandicti["SH"][0][2]
    print "mean and median STR ", meandicti["STR"][0][0], meandicti["STR"][0][2]
    #
    #
    output=open(fili.rstrip(".csv")+"_normalized.csv", "a")
    #we write the column names
    t=dati[0]+[u"cog2_normalized", u"env_extracted\n"]
    output.write(",".join(t))
    #we start at position 1 so we don't get the column names in our machinery
    for row in dati[1:len(dati)]:
        #normalizer returns normalized value and the env
        result=normalizer(row, meandicti, stdev)
        row.append(unicode(result[1]))
        row.append(result[0])
        output.write(",".join(row)+"\n")
    output.close()

