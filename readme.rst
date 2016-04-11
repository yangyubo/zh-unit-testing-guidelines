单元测试准则
===================

:原文版本: 4.1, April 2010
:原文作者: Geotechnical Software Services
:原文链接: http://geosoft.no/development/unittesting.html

:首次翻译: 2009 年 6 月
:再版翻译: 2015 年 10 月

译者 ( `Yang.Y <http://yangyubo.com>`_ ) 前言:
  .. line-block::

:项目主页:
    - `Geotechnical Unit Testing Guidelines <http://geosoft.no/development/unittesting.html>`_
    - `Geotechnical 单元测试指南 - 中文版 <https://github.com/yangyubo/zh-unit-testing-guidelines>`_

    实施单元测试的时候, 如果没有一份经过实践证明的详细规范, 很难掌握测试的 "度", 范围太小施展不开, 太大又侵犯 "别人的" 地盘. 上帝的归上帝, 凯撒的归凯撒, 给单元测试念念紧箍咒不见得是件坏事, 反而更有利于发挥单元测试的威力, 为代码重构和提高代码质量提供动力.

    这份文档来自 Geotechnical, 是一份非常难得的经验准则. 你完全可以以这份准则作为模板, 结合所在团队的经验, 整理出一份内部单元测试准则.

    译文由强大的 reStructuredText_ 文本标记语法驱动.

.. contents:: 测试准则
   :backlinks: none
   :local:

1. 保持单元测试小巧, 快速
-----------------------------

理论上, 任何代码提交前都应该完整跑一遍所有测试套件. 保持测试代码执行迅捷能够缩短迭代开发周期.

2. 单元测试应该是全自动且无交互
------------------------------------

测试套件通常是定期执行的, 执行过程必须完全自动化才有意义. 需要人工检查输出结果的测试不是一个好的单元测试.

3. 让单元测试很容易跑起来
----------------------------

对开发环境进行配置, 最好是敲条命令或是点个按钮就能把单个测试用例或测试套件跑起来.

4. 对测试进行评估
-----------------------

对执行的测试进行覆盖率分析, 得到精确的代码执行覆盖率, 并调查哪些代码未被执行.

5. 立即修正失败的测试
------------------------

每个开发人员在提交前都应该保证新的测试用例执行成功, 当有代码提交时, 现有测试用例也都能跑通.

如果一个定期执行的测试用例执行失败, 整个团队应该放下手上的工作优先解决这个问题.

6. 把测试维持在单元级别
-------------------------

单元测试即类 (Class) 的测试. 一个 "测试类" 应该只对应于一个 "被测类", 并且 "被测类" 的行为应该被隔离测试. 必须谨慎避免使用单元测试框架来测试整个程序的工作流, 这样的测试既低效又难维护. 工作流测试 (译注: 指跨模块/类的数据流测试) 有它自己的地盘, 但它绝不是单元测试, 必须单独建立和执行.

7. 由简入繁
---------------

最简单的测试也远远胜过完全没有测试. 一个简单的 "测试类" 会促使建立 "被测类" 基本的测试骨架, 可以对构建环境, 单元测试环境, 执行环境以及覆盖率分析工具等有效性进行检查, 同时也可以证明 "被测类" 能够被整合和调用.

下面便是单元测试版的 *Hello, world!* :

::

    void testDefaultConstruction()
    {
    Foo foo = new Foo();
    assertNotNull(foo);
    }


8. 保持测试的独立性
-------------------------

为了保证测试稳定可靠且便于维护, 测试用例之间决不能有相互依赖, 也不能依赖执行的先后次序.

9. Keep tests close to the class being tested
------------------------------------------------

[译注: 有意翻译该规则, 个人认为本条规则值得商榷, 大部分 C++, Objective-C和 Python 库均把测试代码从功能代码目录中独立出来, 通常是创建一个和 ``src`` 目录同级的 ``tests`` 目录, 被测模块/类名之前也常常 *不加* ``Test`` 前缀. 这么做保证功能代码和测试代码隔离, 目录结构清晰, 并且发布源码的时候更容易排除测试用例.]

If the class to test is Foo the test class should be called FooTest (not TestFoo) and kept in the same package (directory) as Foo. Keeping test classes in separate directory trees makes them harder to access and maintain.

Make sure the build environment is configured so that the test classes doesn't make its way into production libraries or executables.

10. 合理的命名测试用例
-------------------------

确保每个方法只测试 "被测类" 的一个明确特性, 并相应的命名测试方法. 典型的命名俗定是 ``test[what]``, 比如 ``testSaveAs()``, ``testAddListener()``, ``testDeleteProperty()`` 等.

11. 只测公有接口
--------------------

单元测试可以被定义为 *通过类的公有 API 对类进行测试*. 一些测试工具允许测试一个类的私有成员, 但这种做法应该避免, 它让测试变得繁琐而且更难维护. 如果有私有成员确实需要进行直接测试, 可以考虑把它重构到工具类的公有方法中. 但要注意这么做是为了改善设计, 而不是帮助测试.

12. 看成是黑盒
------------------

站在第三方使用者的角度, 测试一个类是否满足规定的需求. 并设法让它出问题.

13. 看成是白盒
-----------------

毕竟被测试类是程序员自写自测的, 应该在最复杂的逻辑部分多花些精力测试.

14. 芝麻函数也要测试
------------------------

通常建议所有重要的函数都应该被测试到, 一些芝麻方法比如简单的 ``setter`` 和 ``getter`` 都可以忽略. 但是仍然有充分的理由支持测试芝麻函数:

- *芝麻* 很难定义. 对于不同的人有不同的理解.
- 从黑盒测试的观点看, 是无法知道哪些代码是芝麻级别的.
- 即便是再芝麻的函数, 也可能包含错误, 通常是 "复制粘贴" 代码的后果:

  ::

     private double weight_;
     private double x_, y_;

     public void setWeight(int weight)
     {
       weight = weight_;  // error
     }

     public double getX()
     {
       return x_;
     }

     public double getY()
     {
       return x_;  // error
     }

因此建议测试所有方法. 毕竟芝麻用例也容易测试.

15. 先关注执行覆盖率
-------------------------

区别对待 *执行覆盖率* 和 *实际测试覆盖率*. 测试的最初目标应该是确保较高的执行覆盖率. 这样能保证代码在 *少量* 参数值输入时能执行成功. 一旦执行覆盖率就绪, 就应该开始改进测试覆盖率了. 注意, 实际的测试覆盖率很难衡量 (而且往往趋近于 0%).

思考以下公有方法:

::

  void setLength(double length);

调用 ``setLength(1.0)`` 你可能会得到 100% 的执行覆盖率. 但要达到 100% 的实际测试覆盖率, 有多少个 ``double`` 浮点数这个方法就必须被调用多少次, 并且要一一验证行为的正确性. 这无疑是不可能的任务.

16. 覆盖边界值
----------------

确保参数边界值均被覆盖. 对于数字, 测试负数, 0, 正数, 最小值, 最大值, NaN (非数字), 无穷大等. 对于字符串, 测试空字符串, 单字符, 非 ASCII 字符串, 多字节字符串等. 对于集合类型, 测试空, 1, 第一个, 最后一个等. 对于日期, 测试 1月1号, 2月29号, 12月31号等. 被测试的类本身也会暗示一些特定情况下的边界值. 要点是尽可能彻底的测试这些边界值, 因为它们都是主要 "疑犯".

17. 提供一个随机值生成器
--------------------------

当边界值都覆盖了, 另一个能进一步改善测试覆盖率的简单方法就是生成随机参数, 这样每次执行测试都会有不同的输入.

想要做到这点, 需要提供一个用来生成基本类型 (如: 浮点数, 整型, 字符串, 日期等) 随机值的工具类. 生成器应该覆盖各种类型的所有取值范围.

如果测试时间比较短, 可以考虑再裹上一层循环, 覆盖尽可能多的输入组合. 下面的例子是验证两次转换 little endian 和 big endian 字节序后是否返回原值. 由于测试过程很快, 可以让它跑上个一百万次.

::

    void testByteSwapper()
    {
      for (int i = 0; i < 1000000; i++) {
        double v0 = Random.getDouble();
        double v1 = ByteSwapper.swap(v0);
        double v2 = ByteSwapper.swap(v1);
        assertEquals(v0, v2);
      }
    }

18. 每个特性只测一次
-----------------------

在测试模式下, 有时会情不自禁的滥用断言. 这种做法会导致维护更困难, 需要极力避免. 仅对测试方法名指示的特性进行明确测试.

因为对于一般性代码而言, 保证测试代码尽可能少是一个重要目标.

19. 使用显式断言
-------------------

应该总是优先使用 ``assertEquals(a, b)``  而不是 ``assertTrue(a == b)``, 因为前者会给出更有意义的测试失败信息. 在事先不确定输入值的情况下, 这条规则尤为重要,  比如之前使用随机参数值组合的例子.

20. 提供反向测试
---------------------

反向测试是指刻意编写问题代码, 来验证鲁棒性和能否正确的处理错误.

假设如下方法的参数如果传进去的是负数, 会立马抛出异常:

::

  void setLength(double length) throws IllegalArgumentExcepti

可以用下面的方法来测试这个特例是否被正确处理:

::

    try {
      setLength(-1.0);
      fail();  // If we get here, something went wrong
    }
    catch (IllegalArgumentException exception) {
      // If we get here, all is fine
    }


21. 代码设计时谨记测试
--------------------------

编写和维护单元测试的代价是很高的, 减少代码中的公有接口和循环复杂度是降低成本, 使高覆盖率测试代码更易于编写和维护的有效方法.

一些建议:

 - 使类成员常量化, 在构造函数中进行初始化. 减少 ``setter`` 方法的数量.

 - 限制过度使用继承和公有虚函数.

 - 通过使用友元类 (C++) 或包作用域 (Java) 来减少公有接口.

 - 避免不必要的逻辑分支.

 - 在逻辑分支中编写尽可能少的代码.

 - 在公有和私有接口中尽量多用异常和断言验证参数参数的有效性.

 - 限制使用快捷函数. 对于黑箱而言, 所有方法都必须一视同仁的进行测试. 思考以下简短的例子:
   ::

        public void scale(double x0, double y0, double scaleFactor)
        {
          // scaling logic
        }

        public void scale(double x0, double y0)
        {
          scale(x0, y0, 1.0);
        }

   删除后者可以简化测试, 但用户代码的工作量也将略微增加.


22. 不要访问预设的外部资源
------------------------------

单元测试代码不应该假定外部的执行环境, 以便在任何时候/任何地方都能执行. 为了向测试提供必需的资源, 这些资源应该由测试本身提供.

比如一个解析某类型文件的类, 可以把文件内容嵌入到测试代码里, 在测试的时候写入到临时文件, 测试结束再删除, 而不是从预定的地址直接读取.

23. 权衡测试成本
-------------------

不写单元测试的代价很高, 但是写单元测试的代价同样很高. 要在这两者之间做适当的权衡, 如果用执行覆盖率来衡量, 业界标准通常在 80% 左右.

很典型的, 读写外部资源的错误处理和异常处理就很难达到百分百的执行覆盖率. 模拟数据库在事务处理到一半时发生故障并不是办不到, 但相对于进行大范围的代码审查, 代价可能太大了.

24. 安排测试优先次序
------------------------

单元测试是典型的自底向上过程, 如果没有足够的资源测试一个系统的所有模块, 就应该先把重点放在较底层的模块.

25. 测试代码要考虑错误处理
------------------------------

考虑下面的这个例子:

::

    Handle handle = manager.getHandle();
    assertNotNull(handle);

    String handleName = handle.getName();
    assertEquals(handleName, "handle-01");

如果第一个断言失败, 后续语句会导致代码崩溃, 剩下的测试都无法执行. 任何时候都要为测试失败做好准备, 避免单个失败的测试项中断整个测试套件的执行. 上面的例子可以重写成:

::

    Handle handle = manager.getHandle();
    assertNotNull(handle);
    if (handle == null) return;

    String handleName = handle.getName();
    assertEquals(handleName, "handle-01");

26. 写测试用例重现 bug
-------------------------

每上报一个 bug, 都要写一个测试用例来重现这个 bug (即无法通过测试), 并用它作为成功修正代码的检验标准.

27. 了解局限
---------------

*单元测试永远无法证明代码的正确性!!*

一个跑失败的测试可能表明代码有错误, 但一个跑成功的测试什么也证明不了.

单元测试最有效的使用场合是在一个较低的层级验证并文档化需求, 以及 *回归测试*: 开发或重构代码时，不会破坏已有功能的正确性.

参考资料
====================

[1] 维基百科关于单元测试的定义: `Unit Testing <http://en.wikipedia.org/wiki/Unit_testing>`_

[2] 白盒和黑盒测试的简短描述: `What is black box/white box testing? <http://www.faqs.org/faqs/software-eng/testing-faq/section-13.html>`_

[3] 我们最常用的 C++ 单元测试框架: `CxxTest <http://cxxtest.tigris.org/>`_

[4] 我们最常用的 Java 单元测试框架: `TestNG <http://testng.org/>`_

[5] 我们最常用的 C++ 覆盖率分析工具: `LCOV <http://ltp.sourceforge.net/coverage/lcov.php>`_

[5] 我们最常用的 Java 覆盖率分析工具: `Cobertura <http://cobertura.sourceforge.net/>`_

[5] 更多关于不允许访问外部资源观点: `A Set of Unit Testing Rules <http://www.artima.com/weblogs/viewpost.jsp?thread=126923>`_

[6] 来自 Apple 的单元测试建议: `Unit Test Guidelines <http://developer.apple.com/documentation/DeveloperTools/Conceptual/UnitTesting/Articles/UTGuidelines.html>`_

[7] JUnit 最佳实践: `JUnit best practices <http://www.javaworld.com/javaworld/jw-12-2000/jw-1221-junit_p.html>`_

译者推荐中文资料
====================

#. `来自Google的单元测试技巧 <http://www.infoq.com/cn/news/2007/04/google-testing-tips>`_

#. `浅谈测试驱动开发 (TDD) <http://www.ibm.com/developerworks/cn/linux/l-tdd/>`_

#. `TDD/BDD会导致不完整的单元测试吗? <http://www.infoq.com/cn/news/2008/02/unit_tests_forests_n_trees>`_

#. `Mock 不是测试的银弹 <http://www.infoq.com/cn/articles/thoughtworks-practice-partvi>`_

#. `不要把 Mock 当作你的设计利器 <http://news.csdn.net/n/20060726/93003.html>`_

#. `TDD 推荐教程 <http://www.infoq.com/cn/news/2009/05/recommended-tdd-tutorials>`_

#. `单元测试的七种境界 <http://www.yeeyan.com/articles/view/zhaorui/39868>`_

#. `关于 <<单元测试的七种境界>> 的自我总结 <http://hi.baidu.com/dearhwj/blog/item/b4b636361222c1390b55a956.html>`_

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
