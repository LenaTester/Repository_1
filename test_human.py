import pytest
import logging

logger = logging.getLogger()
logger.setLevel('INFO')

from code_for_testing import Human

@pytest.mark.group_1
def test_01_young_human(set_human):
    ''' description
    Pre-conditions:
    1. create young human
    Steps to reproduce:
    1. create 29 years old human
    2. check, that he was added 1 year
    Expected result: age is increased for 1 year'''
    set_human.grow()
    assert set_human.age == 30, f'\nAge is not as expected\nActual: {set_human.age}\nExpected: 30'

@pytest.mark.group_1
def test_02_dead_human(set_human):
    ''' description
    Pre-conditions:
    1. create dead human
    Steps to reproduce:
    1. create 105 years old human
    2. check, that his status is 'dead'
    Expected result: human status is dead'''
    for i in range(77):
        set_human.grow()
    assert set_human.status == 'dead'
    assert set_human.age == 105, f'\nAge is not as expected\nActual: {set_human.age}\nExpected: 105'


@pytest.mark.group_2
def test_03_new_normal_name(set_human):
    ''' description
    Pre-conditions:
    1. set new name for human - name starts from capital and contains more, than 10 letters
    Steps to reproduce:
    1. create new name, which starts from capital and contains more, than 10 letters
    Expected result: name is changed'''
    set_human.change_name('Mike-Michael')
    assert set_human.name == 'Mike-Michael', f'\nName is not as expected\nActual: {set_human.name}\nExpected:' \
                                                  f' The name should start from capital and be more than 10 letters'

@pytest.mark.group_2
def test_04_new_half_normal_name(set_human):
    ''' description
    Pre-conditions:
    1. set new name for human - name starts from non-capital and contains more, than 10 letters
    Steps to reproduce:
    1. create new name, which starts from non-capital and contains more, than 10 letters
    Expected result: name is changed'''
    set_human.change_name('mike-michael')
    assert set_human.name == 'mike-michael', f'\nName is not as expected\nActual: {set_human.name}\nExpected:' \
                                                  f' The name should start from capital and be more than 10 letters'

@pytest.mark.group_2
def test_05_new_half_normal_name_2(set_human):
    ''' description
    Pre-conditions:
    1. set new name for human - name starts from capital and contains less, than 10 letters
    Steps to reproduce:
    1. create new name, which starts from capital and contains less, than 10 letters
    Expected result: name is changed'''
    set_human.change_name('Mike')
    assert set_human.name == 'Mike', f'\nName is not as expected\nActual: {set_human.name}\nExpected:' \
                                                      f' The name should start from capital and be more than 10 letters'

@pytest.mark.group_2
def test_06_new_wrong_name(set_human):
    ''' description
    Pre-conditions:
    1. set new name for human - name starts from non-capital and contains less, than 10 letters
    Steps to reproduce:
    1. create new name, which starts from non-capital and contains less, than 10 letters
    Expected result: name is not changed, Exception is raised'''
    with pytest.raises(Exception):
        set_human.change_name('mike')

def test_07_non_string_name(set_human):
    ''' description
    Pre-conditions:
    1. set new name for human - name is not string
    Steps to reproduce:
    1. create new name, which is not string
    Expected result: name is not changed, TypeError is raised'''
    with pytest.raises(TypeError):
        set_human.change_name(9)

@pytest.mark.group_3
def test_08_new_normal_gender(set_human):
    ''' description
    Pre-conditions:
    1. set new gender for human - 'female'
    Steps to reproduce:
    1. create new gender for human - 'female'
    Expected result: gender is changed'''
    set_human.gender = 'female'
    assert set_human.gender == 'female', f'\nGender is not as expected\nActual: {set_human.gender}\nExpected:' \
                                                f' Gender should be female'
@pytest.mark.group_3
def test_09_new_wrong_gender(set_human):
    ''' description
    Pre-conditions:
    1. set new non-existing gender for human
    Steps to reproduce:
    1. create new gender for human - 'some non-existing gender'
    Expected result: Exception is raised'''
    with pytest.raises(Exception):
        set_human.gender = 'some non-existing gender'

@pytest.mark.group_4
def test_10_living_friend_added(set_human, set_living_friend):
    ''' description
    Pre-conditions:
    1. friend is alive
    Steps to reproduce:
    1. create living friend
    2. try to add friend to the friends list
    Expected result: friend is added, friends list contains 1 record'''
    set_human.make_friends(set_living_friend)
    assert len(set_human.friends) == 1, f'\nFriend has not been added\nActual: {set_human.friends[0].name}' \
                                        f'\nExpected: One friend is added'

@pytest.mark.group_4
def test_11_dead_friend_not_added(set_human, set_dead_friend):
    ''' description
    Pre-conditions:
    1. friend is dead
    Steps to reproduce:
    1. create friend
    2. make friend dead
    3. try to add friend to the friends list
    Expected result: friend is not added, friends list is empty'''
    set_human.make_friends(set_dead_friend)
    assert len(set_human.friends) == 0, f'\nFriend has been added\nActual: One friend has been added' \
                                            f'\nExpected: No friends are added'

@pytest.mark.parametrize('age', [29, 31, 33])
def test_12_young_human(age):
    '''description
    Pre-conditions:
    1. create 3 young humans of different age
    Steps to reproduce:
    1. create 29, 31, 33 years old human, using parametrize
    2. check, that he was added 1 year
    Expected result: age is increased for 1 year'''
    logger.info(f'\nTEST START: {age}')
    new_human = Human('Alessandro', age, 'male')
    new_human.grow()
    if age == 29:
        assert new_human.age == 30, f'\nAge is not as expected\nActual: {new_human.age}\nExpected: 30'
    if age == 31:
        assert new_human.age == 32, f'\nAge is not as expected\nActual: {new_human.age}\nExpected: 32'
    if age == 33:
        assert new_human.age == 34, f'\nAge is not as expected\nActual: {new_human.age}\nExpected: 34'