##erica and patrick look at STR data
##it is the goodest of time

str=read.csv("/Users/ps22344/Downloads/allspeakers_normalized_metadata_lemmas.csv", header=T)
#summary(str)

#setting up the wdir
setwd("/Users/ps22344/Downloads/plots")


#let us plot the s, sh and str for each speaker

speakers=levels(str$speaker)
print (speakers)


for (spkr in speakers)
{
	 print (spkr);
	 #this is the data for the speaker only
	tempdata=str[str$speaker==spkr,];
	# # print ("SS")
	# #let us try a little thing that prints out how many tokens we have for each sound
	print ("SH");
	print (summary(tempdata[tempdata$env=="SH",]));
	print ("STR");
	print (summary(tempdata[tempdata$env=="STR",]));
	print ("\n\n\n------------\n\n");
	png(paste(spkr, ".png"), width=550, height=550);
	#just setting up the plot here
	plot(tempdata[tempdata$env=="S",]$cog2, type="n", ylim=c(234,11626), xlim=c(0,7), main=spkr);
	#here be the plots
	points(tempdata[tempdata$env=="STR",]$env, tempdata[tempdata$env=="STR",]$cog2);
	points(tempdata[tempdata$env=="S",]$env,tempdata[tempdata$env=="S",]$cog2, pch="S");
	points(tempdata[tempdata$env=="SH",]$env, tempdata[tempdata$env=="SH",]$cog2, pch="ʃ");
	dev.off()
}


# let us look at mean, SD etc of COG


for (spkr in speakers)
{
	writeLines("\n\n***************\n\n");
	#print (cat("\n\n***************\n\n"))
	#print ("\n\n***************\n\n")
	print (paste("SPEAKER:", spkr));
	#this is the data for the speaker only
	tempdata=str[str$speaker==spkr,];
	#let us try a little thing that prints out stuff
	for (var in c("S", "SH", "STR"))
	{
		writeLines("\n");
		print (var);
		print (paste("tokens: ", nrow(tempdata[tempdata$env==var,]),sep="   "));
		print (paste("range: ", min(tempdata[tempdata$env==var,]$cog2), max(tempdata[tempdata$env==var,]$cog2), sep="   "));
		print (paste("mean: ", mean(tempdata[tempdata$env==var,]$cog2),sep="   "));
		print (paste("standard dev: ", sd(tempdata[tempdata$env==var,]$cog2),sep="   "))
		
	 }
	
}
