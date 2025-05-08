<template>
    <div class="profile-container">
        <h2>Profile</h2>
        <div class="profile-info">
            <p><strong>ID:</strong> {{ user.id }}</p>
            <p><strong>Name:</strong> {{ user.name }}</p>
            <p><strong>Completed tasks:</strong> {{ user.completedTasks }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'ProfileView',
        data() {
            return {
                user: {
                    id: '',
                    name: '',
                    completedTasks: 0
                }
            }
        },
        async mounted() {
            await this.fetchProfile()
        },
        methods: {
            fetchProfile(){
                try {
                    
                }
            }
        }
    }
</script>