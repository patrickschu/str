import codecs; import os; import collections; import numpy

#enter directory to be processed here
directory="H:/05_Speaker_csv_files"
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

def meanmachine(valuelist):
    mean=numpy.mean(valuelist)
    stdev=numpy.std(valuelist)
    print "mean", mean
    print "standard dev", stdev
    return([mean, stdev])
    
    

#normalizing data
#def normalizer():
#    (raw score-population mean) / population standard deviation

gigalist=[]

for item in datafiles:
    #we read in the csv files, dump all the data in the gigalist
    dati=csvreader(os.path.join(directory,item))
    gigalist.append(dati[1:len(dati)])
    print len(dati)

print "length of gigalist", len(gigalist)

#we flatten the gigalist so that we end up with a list of rows
flatgigalist=[item for sublist in gigalist for item in sublist]
print "length of flatlist", len(flatgigalist)

#setting up more lists, this time to collect all values for a given env

s_list=[]
sh_list=[]
str_list=[]
st_list=[]
sk_list=[]
sp_list=[]
#we'll make this into an iteration
for item in flatgigalist:
    item[9]=int(item[9])
    #item[3] is the env, item[9] the cog2 measurement
    if item[3] == "S":
        s_list.append(item[9])
    if item[3] =="SH":
        sh_list.append(item[9])
    if item[3] =="STR":
        str_list.append(item[9])
    if item[3] =="ST":
        st_list.append(item[9])
        #print "st success"
    if item[3] =="SK":
        sk_list.append(item[9])
    if item[3] =="SP":
        sp_list.append(item[9])
    #else:
    #    print item[3]


total=len(st_list)+len(s_list)+len(sh_list)+len(str_list)+len(sk_list)+len(sp_list)
print "total envs extracted:", total

s_population=meanmachine(s_list)
sh_population=meanmachine(sh_list)
str_population=meanmachine(str_list)
st_population=meanmachine(st_list)
sk_population=meanmachine(sk_list)
sp_population=meanmachine(sp_list)

print "\n\nPopulation\nMeans and Standard Deviations\n----------"
print "S", s_population[0], s_population[1]
print "SH", sh_population[0], sh_population[1]
print "STR", str_population[0], str_population[1]
print "ST", st_population[0], st_population[1]
print "SK", sk_population[0], sk_population[1]
print "SP", sp_population[0], sp_population[1]

#for line in gigaflatfile: add normalized version of cog2 measurement


