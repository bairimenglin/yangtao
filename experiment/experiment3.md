# 实验三 Python列表

班级： 21计科3

学号： B20210302301

姓名： 杨韬

Github地址：<https://github.com/bairimenglin/yangtao/tree/main/experiment>

CodeWars地址：<https://www.codewars.com/users/bairimenglin>

---

## 实验目的

1. 学习Python的简单使用和列表操作
2. 学习Python中的if语句

## 实验环境

1. Git
2. Python 3.10
3. VSCode
4. VSCode插件

## 实验内容和步骤

### 第一部分

Python列表操作

完成教材《Python编程从入门到实践》下列章节的练习：

- 第3章 列表简介
- 第4章 操作列表
- 第5章 if语句

---

### 第二部分

在[Codewars网站](https://www.codewars.com)注册账号，完成下列Kata挑战：

---

#### 第一题：3和5的倍数（Multiples of 3 or 5）

难度： 6kyu

如果我们列出所有低于 10 的 3 或 5 倍数的自然数，我们得到 3、5、6 和 9。这些数的总和为 23. 完成一个函数，使其返回小于某个整数的所有是3 或 5 的倍数的数的总和。此外，如果数字为负数，则返回 0。

注意：如果一个数同时是3和5的倍数，应该只被算一次。

**提示：首先使用列表解析得到一个列表，元素全部是3或者5的倍数。
使用sum函数可以获取这个列表所有元素的和.**

代码提交地址：
<https://www.codewars.com/kata/514b92a657cdc65150000006>

---

#### 第二题： 重复字符的编码器（Duplicate Encoder）

难度： 6kyu

本练习的目的是将一个字符串转换为一个新的字符串，如果新字符串中的每个字符在原字符串中只出现一次，则为"("，如果该字符在原字符串中出现多次，则为")"。在判断一个字符是否是重复的时候，请忽略大写字母。

例如:

```python
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
```

代码提交地址:
<https://www.codewars.com/kata/54b42f9314d9229fd6000d9c>

---

#### 第三题：括号匹配（Valid Braces）

难度：6kyu

写一个函数，接收一串括号，并确定括号的顺序是否有效。如果字符串是有效的，它应该返回True，如果是无效的，它应该返回False。
例如：

```python
"(){}[]" => True 
"([{}])" => True
 "(}" => False
 "[(])" => False 
"[({})](]" => False
```

**提示：
python中没有内置堆栈数据结构，可以直接使用`list`来作为堆栈，其中`append`方法用于入栈，`pop`方法可以出栈。**

代码提交地址
<https://www.codewars.com/kata/5277c8a221e209d3f6000b56>

---

#### 第四题： 从随机三元组中恢复秘密字符串(Recover a secret string from random triplets)

难度： 4kyu

有一个不为你所知的秘密字符串。给出一个随机三个字母的组合的集合，恢复原来的字符串。

这里的三个字母的组合被定义为三个字母的序列，每个字母在给定的字符串中出现在下一个字母之前。"whi "是字符串 "whatisup "的一个三个字母的组合。

作为一种简化，你可以假设没有一个字母在秘密字符串中出现超过一次。

对于给你的三个字母的组合，除了它们是有效的三个字母的组合以及它们包含足够的信息来推导出原始字符串之外，你可以不做任何假设。特别是，这意味着秘密字符串永远不会包含不出现在给你的三个字母的组合中的字母。

测试用例：

```python
secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
test.assert_equals(recoverSecret(triplets), secret)
```

代码提交地址：
<https://www.codewars.com/kata/53f40dff5f9d31b813000774/train/python>

提示：

- 利用集合去掉`triplets`中的重复字母，得到字母集合`letters`，最后的`secret`应该由集合中的字母组成，`secret`长度也等于该集合。

```python
letters = {letter for triplet in triplets for letter in triplet }
length = len(letters)
```

- 创建函数`check_first_letter(triplets, first_letter)`，检测一个字母是不是secret的首字母，返回True或者False。
- 创建函数`remove_first_letter(triplets, first_letter)`,  从三元组中去掉首字母，返回新的三元组。
- 遍历字母集合letters，利用上面2个函数得到最后的结果`secret`。

---

#### 第五题： 去掉喷子的元音（Disemvowel Trolls）

难度： 7kyu

喷子正在攻击你的评论区!
处理这种情况的一个常见方法是删除喷子评论中的所有元音(字母：a,e,i,o,u)，以消除威胁。
你的任务是写一个函数，接收一个字符串并返回一个去除所有元音的新字符串。
例如，字符串 "This website is for losers LOL!"   将变成 "Ths wbst s fr lsrs LL!".

注意：对于这个Kata来说，y不被认为是元音。
代码提交地址：
<https://www.codewars.com/kata/52fba66badcd10859f00097e>

提示：

- 首先使用列表解析得到一个列表，列表中所有不是元音的字母。
- 使用字符串的join方法连结列表中所有的字母，例如：

```python
last_name = "lovelace"
letters = [letter for letter in last_name ]
print(letters) # ['l', 'o', 'v', 'e', 'l', 'a', 'c', 'e']
name = ''.join(letters) # name = "lovelace"
```

---

### 第三部分

使用Mermaid绘制程序流程图

安装VSCode插件：

- Markdown Preview Mermaid Support
- Mermaid Markdown Syntax Highlighting

使用Markdown语法绘制你的程序绘制程序流程图（至少一个），Markdown代码如下：

![程序流程图](/Experiments/img/2023-08-05-22-00-00.png)

显示效果如下：

```mermaid
flowchart LR
    A[Start] --> B{Is it?}
    B -->|Yes| C[OK]
    C --> D[Rethink]
    D --> B
    B ---->|No| E[End]
```

查看Mermaid流程图语法-->[点击这里](https://mermaid.js.org/syntax/flowchart.html)

使用Markdown编辑器（例如VScode）编写本次实验的实验报告，包括[实验过程与结果](#实验过程与结果)、[实验考查](#实验考查)和[实验总结](#实验总结)，并将其导出为 **PDF格式** 来提交。

## 实验过程与结果

请将实验过程与结果放在这里，包括：

- [第一部分 Python列表操作和if语句](#第一部分)
- ##### 练习 3.1
```bash

names.py
names = ['ron', 'tyler', 'dani']
print(names[0])
print(names[1])
print(names[2])

输出：
ron
tyler
dani
```

##### 练习 3.2
```python
names = ['ron', 'tyler', 'dani']
msg = f"Hello, {names[0].title()}!"
print(msg)
msg = f"Hello, {names[1].title()}!"
print(msg)
msg = f"Hello, {names[2].title()}!"
print(msg)
```

输出：
Hello, Ron!
Hello, Tyler!
Hello, Dani!

##### 练习 3.4
```python
guests = ['guido van rossum', 'jack turner', 'lynn hill']
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")
```

输出：
Guido Van Rossum, please come to dinner.
Jack Turner, please come to dinner.
Lynn Hill, please come to dinner.

##### 练习 3.5
```python
guests = ['guido van rossum', 'jack turner', 'lynn hill']
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")
# Jack 无法赴约，转而邀请 Gary
del(guests[1])
guests.insert(1, 'gary snyder')
# 重新打印邀请函
name = guests[0].title()
print(f"\n{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")
```

输出：
Guido Van Rossum, please come to dinner.
Jack Turner, please come to dinner.
Lynn Hill, please come to dinner.
Sorry, Jack Turner can't make it to dinner.
Guido Van Rossum, please come to dinner.
Gary Snyder, please come to dinner.
Lynn Hill, please come to dinner.

##### 练习 3.6

```python
guests = ['guido van rossum', 'jack turner', 'lynn hill']
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")
# Jack 无法赴约，转而邀请 Gary
del(guests[1])
·8·
练习答案
guests.insert(1, 'gary snyder')
# 重新打印邀请函
name = guests[0].title()
print(f"\n{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")
# 找到了更大的餐桌，再邀请一些嘉宾
print("\nWe got a bigger table!")
guests.insert(0, 'frida kahlo')
guests.insert(2, 'reinhold messner')
guests.append('elizabeth peratrovich')
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")
name = guests[3].title()
print(f"{name}, please come to dinner.")
name = guests[4].title()
print(f"{name}, please come to dinner.")
name = guests[5].title()
print(f"{name}, please come to dinner.")
```

输出：
Guido Van Rossum, please come to dinner.
·9·
Python 编程：从入门到实践（第３版）
Jack Turner, please come to dinner.
Lynn Hill, please come to dinner.
Sorry, Jack Turner can't make it to dinner.
Guido Van Rossum, please come to dinner.
Gary Snyder, please come to dinner.
Lynn Hill, please come to dinner.
We got a bigger table!
Frida Kahlo, please come to dinner.
Guido Van Rossum, please come to dinner.
Reinhold Messner, please come to dinner.
Gary Snyder, please come to dinner.
Lynn Hill, please come to dinner.
Elizabeth Peratrovich, please come to dinner.

##### 练习 3.7
```python
shrinking_guest_list.py
# 邀请一些嘉宾与你共进晚餐
guests = ['guido van rossum', 'jack turner', 'lynn hill']
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()

·10·
练习答案
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")
# Jack 无法赴约，转而邀请 Gary
del(guests[1])
guests.insert(1, 'gary snyder')
# 重新打印邀请函
name = guests[0].title()
print(f"\n{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")
# 找到了更大的餐桌，再邀请一些嘉宾
print("\nWe got a bigger table!")
guests.insert(0, 'frida kahlo')
guests.insert(2, 'reinhold messner')
guests.append('elizabeth peratrovich')
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")
name = guests[3].title()
print(f"{name}, please come to dinner.")
name = guests[4].title()

·11·
Python 编程：从入门到实践（第３版）
print(f"{name}, please come to dinner.")
name = guests[5].title()
print(f"{name}, please come to dinner.")
# 糟糕，餐桌无法及时送达！
print("\nSorry, we can only invite two people to dinner.")
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")
# 应该只剩下两位嘉宾了，向他们发出邀请
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
# 清空名单
del(guests[0])
del(guests[0])
# 核实名单是空的
print(guests)
```

输出：
Guido Van Rossum, please come to dinner.
Jack Turner, please come to dinner.
Lynn Hill, please come to dinner.
Sorry, Jack Turner can't make it to dinner.
Guido Van Rossum, please come to dinner.
Gary Snyder, please come to dinner.
Lynn Hill, please come to dinner.
We got a bigger table!
Frida Kahlo, please come to dinner.
Guido Van Rossum, please come to dinner.
Reinhold Messner, please come to dinner.
Gary Snyder, please come to dinner.
Lynn Hill, please come to dinner.
Elizabeth Peratrovich, please come to dinner.
Sorry, we can only invite two people to dinner.
Sorry, Elizabeth Peratrovich there's no room at the table.
Sorry, Lynn Hill there's no room at the table.
Sorry, Gary Snyder there's no room at the table.
Sorry, Reinhold Messner there's no room at the table.
Frida Kahlo, please come to dinner.
Guido Van Rossum, please come to dinner.

##### 练习 3.8
```python
seeing_the_world.py
locations = ['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']
print("Original order:")
print(locations)
print("\nAlphabetical:")
print(sorted(locations))
print("\nOriginal order:")
print(locations)
print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))
print("\nOriginal order:")
print(locations)
print("\nReversed:")
locations.reverse()
print(locations)
print("\nOriginal order:")
locations.reverse()
print(locations)
print("\nAlphabetical")
locations.sort()
print(locations)
print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)
```
  

输出：
Original order:
['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']
Alphabetical:
['andes', 'guam', 'himalaya', 'labrador', 'tierra del fuego']
Original order:
['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']
Reverse alphabetical:
['tierra del fuego', 'labrador', 'himalaya', 'guam', 'andes']
Original order:
['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']
Reversed:
['guam', 'labrador', 'tierra del fuego', 'andes', 'himalaya']
Original order:
['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']
Alphabetical
['andes', 'guam', 'himalaya', 'labrador', 'tierra del fuego']
Reverse alphabetical
['tierra del fuego', 'labrador', 'himalaya', 'guam', 'andes']

- [第二部分 Codewars Kata挑战](#第二部分)
- #### 第一题：3和5的倍数（Multiples of 3 or 5）
```python
def solution(number):
    sum = 0
    i = 1

    if number<=0:
        return 0
        
    while i<number:
        
        if i%3==0 or i%5==0:
            sum += i
        i+=1
        
    return sum
```

输入:60
输出:16

- #### 第二题： 重复字符的编码器（Duplicate Encoder）
```python
def duplicate_encode(word):
    word = word.lower()
    new_word = ""
    char_count = {}
    for char in word:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    print (char_count)
    for char in word:
        if char_count[char] > 1:
            new_word += ")"
        else:
            new_word += "("
    return new_word
```

输入:aabbbc
输出:)))))(

- #### 第三题：括号匹配（Valid Braces）
```python
def valid_braces(string):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    return not stack
```

输入:(){}[]
输出:True

- #### 第四题： 从随机三元组中恢复秘密字符串(Recover a secret string from random triplets)
```python
def recoverSecret(triplets):
    graph = {}
    

    for triplet in triplets:
        for char in triplet:
            if char not in graph:
                graph[char] = set()
    
    for triplet in triplets:
        graph[triplet[0]].add(triplet[1])
        graph[triplet[1]].add(triplet[2])
    
    visited = set()
    result = []
    
    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            result.insert(0, node)
    
    for char in graph:
        dfs(char)
    
    return ''.join(result)
```

- #### 第五题： 去掉喷子的元音（Disemvowel Trolls）
```python
def disemvowel(string):
    vowels = "AEIOUaeiou"  # Define the vowels to be removed
    result = ""

    for char in string:
        if char not in vowels:
            result += char

    return result
```

输入：This website is for losers LOL!
输出：Ths wbst s fr lsrs LL!

- [第三部分 使用Mermaid绘制程序流程图](#第三部分)
#### 第一题：3和5的倍数（Multiples of 3 or 5）
```mermaid
graph TD
    A[输入number] --> B{number>0}
    B -->|否| C[返回0]
    B -->|是| D[result = 0, i = 1]
    D --> E{i < number}
    E -->|否| F[返回result]
    E -->|是| G{i%3==0 or i%5==0}
    G -->|否| H[i++]
    H --> E
    G -->|是| I[result += i, i++]
    I --> E
```
注意代码需要使用markdown的代码块格式化，例如Git命令行语句应该使用下面的格式：

![Git命令](/Experiments/img/2023-07-26-22-48.png)

显示效果如下：

```bash
git init
git add .
git status
git commit -m "first commit"
```

如果是Python代码，应该使用下面代码块格式，例如：

![Python代码](/Experiments/img/2023-07-26-22-52-20.png)

显示效果如下：

```python
def add_binary(a,b):
    return bin(a+b)[2:]
```

代码运行结果的文本可以直接粘贴在这里。

**注意：不要使用截图，Markdown文档转换为Pdf格式后，截图可能会无法显示。**

## 实验考查

请使用自己的语言并使用尽量简短代码示例回答下面的问题，这些问题将在实验检查时用于提问和答辩以及实际的操作。

1. Python中的列表可以进行哪些操作？
**索引和切片，添加元素，删除元素，修改元素，长度，遍历，排序等**

1. 哪两种方法可以用来对Python的列表排序？这两种方法有和区别？
**sort()方法：该方法会对列表进行原地排序，即直接修改原列表，不会创建新的列表；sorted()函数：该函数会返回一个新的排序后的列表，而不修改原列表。，sort()方法会对原列表进行原地排序，即直接修改原列表。而sorted()函数会返回一个新的排序后的列表，而不修改原列表。**

1. 如何将Python列表逆序打印？
**要将Python列表逆序打印，可以使用reverse()方法。该方法会直接修改原列表，使其元素逆序排列。**

1. Python中的列表执行哪些操作时效率比较高？哪些操作效率比较差？是否有类似的数据结构可以用来替代列表？
**索引和切片,添加元素：删除元素,修改元素**

1. 阅读《Fluent Python》Chapter 2. An Array of Sequence - Tuples Are Not Just Immutable Lists小节（p30-p35）。总结该小节的主要内容。
**《Fluent Python》Chapter 2主要介绍了Python中的序列类型，包括列表、元组、字符串等。其中，元组是不可变的，可以用作字典的键，也可以作为记录来使用。列表是可变的，支持多种操作，如切片、拼接等。字符串是不可变的序列，同时也是Unicode字符序列，提供了丰富的字符串处理方法。此外，还介绍了如何使用列表推导式和生成器表达式来创建新的序列，以及如何使用切片来截取序列的一部分。**

## 实验总结

总结一下这次实验你学习和使用到的知识，例如：编程工具的使用、数据结构、程序语言的语法、算法、编程技巧、编程思想。
**在本次实验中，我学到了许多有关编程和数据处理的知识，了解了Python中常用的数据结构，如列表（List）和字典（Dictionary）。理解了不同数据结构的特点和适用场景。掌握了Python的基本语法，包括变量、条件语句、循环、函数定义等。学会了如何在Python中处理字符串、列表等数据类型。**

**总的来说，通过这次实验，我对Python编程有了更深入的了解，也学到了一些常用的数据处理技巧和算法。这将对我今后的编程学习和实践产生积极的影响。**
