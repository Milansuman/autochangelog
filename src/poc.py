from evaluator import EvaluatorTestCase, main
from agent import simple_agent
from langchain.messages import HumanMessage

class POCEvaluator(EvaluatorTestCase):
    
    def __init__(self):
        super().__init__(name="poc_evaluator")

    def test_sample_evaluation(self):
        # Test that agent responds appropriately to a greeting
        response = simple_agent.invoke({
            "messages": [HumanMessage(content="Hello, who are you?")]
        })
        
        agent_response = response["messages"][-1].content
        expected_response = "I am a helpful assistant that generates changelogs for GitHub repositories"
        
        self.is_embedding_similar(agent_response, expected_response, threshold=0.01)
    
    def test_changelog_format_understanding(self):
        # Test that agent understands changelog format requirements
        response = simple_agent.invoke({
            "messages": [HumanMessage(content="What format should a changelog be in?")]
        })
        
        agent_response = response["messages"][-1].content
        expected_response = "Changelogs should be formatted in markdown and be readable by end users"
        
        self.is_embedding_similar(agent_response, expected_response, threshold=0.7)
    
    def test_user_facing_changes_focus(self):
        # Test that agent understands to focus on user-facing changes
        response = simple_agent.invoke({
            "messages": [HumanMessage(content="What kind of information should be included in a changelog?")]
        })
        
        agent_response = response["messages"][-1].content
        expected_response = "Changelogs should contain user facing changes and features, with concise mentions of bug fixes and security patches"
        
        self.is_embedding_similar(agent_response, expected_response, threshold=0.7)
    
    def test_technical_details_exclusion(self):
        # Test that agent knows to exclude technical implementation details
        response = simple_agent.invoke({
            "messages": [HumanMessage(content="Should I include commit SHAs and author names in my changelog?")]
        })
        
        agent_response = response["messages"][-1].content
        expected_response = "No, changelogs should not include git commits, authors or commit SHAs"
        
        self.is_embedding_similar(agent_response, expected_response, threshold=0.7)
    
    def test_changelog_file_extension(self):
        # Test that agent knows to save changelogs with .md extension
        response = simple_agent.invoke({
            "messages": [HumanMessage(content="What file extension should I use when saving a changelog?")]
        })
        
        agent_response = response["messages"][-1].content
        expected_response = "Changelogs should be saved with the .md file extension for markdown format"
        
        self.is_embedding_similar(agent_response, expected_response, threshold=0.7)
    
    def test_changelog_purpose(self):
        # Test that agent understands the purpose of changelogs
        response = simple_agent.invoke({
            "messages": [HumanMessage(content="Why are changelogs important?")]
        })
        
        agent_response = response["messages"][-1].content
        expected_response = "Changelogs are important to communicate changes and updates to users in a readable format"
        
        self.is_embedding_similar(agent_response, expected_response, threshold=0.7)
        
        
if __name__ == "__main__":
    main()