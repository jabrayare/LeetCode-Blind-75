from collections import defaultdict
from typing import List
def groupAnagrams(strs: List[str]):  
   
  map = defaultdict(list)
  for word in strs:
      sorted_word = ''.join(sorted(word))
      map[sorted_word].append(word)
  return map.values()
  
  
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]