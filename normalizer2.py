import codecs; import os; import collections; import numpy

#our normalization formula
#
#(raw score-((mean(s)-mean(sh))/2)
#------------------------------------------
# sd(all measurements of speaker)

#enter directory to be processed here
directory="H:/05_Speaker_csv_files"
datafiles=["LB.csv"]
#os.listdir(directory)

#readings csvs
def csvreader(filename):
    f=codecs.open(str(filename), "r", "utf-8")
    spreadsheet=[]
    for line in f:
        #note that we need to restrip differently depending on mac or windows
        spreadsheet.append(line.rstrip("\r\n").split(","))
    #print "number of rows: ", len(spreadsheet)
    return spreadsheet


#making means and such for each spreadsheet
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
def normalizer(row, dicti, stdev):
    variable=row[3]
    cog2=float(row[9])
    #here cometh the formula
    numerator=cog2-((dicti["S"][0][0]-dicti["SH"][0][0])/2)
    print dicti["S"][0][0]
    print dicti["SH"][0][0]
    denominator=stdev
    normalized_value=numerator/denominator
    return ([variable,normalized_value])
    
    


#what environment do we want to look at?
envs=["S","SH","STR", "ST", "SK", "SP"]



#Main
#establishing mean, median, and stdev
for item in datafiles:
    #this dictioanry collects the means etc for each env for this speaker.
    meandicti=collections.defaultdict(list)
    print item
    #we read in the csv files, dump all the data in the gigalist
    dati=csvreader(os.path.join(directory,item))
    for envi in envs:
        #we fill the dictionary with the respective values
        meandicti[envi].append(meanmachine(envi, dati))
    # we calculate the stdev over all measurements by taking
    #the values for each env from the dictionary
    allvalues=[meandicti[envi][0][3] for envi in envs]
    #we need to flatten that
    allvalues_flat=[item for sublist in allvalues for item in sublist]
    stdev=numpy.std(allvalues_flat)
    print stdev
    for row in dati[1:len(dati)]:
        #print row
        result=normalizer(row, meandicti, stdev)
        #row.append(result)
        print result
        
        #print row
        
    

print len(meandicti)

    #meandicti[s_list.append(meanmachine("S", dati)
    #sh_list.append(meanmachine("SH", dati)
    #str_list.append(meanmachine("SH", dati)
    #st_list.append(meanmachine("ST", dati)
    #sk_list.append(meanmachine("SK", dati)
    #sp_list.append(meanmachine("SP", dati)


#get all the S, SH, etc for a mean
#put that mean into list
#normalizing data
#raw score-population mean) / population standard deviation
