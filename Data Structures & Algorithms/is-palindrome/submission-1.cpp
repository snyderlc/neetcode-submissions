class Solution {
public:
    bool isPalindrome(string s) {
      vector<char>a;
      for (int i=0; i<s.length(); i++){
        s[i]=tolower(s[i]);
        if (isalnum(s[i])){
          a.push_back(s[i]);
        }
      }
      for (int i=0; i<a.size(); i++){
        if  (a[i] != a[a.size()-i-1]){
          return false;
        }
      }
      return true;
    }
};
