class mem_A:
    def __init__(self) -> None:
        self._mem = {}

    def val(self,m,n):
        def A(m,n):
            if m == 0:
                return n + 1
            elif m > 0 and n == 0:
                return self.val(m-1, 1)
            else:
                return self.val(m-1,self.val(m,n-1))

        t = (m,n)
        if t not in self._mem:
            self._mem[t] = A(m,n)
        return self._mem[t]

    def mem(self):
        return self._mem

a = mem_A()
print(a.val(2,3))
print(a.mem())