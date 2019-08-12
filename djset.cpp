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

