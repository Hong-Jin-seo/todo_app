import streamlit as st

st.title('To-do List☑️')

# (할 일 + 했는지 여부) 객체로 관리하기 위해 만든 클래스
class Todo:
    def __init__(self, task: str, done: bool = False):
        self.__task = task
        self.__done = done

    def get_task(self):
        return self.__task

    def get_done(self):
        return self.__done

    def set_done(self, done: bool):
        self.__done = done

    # 객체가 list 안에 있을 때 list 안의 요소들을 출력하면 __repr__만 나온다 (__str__은 안 나옴)
    def __repr__(self):
        return f'Task: {self.__task}, Done: {self.__done}'

    # def __str__(self):
    #     return f'Task: {self.__task}, Done: {self.__done}'


# repr 심화 설명
# todo = Todo('숙제하기')
# print(id(todo))
# todo2 = eval(repr(todo))
# print(id(todo2))

# Todo 객체를 list에 쌓는 용도의 함수 (추가 할 할 일을 작성하면 실행되는 함수)
def add_todo():
    print(f'함수가 호출될 때 주머니에 담긴 값 : {st.session_state.new_task}')
    todo = Todo(st.session_state.new_task)
    # print(todo)
    st.session_state.todos.append(todo)
    st.session_state.new_task = ''

def togle_done(index: int):
    todo = st.session_state.todos[index]
    todo.set_done(not todo.get_done())

def delete_todo(index: int):
    st.session_state.todos.pop(index)

def move_up(index: int):
    if index > 0:
        st.session_state.todos[index], st.session_state.todos[index-1] = \
        st.session_state.todos[index-1], st.session_state.todos[index]

def move_down(index: int):
    if index < len(st.session_state.todos) - 1:
        st.session_state.todos[index], st.session_state.todos[index+1] = \
        st.session_state.todos[index+1], st.session_state.todos[index]

# todos (todo 객체를 담을 리스트를 초기화)
if 'todos' not in st.session_state:
    st.session_state.todos = []

# key 속성을 사용하면 key에 적힌 이름으로 사용자가 입력한 값이 session_state에 저장
# input 창에 내용(기존과 다른 내용)을 작성하고 enter하면 add_todo 함수 호출
st.text_input('새로운 할 일 추가', key='new_task', on_change=add_todo)

if st.session_state.todos:
    for i, todo in enumerate(st.session_state.todos):
        # st.write(f'{i + 1}번째 todo : {todo}')
        display_text = f'~~{todo.get_task()}~~' if todo.get_done() else todo.get_task()
        col1, col2, col3, col4 = st.columns([0.7, 0.1, 0.1, 0.1])
        # col1.checkbox(f'{i + 1}', value=todo.get_done(), key=f'done_{i}', on_change=togle_done, args=(i,))
        col1.checkbox(f'{display_text}', value=todo.get_done(), key=f'done_{i}', on_change=togle_done, args=(i,))
        # col2.markdown(f'~~{todo.get_task()}~~' if todo.get_done() else todo.get_task())
        # 위로 이동 버튼
        with col2:
            if st.button('⬆️', key=f'up_{i}'):
                move_up(i)
                st.rerun()

        # 아래로 이동 버튼
        with col3:
            if st.button('⬇️', key=f'down_{i}'):
                move_down(i)
                st.rerun()
        # 삭제 버튼
        with col4:
            if st.button('삭제', key=f'del_{i}'):
                delete_todo(i)
                st.rerun()

        # if col2.button('삭제', key=f'del_{i}'):
        #     st.session_state.todos.pop(i)
        #     st.rerun()
else:
    st.info('할 일을 추가해보세요.')

# pip list하면 현재 가상환경(pystusdy_env)에 있는 도구들(패키지들)을 알 수 있음
# streamlit에 배포하기 위해 github에 올릴 때는 requirements.txt로 만들어서 push
# pip list --format=freeze > requirements.txt

# streamlit에서 충돌 발생하면 LLM 활용해서 해당 라이브러리에 적합한 버전으로 수정 및 삭제하면 배포 가능
# requirements.txt에서 'win'으로 검색해서 세가지 삭제하기
# 1. pywin32==311
# 2. pywinpty==2.0.15
# 3. win_inet_pton==1.1.0

# mac은 아마도 pyodbc랑 unixodbc 이 두 개를 지워야 할 듯