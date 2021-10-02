const secondsInHour = 3600

const app = Vue.createApp({
    data() {
        return {
            darkTheme: false,
        }
    },
    computed: {
        iconTheme() {
            return {
                'fas fa-sun': this.darkTheme,
                'fas fa-moon': !this.darkTheme,
            }
        }
    },
    mounted() {
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            this.darkTheme = true
        }
    },
    watch: {
        darkTheme(status) {
            if (status == true) {
                document.body.classList.add('theme-dark')
            } else {
                document.body.classList.remove('theme-dark')
            }
        }
    },
})

app.component('Calculator', {
    template: /*html*/
        `<form class="calculator">
            <div class="calculator-body">
                <div class="field">
                    <label for="hours">Hours</label>
                    <input type="number" name="hours" id="hours" v-model="hours" min="0">
                </div>
                <div class="field">
                    <label for="minutes">Minutes</label>
                    <input type="number" name="minutes" id="minutes" v-model="minutes" min="0">
                </div>
                <div class="field">
                    <label for="seconds">Seconds</label>
                    <input type="number" name="seconds" id="seconds" v-model="seconds" min="0">
                </div>
                <hr>
                <div class="field">
                    <label for="hourly_rate">Hourly Rate</label>
                    <input type="number" name="hourly_rate" id="hourly_rate" step="0.01" v-model="hourlyRate" min="0.00">
                </div>
            </div>
            <div class="calculator-footer">
                <div>Result: <span :class="{ 'text-green': result > 0 }">\${{ result }}</span></div>
            </div>
        </form>`,
    data() {
        return {
            hours: 0,
            minutes: 0,
            seconds: 0,
            hourlyRate: 0.00,
        }
    },
    computed: {
        result() {
            let totalTimeInSeconds = (this.hours * 3600) + (this.minutes * 60) + this.seconds
            let dollarsPerSecond = this.hourlyRate / 3600
            return (totalTimeInSeconds * dollarsPerSecond).toFixed(2)
        },
    }
})

app.mount('#app')
