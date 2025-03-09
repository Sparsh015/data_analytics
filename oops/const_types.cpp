#include <bits/stdc++.h>
using namespace std;

class Rectangle {
private:
    int length;
    int width;

public:
    Rectangle(int l, int w) {
        length = l;
        width = w;
    }

    Rectangle() {
        length = 1;
        width = 1;
    }

    Rectangle( Rectangle &rect) {
        length = rect.length;
        width = rect.width;
    }

    void display() {
        cout << "Length: " << length << ", Width: " << width << endl;
    }
};

int main() {
    Rectangle rect; 
    rect.display(); 

    Rectangle rect2(5, 10); 
    rect2.display(); 

    Rectangle rect3 = rect2; 
    rect3.display(); 

    return 0;
}
