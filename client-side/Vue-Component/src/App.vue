<template>
<div>
  <input @input="getCompletions" :value="complete"/>
  <div v-for="word in completing.splice(0,8)" id="wordlist">
  <p @click="changeValue(word)">{{ word }}</p>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return {
      complete: '',
      completing: []
    }
  },
  methods: {
    async getCompletions(event){
      console.log(event.target.value)
      this.complete = event.target.value
      const body = {
        'msg': this.complete
      }
      const request = await axios.post('http://localhost:5000', body)
      console.log(request.data)
      this.completing = request.data
      if (this.complete === ''){
        this.completing = []
      }
    },
    changeValue(word){
      this.complete = word
      this.completing = []
    }
  }
}
</script>

<style>
p {
  color: black;
  font-weight: bold;
}
#wordlist {
  background-color: white;
  box-shadow: 1.5px 1.5px 1.5px lightblue
}
</style>