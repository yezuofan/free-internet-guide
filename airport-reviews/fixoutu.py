c = open('/home/yzf/shared/机场推广/free-internet-guide/airport-reviews/outu.md').read()
old = '[666.youtu6.shop/register?code=Vfs3Qqkm](https://666.youtu6.shop/register?code=***'
new = '[悠兔注册地址](https://666.youtu6.shop/register?code=***'
print(f"old in content: {old in c}")
c2 = c.replace(old, new)
print(f"changed: {c != c2}")
open('/home/yzf/shared/机场推广/free-internet-guide/airport-reviews/outu.md', 'w').write(c2)