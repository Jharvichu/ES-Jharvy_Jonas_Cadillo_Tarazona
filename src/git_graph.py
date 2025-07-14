import os
import sys
import zlib
import argparse
import re

# Referencia para la funcion extraccion: https://gist.github.com/lordjabez/7f24c848a1424365617300b0d9bc2d04

def extraccion(repositorio):

    if not os.path.isdir(repositorio):
        print("No se encontro el repositorio")
        sys.exit(1)

    git_objects = os.path.join(repositorio, ".git/objects")

    if not os.path.isdir(git_objects):
        print("No se encontro la carpeta .git/objets")
        sys.exit(1)

    object_list = os.listdir(git_objects)

    git_analisis = []

    for object in object_list:
        with open(object,'rb') as object_file:
            contenido_object = zlib.decompress(object_file.read())
            info_blob = parse_blob(contenido_object)
            git_analisis.append(info_blob)

    return git_analisis

def parse_blob(contenido):
    recurso = []

    pattern = r'*commit\s+(?P<hash>[^"]+)*\nauthor*<author>\s+(?P<padre>[^"]+)*'
    hash = re.search(pattern, contenido).group("hash")
    padre = re.search(pattern, contenido).group("padre")

    return recurso.append({
        "hash": hash,
        "padre": padre
    })

def main():
    parse = argparse.ArgumentParser(description="Escribir la ruta repositorio")
    parse.add_argument("--name", type=str, default='repositorio')
    args = parse.parse_args()
    path = args.output

    git_analisis = extraccion(path)

    generate_dot(git_analisis)

def generate_dot(git_analisis):
        relaciones_escritas = set()
        dot_path = os.path.dirname(__file__)
        with open(dot_path, 'w') as f:
            f.write('digraph Dependencies {\n')

        for modulo, deps in git_analisis.items():
            for dep in set(deps):
                relacion = f'"{modulo}" -> "{dep}";'
                if relacion not in relaciones_escritas:
                    f.write(f'    {relacion}\n')
                    relaciones_escritas.add(relacion)
        f.write('}\n')

if __name__ == "__main__":
    main()