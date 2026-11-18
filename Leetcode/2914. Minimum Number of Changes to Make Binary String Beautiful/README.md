
<h2><a href="https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful">2914. Minimum Number of Changes to Make Binary String Beautiful</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given a 0-indexed binary string <code>s</code> having an even length.</p>

<p>A string is beautiful if it's possible to partition it into one or more substrings such that:</p>

<ul>
<li>Each substring has an even length.</li>
<li>Each substring contains only 1's or only 0's.</li>
</ul>

<p>You can change any character in <code>s</code> to 0 or 1.</p>

<p>Return the minimum number of changes required to make the string <code>s</code> beautiful.</p>

---

### Example 1

<pre>
Input: s = "1001"
Output: 2
Explanation:
We change s[1] to 1 and s[3] to 0 to get "1100".
The string "1100" is beautiful because we can partition it into "11|00".
</pre>

### Example 2

<pre>
Input: s = "10"
Output: 1
Explanation:
We change s[1] to 1 to get "11".
The string "11" is beautiful because we can partition it into "11".
</pre>

### Example 3

<pre>
Input: s = "0000"
Output: 0
Explanation:
The string is already beautiful.
</pre>

---

### Constraints

<ul>
<li>2 ≤ s.length ≤ 10⁵</li>
<li>s has an even length.</li>
<li>s[i] is either '0' or '1'.</li>
</ul>

---

# Solution

### Approach (Greedy)

**Key idea:**

Since every substring must have an even length, we can partition the string into consecutive pairs.

Each pair must contain identical characters:
- `00` is beautiful.
- `11` is beautiful.
- `01` or `10` requires exactly one change.

Therefore, we count the number of pairs containing different characters.

### Steps

1. Initialize `changes = 0`.
2. Iterate through the string with a step of 2.
3. For each pair:
   - Compare `s[i]` and `s[i + 1]`.
   - If they are different, increment `changes`.
4. Return `changes`.

---

### Complexity

- <strong>Time Complexity:</strong> O(n)
- <strong>Space Complexity:</strong> O(1)

---

### Tags

string, greedy
