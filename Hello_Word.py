from typing import Dict, TypedDict
from langgraph.graph import StateGraph #framework que ayuda a disenar y manejar el flujo de las tareas en tu app usando grafos 

#AgntState - es una estructura de datos que trackea la inforamcion que la nuesta app corre.
#Especificamos el tipo de dato de MESSAGE

class AgentState(TypedDict):
    message: str 
    
def greeting_node(state: AgentState) -> AgentState:
    """Nodo que agrega un mensaje de saludo al state."""
    
    state['message'] = "Hola " + state["message"] + ", como estas?!"
    return state


#Construccion del grafo de estados
graph = StateGraph(AgentState)

graph.add_node("gretter", greeting_node) #2 parametros nombre y accion 

graph.set_entry_point("gretter") #punto de entrada del grafo
graph.set_finish_point("gretter") #punto de salida del grafo

app = graph.compile() #compila el grafo en una app ejecutable


from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png())) #dibuja el grafo en formato mermaid

result = app.invoke({"message": "Bob"}) #invoca la app con un estado inicial

print(result["message"])