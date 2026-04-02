class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            valid.add(local + "@" + domain)
        return len(valid)
