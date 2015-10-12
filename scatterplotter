##reading the dir
##directory=choose.dir()
setwd("H:/str/rplots")
directory="H:/str/finalfiles";
filis=list.files(path=directory);
print("no of files");
print(length(filis));
for (fili in filis)
{
print("------------------");
print (fili);
dataset=read.csv(paste(directory,fili, sep="/"), header=T);
speaker=levels(as.factor(dataset$speaker));
print(speaker);
styles=levels(as.factor(dataset$style));
print("style");
print(styles);
for (styli in styles)
{
print (styli);
styledataset=subset(dataset, dataset$style==styli);
envs=levels(styledataset$env);
print (envs);
print (length(envs));
tokens=nrow(styledataset);
#print (tokens);

#par(mfrow=c(1,length(envs)));
for (env in envs)
{
png(filename=paste(speaker,"_", styli,"_",env,"_scatter.png", sep=""), width=1600, height=800);
print(env);
plot(sort(dataset[dataset$env==env,]$cog2), main=paste(speaker,env));
dev.off()
}
}
}
