#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        # 一共top_nums个桶
        c = Counter(tasks)
        top1_nums = c.most_common(1)[0][1]
        # 最后一个桶里面的任务数量取决于出现频率最高的任务有几个，比如这题里面的A：3，B：3，则最后一个桶就是放俩个
        last_bucket = list(c.values()).count(top1_nums)
        tmp = (top1_nums-1) * (n+1) + last_bucket
        res = max(tmp, len(tasks))
        return res
# @lc code=end

