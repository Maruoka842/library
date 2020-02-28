---
layout: default
---

<!-- mathjax config similar to math.stackexchange -->
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    TeX: { equationNumbers: { autoNumber: "AMS" }},
    tex2jax: {
      inlineMath: [ ['$','$'] ],
      processEscapes: true
    },
    "HTML-CSS": { matchFontHeight: false },
    displayAlign: "left",
    displayIndent: "2em"
  });
</script>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery-balloon-js@1.1.2/jquery.balloon.min.js" integrity="sha256-ZEYs9VrgAeNuPvs15E39OsyOJaIkXEEt10fzxJ20+2I=" crossorigin="anonymous"></script>
<script type="text/javascript" src="../assets/js/copy-button.js"></script>
<link rel="stylesheet" href="../assets/css/copy-button.css" />


# :warning: djset.cpp

<a href="../index.html">Back to top page</a>

* category: <a href="../index.html#5058f1af8388633f609cadb75a75dc9d">.</a>
* <a href="{{ site.github.repository_url }}/blob/master/djset.cpp">View this file on GitHub</a>
    - Last commit date: 2019-08-12 22:04:20+09:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
#include <vector>

struct DJSet {
  int n;
  std::vector<int> upper;

  DJSet(int n) : upper(n, -1){}

  int root(int x) {
    return upper[x] < 0 ? x : (upper[x] = root(upper[x]));
  }

  bool equiv(int x, int y){
    return root(x) == root(y);
  }

  void setUnion(int x, int y) {
    x = root(x);
    y = root(y);
    if (x == y) return;
    if (upper[x] < upper[y]){
      x ^= y;
      y ^= x;
      x ^= y;
    }
    upper[y] += upper[x];
    upper[x] = y;
  }
  
};


```
{% endraw %}

<a id="bundled"></a>
{% raw %}
```cpp
#line 1 "djset.cpp"
#include <vector>

struct DJSet {
  int n;
  std::vector<int> upper;

  DJSet(int n) : upper(n, -1){}

  int root(int x) {
    return upper[x] < 0 ? x : (upper[x] = root(upper[x]));
  }

  bool equiv(int x, int y){
    return root(x) == root(y);
  }

  void setUnion(int x, int y) {
    x = root(x);
    y = root(y);
    if (x == y) return;
    if (upper[x] < upper[y]){
      x ^= y;
      y ^= x;
      x ^= y;
    }
    upper[y] += upper[x];
    upper[x] = y;
  }
  
};


```
{% endraw %}

<a href="../index.html">Back to top page</a>

