## Preguntas

### Por qué git es un DAG

Git es un grafo dirigido aciclico ya que, su estructura interna esta definida para que cada commit tenga una referencia a su padre, y que así se guarde una relacion entre cada version del proyecto. Cada commit tambien tiene de referencia a un `tree`, es decir tiene referencia a un arbol de directorios y a blobs.

Dado que cada commit tiene referencia a su padre, se podria considerar que de este nodo HEAD tiene un arista dirigida hacia su nodo padre. Al cumplir esto, en `git_graph.py` se extrae de cada object su hash y el hash de su padre, teniendo asi varios hash guardados y con la funcion `generate_dot` reacomodamos los hash para que tengan una referencia y obtengamos asi el DAG del repositorio.

### Mediator vs Adpater

Mediator brinda un mejor desacoplamiento ya que este patron tiene como funcion la coordinación de varios microservicios que deben ejecutarse de un determinado orden y que evita que los microservicios se comuniquen entre ellos, asi evitando acoplamiento. 

Ademas facilita la inyeccion de back-pressure, ya que al tener como funcion la coordinacion de microservicios, puede modificar la produccion de datos de un microservicio en consistencia con el consumo de datos de otro microservicio, en cambio, con el patron adapter no se podria hacer eso, ya que Adapter solamente transforma el valor entrante de un microservicio a un determinado tipo de valor para que pueda consumir el otro microservicio. Eso podria ocasionar cuellos de botella, ya que puede que el primer microservicio produzca mas datos que el segundo microservicio pueda consumir.

