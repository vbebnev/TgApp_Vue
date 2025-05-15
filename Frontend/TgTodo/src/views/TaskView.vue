<template>
<div>
    <h1>Профиль</h1>
    <p v-if="platform">Открыто из Telegram на платформе: {{ platform }}</p>
    <p v-else>Telegram WebApp не найден</p>
  </div>

    <div class="tasks_container">
        <div class="tasks-header">
            <input
                v-model="newTask"
                type="text"
                placeholder="Enter new task..."
                class="task-input"
                @keyup.enter="createTask"
            />
            <button class="add-button" @click="createTask">+</button>
        </div>
        <div class="tasks-list">
            <div
                v-for="task in tasks"
                :key="task.id"
                class="task-item"
            >
            <div class="task-text">
                {{ task.title }}
            </div>
            <button
                class="complete-button"
                @click="completeTask(task.id)">Done
            </button>
            </div>
        </div>
    </div>
</template>

<script>
import { getTelegramWebApp } from '../telegram'

export default{
    name:'TasksView',
    data() {
        return {
            tasks:[],
            newTask:''
        }
    },
    async mounted() {    
        const webApp = getTelegramWebApp()
        if (webApp) {
        this.platform = webApp.platform
        }

        await this.fetchTasks()
    },
methods: {
    async fetchTasks() {
        try {
            console.log('trying to fetch tasks')
            console.log('tlg web app - '+ window.Telegram.WebApp)
            const tg_user = window.Telegram.WebApp.initDataUnsafe?.user
            console.log('telega answered')
            const response = await fetch(`https://solid-space-waddle-jrj697xgx47fgxv-8000.app.github.dev/api/taks/${tg_user.id}`)
            console.log('backend answered')
            const data = await response.json()
            this.tasks = data
        }
        catch (error) {
            console.log('error', error)
        }
    },
    async addTask() {

        if(!this.newTask) return 

        try {
            const tg_user = window.Telegram.WebApp.initDataUnsafe?.user
            const response = await fetch(`https://solid-space-waddle-jrj697xgx47fgxv-8000.app.github.dev/api/add`, {
                method: 'POST', 
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({tg_id: tg_user.id, title: this.newTask})
            })
            if(response.ok) {
                this.newTask = ''
                await this.fetchTasks()
            } else {
                console.error('error', response.status)
            }
        } catch (error) {
            console.log ('Error', error)
        }
    },
    async completeTask(taskId) {
        try {
            const response = await fetch(`https://solid-space-waddle-jrj697xgx47fgxv-8000.app.github.dev/api/complete`, {
                method: 'POST', 
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({id: taskId})
            })
            if(response.ok) {
                await this.fetchTasks()
            } else {
                console.error('error', response.status)
            }
        } catch (error) {
            console.log ('Error', error)
        }        
    }
}
}
</script>

<style scoped>
.task-container {
    flex:1;
    display:flex;
    flex-direction: column;
    padding: 16px;
    overflow-y: auto;
}
.task-header {
    flex-direction:row;
    justify-content: center;
    align-items: center;
    margin-bottom: 16px;
}
.task-input {
    flex:1;
    padding: 8px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 8px;
    margin-right: 8px;
}
.add-button {
    background-color: #007aff;
    color: white;
    border: none;
    padding: 0 16px;
    font-size: 24px;
    border-radius: 50%;
    cursor: pointer;
    outline: none;
    height: 40px;
    width: 40px;
}
.task-list {
    display:flex;
    flex-direction: column;
    gap:8px;
}
 .task-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #ffffffcc;
    padding: 8px 12px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
 }

 .task-text {
    font-size: 16px;
 }
 
 .complete-button {
    background-color: #4caf50;
    color: white;
    border: none;
    padding: 6px 12px;
    border-radius: 8px;
    cursor:pointer;
 }
</style>