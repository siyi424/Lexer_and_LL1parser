# LL(1) analyze


class LL1_parser:
    def __init__(self, path) -> None:
        self.dict = self._gen_dict(path)  # grammer
        self.First = {}
        self.Follow = {}
        self.Select = {}

    def _gen_dict(self, path):
        """
        read syntax txt file, and generate a dict.
        """
        dict = {}
        with open(path, "r") as f:
            cont = f.read()
        for line in cont.splitlines():
            res = line.split("->")
            vl, vr = [x.strip() for x in res]
            if vl not in dict:
                dict[vl] = [vr]
            else:
                dict[vl].append(vr)
        return dict

    def run(self):
        self.Vt, self.Vn = self._preInfo()

    def _preInfo(self):
        """
        get Vt and Vn set
        """
        Vt = []  # final ch
        Vn = []  # not final ch
        for key, values in self.dict.items():
            Vn.append(key)
            for value in values:
                for ch in value:
                    if ch.isupper():
                        Vn.append(ch)
                    else:
                        Vt.append(ch)
        Vt = list(set(Vt))
        Vn = list(set(Vn))
        print("终结符：", Vt)
        print("非终结符：", Vn)
        return Vt[:], Vn[:]
    
    def get_First(self, S):
        def cal_F(S, s_list):
            for item in self.dict[S]:
                if item[0] in self.Vt:
                    s_list.append(item[0])
                else:
                    cal_F(item[0], s_list)
            s_list = list(set(s_list))
            return s_list[:]

        if S in self.Vn:
            s_first = []
            return cal_F(S, s_first)
        else:
            return list(S)
            



path = "./test/test_grammer.txt"
my_parser = LL1_parser(path)
my_parser.run()
l = my_parser.get_First("P")
print(l)
