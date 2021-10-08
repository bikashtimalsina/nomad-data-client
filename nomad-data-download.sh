#!/bin/bash
TOTAL_FILES=`cat DownloadFiles.txt|wc -l`
# The python script generates the calc id and upload id of all search based on the criteria and the url link into a text file
# This script then download the data mainly vasprun.xml. This is only for getting VASP data. However other data from Quantum Espresso can also be obtained accordingly
if [ -d "NOMAD-Files" ];then
rm -rf NOMAD-Files
fi
mkdir NOMAD-Files
for (( i=1; i<=${TOTAL_FILES}; i++ )){
url=`cat DownloadFiles.txt|sed -n ${i}p|awk -F "\t" '{print $5}'`
tag=`cat DownloadFiles.txt|sed -n ${i}p|awk -F "\t" '{print $1}'`
filename=`cat DownloadFiles.txt|sed -n ${i}p|awk -F "\t" '{print $4}'`
wget $url
wait $!
mv ${filename} ./NOMAD-Files/${tag}_${i}_${filename}
}
