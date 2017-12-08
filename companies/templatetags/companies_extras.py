from django import template

register = template.Library()
import math

@register.simple_tag # show player distance form other players or planets
def find_distance(x, y, z, x2, y2, z2, *args, **kwargs):
	distance = math.sqrt((x-x2)*(x-x2) + (y-y2)*(y-y2) + (z-z2)*(z-z2))
	distance = round(distance, 2)
	return distance

# dont need this probably
# @register.simple_tag # show player fuel cost for trade
# def fuel_cost(distance, amount, *args, **kwargs):
# 	cost = (distance / 5000) * amount
# 	cost = round(cost)
# 	return cost

@register.simple_tag
def readable_int(number, *args, **kwargs):
	readable = '{:,}'.format(number) # define format use commas
	return readable

@register.simple_tag
def parse_mine_info(mine, *args, **kwargs):
	element = mine[0] 
	amount = mine[1]
	return element, amount # return array as set so template can target it.
