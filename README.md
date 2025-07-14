# ES-Jharvy_Jonas_Cadillo_Tarazona

## Archivo de git_graph

Este script llamado `git_graph.py` tiene como funcionalidad extraer el hash del commit y el hash de su padre, a traves de la función extractor. Esta funcion, tiene como parametro la ruta del repositorio y internamente busca la carpeta `.git/objects/`. Cuando ya llega a esta carpeta, lista todos los objetos y comienza a, primeramente a descomprimir con ZLIB, y luego parsea con la funcion `parse_blob` el hash del objeto y el hash del padre. 

Cuando ya se parseo completamente, realiza el archivo `.dot`

Para ejecutar solamente el script, se escribe el siguiente comando:

```bash
python3 git_graph --name ruta/al/repositorio
```