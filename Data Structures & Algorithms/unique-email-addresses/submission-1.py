class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        validCount =0
        validMap = {}
        for email in emails:
            splitted = email.split("@")
            local_name = splitted[0]
            domain_name = splitted[1]
            notValid = False
            for c in local_name:
                if not (c.isalnum() or c == '.' or c == '+'):
                    notValid = True
            for c in domain_name:
                if not (c.isalnum() or c == '.'):
                    notValid = True
            if notValid:
                continue
            if '+' in local_name:
                local_name = local_name.split('+')[0]
            if '.' in local_name:
                local_name=local_name.replace(".", "")
            email = local_name + domain_name
            if not email in validMap:
                validCount += 1
                validMap[email] = 0
        return validCount

            
            