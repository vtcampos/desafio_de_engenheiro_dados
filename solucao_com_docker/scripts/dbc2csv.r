library("read.dbc")



dbc_path = 'data/dbc'
csv_path = 'data/csv'


dbc_files = list.files(dbc_path)


dbc2csv = function(dbc_path, dbc_file, csv_path) {
    # Le o .dbc
    df = read.dbc(file.path(dbc_path, dbc_file, fsep='\\')) 
    # Ajusta o nome do csv exportado
    csv_file = paste(substr(dbc_file,1,13),'.csv', sep="") 
    # Exporta o csv
    write.csv(df, file=file.path(csv_path,csv_file, fsep='\\'), row.names=FALSE) 
    print(paste(csv_file, 'Saved'))
}


for (i in dbc_files){
    dbc2csv(dbc_path, i, csv_path)
}