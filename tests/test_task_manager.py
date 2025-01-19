import pytest
from app.task_manager import TaskManager

@pytest.fixture
def task_manager():
    return TaskManager()

def test_add_task_and_set_priority(task_manager):
    checking_name_and_priority = TaskManager()
    checking_name_and_priority.add_task('TASK1','normal')
    checking_name_and_priority.add_task('task2', 'low')
    checking_name_and_priority.add_task('Task3','high' )
    print(checking_name_and_priority.tasks)

    checking_list_tasks = checking_name_and_priority.list_tasks()
    print(checking_list_tasks)

def test_raising_error_for_invalid_priority(task_manager):
    checking_raising_error = TaskManager()
    try:
        checking_raising_error.add_task('Task with invalid priority', '1234')
    except ValueError as error:
        print(error)

def test_status_is_completed(task_manager):
    checking_completed_status = TaskManager()
    checking_completed_status.add_task('Task4', 'low')
    updated_task = checking_completed_status.mark_task_completed('Task4')
    assert updated_task['completed'] is True
    print(f'Completed status is set to', updated_task['completed'])

    checking_incomplete_status = TaskManager()
    try:
        checking_incomplete_status.mark_task_completed('Task4')
    except ValueError as error1:
        print(error1)

def test_task_removal(task_manager):
    checking_task_removal = TaskManager()
    checking_task_removal.add_task('Task5', 'low')
    removed_task = checking_task_removal.remove_task('Task5')
    print(f'Completed status is set to', removed_task['completed'])

    checking_task_removal_error = TaskManager()
    try:
        checking_task_removal_error.remove_task('Task5')
    except ValueError as error2:
        print(error2)