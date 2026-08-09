---
title: "java基础学习"
date: "2026-08-09"
draft: false
tags: []
categories: []
---
常见的Dos命令

```java
# 盘符切换	d:
# 查看当前目录下的所有文件  dir
# 返回上一级	cd ..
# 清理屏幕 cls
# 退出终端 exit
# 查看电脑的ip	ipconfig
# 打开计算机	clac
# 常见文件	cd >a.txt
# 删除文件	del 文件名
```

# JAVA基础

### 1.注释,标识符,关键字

- 平时我们编写代码,在代码量比较少的时候,我们还可以看懂自己写的什么,但当项目结构一旦复制起来,就需要用到注释
- 注释并不会被执行

- java中的注释有三种:
  - 单行注释		//
  - 多行注释                /**      */
  - 文档注释               /**  @Description    */

### 2.数据类型

#### **关键字:**

- ```java
  abstract,assert,boolean,break,byte,case,catch,char,class,const,continue,
  default,do,double,else,enum,extends,final,finally,float,for,goto,if,
  implements.import,instanceof,int,interface,long,native,new,package,private,
  protected,public,return,strictfp,short,static,super,switch,synchronized,this,
  throw,throws,transient,try,void,volatile,while
  ```

- java所有的组成部分都需要名字.类名,变量名以及方法名都被称为标识符

**标识符注意到:**

- 所有的标识符都应该以字母(A-Z或者a-z),美元符($),或者下划线(_)开始
- 首字符之后可以是字母(A-Z或者a-z),美元符($),或者下划线(_)或者数字的任何字符组成
- **不能使用关键字作为变量名或方法名**
- 标识符是**大小写敏感**的
- 合法标识符举例:age,$salary,_value,_1_value
- 非法标识符举例:123abc,-salary,#abc
- **可以使用中文命名,但是一般不建议这样去使用,也不建议使用拼音**

#### **数据类型**

- 强类型语言(java,C++属于强类型语言)

  - 要求变量的使用要严格符合规定,所有变量都必须先定义后才能使用

- 弱类型语言

- java的数据类型分为两大类

  - 基本类型(primitive type)

  - ```java
    //整数
    int num = 10; //最常用(int占4个字节)
    byte num = 20;//byte占1个字节
    short num = 30;//short占据2个字节
    long num = 30l; //long类型要在数字后面加个L(long占8个字节)
    
    //小数:浮点数
    float num = 50.1F; //float类型要在数字后面加个F(float占4个字节)
    double num = 3.122312313123;//double占8个字节
    
    //字符
    char name = '国';//char占2个字节
    //字符串,string不是关键字,类
    
    //布尔值:是非(boolean占1个字节)
    boolean flag = true;	
    // boolean flag = false;
    ```

  - 引用类型(reference type)

**什么是字节:**

- 位(bit):是计算机 **内部数据** 存储的最小单位,11001100是一个八位二进制数
- 字节(byte):是计算机中 **数据处理** 的基本单位,习惯上用大写 B 来表示
- 1B(byte,字节) = 8 bit(位)
- 字符:是指计算机中使用的字母,数字,字和符号

- 1bit表示1位
- 1Byte表示一个字节   1B = 8b
- 1024B = 1KB
- 1024KB = 1M
- 1024M = 1G

**整数拓展:**(二进制,十进制,八进制,十六进制)

**浮点数拓展:**(存在舍入误差,接近但不等于,最好避免使用浮点数进行比较)

### 3.类型转换

- 由于java是强类型语言,所有要进行有些运算的时候,需要用到类型转换

  ```java
  低------------------------------------------高
  byte,short,char->int->long->float->double
  
  //强制转换	(类型)变量名		高--低
  //自动转换	低--高
  ```

- 运算中,不同类型的数据先转化为同一类型,然后进行运算

- 强制类型转换

  - ```java
    注意点:
    1.不能对布尔值进行转换
    2.不能把对象类型转换为不相干的类型
    3.在把高容量转换到低容量的时候,强制转换
    4.转换的时候可能存在内存溢出,或者精度问题
    5.先转换后计算
    ```

- 自动类型转换

### 4.变量,常量

#### 变量:

- 变量是什么:就是可以变化的量
- java是一种强类型语言,每个变量都必须声明其类型
- java变量是程序中最基本的存储单元,其要素包括**变量名**,**变量类型**和**作用域**

```java
type varName [=value][{,varName[=value]}]
//数据类型	变量名 = 值;可以使用逗号隔开来声明多个同类型变量
```

- 注意事项
  - 每个变量都有类型,类型可以是基本变量,也可以是引用变量
  - 变量名必须是合法的标识符
  - 变量声明是一条完整的语句,因此每一个声明都必须以分号结束

**变量作用域**:

```java
public class Variable{
    static int allClicks = 0;	//类变量	static
    String str = "hello world"	//实例变量:从属于对象;如果不自行初始化,这个类型的默认值
    //布尔值:默认是false,除了基本类型,其余的默认值都是null;
    public void method(){
        int i = 0;		//局部变量:必须声明和初始化值
    }
}
```

**变量的命名规则:**

- 所有变量,方法,类名:见名知意
- 类成员变量:首字母小写和驼峰原则:monthSalary
- 局部变量:首字母小写和驼峰原则
- 常量:大写字母和下下划线:MAX_VALUE
- 类名:首字母大写和驼峰原则:Man,GoodMan
- 方法名:首字母小写和驼峰原则:run(),runRun()

**4.2 常量(final):**

- 常量(Constant):初始化(initialize)后不能再改变值,不会变动的值

- 所谓常量可以理解陈一种特殊的变量,它的值被设定后,在程序运行过程中不允许被改变

- ```java
  final 常量名 = 值
  final double PI = 3..14;
  //常量(final)为修饰符,不存在先后顺序
  ```

- 常量名一般使用大写字符

### 5.运算符

- Java语言支持如下运算符:
  - 算术运算符:+,-,*,/,%,++,--
  - 赋值运算符:=
  - 关系运算符:>,<,>=,<=,==,!= ,instanceof
  - 逻辑运算符:&&,||,!
  - 位运算符:&,|,^,~,>>,<<,>>>(效率极高)
  - 条件运算符: ?, :[关系式?表达式1:表达式2]
  - 拓展赋值运算符:+=,-=,*=,/=

### 6.包机制,JavaDoc

#### 包机制

- 为了更好地组织类,Java提供了包机制,用于区别类名的命名空间

- 包语句的语法格式为:

  ```java
  package pkg1[.pkg2[.pkg3.....]]
  ```

- 一般利用公司域名倒置为包名;

- 为了能够使用某一个包的成员,需要在Java程序中明确导入该包.使用"import"语句可完成此功能

  ```java
  import package1[.package2...].(classname|*)
  ```

#### JavaDoc

- javadoc命令是用来生成自己API文档

# JAVA流程控制

### 1.用户交互Scanner

- 可以通过Scanner类来获取用户的输入
- 基本语法:Scanner s = new Scanner(System.in);
- 通过Scanner类的next()与nextLine()方法获取输入的字符串,在读取前我们一般需要 使用hasNext() 与 hasNextLine() 判断是否还有输入的数据

```java
//创建一个扫描器对象,用于接收键盘数据
Scanner scanner = new Scanner(System.in);
//判断用户有没有输入字符串
if(scanner.hasNext()){
    //使用hext方法接收
    String str = scanner.next();
    System.out.println("输出的内容为"+str);
}

//凡是属于IO流的类如果不关闭会一直占用资源
scanner.close();
```

- **next():**
  - 一定要读取到有效字符后才可以结束输入
  - 对输入有效字符之前遇到的空白,next()方法会自动将其去掉
  - 只有输入有效字符后才将其后面输入的空白作为分隔符或者结束符
  - **next()不能得到带有空格的字符串**
- **nextLine():**
  - 以Enter为结束符,也就是说 nextLine()方法返回的是输入回车之前的所有字符
  - 可以获得空白

### 2.顺序结构

- JAVA的基本结构就是顺序结构,除非特别指明,否则就按照顺序一句一句执行
- 顺序结构是最简单的算法结构
- 语句与语句之间,框与框之间是按从上到下的顺序进行的,它是由若干个依次执行的处理步骤组成的,**它是任何一个算法都离不开的一种基本算法结构**

### 3.选择结构

1. if 单选择结构

   1. 我们很多时候需要去判断一个东西是否可行,然后我们才去执行,这样一个过程在程序中用if语句来表示

   2. 语法

      ```java
      if(布尔表达式){
          //如果布尔表达式为true将执行的语句
      }
      ```

2. if 双选择结构

   1. 那现在有个需求,公司要收购一个软件,成功了,给人支付100万元,失败了,自己找人开发.这样的需求用一个if就搞不定,需要两个判断,需要一个双选择结构,所以就有了if-else结构

   2. 语法

      ```java
      if(布尔表达式){
          //如果布尔表达式的值为true
      }else{
          //如果布尔表达式的值为false
      }
      ```

      

3. if多选择结构

   1. 语法

      ```java
      if(布尔表达式 1){
          //如果布尔表达式 1 的值为true执行代码
      }else if(布尔表达式 2){
           //如果布尔表达式 2 的值为true执行代码
      }else if(布尔表达式 3){
           //如果布尔表达式 3 的值为true执行代码
      }else{
          //如果以上布尔表达式都不为true执行代码
      }
      ```

      

4. 嵌套的if结构

   1. 使用嵌套的if....else语句是合法的.也就是说你可以在另一个if或者else if语句中使用if或者else if语句

   2. 语句:

      ```java
      if(布尔表达式 1){
          //如果布尔表达式 1 的值为true执行代码
          if(布尔表达式 2){
              //如果布尔表达式 2 的值为true执行代码
          }
      }
      ```

      

5. switch多选择结构

   1. 多选择结构还有一个实现方式就是switch case 语句
   2. switch case 语句判断一个变量与一系列值是否相等,每个值称为一个分支
   3. switch语句中的变量类型可以是:
      1. byte,short,int 或者char
      2. **从Java SE 7 开始**
      3. **switch 支持字符串 String类型了**
      4. 同时case标签必须为字符串常量或字面量
   
   ```java
   switch(expression){
       case value:
           //语句
           break; //可选
       case value:
           //语句
           break;//可选
       //你可以有任意数量的case语句
       default: //可选
           //语句
   }
   ```
   
   

### 4.循环结构

- **while循环**

  - while是最基本的循环,它的结构为:

    ```java
    while(布尔表达式){
        //循环内容
    }
    ```

  - 只要布尔表达式为true,循环就会一直循环下去

  - 大多数情况是会让循环停下来,需要一个让表达式失效的方法来结束循环

  - 少部分情况需要循环一直执行

  - 循环条件一直为true就会造成无线循环[死循环],正常的业务编程中应该尽量避免死循环.会影响程序性能或者造成程序卡死崩溃

- **do ... while 循环**

  - 对于while语句而言,如果不满足条件,则不能进入循环,但有时候我们需要即使不满足条件,也至少执行一次

  - do ... while 循环和while循环相似,不同的是,do ... while循环至少会执行一次

    ```java
    do{
        //代码语句
    }while(布尔表达式)
    ```

  - while 和 do - while的区别:

    - while先判断后执行.dowhile是先执行后判断
    - do ... while总是保证循环体会被至少执行一次.这是他们的主要差别

- **for循环**

  - 虽然所有循环结构都可以用while或者do....while表示,但java提供了另一种语句 for循环,使一些循环结构变得更加简单

  - for循环语句是支持迭代的一种通用结构,是最有效,最灵活的循环结构

  - for循环结构执行的次数是在执行前就确定的

    ```java
    for(初始化;布尔表达式;更新){
        //代码语句
    }
    ```

    

- 在Java5中引入了一种主要用于数组的**增强型for循环**

  - 先了解,数组重点使用

  - 语句

    ```java
    for(声明语句 : 表达式){
        //代码句子
    }
    ```

  - 声明语句:声明新的局部变量,该变量的类型必须和数组元素的类型匹配,其作用域限定在循环语句块,其值与此时数组元素的值相等

  - 表达式 : 表达式是要访问的数组名,或者是返回值为数组的方法

### 5.break & continue

- break在任何循环语句的主题部分,均可用break控制循环的流程.break用于强行退出循环,不执行循环中剩余的语句(break语句也在switch语句中使用)
- contnue语句用在循环语句体中,用于终止某次循环过程,即跳过循环体中尚未执行的语句,接着进行下一次是否执行循环的判定
- 关于goto关键字
  - goto关键字很早就在程序设计语言中出现,尽管goto仍是java的一个保留字,但并未在语言中得到正式使用:java没有goto,然而,在break和continue这两个关键字的身上,仍然能看出一些goto的影子----带标签的break和continue
  - "标签"是指后面跟一个冒号的标识符
  - 对java来说唯一用到标签的地方是在循环语句之前,而在循环之前设置标签的唯一理由是:希望在其中嵌套另一个循环,由于break和continue关键字通常只中断当前循环,但若随同标签使用,就会中断到存在标签的地方

# JAVA方法详解

### 1.何谓方法

- System.out.println()是什么
- java方法是语句的集合,它们在一起执行一个功能
  - 方法是解决一类问题的不在的有序组合
  - 方法包含于类或对象中
  - 方法在程序中被创建,在其他地方被引用
- 设计方法的原则:方法的本意是功能块,就是实现某个功能的语句块的集合.我们设计方法的时候,最好保存方法的原子性,**就是一个方法只完成1个功能,利于后期的拓展**

### 2.方法的定义及调用

#### 2.1 方法的定义

- Java的方法类似于其他语言的方式,是一段**用来完成特定功能的代码片段**,一般情况下,定义一个方法包含以下语句:

- **方法包含一个方法头和一个方法体**,下面是一个方法的所有部分:

  - **修饰符**:修饰符,这是可选的,告诉编译器如何调用该方法.定义了该方法的访问类型

    - 访问修饰符

      - **default**(即默认,什么也不写): 在同一包内可见，不使用任何修饰符。使用对象：类、接口、变量、方法

        ```java
        // MyClass.java
         
        class MyClass {  // 默认访问修饰符
         
            int x = 10;  // 默认访问修饰符
         
            void display() {  // 默认访问修饰符
                System.out.println("Value of x is: " + x);
            }
        }
         
        // MyOtherClass.java
         
        class MyOtherClass {
            public static void main(String[] args) {
                MyClass obj = new MyClass();
                obj.display();  // 访问 MyClass 中的默认访问修饰符变量和方法
            }
        }
        ```

        

      - **private** : 在同一类内可见。使用对象：变量、方法。 **注意：不能修饰类（外部类）**

        ```java
        public class Logger {
           private String format;
           public String getFormat() {
              return this.format;
           }
           public void setFormat(String format) {
              this.format = format;
           }
        }
        ```

        

      - **public** : 对所有类可见。使用对象：类、接口、变量、方法

        ```java
        public static void main(String[] arguments) {
           // ...
        }
        ```

        

      - **protected** : 对同一包内的类和所有子类可见。使用对象：变量、方法。 **注意：不能修饰类（外部类）**

        ```java
        class AudioPlayer {
           protected boolean openSpeaker(Speaker sp) {
              // 实现细节
           }
        }
         
        class StreamingAudioPlayer extends AudioPlayer {
           protected boolean openSpeaker(Speaker sp) {
              // 实现细节
           }
        }
        ```

        

    - 非访问修饰符

      - **static** 修饰符，用来修饰类方法和类变量。

        - **静态变量：**static 关键字用来声明独立于对象的静态变量，无论一个类实例化多少对象，它的静态变量只有一份拷贝。 静态变量也被称为类变量。局部变量不能被声明为 static 变量。

        - **静态方法：**static 关键字用来声明独立于对象的静态方法。静态方法不能使用类的非静态变量。静态方法从参数列表得到数据，然后计算这些数据。

          ```java
          public class InstanceCounter {
             private static int numInstances = 0;
             protected static int getCount() {
                return numInstances;
             }
           
             private static void addInstance() {
                numInstances++;
             }
           
             InstanceCounter() {
                InstanceCounter.addInstance();
             }
           
             public static void main(String[] arguments) {
                System.out.println("Starting with " +
                InstanceCounter.getCount() + " instances");
                for (int i = 0; i < 500; ++i){
                   new InstanceCounter();
                    }
                System.out.println("Created " +
                InstanceCounter.getCount() + " instances");
             }
          }
          ```

          

      - **final** 修饰符，用来修饰类、方法和变量，final 修饰的类不能够被继承，修饰的方法不能被继承类重新定义，修饰的变量为常量，是不可修改的

        - **final 变量：**final 表示"最后的、最终的"含义，变量一旦赋值后，不能被重新赋值。被 final 修饰的实例变量必须显式指定初始值。final 修饰符通常和 static 修饰符一起使用来创建类常量

          ```java
          public class Test{
            final int value = 10;
            // 下面是声明常量的实例
            public static final int BOXWIDTH = 6;
            static final String TITLE = "Manager";
           
            public void changeValue(){
               value = 12; //将输出一个错误
            }
          }
          ```

        - **final 方法**:父类中的 final 方法可以被子类继承，但是不能被子类重写。

          声明 final 方法的主要目的是防止该方法的内容被修改。

          如下所示，使用 final 修饰符声明方法

          ```java
          public class Test{
              public final void changeName(){
                 // 方法体
              }
          }
          ```

        - **final 类**:final 类不能被继承，没有类能够继承 final 类的任何特性。

          ```java
          public final class Test {
             // 类体
          }
          ```

          

      - **abstract** 修饰符，用来创建抽象类和抽象方法。

        - **抽象类**:抽象类不能用来实例化对象，声明抽象类的唯一目的是为了将来对该类进行扩充。一个类不能同时被 abstract 和 final 修饰。如果一个类包含抽象方法，那么该类一定要声明为抽象类，否则将出现编译错误。抽象类可以包含抽象方法和非抽象方法。

          ```java
          abstract class Caravan{
             private double price;
             private String model;
             private String year;
             public abstract void goFast(); //抽象方法
             public abstract void changeColor();
          }
          ```

        - **抽象方法**抽象方法是一种没有任何实现的方法，该方法的具体实现由子类提供。

          抽象方法不能被声明成 final 和 static。

          任何继承抽象类的子类必须实现父类的所有抽象方法，除非该子类也是抽象类。

          如果一个类包含若干个抽象方法，那么该类必须声明为抽象类。抽象类可以不包含抽象方法。抽象方法的声明以分号结尾

          ```java
          public abstract class SuperClass{
              abstract void m(); //抽象方法
          }
           
          class SubClass extends SuperClass{
               //实现抽象方法
                void m(){
                    .........
                }
          }
          ```

          

      - **synchronized** 和 volatile 修饰符，主要用于线程的编程。

        - synchronized 关键字声明的方法同一时间只能被一个线程访问。synchronized 修饰符可以应用于四个访问修饰符。

          ```java
          public synchronized ` showDetails(){
          .......
          }
          
          ```

          - **transient修饰符**:序列化的对象包含被 transient 修饰的实例变量时，java 虚拟机(JVM)跳过该特定的变量。该修饰符包含在定义变量的语句中，用来预处理类和变量的数据类型

          ```java
          public transient int limit = 55;   // 不会持久化
          public int b; // 持久化
          ```

      - ### volatile 修饰符

        - volatile 修饰的成员变量在每次被线程访问时，都强制从共享内存中重新读取该成员变量的值。而且，当成员变量发生变化时，会强制线程将变化值回写到共享内存。这样在任何时刻，两个不同的线程总是看到某个成员变量的同一个值。

        - 一个 volatile 对象引用可能是 null。

          ```java
          public class MyRunnable implements Runnable
          {
              private volatile boolean active;
              public void run()
              {
                  active = true;
                  while (active) // 第一行
                  {
                      // 代码
                  }
              }
              public void stop()
              {
                  active = false; // 第二行
              }
          }
          ```

          

  - **返回值类型**:方法可能会返回值.returnValueType是方法返回值的数据类型.有些方法执行所需的操作,但没有返回值.在这种情况下,returnValueType是关键字void
  - **方法名**:是方法的实际名称,方法名和参数表共同构成方法签名
  - **参数类型**:参数像是一个占位符.当方法被调用时,传递值给参数.这个值被称为实参或变量.参数列表是指方法的参数类型,顺序和参数的个数.参数是可选的,方法可以不包含任何参数
    - 形式参数:在方法被调用时由于接收外界输入的数据
    - 实参:调用方法时实际传给方法的数据
  - **方法体**:方法体包含具体的语句,定义该方法的功能

- 语法

  ```java
  修饰符	返回值类型 方法名(参数类型 参数名){
      ....
      方法体
      ....
      return 返回值;
  }
  
  public(公开) static(静止) void(无返回,不可实例化的占位符) 方法名(String[] args){
      
      return 返回值;
  }
  ```

#### 2.2 方法的调用

- 调用方法:对象名.方法名(实参列表)

- Java支持两种调用方法的方式,根据方法是否返回值来选择

- 当方法返回一个值的时候,方法调用通常被当做一个值

  ```java
  int larger = max(30,40);
  ```

- 如果方法返回值是void,方法调用一定是一条语句

  ```java
  System.out.println("Hello,kuangshen")
  ```
  
- 静态方法:static

- 非静态方法


### 3.方法重载

- 重载就是在一个类中,有相同的函数名称,但形参不同的函数
- 方法的重载的规则:
  - 方法名称必须相同
  - 参数列表不同(个数不同,或类型不同,参数排列顺序不同等)
  - 方法的返回类型可以相同也可以不相同
  - 仅仅返回类型不同不足以成为方法的重载
- 实现理论:
  - 方法名称相同时,编译器会根据调用方法的参数个数,参数类型等去逐个匹配,以选择对应的方法,如果匹配失败,则编译器报错

```java
public static void main(String[] args) {
        double max = max(10,20);
        System.out.println(max);
    }

    public static double max(double num1, double num2) {
        double result = 0;
        if (num1 == num2){
            System.out.println("num1 == num2");
            return 0;
        }
        if (num1 > num2){
            result = num1;
        }else {
            result = num2;
        }
        return result;
    }

    public static double max(int num1, int num2) {
        int result = 0;
        if (num1 == num2){
            System.out.println("num1 == num2");
            return 0;
        }
        if (num1 > num2){
            result = num1;
        }else {
            result = num2;
        }
        return result;
    }
```



### 4.命令行传参

- 有时候你希望运行一个程序时候再传递给它消息,要靠传递命令行参数给main()函数实现

  ```java
  public class CommandLine{
      public static void main(String args[]){
          for(int i=0;i<args.length;i++){
              System.out.println("args["+i+"]:"+args[i])
          }
      }
  }
  ```

  

### 5.可变参数

- JDK1.5开始,java支持传递同类型的可变参数给一个方法

- 在方法声明中,在指定参数类型后加一个省略号(....)

- 一个方法中只能指定一个可变参数,它必须是方法的最后一个参数.任何普通的参数必须在它之前声明

  ```java
  public static void printMax(double... numbers){
      if(numbers.length == 0){
          System.out.println("No argument passed");
          return;
      }
      double result = numbers[0];
      
      //排序
      for(int i = 1;i < numbers.length;i++){
          if(numbers[i] > result){
              result = numbers[i];
          }
      }
      System.out.println("The max value is" + result);
  }
  ```

  

### 6.递归

- A方法调用B方法,容易理解
- 递归就是:A方法调用A方法,就是自己调用自己
- 利用递归可以用简单的程序来解决一些复杂的问题,它通常把一个大型复杂的问题层层转化为一个与原问题相似的规模较小的问题来求解.递归策略只需少量的程序就可描述出解题过程所需要的多次重复计算,大大的减少了程序的代码量,递归的能力终于用有效的语句来定义对象的无限集合
- **递归结构**包括两个部分:
  - **递归头**:什么时候不调用自身方法.如果没有头,将陷入死循环
  - **递归体**:什么时候需要调用自身方法

# JAVA数组

### 1.数组概念

- 数组是相同类型数据的有序集合
- 数组描述的是相同类型的若干个数据,按照一定的先后次序排列组合而成
- 其中,每一个数据称作一个数组元素,每个数组元素可以通过一个下标来访问他们

### 2.数组声明创建

- 首先必须声明数组变量,才能在程序中使用数组.下面是声明数组变量的语法:

  ```java
  dataType[] arrayRefVar;	//首选的方法
  或
  dataType arrayRefVar [];  //效果相同,但不是首选方法	
  ```

- Java语法使用new操作符来创建数组,语法如下:

  ```java
  dataType[] arrayRefVar = new dataType[arraySize];
  ```

- 数组的元素是通过索引访问的,数组索引从0开始

- 获得数组长度:

  ```java
  arrays.length
  ```

**数组的四个基本特点:**

- 其长度是确定的,数组一旦被创建,它的大小就是不可以改变的
- 其元素必须是相同类型,不允许出现混合类型
- 数组中的元素可以是任何数据类型,包括基本类型和引用类型
- 数组变量属引用类型,数组也可以看成是对象,数组中的每个元素相当于该对象的成员变量.数组本身就是对象,java中对象是在堆中的,因此数组无论保存原始类型还是其他对象类型,**数组对象本身是在堆中的**

### 3.内存分析

- Java内存分析:
  1. 堆
     1. 存放new的对象和数组
     2. 可以被所有的线程共享,不会存放别的对象引用
  2. 栈
     1. 存放基本变量类型(会包含这个基本类型的具体数值)
     2. 引用对象的变量(会存放这个引用在堆里面的具体地址)
  3. 方法区:
     1. 可以被所有的线程共享
     2. 包含了所有的class和static变量

**三种初始化**:

- 静态初始化

  ```java
  int[] a ={1,2,3};
  Man[] mans = {new Man(1,1),new Man(2,2)};
  ```

- 动态初始化

  ```java
  int[] a = new int[2];
  a[0] = 1;
  a[1] = 2;
  ```

- 数组的默认初始化

  - 数组是引用类型,它的元素相当于类的实例变量,因此数组一经分配空间,其中的每个元素也被按照实例变量同样的方式被隐式初始化

**数组边界:**

- 下标的合法区间:[0,length -1],如果越界就会报错:

  ```java
  public static void main(String[] args){
      int[] a = new int[2];
      System.out.println(a[2]);
  }
  ```

- **ArraylndexOutOfBoundsException:数组下标越界异常**

- 小结:

  - 数组是相同数据类型(数据类型可以为任意类型)的有序集合
  - 数组也是对象.数组元素相当于对象的成员变量
  - 数组长度的确定的,不可变的,如果越界,则报:ArraylndexOutofBounds

### 4.数组使用

- For-Rach循环
- 数组作方法入参
- 数组作返回值

### 5.多维数组

- 多维数组可以看成是数组的数组,比如二维数组就是一个特殊的一维数组,其每一个元素都是一个一维数组

- 二维数组

  ```java
  int a[][] = new int[2][5];
  ```

  

### 6.Arrays类

- 数组的工具类java.util.Arrays
- 由于数组对象本身并没有什么方法可以供我们调用,但API中提供了一个工具类Arrays供我们使用,从而可以对数据对象进行一些基本的操作
- **查看JDK帮助文档**
- Arrays类中的方法都是static修饰的静态方法,在使用的时候可以直接使用类名进行调用,而"不用"使用对象类调用(注意:是"不用"而不是"不能")
- 具有以下常用功能:
  - 给数组赋值:通过fill方法
  - 对数组排序:通过sort方法,按升序
  - 比较数组:通过equals方法比较数组中元素值是否相等
  - 查找数组元素:通过binarySearch方法能对排序好的数组进行二分查找法操作

### 7.冒泡排序

- 冒泡排序无疑是最为出名的排序算法之一,总共有八大排序
- 冒泡的代码还是相当简单,两层循环,外层冒泡轮数,里程依次比较
- 算法的时间复杂度为O(n2)

```java
1.比较数组中,两个相邻的元素,如果第一个数比第二个数打,就交换他们的位置
2.每一次比较,都会产生出一个最大,或者最小的数字
3.下一轮则可以少一次排序
4.依次循环,直到结束
```



### 8.稀疏数组

- 当一个数组中大部分元素为0,或者为同一值的数组时,可以使用稀疏数组来保存该数组
- 稀疏数组的处理方式是:
  - 记录数组一共有几行几列,有多少个不同值
  - 把具有不同值的元素和行列及值记录在一个小规模的数组中,从而缩小程序的规模

```java
//1.创建一个二维数组    0:没有棋子,1:黑棋,2:白棋
        int[][] arr = new int[11][11];
        arr[1][2] = 1;
        arr[2][3] = 1;
        //输出原始的数组
        System.out.println("输出原始的数组");

        for (int[] ints : arr) {
            for (int anInt : ints) {
                System.out.print(anInt+"\t");
            }
            System.out.println();
        }
        //转换为稀疏数组
        //获取有效值的个数
        int sum = 0;
        for (int i = 0; i < 11; i++) {
            for (int j = 0; j < 11; j++) {
                if (arr[i][j] != 0) {
                    sum ++;
                }
            }
        }
        System.out.println("有效值的个数:"+sum);

        //创建一个稀疏数组的数组
        int[][] arr2 = new int[sum+1][3];
        arr2[0][0] = 11;
        arr2[0][1] = 11;
        arr2[0][2] = sum;

        //遍历二维数组,将非零的值,存放稀疏数组中
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                if (arr[i][j] != 0) {
                    count++;
                    arr2[count][0] = i;
                    arr2[count][1] = j;
                    arr2[count][2] = arr[i][j];
                }
            }
        }
        //输出稀疏数组
        System.out.println("稀疏数组");
        for (int i = 0; i < arr2.length; i++) {
            System.out.println(arr2[i][0]+"\t" +
                    arr2[i][1]+"\t"+
                    arr2[i][2]+"\t");
        }

        System.out.println("==================");
    }
```

# JAVA面向对象

### 1.初始面向对象

#### 面向过程&面向对象

- **面向过程思想**
  - 步骤清晰简单,第一步做什么,第二步做什么..........
  - 面对过程适合处理一些较为简单的问题
- **面向对象思想**
  - 物以类聚**,分类**的思维模式,思考问题首先会解决问题需要哪些分类,然后对这些分类进行单独思考.最后,才对某个分类下的细节进行面向过程的思索
  - 面向对象适合处理复杂的问题,适合处理需要多人协作的问题
- 对于描述复杂的事物,为了从宏观上把握,从整体上合理分析,需要使用面向对象的思路来分析整个系统,但是,具体到微观操作,仍然需要面向过程的思路去处理

#### 什么是面向对象

- 面向对象编程(Object-Oridented Programming,OOP)
- 面向对象编程的本质就是:**以类的方法组织代码,以对象的组织(封装)数据**
- 抽象
- 三大特性:
  - **封装**
  - **继承**
  - **多态**
- 从认识论角度考虑是先有对象后有类.对象,是具体的事物.类,是抽象的,是对对象的抽象
- 从代码运行角度考虑是先有类后有对象.类是对象的模板

### 2.方法回顾和加深

##### 拓展:

- 调用非静态方法需要将非静态方法实例化

  ```java
  Student st = new Student().say();
  
  say():方法名
  Student():非静态方法的类名
  ```

  

### 3.对象的创建分析

#### 类与对象的关系:

- **类是一种抽象的数据类型,它是对某一类事物整体描述/定义,但是并不能代表某一个具体的事物**
  - 动物,植物,手机,PC
  - Person类,Pet类,Car类等,这些类都是用来描述/定义某一类具体的事物应该具备特点和行为
- **对象是抽象概念的具体实例**
  - 张三就是人的一个具体实例,张三家里的旺财就是狗的一个具体实例
  - 能够体现出特点,展现出功能的是具体的实例,而不是一个抽象的概念

#### 创建与初始化对象:

- **使用new关键字创建对象**

- 使用new关键字创建的时候,除了分配内容空间之外,还会给 创建好的对象 进行默认的初始化以及对类中构造器的调用

- **类中的构造器**也称为**构造方法**,是在进行创建对象的时候必须要调用的,并且构造器有以下两个特点:
  1. 必须和类的名字相同
  2. 必须没有返回类型,也不能写void
  
- **构造器必须掌握**

  ```java
  //无参构造
  //1.使用new关键字,本质就是调用构造器
  //2.用来初始化值
  public Person(){}
  //有参构造:一旦定义了有参构造,无参就必须显示定义
  public Person(String name){
      this.name = name;
  }
  ```

#### 总结:

1. 和类名相同
2. 没有返回值

#### 左右:

1. new 本质在调用构造方法
2. 初始化对象的值

#### 注意点:

1. 定义有参构造之后,如果想使用无参构造,显示的定义一个无参的构造

### 4.面向对象三大特性

#### 4.1 封装

- 该露的露,该藏的藏
  - 我们程序设计要追求"**高聚合,低耦合**".高内聚就是类的内部数据操作细节自己完成,不允许外部干涉;低耦合:仅暴露少量的方法给外部使用
- 封装(数据的隐藏)
  - 通常,应禁止直接访问一个对象中数据的实际表示,而应通过操作接口来访问,这称为信息隐藏
- **属性私有:get/set**

#### 4.2 继承

- 继承的本质是对某一批类的抽象，从而实现对现实世界更好的建模
- **extands**的意思是“拓展”，子类是父类的拓展
- JAVA中只有单继承，没有多继承
- 继承是类和类之间的一种关系。除此之外，类和类之间的关系还有依赖，组合，聚合等
- 继承关系的两个类，一个为之类（派生类）一个为父类（基类）。子类继承父类，使用关键字extends来表示
- 子类和父类之间，从意义上讲应该具有“is a”的关系
- object类
- super
  - 注意点：
    - super调用父类的构造方法，必须做构造方法的第一个
    - super必须只能出现在子类的方法或者构造方法中
    - super和this不能同时调用构造方法

  - VS   this
    - 代表的对象不同：
      - this ：本身调用者这个对象
      - super：代表父类对象的应用

    - 前提：
      - this：没有继承也可以使用
      - super：只能中继承条件才可以使用

    - 构造方法：
      - this(); :本类的构造
      - super(); : 父类的构造

- 方法重写：需要有继承关系，子类重写父类的方法
  - 方法名必须相同
  - 参数列表必须相同
  - 修饰符：范围可以扩大但不能缩小：  private < public
  - 抛出的异常：范围可以被缩小但不能扩大     ClassNotFoundExcetion -->Excetion(大)
- 重写：子类的方法和父类必须一致，方法体不同

为什么需要重写：

1. 父类的功能，子类不一定需要，或者不一定满足

#### 4.3 多态

- 动态编译：类型：可拓展性
- 即同一方法可以根据发送对象的不同而采用多种不同的行为方式
- 一个对象的实际类型是确定的，但可以指向对象的引用的类型有很多(父类，有关系的类)
- 多态存在的条件
  - 有继承关系
  - 子类重写父类方法
  - 父类引用指向子类对象
- 注意：
  - 多态是方法的多态，属性没有多态性
  - 父类和子类，有联系   类型转换异常
  - 存在条件：继承关系，方法需要重写，父类引用指向子类对象

- **instanceof** 类型转换-->引用类型转换，判断一个对象是什么类型

### 5.抽象类和接口

#### 5.1抽象类

- **abstract**修饰符可以用来修饰方法也可以修饰类，如果修饰方法，那么该方法就是抽象方法；如果修饰类，那么该类就是抽象类
- 抽象类中可以没有抽象方法，但是有抽象方法的类一定要声明为抽象类
- 抽象类，不能使用new关键字来创建对象，它是用来让子类继承的
- 抽象方法，只有方法的声明，没有方法的实现，它是用来让子类实现的
- 子类继承抽象类，那么就必须要实现抽象类没有实现的抽象方法，否则该子类也要声明为抽象类

抽象类的特点：

1. 不能new这个抽象类，只能靠子类去实现它：约束
2. 抽象类可以写普通方法
3. 抽象方法必须只抽象类中

#### 5.2接口

- **普通类：只有具体实现**
- **抽象类：具体实现和规范（抽象方法）都有**
- **接口：只有规范**
- 接口就是规范，定义的是一组规范，体现了现实世界中“如果你是。。。则必须能”的思想。
- **接口的本质是契约**，就像我们的法律一样，制定好后大家都遵守
- OO的精髓，是对对象的抽象，最能体现这一点的就是接口
- 声明类的关键字是class，声明接口的关键字是interface
- 接口的作用：
  - 约束
  - 定义一些方法，让不同的人实现
  - public abstract
  - public static final
  - 接口不能被实例化，接口中没有构造方法
  - implements可以实现多个接口，实现接口必须重写接口中的方法


### 6.内部类及OOP实战

- 内部类就是在一个类的内部在定义一个类，比如，A类中定义一个B类，那么B类相对A类来说就称为**内部类**，而A类相对B类来说就是外部类

- #### 1.成员内部类

- #### 2.静态内部类

- #### 3.局部内部类

- #### 4.匿名内部类

# JAVA异常

### 1.什么是异常

- 软件程序在运行过程中，非常可能遇到刚刚提到的这些异常问题，我们叫异常，英文是：**Exception**，意思是例外，这些，例外情况，或者叫异常，怎么让我们写的程序做出合理的处理，而不至于程序崩溃
- 异常指程序运行中出现的不期而至的各种情况，如：文件找不到，网络连接失败，非法参数等
- 异常发生中程序运行期间，它影响了正常的程序执行流程

### 2.异常体系结构

- 要理解java异常处理是如何工作的，需要掌握以下三种类型的异常：
- **异常处理框架**
  - java把异常当作对象来处理，并定义一个基类java.lang.Throwable作为所有异常的超类
  - 在java API 中已经定义了许多异常类，这些异常分为两大类：**错误Error** 和 **异常Exception**

- **检查性异常**：最具代表的检查性异常是用户错误或问题引起的异常，这是无法预见的
- **运行时异常**：运行时异常是可能被程序员避免的异常。与检查性异常相反，运行时异常中编译时被忽略
- **错误 ERROR**：错误不是异常，而时脱离程序员控制的问题。错误在代码中通常被忽略。

####  Error

* Error类对象由java虚拟机生成并抛出，大多数错误与代码编写者所执行的操作无关
* java虚拟机运行错误(Virtual MachineError),当JVM不再有继续执行操作所需的内存资源时，将出现 OutOfMemoryError。这些异常发生时，java虚拟机 （JVM）一般会选择线程终止。
* 还有发生中虚拟机试图执行应用时，如类定义错误（NoClassDefFoundError），链接错误（LinkageError），这些错误是不可查的，因为他们在应用程序的控制和处理能力之外，而且绝大多数是程序运行时不允许出现的状况

#### Exception

- 在Exception分支中有一个重要的子类RuntimeException(运行时异常)
  - ArraylndexOutOfBoundsException(数组下标越界)
  - NullPointerException(空指针异常)
  - ArithmeticException(算术异常)
  - MissingResourceException(丢失资源)
  - ClassNotFoundException(找不到类)等异常，这些异常是不检查异常，程序中可以选择捕获处理，也可以不处理
- 这些异常一般是由程序逻辑错误引起的，程序应该从逻辑角度尽可能避免这类异常的发生
- Error 和 Exception的区别：Error通常是灾难性的致命的错误，是程序无法控制和处理的，当出现这些异常时，java虚拟机（JVM）一般会选择终止线程，Excepton通常情况下是可以被程序处理的，并且中程序中应该尽可能的钱处理这些异常

### 3.java异常处理机制

- #### 抛出异常

- #### 捕获异常

- #### 异常处理五个关键字

  - ##### try,catch, finally,throw,throws

  ```java
  public class Test {
      public static void main(String[] args) {
          int a = 1;
          int b = 0;
  
          try {
              //try监控区域
              System.out.println(a/b);
          }catch (ArithmeticException e){
              //catch（想要捕获的异常类型） 捕获异常
              System.out.println("除数不能为 0 ");
          }finally {
              // finally 处理善后工作，可以不要
              System.out.println("finally");
          }
      }
  }
  ```

  

### 4.处理异常

### 5.自定义异常

- 使用java内置的异常类可以描述中编程时出现的大部分异常情况，除此之外，用户还可以自定义异常，用户自定义异常类，只需继承Exception类即可。
- 在程序中使用自定义异常类，大体可分为以下几个步骤：
  1. 创建自定义异常类
  2. 在方法中通过throw关键字抛出异常对象
  3. 如果在当前抛出异常的方法中处理异常，可以使用try-catch语句捕获并处理；否则中方法的声明处通过throws关键字指明要抛出给方法调用者的异常，继续进行下一步操作
  4. 在出现异常方法的调用者中捕获并处理异常



# JAVA集合进阶

### 1.双列集合

双列集合的特点：

1. 双列集合一次需要存一对数据，分别为**键**和**值**
2. 键不能重复，值可以重复
3. 键和值谁一一对应的，每一个键只能找到自己对应的值
4. 键 + 值 这个整体，称之为""键值对"或者""键值对对象"，在java中叫做"Entry对象"

### 2.Map集合常用的API

map是双列集合的顶层接口，功能是全部双列集合都可以继承使用的

![image-20240727153548698](/Users/xiangbaihan/Library/Application Support/typora-user-images/image-20240727153548698.png)

put方法：添加

```java
 Map<String , String> map = new HashMap<>();
				map.put("name" , "张三");
        map.put("id" , "你好");
        map.put("ws" , "网络");

        System.out.println(map);
put方法的细节：
  添加/覆盖
//在添加数据的时候，如果键不存在，那么直接把键值对对象添加到map集合当中，方法返回null
//在添加数据的时候，如果键是存在，会把原有的键值对对象覆盖，会把被覆盖的值进行返回
```

remove方法：删除

```java
map.remove("name");
```

clear方法：清空

```java
map.clear();
```

containsKey方法：是否包含

```java
//判断是否包含
boolean keyResult = m.containsKey("name");
```

### 3.map的遍历方式（键值对）

**键找值**

```java
Map<String , String> map = new HashMap<>();
				map.put("name", "张三");
        map.put("age", "18");
        map.put("sex", "男");
        map.put("asa", "sdx");
        map.put("sads", "男dsa");
        map.put("sedsadax", "男xzcas");
        
        //通过键找值便利
        Set<String> strings = map.keySet();
        //遍历单列集合，得到每一个值
        for (String string : strings) {
            System.out.println(string + ":" + map.get(string));
        }
```

**键值对**：

```java
Map<String , String> map = new HashMap<>();

        map.put("1","张三");
        map.put("2","李四");
        map.put("3","王五");
        map.put("4","赵六");
        map.put("5","田七");

        Set<Map.Entry<String, String>> entries = map.entrySet();

        for (Map.Entry<String, String> entry : entries) {
            System.out.println(entry.getKey() + ":" + entry.getValue());
        }
```

**lambda表达式：**

![image-20240727163828503](/Users/xiangbaihan/Library/Application Support/typora-user-images/image-20240727163828503.png)

```java
Map<String , String> map = new HashMap<>();

        map.put("1","张三");
        map.put("2","李四");
        map.put("3","王五");
        map.put("4","赵六");
        map.put("5","田七");

        map.forEach(new BiConsumer<String, String>() {
            @Override
            public void accept(String key, String value) {
                System.out.println(key + "=" + value);
            }
        });
        System.out.println("============================");
        map.forEach((String key, String value )->{
            System.out.println(key + "=" + value);
            }
        );

        System.out.println("============================");
        //最简单的lambda表达式
        map.forEach((key, value)->System.out.println(key + "=" + value));
```

### 4.hashmap的基本使用

**hashmap的特点**：

1. hashmap是map里面的一个实现类
2. 没有额外需要学习的特有方法，直接使用map里面的方法
3. 特点都是由键决定：无序，不重复，无索引
4. hashmap跟hashset底层原理是一模一样的，都是哈希表结构
5. 依赖hashcode方法和equals方法保证**键的唯一**
6. 如果键存储的是自定义对象，需要重写hashcode和equals方法，如果值存储自定义对象，不需要重写hashcode和equals方法

5.LinkedHashMap

- 由键决定：有序，不重复，无索引
- 这里的有序指的是保证存储和取出的元素顺序一致
- 原理：底层数据依然是哈希表，只是每个键值对元素又额外的多了一个双链表的机制记录存储的顺序

# JAVA注解

### 1.注解

- Annotation是JDK5.0开始引入的新技术
- Annotation的作用:
  - 不是程序本身,可以对程序作出接收(这一点和注释(comment)没什么区别)
  - **可以被其他程序读取**
- Annotation的格式:
  - 注解是以"@注释名"在代码中存在的,还可以添加一些参数值,例如:@SuppressWarnings(value=''unchecked'')
- Annotation在哪里使用:
  - 可以附加在package,class,method,field等上面,相当于给他们添加了额外的辅助信息

### 2.内置注解

- **@Override**：定义在java.lang.Override中，此注释只适用于修饰方法，表示一个方法声明打算重写超类中的另一种方法声明
- **@Deprecated**:定义在java.lang.Deprecated中,此注释可以用于修辞方法,属性,类,表示不鼓励程序员使用这样的元素,通常是因为它很危险或者存在更好的选择
- **@SuppressWarnings**:定义在java.lang.SuppressWarnings中,用来抑制编译时的警告信息

### 3.元注解

- 元注解的作用就是负责注解其他注解,Java定义了4个标准的meta-annotation类型,他们被用来提供对其他annotation类型作说明
- 这些类型和它们所支持的类在java.lang.annotation包中可以找到.(**@Target,@Retention,@Documented,@Inherited**)
  - **@Target**:用于描述注解的使用范围(即:被描述的注解可以用到什么地方)
  - **@Retention**:表示需要在什么级别保存该注解信息,用于描述注解的生命周期
    - (SOURCE<CLASS<**RUNTIME**)
  - **@Document**:说明该注解将被包含在javadoc中
  - **@Inherited**:说明子类可以继承父类中的该注解

### 4.自定义注解

- 使用**@interface**自定义注解时,自动继承了java.lang.annotation.Annotation接口
- 分析:
  - @interface用来声明一个注解,格式:public@interface 注解名{定义内容}
  - 其中的每一个方法实际上是声明了一个配置参数
  - 方法的名称就是参数的名称
  - 返回值类型就是参数的类型(返回值只能是基本类型,class,String,enum)
  - 可以通过default来声明参数的默认值
  - 如果只有一个参数成员,一般参数名为value
  - 注解元素必须要有值,我们定义注解元素时,经常使用空字符串,0作为默认值

# JAVA反射

## 学习

### 静态VS动态语言

**动态语言**:

- 是一类在运行时可以改变其结构的语言:例如新的函数,对象,甚至代码可以被引进,已有的函数可以被删除或是其他结构上的变化.通俗点说就是在运行时代码可以根据某些条件改变自身结构.
- 主要动态语言:Object-C,C#,JavaScript,PHP,Python等

**静态语言:**

- 与动态语言相对应的,运行时结构不可变的语言是静态语言,如java,C,C++
- java不是动态语言,但java可以称之为"准动态语言",即java有一定的动态性,可以利用反射机制获得类似动态语言的特性

### Java Reflection(反射):

- Reflection(反射)是java被视为动态语言的关键,反射机制允许程序在执行期借助于Reflection API取得任何类的内部消息,并能直接操作任何对象的内部属性及方法

  ```java
  Class c = Class.forName("java.lang.String")
  ```

- 加载完类之后,在堆内存的方法区中就产生了一个Class类型的对象(一个类只有一个Class对象),这个对象就包含了完整的类的结构信息.我们可以通过这个对象看到类的结构.这个对象就像一个镜子,透过这个镜子看到类的结构,所以,形象的称之为**反射**

### java反射的优点和缺点:

**优点:**

- 可以实现动态创建对象和编译,体现出很大的灵活性

**缺点:**

- 对性能有影响,使用反射基本上是一种解释操作,我们可以告诉JVM,我们做什么并且它满足我们的要求.这类操作总是慢于 直接执行相同的操作

### Class类:

在Object类中定义了以下的方法,此方法将被所有子类继承

```java
public final Class getClass()
```

以上的方法返回值的类型是一个Class类,此类的java反射的源头,实际上所谓反射从程序的运行结果来看也很好理解,即:可以通过对象反射求出类的名称.

对象照镜子后可以得到的信息:每个类的属性,方法和构造器,某个类到底实现了哪些接口,对于每个类而言,JRE都为其保留一个不变的Class类型的对象.一个Class对象包含了特定的某个结构(class/interface/enum/annotation/primitive type/void [])的有关信息

- Class本身也是一个类
- Class对象只能由系统建立对象
- 一个加载的类在JVM中只会有一个Class实例
- 一个Class对象对应的是一个加载到JVM中的一个.class文件
- 每个类的实例都会记得自己是由那个class实例所生成
- 通过class可以完整地得到一个类中的所有被加载的结构
- class类是Reflection的根源.针对任何你想动态加载,运行的类,唯有先获得相应的class对象

| 方法名                                  | 功能说明                                                |
| --------------------------------------- | ------------------------------------------------------- |
| static ClassforName(String name)        | 返回指定类名name的Class对象                             |
| Object newInstance()                    | 调用缺省构造函数,返回Class对象的一个实例                |
| getName()                               | 返回此Class对象所表示的实体(类,接口,数组类或void)的名称 |
| Class getSuperClass()                   | 返回当前Class对象的父类的Class对象                      |
| Class[] getinterfaces()                 | 获取当前Class对象的接口                                 |
| ClassLoader getClassLoader()            | 返回该类的类加载器                                      |
| Constructor[] getConstructors()         | 返回一个包含某些Constructor对象的数组                   |
| Method getMothed(String name,Class...T) | 返回一个Method对象,此对象的形参类型为paramType          |
| Field[] getDeclaredFields()             | 返回Field对象的一个数组                                 |

### 获取Class类的实例:

1. 获已知具体的类,通过类的class属性获取,该方法最为安全可靠,程序性能最高

   ```java
   Class clazz = Person.class;
   ```

2. 已知某个类的实例,调用该实例的getClass()方法获取Class对象

   ```java
   Class clazz = person.getClass();
   ```

3. 已知一个类的全类名,且该类在类路径下,可通过Class类的静态方法forName()获取,可能抛出ClassNotFoundException

   ```java
   Class clazz = Class.forName("demo01.Student");
   ```

4. 内置基本数据类型可以直接用类名.Type

5. 还可以利用ClassLoader

### 哪些类型可以有Class对象:

- class:外部类,成员(成员内部类,静态内部类),局部内部类,匿名内部类
- interface:接口
- []:数组
- enum:枚举
- annotation:注解@interface
- primitive type:基本数据类型
- void

### java内存分析:

![image-20240622162946055](C:\Users\x\AppData\Roaming\Typora\typora-user-images\image-20240622162946055.png)

**了解:类的加载过程**

当程序主动使用某个类时,如果该类还未被加载到内存中,则系统会通过如下三个步骤来对该类进行初始化

![image-20240622163450884](C:\Users\x\AppData\Roaming\Typora\typora-user-images\image-20240622163450884.png)

**类的加载与ClassLoader的理解:**

- **加载**:将class文件字节码内容加载到内存中,并将这些静态数据转换成方法区的运行时数据结构,然后生成一个代表这个类的java.lang.Class对象
- **链接**:将java类的二进制代码合并到JVM的运行状态之中的过程
  - **验证**:确保加载的类信息符合JVM规范,没有安全方面的问题
  - 准备:正式为类变量(static)分配内存并设置类变量默认初始化的阶段,这些内存都将在方法区中进行分配
  - **解析**:虚拟机常量池内的符号引用(常量名)替换为直接引用(地址)的过程
- **初始化**:
  - 执行类构造器<clinit>()方法的过程.类构造器<clinit>()方法是由编译期自动收集类中所有类变量的赋值动作和静态代码块中的语句合并产生(类构造器是构造类信息的,不是构造该类对象的构造器)
  - 当初始化一个类的时候,如果发现其父类还没有进行初始化,则需要先触发其父类的初始化
  - 虚拟机会保证一个类的<clinit>()方法在多线程环境中被正确加锁和同步

**说明时候会发生类初始化:**

- 类的主动引用(一定会发生类的初始化)
  - 当虚拟机启动,先初始化main方法所在的类
  - new 一个类的对象
  - 调用类的静态成员(除了final常量)和静态方法
  - 使用java.lang.reflect包的方法对类进行反射调用
  - 当初始化一个类,如果其父类没有被初始化,则先会初始化它的父类
- 类的被动引用(不会发生类的初始化):
  - 当访问一个静态域时,只有真正声明这个域的类才会被初始化.如:通过子类引用父类的静态变量,不会导致子类初始化
  - 通过数组定义类引用,不会触发此类的初始化
  - 引用常量不会触发此类的初始化(常量在链接阶段就存入调用类的常量池中)

**类加载器的作用:**

- 类加载的作用:将class文件字节码内容加载到内存中,并将这些静态数据转换成方法区的运行时数据结构,然后在堆中生成一个代表这个类的java.lang.Class对象,作为方法区中类数据的访问入口
- 类缓存:标准的javaSE类加载器可以按要求查找类,但一旦某个类被加载到类加载器中,它将维持加载(缓存)一段时间.不过JVM垃圾回收机制可以回收这些Class对象

类加载器作用是用来把类(class)转载进内存的,JVM规范定义了如下类型的类的加载器:

## 反射再学习：

### 1.反射基础：

反射允许对成员变量，成员方法和构造方法的信息进行编程访问

### 2.获取class对象的三种方式

1. ```java
   Class.forName("全类名")
   ```

2. ```java
   类名.class
   ```

3. ```java
   对象.getClass();
   ```

### 3.利用反射获取构造方法

**Class类中用于获取构造方法的方法：**

Constructor<?>[ ] getConstructors():返回所有公共构造方法对象的数组

Constructor<?>[ ] getDeclaredConstructors():返回所有构造方法对象的数组

Constructor<T>[ ] getConstructors(Class<?> ... parameterTypes):返回单个公共构造方法对象

Constructor<T>[ ] getDeclaredConstructors(Class<?> ... parameterTypes):返回单个构造方法对象



**Constructor类中用于创建对象的方法：**

T newlnstance(Object ... initargs):根据指定的构造方法创建对象

setAccessible(boolean flag):设置为true,表示取消访问检查



### 4.利用反射获取成员变量

**Class类中用于获取成员变量的方法：**

Field[ ] getFields():返回所有公共成员变量对象的数组

Field[ ] getDeclaredFields():返回所有成员变量对象的数组

Field[ ] getFields(String name):返回单个公共成员变量对象

Field[ ] getDeclaredFields(String name):返回单个成员变量对象



**Field类中用于创建对象的方法：**

void set(Object obj,Object value):赋值

Object get(Object obj)：获取值



# JAVA拓展

## 1.JWT：加密

- 全称：JSON Web Token
- 定义人一种简洁的，自包含的格式用于通信双方以json数据格式安全的传输信息
- 组成
  - 第一部分：Header(头) ，记录令牌类型，签名算法等
  - 第二部分：Payload（有效载荷），携带一些自定义信息，默认信息等
  - 第三部分：Signature（签名），防止Token被篡改，确保安全性，将header，payload，并加入指定密钥，通过指定算法计算而来
  - ![image-20240728185753199](/Users/xiangbaihan/Library/Application Support/typora-user-images/image-20240728185753199.png)

```java
//生成jwt		
		@Test
    public void contextLoads() {
        Map<String, Object> claims = new HashMap<>();
        claims.put("id",1);
        claims.put("username","张三");
        //生成jwt的代码
        String thken = JWT.create()
                .withClaim("user",claims)  //添加载荷
                .withExpiresAt(new Date(System.currentTimeMillis()+1000*60*60*12)) //添加过期时间
                .sign(Algorithm.HMAC256("heiha"));//指定算法，配置密钥

        System.out.println(thken);
    }
//验证jwt
 		@Test
    public void testParse(){
        //定义字符串，模拟用户传递过来的token
        String token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" +
                ".eyJ1c2VyIjp7ImlkIjoxLCJ1c2VybmFtZSI6IuW8oOS4iSJ9LCJleHAiOjE3MjIyMDkzMTR9" +
                "._5yJMjqhxd2eGR046HmMbjsmzuAXothW73h141Sn1xE";
        JWTVerifier jwtVerifier = JWT.require(Algorithm.HMAC256("heima")).build();
        DecodedJWT decodedJWT = jwtVerifier.verify(token);  //验证token，生成一个解析后的jwt对象
        Map<String, Claim> claims = decodedJWT.getClaims();
        System.out.println(claims.get("user"));
    }
```

注意事项：

- jwt校验时使用的签名密钥，必须和生成jwt令牌时使用的密钥是配套的
- 如果jwt令牌解析校验时报错，则说明jwt令牌被篡改 或 失效了，令牌非法



# JAVA多线程详解

## 1.线程，进程，多线程

- 线程就是独立的执行路径
- 在程序运行时，即使没有自己创建线程，后台也会有多个线程
- main（）称之为主线程，为系统的入口，用于执行整个程序
- 在一个进程中，如果开辟了多个线程，线程的运行由调度器安排调度，调度器是与操作系统密切相关的，先后顺序是不能认为的干涉的
- 对同一份资源操作时，会存在资源抢夺的问题，想要加入并发控制
- 线程会带来额外的开销，如cpu调度时间，并发控制开销
- 每个线程在自己的工作内存交互，内存控制不当会造成数据不一致