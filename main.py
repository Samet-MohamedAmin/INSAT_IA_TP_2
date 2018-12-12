#! /bin/python3

import app as main_program
import json, time

class csp:
    def __init__(self, domain, vars, problem):
        self.final_result = []
        self.domain = domain
        # self.constraints = constraints
        self.vars = vars
        self.result = [0]*len(variables)
        self.problem = problem

        # n_reines, sudoku

    def place_or_not_place(self, line, variable):
        if self.problem == 1:
            if line == 0: return True
            for i in range(line):
                if (abs(int(variable) - int(self.result[i])) == abs(line - i)) and int(self.result[i]) != 0 \
                        or int(variable) == int(self.result[i]):
                    return False
            return True

        else:
            if line == 0: return True
            for i in range(5):
                if (self.result[i] == self.result[5]) and not (self.result[i] == 0):
                    return False
            for i in range(4):
                if (self.result[i] == self.result[i+1]) and not (self.result[i] == 0):
                    return False

            return True

    def backtrack_solve(self, line):
        if line >= len(self.vars): return True
        else:
            for d in self.domain:
                res = self.result[:]
                res[line] = d
                self.final_result.append([x for x in res if x])
                if self.place_or_not_place(line, d):
                    self.result[line] = d
                    self.print_solution()
                    if self.backtrack_solve(line+1):
                        return True

                    self.result[line] = 0

        return False

    def print_solution(self):
        print('-'*10)
        for i in range(len(self.vars)):
            print('%s is set to %s' %(self.vars[i], self.result[i]))
        if self.problem != 1: time.sleep(1)

    def remove(self, tmp, line, original):
        FD = [x[:] for x in tmp] # Array.Copy(tmp, FD, tmp.Length)
        for i in list(range(line+1, len(tmp))):
            for v in FD[i]:
                self.result[i] = v
                if not self.place_or_not_place(i, v):
                    index = FD[i].index(v)
                    if index >= 0:
                        del FD[i][index] # FD[i].RemoveAt(index)
                self.result[i] = 0

        return FD


    def forward_trace(self, forward_domain):
        print('-'*30)
        for i in range(len(forward_domain)):
            print('line %s is set to %s' %(i, self.result[i]), forward_domain[i])
            print()
        if self.problem != 1: time.sleep(1)        


    def forward_solve(self, forward_domain, line,):
        if line >= len(self.vars): return True
        else:
            for i in range(line, len(forward_domain)):
                if len(forward_domain[i]) == 0: return False
                for d in forward_domain[i]:
                    if self.place_or_not_place(line, d):
                        self.result[line] = d
                        original = [x[:] for x in forward_domain]
                        forward_domain = self.remove(forward_domain, line, original)
                        # print trace
                        self.forward_trace(forward_domain)
                        self.final_result.append([x for x in self.result if x])
                        if self.forward_solve(forward_domain, line + 1): return True
                        forward_domain = original
                        self.result[line] = 0


if __name__ == '__main__':
    with open('csp/csp.json') as json_data:
        csp_data = json.load(json_data)


         

    print('choose the problem')
    p_choice = int(input('[1] n queens \t [2] map filling > '))
    print('choose the algorithm')
    s_choice = int(input('[1] backtrack \t [2] forward > '))

    if p_choice == 1:
        """n_queens"""

        for element in csp_data:
            if element['problem'] == '8_queens':
                parameters = element['parameters']

        variables = parameters['variables'] #['Q'+str(i) for i in range(8)]
        domain = parameters['domain'] #list(range(1, 9))
        p = csp(domain, variables, p_choice)
        if s_choice == 1:
            if not p.backtrack_solve(0):
                print('there\'s no solution')
            p.print_solution()

            main_program.main(p.final_result)

        elif s_choice == 2:
            forward_domain = []
            for i in range(8):
                forward_domain.append(list(range(1, 9)))
            if not p.forward_solve(forward_domain, 0):
                print('THERE\'S NO SOLUTION')
            p.print_solution()

            main_program.main(p.final_result)


    elif p_choice == 2:
        """map filling"""

        for element in csp_data:
            if element['problem'] == 'map_filling':
                parameters = element['parameters']


        variables = parameters['variables'] #['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
        domain = parameters['domain'] #['R', 'G', 'B']

        p = csp(domain, variables, p_choice)

        if s_choice == 1:
            if not p.backtrack_solve(0):
                print('there\'s no solution')
            p.print_solution()

        if s_choice == 2:
            forward_domain = []
            for i in range(len(variables)):
                forward_domain.append(list(domain))
            if not p.forward_solve(forward_domain, 0):
                print('THERE\'S NO SOLUTION')
            p.print_solution()
