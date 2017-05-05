(function() {

  'use strict'

  var app = new Vue({
    el: '#app',

    data: {
      people: [{}, {}]
    },

    methods: {
      addPerson: function () {
        this.people.push({})
      },

      removePerson: function (index) {
        this.people.splice(index, 1)
      },

      submit: function (e) {
        e.preventDefault()

        var request = new XMLHttpRequest()
        request.open('post', '/rsvp')
        request.setRequestHeader('Content-Type', 'application/json')

        request.onreadystatechange = function () {
          if(request.readyState === XMLHttpRequest.DONE) {
            if(request.status === 204) {
              alert('done.')
            } else {
              alert('error.')
            }
          }
        }

        request.send(JSON.stringify(this.people))
      }
    }
  })

}())
