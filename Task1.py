from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name: str
    
    
def task1_node(state:AgentState) -> AgentState:
    
    state['name'] = state['name'] + "! , you are doing a great job with Langgraph!"
    return state

#Construccion del grafo de estados
graph = StateGraph(AgentState)
graph.add_node("task1", task1_node)
graph.set_entry_point("task1")
graph.set_finish_point("task1")
app = graph.compile() #definir app que luego sera invocada

#invocacion de la app
result = app.invoke({"name": "Esteban"})
print(result["name"])