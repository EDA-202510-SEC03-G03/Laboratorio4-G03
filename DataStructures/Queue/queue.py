import DataStructures.List.array_list as a

def new_queue():
    queue = a.new_list()
    return queue

def enqueue(my_queue: a, element):
    my_queue.add_last(element)
    return my_queue
    
def dequeue(my_queue: a):
    if is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty') 
    elemento_a_eliminar = my_queue.first_element()
    my_queue.remove_first()
    return elemento_a_eliminar


def peek(my_queue: a): 
    if is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty') 
    return a.get_element(my_queue, 0)
    
def is_empty(my_queue):
    return a.is_empty(my_queue)
       
def size(my_queue):
    return my_queue["size"]