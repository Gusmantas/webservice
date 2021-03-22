$('#test-btn').click(async function() {
  let ageValue = $('#age-input').val()
  let incomeValue = $('#income-input').val()

  let testValues = {
    age: ageValue,
    income: incomeValue
  }

  let res = await fetch('/api/predict', {
    method: 'POST',
    body: JSON.stringify(testValues)
  })

  let prediction = await res.json()

  $('#prediction').html(`
    Will user click this ad: <em>${prediction['will-click']}</em>
    <br>
    Probability of clicking this ad: <em>${prediction['probability']}%</em>
  `)
})