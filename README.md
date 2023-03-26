# assertion_test
根据接口返回的response.body自动生成断言,数据取值来自jsonpath  

## 格式  
list返回长度，后续验证list长度是否匹配  
string返回具体内容，后续验证内容是否一致  
dict返回key，后续验证接口返回包含该字段  

## 使用说明  
```
import assertion  
assertion.auto_assert(response.body)  
```
其中*body*已loads  

## TODO  
* 根据断言生成goapi断言形式的文本，并提供写入txt的方法  
* 生成postman中tests结构的文本  
* 根据输出的断言自动测试的脚本