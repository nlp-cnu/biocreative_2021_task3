class Tweet(object):
    def __init__(self, twid, userid, created, text=''):
        self.twid = twid
        self.text = text
        self.userid = userid
        self.created = created

        self.contains_drug = False
        self.anns = []
        self.span = ''
        self.drug = ''

    def list(self):
        if not self.contains_drug:
            # return "%s\t%s\t-\t-\t-\t-" % (self.twid, self.text)
            return [self.twid, self.userid, self.created, self.text, '-', '-', '-', '-']
        else:
            # return "%s\t%s\t%d\t%d\t%s\t%s" % (self.twid, self.text, self.anns[0], self.anns[1]
            #                                    , self.span, self.drug)
            return [self.twid, self.userid, self.created, self.text, self.anns[0], self.anns[1], self.span, self.drug]



    def id(self):
        return self.twid

    def pop(self, start, end, span, drug):
        if not self.contains_drug:
            self.contains_drug = True
            self.anns.append(start)
            self.anns.append(end)
            self.span = span
            self.drug = drug


