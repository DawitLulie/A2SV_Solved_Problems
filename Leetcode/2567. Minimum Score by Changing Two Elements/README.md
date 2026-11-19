
<h2><a href="https://leetcode.com/problems/minimum-score-by-changing-two-elements">2567. Minimum Score by Changing Two Elements</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given an integer array <code>nums</code>.</p>

<ul>
<li>The low score of <code>nums</code> is the minimum absolute difference between any two integers.</li>
<li>The high score of <code>nums</code> is the maximum absolute difference between any two integers.</li>
</ul>

<p>The score of <code>nums</code> is the sum of the high and low scores.</p>

<p>Return the minimum score after changing two elements of <code>nums</code>.</p>

---

### Example 1

<pre>
Input: nums = [1,4,7,8,5]
Output: 3
Explanation:
Change nums[0] and nums[1] to 6.
The array becomes [6,6,7,8,5].
The low score is |6 - 6| = 0.
The high score is |8 - 5| = 3.
The total score is 3.
</pre>

### Example 2

<pre>
Input: nums = [1,4,3]
Output: 0
Explanation:
Change nums[1] and nums[2] to 1.
The array becomes [1,1,1].
The high score and low score are both 0.
</pre>

---

### Constraints

<ul>
<li>3 ≤ nums.length ≤ 10⁵</li>
<li>1 ≤ nums[i] ≤ 10⁹</li>
</ul>

---

# Solution

### Approach (Sorting + Greedy)

**Key idea:**

Sort the array first. Since we can change any two elements, we only need to consider three possible cases.

After sorting, the minimum score can be obtained by removing the influence of the two smallest elements, the two largest elements, or one element from each end.

The three possible answers are:

1. <code>nums[n-1] - nums[2]</code> — Change the two smallest elements.
2. <code>nums[n-2] - nums[1]</code> — Change the smallest and largest elements.
3. <code>nums[n-3] - nums[0]</code> — Change the two largest elements.

Take the minimum of these three values.

### Steps

1. Sort the array in ascending order.
2. Calculate the three possible differences:
   - <code>nums[n-1] - nums[2]</code>
   - <code>nums[n-2] - nums[1]</code>
   - <code>nums[n-3] - nums[0]</code>
3. Return the minimum of the three differences.

---

### Complexity

- <strong>Time Complexity:</strong> O(n log n) — Sorting the array.
- <strong>Space Complexity:</strong> O(1) — Extra space, assuming in-place sorting.

---

### Tags

array, sorting, greedy
