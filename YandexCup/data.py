class datacenter:
    def __init__(self, server):
        self.max_server = server
        self.server = server
        self.res = 0
        self.server_status = {num + 1: 1 for num in range(server)}

    def get(self):
        return self.server * self.res
    
    def reset(self):
        self.server = self.max_server
        self.res += 1
        self.server_status = {num + 1: 1 for num in range(self.server)}
    
    def disable(self, server):
        if self.server_status[server] == 1:
            self.server_status[server] = 0
            self.server -= 1
        

def main():
    n, m, q = map(int, input().split())
    data_cen = {num + 1: datacenter(m) for num in range(n)}
    for i in range(q):
        read_data = input().split()
        if read_data[0] == "RESET":
            data_cen[int(read_data[1])].reset()
        elif read_data[0] == "DISABLE":
            data_cen[int(read_data[1])].disable(int(read_data[2]))
        elif read_data[0] == "GETMAX":
            data = {key: value.get() for key, value in data_cen.items()}
            print(max(data, key=data.get))
        elif read_data[0] == "GETMIN":
            data = {key: value.get() for key, value in data_cen.items()}
            print(min(data, key=data.get))

if __name__ == "__main__":
    main()