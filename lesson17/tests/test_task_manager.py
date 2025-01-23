import pytest
from lesson17.app.task_manager import TaskManager
import allure

@pytest.fixture
def task_manager():
    return TaskManager()

@allure.feature("Task Management")
@allure.story("Add Tasks")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_task_and_set_priority(task_manager):
    with allure.step("Create new Tasks"):
        add_task_and_set_priority = TaskManager()

    with allure.step("Add tasks with varying priorities"):
        add_task_and_set_priority.add_task('TASK1', 'normal')
        add_task_and_set_priority.add_task('task2', 'low')
        add_task_and_set_priority.add_task('Task3', 'high')

    with allure.step("Verify the number of tasks added"):
        assert len(add_task_and_set_priority.tasks) == 3

@allure.feature("Task Management")
@allure.story("Invalid Priority")
@allure.severity(allure.severity_level.CRITICAL)
def test_raising_error_for_invalid_priority(task_manager):
    with allure.step("Create a task with invalid priority"):
        raising_error_for_invalid_priority = TaskManager()

    with allure.step("Raising an error for invalid priority"):
        with pytest.raises(ValueError, match="Приоритет должен быть 'low', 'normal' или 'high'"):
            raising_error_for_invalid_priority.add_task('Invalid Task', '12234')


@allure.feature("Task Management")
@allure.story("Checking that task is completed")
@allure.severity(allure.severity_level.CRITICAL)
def test_mark_task_completed(task_manager):
    with allure.step("Check for completed task"):
        task_completed = TaskManager()

    with allure.step("Add a new task"):
        task_completed.add_task('Task4', 'low')
    with allure.step("Mark task completed"):
        updated_task = task_completed.mark_task_completed('Task4')
    with allure.step("Check the task is really completed"):
        assert updated_task['completed'] is True
    with allure.step("Check task #4 is completed"):
        assert updated_task['name'] == 'Task4'

@allure.feature("Task Management")
@allure.story("Checking raising error for incomplete task")
@allure.severity(allure.severity_level.NORMAL)
def test_mark_task_completed_raises_error(task_manager):
    with allure.step("Error check"):
        error_for_incomplete_task = TaskManager()
    with allure.step("Check for error message"):
        with pytest.raises(ValueError, match="Задача с таким названием не найдена"):
            error_for_incomplete_task.mark_task_completed('NonExistentTask')

@allure.feature("Task Management")
@allure.story("Checking that task is removed")
@allure.severity(allure.severity_level.CRITICAL)
def test_remove_task(task_manager):
    with allure.step("Error check"):
        deleted_task = TaskManager()
    with allure.step("Add a new task"):
        deleted_task.add_task('Task5', 'low')
    with allure.step("Remove added task"):
        removed_task = deleted_task.remove_task('Task5')
    with allure.step("Check that task# 5 is removed"):
        assert removed_task['name'] == 'Task5'

@allure.feature("Task Management")
@allure.story("Checking error for removed task")
@allure.severity(allure.severity_level.NORMAL)
def test_remove_task_raises_error(task_manager):
    with allure.step("Check an error"):
        error_for_removed_task = TaskManager()
    with allure.step("Error appears when calling for removed task"):
        with pytest.raises(ValueError, match="Задача с таким названием не найдена"):
            error_for_removed_task.remove_task('NonExistentTask')
