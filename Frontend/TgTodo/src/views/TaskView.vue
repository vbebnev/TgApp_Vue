<template>
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
export default{
    name:'TasksView',
    data() {
        return {
            tasks:[],
            newTask:''
        }
    },
    async mounted() {
        await this.fetchTasks()
    },
methods: {
    async fetchtasks() {
        try {
            const tg_user = window.Telegram.webapp.initDataUnsafe?.user
            const response = await fetch(`https://solid-space-waddle-jrj697xgx47fgxv-8000.app.github.dev/api/taks/${tg_user.id}`)
            const data = await response.json()
            this.tasks = data
        }
        catch (error) {
            console.log('error', error)
        }
    }
})
}
</script>