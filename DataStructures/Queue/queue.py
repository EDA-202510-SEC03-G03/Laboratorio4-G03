import DataStructures.List.array_list as a

def new_queue():
    queue = a.new_list()
    return queue






def enqueue(my_queue: a, element):
    my_queue.add_last(element)
    return my_queue
    
def dequeue(my_queue: a):
    if a.is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')
    
    elemento_a_eliminar = my_queue.first_element()
    my_queue.remove_first()
    return elemento_a_eliminar














def peek(my_queue): 
    pass
    
def is_empty(my_queue):
    if my_queue["size"] == 0:
        return True 
    else:
        return False 

def size(my_queue):
    return my_queue["size"]
