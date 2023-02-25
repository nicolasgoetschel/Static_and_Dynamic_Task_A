### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      # Here, we should use a comparison operator (==) instead of the assignment operator (=) we used
      return True
    else
    # colon (:) missing after else
      return False
   

  dif highest_card(self, card1 card2):
  # (def is misspelled)
  # we're missing a comma (,) between card1 and card2)
  if card1.value > card2.value:
    # indention error
    return card
  # card is not initialised, this should be card1

  else:
    return card2
  


def cards_total(self, cards):
  # indention error
  total
  # total variable is not initialised to a value
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # total should be converted to a string.
    # return is indented too far to the right.
  
```
