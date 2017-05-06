(function() {

  'use strict'

  var app = new Vue({
    el: '#app',

    data: {
      people: [{}, {}],
      submitting: false,
      submitted: false
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
              app.submitted = true
            } else {
              alert('Error: Your RSVP was not saved. Blame Ryan.')
            }

            app.submitting = false
          }
        }

        request.send(JSON.stringify(this.people))
        app.submitting = true
      }
    }
  })

}())
