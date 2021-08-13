/*
1. 查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数。
列：d.deptno, d.dname, d.loc, 部门人数
表：dept d, emp e
条件：e.deptno=d.deptno
*/


SELECT t_dept.*,COUNT(*) 
FROM t_employees,t_dept 
WHERE t_employees.`deptno` = t_dept.`deptno`
GROUP BY deptno



/*
3. 列出所有员工的姓名及其直接上级的姓名。
列：员工姓名、上级姓名
表：emp e, emp m
条件：员工的mgr = 上级的empno*/


SELECT t1.ename, t2.ename 
FROM t_employees t1 LEFT JOIN t_employees t2 
ON t1.MGR = t2.empno 




/*
4. 列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称。
列：e.empno, e.ename, d.dname
表：emp e, emp m, dept d
条件：e.hiredate<m.hiredate
思路：
1. 先不查部门名称，只查部门编号!
列：e.empno, e.ename, e.deptno
表：emp e, emp m
条件：e.mgr=m.empno, e.hiredate<m.hireadate
*/


SELECT t1.`ename`,t1.`empno`,t3.`dname`
FROM t_employees t1, t_employees t2, t_dept t3
WHERE t1.MGR = t2.empno AND t1.hiredate < t2.hiredate  AND t1.`deptno` = t3.`deptno`


/*
5. 列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。
列：* 
表：emp e, dept d
条件：e.deptno=d.deptno
*/

SELECT * 
FROM  t_employees RIGHT OUTER JOIN t_dept 
ON t_employees.`deptno` = t_dept.`deptno`



/*
7. 列出最低薪金大于15000的各种工作及从事此工作的员工人数。
列：job, count(*)
表：emp e
条件：min(sal) > 15000
分组：job
*/

SELECT job, COUNT(*)
FROM t_employees
WHERE sal > 15000
GROUP BY job


/*
8. 列出在销售部工作的员工的姓名，假定不知道销售部的部门编号。
列：e.ename
表：emp
条件：e.deptno=(select deptno from dept where dname='销售部')
*/


SELECT *
FROM t_employees
WHERE t_employees.`deptno` = (SELECT deptno FROM t_dept WHERE dname = "sales")




/*
9. 列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，工资等级。
列：* 
表：emp e
条件：sal>(查询出公司的平均工资)
*/


-- 列出薪金高于公司平均薪金的所有员工信息，所在部门名称  -- 上级领导，工资等级=不会
SELECT t_employees.*,t_dept.`dname`
FROM t_employees,t_dept
WHERE sal > ALL(SELECT AVG(sal) FROM t_employees) AND t_employees.`deptno` = t_dept.`deptno`




/*
10.列出与clack从事相同工作的所有员工及部门名称。
列：e.*, d.dname
表：emp e, dept d
条件：job=(查询出庞统的工作)
*/

-- 没有庞统，用了张飞

SELECT t_employees.`ename`,t_dept.`deptno`
FROM t_employees,t_dept
WHERE t_employees.`deptno` = t_dept.`deptno` AND job = (SELECT job FROM t_employees WHERE ename = "张飞")



/*
11.列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称。
列：e.ename, e.sal, d.dname
表：emp e, dept d
条件；sal>all (30部门薪金)
*/


SELECT t_employees.`ename`,t_employees.`sal`,t_dept.`dname`
FROM t_employees,t_dept
WHERE t_employees.`deptno` = t_dept.`deptno` AND sal > ALL (SELECT sal FROM t_employees WHERE deptno = 30)

