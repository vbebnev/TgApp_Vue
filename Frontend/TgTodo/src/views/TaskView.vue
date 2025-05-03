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
            <div class="class-text">
                {{ task.title }}
            </div>
            <button
                class="complete-button"
                @click=completeTask(task.id)>Done
            </button>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    name:'TaskView',
    data() {
        return {
            tasks:[],
            newTask:''
        }
    },
    async mounted( {
        await this.fetchTasks()
    },
methods: {
    
})
}
</script>