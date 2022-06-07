import pytest
import logging

from code_for_testing import Human

logger = logging.getLogger()
logger.setLevel('INFO')

@pytest.mark.group_1
def test_01_young_human(self):
    ''' description
    Pre-conditions:
    1. create young human
    Steps to reproduce:
    1. create 29 years old human
    2. check, that he was added 1 year
    Expected result: age is increased for 1 year'''
    self.human.grow()
    assert self.human.age == 30, f'\nAge is not as expected\nActual: {self.human.age}\nExpected: 30'

@pytest.mark.group_1
def test_02_dead_human(self):
    ''' description
    Pre-conditions:
    1. create dead human
    Steps to reproduce:
    1. create 105 years old human
    2. check, that his status is 'dead'
    Expected result: human status is dead'''
    for i in range(77):
        self.human.grow()
    assert self.human.status == 'dead'
    assert self.human.age == 105, f'\nAge is not as expected\nActual: {self.human.age}\nExpected: 105'


@pytest.mark.group_2
def test_03_new_normal_name(self):
    ''' description
    Pre-conditions:
    1. set new name for human - name starts from capital and contains more, than 10 letters
    Steps to reproduce:
    1. create new name, which starts from capital and contains more, than 10 letters
    Expected result: name is changed'''
    self.human.change_name('Mike-Michael')
    assert self.human.name == 'Mike-Michael', f'\nName is not as expected\nActual: {self.human.name}\nExpected:' \
                                                  f' The name should start from capital and be more than 10 letters'

@pytest.mark.group_2
def test_04_new_half_normal_name(self):
    ''' description
    Pre-conditions:
    1. set new name for human - name starts from non-capital and contains more, than 10 letters
    Steps to reproduce:
    1. create new name, which starts from non-capital and contains more, than 10 letters
    Expected result: name is changed'''
    self.human.change_name('mike-michael')
    assert self.human.name == 'mike-michael', f'\nName is not as expected\nActual: {self.human.name}\nExpected:' \
                                                  f' The name should start from capital and be more than 10 letters'

@pytest.mark.group_2
def test_05_new_half_normal_name_2(self):
    ''' description
    Pre-conditions:
    1. set new name for human - name starts from capital and contains less, than 10 letters
    Steps to reproduce:
    1. create new name, which starts from capital and contains less, than 10 letters
    Expected result: name is changed'''
    self.human.change_name('Mike')
    assert self.human.name == 'Mike', f'\nName is not as expected\nActual: {self.human.name}\nExpected:' \
                                                      f' The name should start from capital and be more than 10 letters'

@pytest.mark.group_2
def test_06_new_wrong_name(self):
    ''' description
    Pre-conditions:
    1. set new name for human - name starts from non-capital and contains less, than 10 letters
    Steps to reproduce:
    1. create new name, which starts from non-capital and contains less, than 10 letters
    Expected result: name is not changed, Exception is raised'''
    with pytest.raises(Exception):
        self.human.change_name('mike')

@pytest.mark.group_2
def test_07_non_string_name(self):
    ''' description
    Pre-conditions:
    1. set new name for human - name is not string
    Steps to reproduce:
    1. create new name, which is not string
    Expected result: name is not changed, TypeError is raised'''
    with pytest.raises(TypeError):
        self.human.change_name(9)

@pytest.mark.group_3
def test_08_new_normal_gender(self):
    ''' description
    Pre-conditions:
    1. set new gender for human - 'female'
    Steps to reproduce:
    1. create new gender for human - 'female'
    Expected result: gender is changed'''
    self.human.gender = 'female'
    assert self.human.gender == 'female', f'\nGender is not as expected\nActual: {self.human.gender}\nExpected:' \
                                                f' Gender should be female'
@pytest.mark.group_3
def test_09_new_wrong_gender(self):
    ''' description
    Pre-conditions:
    1. set new non-existing gender for human
    Steps to reproduce:
    1. create new gender for human - 'some non-existing gender'
    Expected result: Exception is raised'''
    with pytest.raises(Exception):
        self.human.gender = 'some non-existing gender'

@pytest.mark.group_4
def test_10_living_friend_added(self, set_living_friend):
    ''' description
    Pre-conditions:
    1. friend is alive
    Steps to reproduce:
    1. create living friend
    2. try to add friend to the friends list
    Expected result: friend is added, friends list contains 1 record'''
    self.human.make_friends(set_living_friend)
    assert len(self.human.friends) == 1, f'\nFriend has not been added\nActual: {self.human.friends[0].name}' \
                                        f'\nExpected: One friend is added'

@pytest.mark.group_4
def test_11_dead_friend_not_added(self, set_dead_friend):
    ''' description
    Pre-conditions:
    1. friend is dead
    Steps to reproduce:
    1. create friend
    2. make friend dead
    3. try to add friend to the friends list
    Expected result: friend is not added, friends list is empty'''
    self.human.make_friends(set_dead_friend)
    assert len(self.human.friends) == 0, f'\nFriend has been added\nActual: One friend has been added' \
                                            f'\nExpected: No friends are added'

@pytest.mark.parametrize('age', [29, 31, 33])
def test_01_young_human(self, age):''''''
    '''description
    Pre-conditions:
    1. create 3 young humans of different age
    Steps to reproduce:
    1. create 29, 31, 33 years old human, using parametrize
    2. check, that he was added 1 year
    Expected result: age is increased for 1 year
    '''logger.info(f'\nTEST START: {age}')
    self.human.grow()
    assert self.human.age == 30, f'\nAge is not as expected\nActual: {self.human.age}\nExpected: 30'