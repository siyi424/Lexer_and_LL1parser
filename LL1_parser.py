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

        # get First set
        all_V = self.Vt + self.Vn
        for v in all_V:
            self.First[v] = self.get_First(v)
        
        # get Follow set
        for vn in self.Vn:
            self.Follow[vn] = self.get_Follow(vn)
        
        print("First Set: ")
        print(self.First)

        # reformat Vn in Follow set
        correct = set()
        while len(correct) != len(self.Vn):
            for key, values in self.Follow.items():
                self.Follow[key] = list(set(values))

                new_values = values[:]
                for value in values:
                    if value == key:
                        new_values.remove(value)
                        continue
                    if value.isupper():
                        if value in correct:
                            # check if has UpperValue select set
                            new_values += self.Follow[value]
                            new_values.remove(value)
                self.Follow[key] = list(set(new_values))
                # update correct set
                all_cor = True
                for value in values:
                    if value.isupper():
                        all_cor = False
                if all_cor:
                    correct.add(key)

        print("Follow Set: ")
        print(self.Follow)

        # get Sellect set
        self.get_Sellect()

        print("Select Set:")
        print(self.Select)

        # judge LL1
        self.judge_LL1()


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
        def cal_Fir(S, s_list):
            for item in self.dict[S]:
                if item[0] in self.Vt:
                    s_list.append(item[0])
                else:
                    cal_Fir(item[0], s_list)
            s_list = list(set(s_list))
            return s_list[:]

        if S in self.Vn:
            s_first = []
            return cal_Fir(S, s_first)
        else:
            return list(S)

    def get_Follow(self, S):
        '''
        take care: recursion depth in while loop!
        '''
        def cal_Fo(S, s_list):
            if S == "S":
                s_list.append("#")
            for key, items in self.dict.items():
                for item in items:
                    if S not in item:
                        continue
                    vr = item[::-1]
                    p = 0
                    updated = True
                    while vr[p] != S and updated:
                        p_first = self.First[vr[p]][:]
                        if "ε" in p_first:
                            p_first.remove("ε")
                            if p_first:
                                s_list += p_first
                            
                        else:
                            # right part is not -> "ε"
                            updated = False
                            s_list += p_first
                        p += 1

                    if updated:
                        # recursion way will exceeded!
                        # cal_Fo(key, s_list)

                        # # change another way:
                        s_list.append(key)


            return list(set(s_list))

        if S in self.Vn:
            s_follow = []
            return cal_Fo(S, s_follow)
        else:
            return list(S)
        

    def get_Sellect(self):
        # get right part
        for key, items in self.dict.items():
            self.Select[key] = []
            # cal single part Select set
            for item in items:
                # cal item First set
                first = []
                for ch in item:
                    ch_first = self.get_First(ch)
                    if 'ε' not in ch_first:
                        first += ch_first
                        break
                    first += ch_first
                first = list(set(first))
                # cal item Select set
                if 'ε' not in first:
                    self.Select[key].append(first)
                else:
                    follow = self.get_Follow(key)
                    if first == ['ε']:
                        added = follow
                    else:
                        added = first.remove('ε') + follow
                    added = list(set(added))
                    self.Select[key].append(added)
        return

        
    def judge_LL1(self):
        '''
        if the same Vn's Select set has intersection, then this grammer must not be  LL1.
        '''
        for key, values in self.Select.items():
            Intered = False
            lens = len(values)
            for i in range(lens):
                for j in range(i+1, lens):
                    list1 = values[i]
                    list2 = values[j]
                    if set(list1) & set(list2):
                        Intered = True
                        print("This grammer is not a LL1 syntax grammer, NO!")
                        print("Vn: ", key, "has intersected Selected set.")
                        return
        print("This grmmer is a LL1 syntax grammer, YES!")








path = "./test/test_grammer.txt"
my_parser = LL1_parser(path)
my_parser.run()
# print("Select:")
# print(my_parser.Select)
