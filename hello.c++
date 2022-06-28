#include <iostream>
#include <stdio.h>
#include <map>
using namespace std;

int main(){
   map<string, int> m, m2;
   int n, s;
   string direktor;
   int xodimlar;
   cin >> n;
   for (int i = 0; i < n; i++){
      cout << i+1 << " - maktabni kiriting:\n";
      cin.ignore();
      cout << "Maktab nomi va direktor FIO: "; getline(cin, direktor);
      cout << "Xodimlar soni: "; cin >> xodimlar;
      m.insert(make_pair(direktor, xodimlar));
   }

   cout << "Xodimlar soni qancha bo'lgan maktablar kerak: ";
   cin >> s;

   for (auto i = m.begin(); i != m.end(); i++){
      if (i->second == s){
         m2.insert(*i);
      }
   }

   cout << "Xodimlar soni " << s << " ga teng bo'lgan maktablar:\n";
   for (auto i = m2.begin(); i != m2.end(); i++){
      cout << i->first << " " << i->second << endl;
   }

   int k;
   cout << "faylga yozilsinmi (1-ha, 0-yo'q): ";
   cin >> k;
   if (k == 1){
      freopen("out.txt", "w", stdout);
      cout << "Xodimlar soni " << s << " ga teng bo'lgan maktablar:\n";
      for (auto i = m2.begin(); i != m2.end(); i++){
         cout << i->first << " " << i->second << endl;
      }
   }

   return 0;
}