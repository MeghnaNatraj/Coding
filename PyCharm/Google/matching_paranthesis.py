__author__ = 'Meghna'


def pargen(left,right,ans):
    if(left==0 and right==0):
        print(ans)
    if(left>0):
        pargen(left-1,right+1,ans+'(');
    if(right>0):
        pargen(left,right-1,ans+')');
pargen(3,0,'');

# def count(path):
#     return path.count('(')+path.count('P')
# def parens(n,path,result):
#     print(path,result)
#     if n == 0:
#         return
#     else:
#         c = count(path)
#         if (c == n):
#             length = len(path)
#             i = 0
#             while i < length:
#                 if path[i] == 'P':
#                     path = path[:i]+'()'+path[i+1:]
#                     length +=1
#                 i +=1
#             result.append(path)
#         else:
#             for i in range(len(path)):
#                 if path[i] == 'P':
#                     parens(n, path[:i]+'PP'+path[i+1:],result)
#                     parens(n, path[:i]+'(P)'+path[i+1:],result)
#     return result
# print(parens(3,'P',[]))

