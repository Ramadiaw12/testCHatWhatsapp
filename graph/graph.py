from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List, Literal, List, Sequence, Annotated

# from IPython.display import Image

# STATE OF THE GRAPH
class ChatState(TypedDict):
    message: str
    user_id:int
    conversation_id:id
    context:str
    retrivied_document:str
    tool_result: str



# NODE 1
def user_analyse(state:ChatState) -> ChatState:
    """  """
    messages=state['context']
    result=state['tool_result']
    


