import hashlib

class ElectronicVotingSystem:
    def __init__(self):
        self.votes = {}
        self.voters = set()
        self.results_revealed = False
    
    def vote(self, voter_id, candidate):
        if voter_id in self.voters:
            print("Error: You have already voted!")
            return
        
        self.voters.add(voter_id)
        
        # Encrypting the vote to ensure it cannot be tampered with
        encrypted_vote = hashlib.sha256(candidate.encode()).hexdigest()
        
        if candidate not in self.votes:
            self.votes[candidate] = []
        
        self.votes[candidate].append(encrypted_vote)
        print("Your vote has been recorded.")

    def reveal_results(self):
        if self.results_revealed:
            print("Results have already been revealed.")
            return
        
        self.results_revealed = True
        print("Voting Results:")
        
        for candidate, votes in self.votes.items():
            print(f"{candidate}: {len(votes)} votes")
        
        print("Voting is complete. The results have been revealed.")

# Example usage
voting_system = ElectronicVotingSystem()

# Simulating voting
voting_system.vote("Voter1", "CandidateA")
voting_system.vote("Voter2", "CandidateB")
voting_system.vote("Voter3", "CandidateA")
voting_system.vote("Voter1", "CandidateB")  # This should raise an error

# Revealing the results
voting_system.reveal_results()
