import unittest

from dungeonbot.cogs.splash import Splash, UnknownSubstance

def mock_random(distance, direction, damage=0):
  def randint(min, max):
    if max == 6:
      return distance
    if max == 8:
      return direction
    if max == 3:
      return damage

    raise Exception('Invalid max int requested')

  return randint


class SplashTest(unittest.TestCase):

  def test_tequila(self):
    splash = Splash(None)
    splash.randint = mock_random(6, 4, 3)
    self.assertRaises(UnknownSubstance, splash.handle_splash, 'tequila')

  def test_oil_short(self):
    splash = Splash(None)
    splash.randint = mock_random(1, 2, 3)
    message = splash.handle_splash('oil')
    self.assertEqual(message, 'Your oil landed 1 foot right and did 3 damage.')

  def test_oil_long(self):
    splash = Splash(None)
    splash.randint = mock_random(6, 4, 3)
    message = splash.handle_splash('oil')
    self.assertEqual(message, 'Your oil landed 6 feet short (before) and did 0 damage.')

  def test_acid_short(self):
    splash = Splash(None)
    splash.randint = mock_random(1, 2, 3)
    message = splash.handle_splash('acid')
    self.assertEqual(message, 'Your acid landed 1 foot right and did 1 damage.')

  def test_acid_long(self):
    splash = Splash(None)
    splash.randint = mock_random(5, 4, 3)
    message = splash.handle_splash('acid')
    self.assertEqual(message, 'Your acid landed 5 feet short (before) and did 0 damage.')

  def test_holy_water_short(self):
    splash = Splash(None)
    splash.randint = mock_random(2, 3, 3)
    message = splash.handle_splash('holy water')
    self.assertEqual(message, 'Your holy water landed 2 feet short right and did 0 damage.')

  def test_holy_water_long(self):
    splash = Splash(None)
    splash.randint = mock_random(7, 5, 3)
    message = splash.handle_splash('holy water')
    self.assertEqual(message, 'Your holy water landed 7 feet short left and did 0 damage.')
