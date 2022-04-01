from ftplib import *
from logging import exception
import functions
from datetime import date, timedelta
import os
import zipfile
import glob
import shutil 

# Conexão com o servidor 
try:
    

    ftp = FTP('')  #ip servidor
    ftp.login('',open('').read().strip())  #nome de usuario e senha  


    files = ftp.mlsd()
    for item in files:
        file_attributes = dict(item[1])
        modify = file_attributes['modify']
        dataDeOntem = date.today() - timedelta(days=1)
        dataFormatada = date(int(modify[0:4]), int(modify[4:6]), int(modify[6:8]))
    if dataDeOntem > dataFormatada:
     tipoarquivo = file_attributes['type']
     if (tipoarquivo == 'file'):
         nomeArquivo = item[0]
         print(nomeArquivo)
         caminho_pasta =r"C:\projetos\TI\ServicoBackupDatacenter\backup"
         
    ftp.retrbinary(f"RETR {nomeArquivo}", open(f'{caminho_pasta}\{nomeArquivo}','wb').write)
         
    ftp.quit()
   
    # Gerando arquivo .rar

    filename_zip = f'C:\\projetos\\TI\\ServicoBackupDatacenter\\backup\\{functions.diaDaSemana(dataDeOntem.weekday())}.rar'
    fantasy_zip = zipfile.ZipFile(filename_zip, 'w')
 
    for folder, subfolders, files in os.walk('C:\\projetos\\TI\\ServicoBackupDatacenter\\backup'):
     for file in files:
        if (not file.endswith('.rar')):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file),'C:\\projetos\\TI\\ServicoBackupDatacenter\\backup'), compress_type = zipfile.ZIP_DEFLATED)
    fantasy_zip.close()

    # Excluir os arquivos

    files = glob.glob('C:\\projetos\\TI\\ServicoBackupDatacenter\\backup\\**\\*.*' , recursive=True)

    for f in files:
     if not f.endswith('.rar'):
        os.remove(f)

    # Movendo os arquivos para o storage  

    source = f'C:\\projetos\\TI\\ServicoBackupDatacenter\\backup\\{functions.diaDaSemana(dataDeOntem.weekday())}.rar'

    destination = f'Y:\\Receitas\\{functions.diaDaSemana(dataDeOntem.weekday())}.rar'
    shutil.copyfile(source,destination)

    destination2 = f'Z:\\Receitas\\{functions.diaDaSemana(dataDeOntem.weekday())}.rar'
    shutil.copyfile(source,destination2)

# Renomeando o arquivo e movendo, para o HD da Viviane  

    newfile = f'C:\\projetos\\TI\\ServicoBackupDatacenter\\backup\\{functions.renomearArquivoData(dataDeOntem)}'
    os.renames(source,newfile)

    destination3 = f'B:\\{functions.renomearArquivoData(dataDeOntem)}'
    shutil.move (newfile,destination3)
except Exception as error:
        print('ocorreu um erro, analise o arquivo *log*, ou chame o Analista para Resolve-lo')
        with open('log.txt','a') as log:
            print(f'detalhes do erro:',error ,file =log)