class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid = set()
        if not len(emails):
            return 0 
        for email in emails:
            current = self.process(email)
            valid.add(current)
        return len(valid)
    
    def process(self, email):
        local, domain = "", ""
        for i, char in enumerate(email):
            if char == "@":
                local, domain = email[:i], email[i + 1:]
                break
        #process local name
        p_local = ""
        for i in range(len(local)):
            if local[i] != ".":
                p_local += local[i]
            if i + 1 < len(local) and local[i + 1] == "+":
                break
        return p_local + "@" + domain
