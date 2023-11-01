import prism_ai as pai
import time
# pai.api_url = "http://localhost:8000/"
pai.api_url = "https://api-test.prism-ai.ch/"

def test_response_stream_bare(): 

    a = pai.Reply.stream(
        prompt="Testing testing 1 2 3, do you read me? Over."
    )
    for elt in a: 
        pass
    return 

def test_response_bare():

    a = pai.Reply.create(
        prompt="Testing testing 1 2 3, do you read me? Over."
    )
    print(a) 

    return

def test_create_knowledge_base():

    kb = pai.KnowledgeBase.create(
        name = "Test Knowledge Base",
    )
    print(kb)

    return kb

def test_create_knowledge_from_url(kb_id):

    a = pai.Knowledge.create(
        method = "url",
        name = "test knowledge url", 
        knowledge_base_id=kb_id,
        url = "https://www.gwcustom.com/about/",
        recursion = True, 
        max_recursion = 10, 
        only_base_url = True,
    )
    print(a)

    return a

def test_create_knowledge_from_text(kb_id):

    b = pai.Knowledge.create(
        method = "text",
        name = "test knowledge text",
        knowledge_base_id=kb_id,
        text = "The managing director and sole founder of GWCustom (GWC GmbH) is Griffin White, a data scientist and software developer from the United States, currently residing in Switzeraland.",
    )

    return b 


def test_create_knowledge_from_files(kb_id):

    c = pai.KnowledgeBase.add(
        id = kb_id,
        base_dir = "/home/grifffin/Desktop/Test_Files_3/"
    )

    return c

def test_response_stream_contextualized(kb_id):

    a = pai.Reply.stream(
        prompt="What are the specific company advantages of GWC GmbH?",
        knowledge_base = [kb_id],
    )
    for elt in a: 
        pass
    return


def test_on_context():

    pass

if __name__ == "__main__":
    test_response_stream_bare()
    test_response_bare()
    kb = test_create_knowledge_base()
    test_create_knowledge_from_url(kb.json['id'])
    test_create_knowledge_from_text(kb.json['id'])
    test_create_knowledge_from_files(kb.json['id'])
    print("Waiting")
    time.sleep(120)
    print("Starting")
    test_response_stream_contextualized(kb.json['id'])
    test_on_context()
    pass


    