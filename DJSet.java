{
    class DJSet {
	int n;
	int[] upper;
	
	public DJSet(int n_) {
	    n = n_;
	    upper = new int[n_];
	    Arrays.fill(upper, -1);
	}
	
	int root(int x) {
	    return upper[x] < 0 ? x : (upper[x] = root(upper[x]));
	}

	boolean equiv(int x, int y) {
	    return root(x) == root(y);
	}
	
	void setUnion(int x, int y) {
	    x = root(x);
	    y = root(y);
	    if (x == y)
		return;
	    if (upper[x] < upper[y]) {
		x ^= y;
		y ^= x;
		x ^= y;
	    }
	    upper[y] += upper[x];
	    upper[x] = y;
	}
	
	int sz(int x) {
	    return -upper[root(x)];
	}
    }
}
