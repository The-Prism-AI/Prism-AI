import prism_ai as pai
import time
pai.api_url = "http://localhost:8000/"
# pai.api_url = "https://api-test.prism-ai.ch/"

def test_response_stream_bare(): 

    stream = pai.Reply.stream(
        prompt = "Testing testing 1 2 3 do you read me? Over.",
        # knowledge_base = [],
        hyde = True
        )

    for chunk in stream:
        # handle the chunk
        pass
    return 

def test_response_bare():

    a = pai.Reply.create(
        prompt = "Testing testing 1 2 3 do you read me? Over.",
        # knowledge_base = [],
        hyde = True
        )
    print(a) 

    return

def test_create_knowledge_base():

    kb = pai.KnowledgeBase.create(
        name = "Test Knowledge Base", 
        # base_url = "https://www.gwcustom.com/",
        # only_base_url = True, 
        # recursion = True, 
        # max_recursion = 100, 
        # kb_meta_context = "This is information which was extracted from Prism's website",
        # generate_meta_context = True,
        # smart_index = False, 
        # ner = True 
    )

    print(kb)

    return kb

def test_create_knowledge_base_from_path():

    kb = pai.KnowledgeBase.create(
        name = "Local Prism Information", 
        base_dir = "/home/grifffin/Desktop/Test_Files_3/",
        recursion = True, 
        kb_meta_context = "This is a placeholder for now.",
        generate_meta_context = True,
        smart_index = False, 
        ner = True
        )
    print(kb)
    return kb

def test_create_knowledge_base_from_url():

    kb = pai.KnowledgeBase.create(
        name = "Online Prism Information", 
        base_url = "https://www.prism-ai.ch/",
        only_base_url = True, 
        recursion = True, 
        max_recursion = 5, 
        kb_meta_context = "This is information which was extracted from GWCustom's website",
        generate_meta_context = True,
        smart_index = False, 
        ner = True 
        )

def add_knowledge_from_url(kb_id):

    kb = pai.KnowledgeBase.add(
        kb_id = kb_id, 
        base_url = "https://www.narwhal.ch/",
        only_base_url = True, 
        recursion = True, 
        max_recursion = 10, 
        kb_meta_context = "This is information which was extracted from Narwhal's website",
        generate_meta_context = True,
        smart_index = False, 
        ner = True 
        )

    print(kb)
    return kb

def get_kb(kb_id):

    kb = pai.KnowledgeBase.get(
        kb_id = kb_id,
        verbose = True
        )

    print(kb)

    return kb

def test_create_knowledge_from_file(kb_id):

    knowledge = pai.Knowledge.create(
        method = "url", 
        name = "Knowledge about Prism", 
        kb_id = kb_id, 
        source = "https://www.narwhal.ch/about/",
        meta_context = "This is information retrieved from the Narwhal website."
        )
    
    print(knowledge)
    return knowledge

def test_create_knowledge_from_file(kb_id):

    knowledge = pai.Knowledge.create(
        method = "file", 
        name = "Knowledge about Prism", 
        kb_id = kb_id, 
        source = "/home/grifffin/Desktop/Test_Files/SR-961.015.2-01012013-DE.pdf",
        meta_context = "This is a random law."
        )
    print(knowledge)
    return knowledge

def test_create_knowledge_from_text(kb_id):

    knowledge = pai.Knowledge.create(
        method = "text", 
        name = "Knowledge about Prism", 
        kb_id = 1, 
        source = "Did you know that Prism supports fully private instances? That means nobody but you ever touches your data!",
        meta_context = "This is information retrieved from the Prism documentation."
        )
    
    print(knowledge)
    return knowledge

def test_contextualized_response(kb_id):

    reply = pai.Reply.create(
        prompt = "Who is Griffin White?",
        knowledge_base = [kb_id],
        hyde = True
        )
    
    print(reply)
    return reply

def test_contextualized_stream(kb_id): 

    stream = pai.Reply.stream(
        prompt = "Tell me something Interesting that about prism-ai.",
        knowledge_base = [1],
        hyde = True
        )

    for chunk in stream:
    # handle the chunk
        pass    
    return

if __name__ == "__main__":

    test_response_bare()
    test_response_stream_bare()
    print(0)
    kb = test_create_knowledge_base()
    kb_id = kb.id
    print(1)
    time.sleep(5)
    add_knowledge_from_url(kb_id)
    time.sleep(5)
    print(2)
    kb = get_kb(kb_id)
    time.sleep(5)
    print(3)
    test_create_knowledge_from_file(kb_id)
    time.sleep(5)
    print(4)
    test_create_knowledge_from_text(kb_id)
    time.sleep(5)
    print(5)
    test_contextualized_response(kb_id)
    time.sleep(5)
    print(6)
    test_contextualized_stream(kb_id)
    time.sleep(5)
    print(7)
    test_response_bare()
    print(8)
    time.sleep(5)
    test_response_stream_bare()
    time.sleep(5)
    print(9)
    test_create_knowledge_base_from_path()
    time.sleep(5)
    print(10)
    test_create_knowledge_base_from_url()
    time.sleep(5)

    pass        
