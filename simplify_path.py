class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        finalpath = []
        dirr = path.split("/")

        for i in dirr:
            if i == "." or not i:
                continue
            elif i == "..":
                if finalpath:
                    finalpath.pop()
            else:
                finalpath.append(i)

        return "/" + "/".join(finalpath)
