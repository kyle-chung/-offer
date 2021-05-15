请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。

# O(n) and O(n)
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        n = str(n)
        n = list(n)
        count = 0
        for i in range(len(n)):
            if n[i] == '1':
                count += 1
        return count

# 时间复杂度 O(log_2 n),空间复杂度 O(1)O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
         
&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数

# 时间复杂度 O(M)：M为二进制数字n中1的个数
# 空间复杂度 O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res

