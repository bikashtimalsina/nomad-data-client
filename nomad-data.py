from bravado.client import SwaggerClient
import re
nomad_url = 'http://nomad-lab.eu/prod/rae/api'
# create the bravado client
client = SwaggerClient.from_url('%s/swagger.json' % nomad_url)
# perform the search request to print number of public entries
data = client.repo.search(only_atoms=['Nb', 'Sn']).response().result
# print the total ammount of search results
total_results=data.pagination.total
pages=int(total_results/50)+1
print(total_results)
# print the data of the first result
#get_data_check=https://nomad-lab.eu/prod/rae/api/raw/calc/kp7507aMQFKDGPgVTg7GWQ/P8x0nSIuDOUI1bDfF9XroPPi-gP6/vasprun.xml.relax2 -o download.zip
#url_to_know=https://nomad-lab.eu/prod/rae/api/raw/calc/upload_id/calc_id/vasprun.xml.relax2?length=16384&decompress=true
#next_test_url=http://nomad-lab.eu/prod/rae/api/raw/query?upload_id=kp7507aMQFKDGPgVTg7GWQ -o download.zip
nomad_data=[]
for j in range(pages):
	data = client.repo.search(only_atoms=['Nb','Sn'],page=j+1,per_page=50).response().result
#	client.raw.get(upload_id=calc['upload_id'], path=calc['mainfile']).response()
	data_size=len(data.results)
	for i in range(data_size):
		print(data.results[i]['mainfile'])
		m=re.search(r'vasprun.*',data.results[i]['mainfile'])
		if m is None:
			print("Nothing")
		else:
			print(m.group(0))
			vasprun_string=m.group(0)
			data_fetch="https://nomad-lab.eu/prod/rae/api/raw/calc/"+data.results[i]['upload_id']+"/"+data.results[i]['calc_id']+"/"+vasprun_string
			nomad_data.append([data.results[i]['formula'],data.results[i]['upload_id'],data.results[i]['calc_id'],vasprun_string,data_fetch])
with open("DownloadFiles.txt","w") as file:
	for i in range(len(nomad_data)):
		file.write(nomad_data[i][0])
		file.write("\t")
		file.write(nomad_data[i][1])
		file.write("\t")
		file.write(nomad_data[i][2])
		file.write("\t")
		file.write(nomad_data[i][3])
		file.write("\t")
		file.write(nomad_data[i][4])
		file.write("\n")
file.close()
