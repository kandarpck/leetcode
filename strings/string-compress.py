from itertools import groupby


class Solution:
    def compress_string(self, ip):
        res = ip[0]
        count = 1
        for idx in range(len(ip) - 1):
            if ip[idx] == ip[idx + 1]:
                count += 1
            else:
                res += str(count)
                count = 1
                res += ip[idx + 1]
        res += str(count)
        return res

    def compress_groupby(self, ip):
        res = ''
        for char, group in groupby(ip):
            res = res + char + str(sum(1 for _ in group))
        return res

    def decompress_string(self, ip):
        res = ''
        for idx in range(0, len(ip), 2):
            res += ip[idx] * int(ip[idx + 1])
        return res

    def compress_e(self, ip):
        seen_e = False
        idx = 0
        while idx < len(ip) - 1:
            if ip[idx] == 'e' or ip[idx] == 'E':
                if seen_e:
                    ip = ip[:idx] + ip[idx + 1:]
                else:
                    idx += 1
                    seen_e = True
            else:
                seen_e = False
                idx += 1

        return ip


if __name__ == '__main__':
    sol = Solution()
    ip = "heeeelllleooo"
    ct = sol.compress_string(ip)
    print(ct)
    ct = sol.compress_groupby(ip)
    print(ct)
    print(sol.decompress_string(ct))

    print(sol.compress_e(ip))
