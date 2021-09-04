-- Exam 3.1
select e.name, COUNT(eh.employee_id) as e_count from employee e
join employee_hobby eh on e.employee_id = eh.employee_id
where e_count > 1

-- Exam 3.2
select e.name, COUNT(eh.employee_id) as e_manhour from employee e
join employee_work ew on e.employee_id = ew.employee_id
where e_manhour >= 350

-- Exam 3.3
select eh.name, COUNT(eh.employee_id) as e_manhour from employee e
join employee_hobby eh on e.employee_id = eh.employee_id
join employee_work ew on e.employee_id = ew.employee_id
where ew.perf > 70

-- Exam 3.4
select e.name, e.lastname from employee e
join employee_work ew on e.employee_id = ew.employee_id
where ew.perf > 80 and e.age > 25