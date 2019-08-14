message = 0
test = 0
pickle = 0

while message < 10 do
  message = message + 1
  test = test - 5
end

for i = 1, 3, 1 do
  pickle = pickle + 10
end

function love.draw()
  love.graphics.setFont(love.graphics.newFont(50))
  love.graphics.print(message)
  love.graphics.print(test)
  love.graphics.print(pickle)
end
