command: "python github.widget/get-data.py"

# the refresh frequency in milliseconds
refreshFrequency: 1000000

render: -> """
  <h1>My Pending Reviews</h1>
  <table class='gl-list'></table>
"""

update: (output, domEl) ->
  @$domEl = $(domEl)
  @renderData output

renderData: (data) ->
  el = @$domEl.find('.gl-list')
  el.html('')

  for key, value of JSON.parse data
    if key == 'error'
      el.append "<span class='error'>#{value}</span>"
    else if key == 'message'
      el.append "<span class='message'>#{value}</span>"
    else
      el.append @renderRepo(key, value)

renderPR: (value) ->
  return """
    <tr class="pr">
        <td><a href="#{value.url}">#{value.name} [No: #{value.number}]</a></td>
    </tr>
  """

renderRepo: (key, value) ->
  @html = """
      <tr class="repo">
          <td>#{value.full_name}</td>
      </tr>
  """

  for pr, i in value.prs
    @html += @renderPR(pr)
  return @html

style: """
  color: #FFFFFF
  font-family: Helvetica Neue
  left: 12px
  top: 30px
  h1
    font-size: 2em
    font-weight: 100
    margin: 0
    padding: 0
    padding-bottom: 10px
  ul
    font-weight: 200
    line-height: 1.4em
    list-style-type: none
    margin: 0
    padding: 0
  .gl-mr
    color: white
  .gl-mr-true
    color: yellow
  tr.repo td
    border-bottom: 1px dashed rgba(255, 255, 255, 0.3)
    font-size: 18px
  tr.pr td
    font-size: 14px
    padding-bottom: 6px
  a
    color: white
    text-decoration: none
  .message
    color: rgb(0, 125, 57)
  .error
    color: rgb(201, 199, 5)

"""
