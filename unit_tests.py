import prism_ai as pai
pai.api_url = "http://localhost:8000/"

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

    pass

def test_create_knowledge_from_url():

    pass

def test_create_knowledge_from_text():

    pass

def test_create_knowledge_from_file():

    pass

def test_on_context():

    pass

if __name__ == "__main__":
    test_response_stream_bare()
    test_response_bare()
    test_create_knowledge_base()
    test_create_knowledge_from_url()
    test_create_knowledge_from_text()
    test_create_knowledge_from_file()
    test_on_context()
    pass


    