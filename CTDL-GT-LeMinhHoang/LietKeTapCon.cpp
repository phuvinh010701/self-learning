#include <iostream>
#include <vector>

using namespace std;

void input(int& n, int& k) {
	cout << "Nhap n:";
	cin >> n;
	cout << "\nNhap k:";
	cin >> k;
}

void output(vector<int>a, int k) {
	for (int i = 0; i < k; i++) {
		cout << a[i] << " ";
	}
	cout << endl;
}

vector <int> init(int k) {
	vector <int> a(k);
	for (int i = 0; i < k; i++) {
		a[i] = i + 1;
	}
	return a;
}

void process(vector <int> a, int n, int k) {
	a = init(k);
	while (a[0] != n - k + 1) {
		output(a, k);
		int i = k - 1;
		while (i >= 0 && a[i] == n - k + i + 1) {
			i--;
		}
		if (i >= 0) {
			a[i] += 1;
			for (int j = i + 1; j < k; j++) {
				a[j] = a[j - 1] + 1;
			}
		}
	}
	output(a, k);
}

int main(){
	int n, k;
	vector <int> a;
	input(n, k);
	process(a, n, k);
	return 0;
}