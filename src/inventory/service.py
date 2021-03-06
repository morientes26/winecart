# -*- coding: utf-8 -*-
"""
Service for inventory managment
"""

import datetime
from collections import namedtuple
from inventory.models import *

import logging

logger = logging.getLogger(__name__)


class InventoryService:
	"""
	Service for getting information about products, orders, events
	"""

	def get_product_by_id(self, id):
		"""
		Args: id: product primary key
		Returns: tuples 'product' with keys product, wine
		Throws: Exception
		"""
		product = Product.objects.get(pk=id)
		if not product:
			logger.error("Product not found by pk =  ", id)
			raise Exception("Product not found")

		return product

	def get_products(self, group):
		"""
		Args: group - String of group name
		Returns: list of products
		"""
		event = self.get_event()
		if event:
			logger.debug('finded actual event')
			return self.get_all_products_in_event(event, group)
		else:
			logger.debug('not actual event')
			return self.get_all_products_in_cart(group)

	def upload_photos(self, request, product):
		if request.FILES:
			logger.debug(request.FILES)

			if 'photo_upload' in request.FILES:
				photo = Photo.objects.create(blob=request.FILES['photo_upload'])
				product.photos = photo

			for i in range(1, 5):
				if 'award_upload_' + str(i) in request.FILES:
					photo = Photo.objects.create(blob=request.FILES['award_upload_' + str(i)])
					photo.save()
					award = Award.objects.create(name=request.POST['award_name_' + str(i)], photo=photo)
					award.save()
					product.awards.add(award)
			product.save()
			
		if 'award_remove' in request.POST:
			for ax in request.POST.getlist('award_remove'):
				aw = Award.objects.get(pk=int(ax))
				logger.debug('delete award %s', aw)
				product.awards.remove(aw)
				aw.delete()
		
			product.save()

	def get_new_products(self):
		products = Product.objects.filter(is_new=True)
		logger.debug('get_new_products - fetching %s data', products.count())
		return products

	def get_all_products_in_cart(self, group='*'):
		grp = Group.objects.filter(name=group)
		if grp:
			products = Product.objects.filter(active=True, group=grp)
		else:
			products = Product.objects.filter(active=True)
		logger.debug('get_all_products_in_cart - fetching %s data', products.count())
		return products

	def get_all_products_in_event(self, event, group):
		products = event.products
		result = []
		logger.debug(products.all())
		for prod in products.all():
			if prod.group:
				logger.debug(prod)
				if prod.group.name == group:
					result.append(prod)

		logger.debug('get_all_products_in_event from %s - fetching %s data', event, result.__sizeof__())
		return result

	def get_actual_orders_by_name(self, customer_name):
		orders = Order.objects.filter(done=False, customer_name=customer_name)
		logger.debug('get_actual_orders_by_name - fetching %s data', orders.count())
		return orders

	def get_all_back_orders(self):
		""" get all not competed orders """
		orders = Order.objects.filter(done=False)
		return orders

	def get_event(self):
		now = datetime.datetime.now()
		events = Event.objects.filter(date_from__lte=now, date_to__gte=now).order_by('id')
		if events:
			return events[0]
		else:
			return None

	def get_unit_price(self, product):
		if product.size is not None:
			if product.size > 0:
				up = Decimal(product.price / product.size)
				setting = UserPreference.objects.filter(pk=1) 
				print(setting)    
				return round(up, 2) * float(setting[0].unit_amount)  # (jednotkova cena je jedno deci nie liter)
		return product.price

# ----------------------------------------------------------------------------------

	"""@deprecated"""

	def create_order(self, customer_name, event_id, product_list):
		event = Event.objects.get(pk=event_id)
		items = Product.objects.filter(pk__in=product_list)
		if event == None or items == None:
			raise ValueError('input parameters are bad')
		order = Order.objects.create(customer_name=customer_name, event=event, items=items)
		return order

	def done_order(self, id):
		try:
			order = Order.objects.get(pk=id)
			order.done = True
			order.save()
			logger.debug('done_order - fetching %s data', order)
		except Product.DoesNotExist:
			logger.error("Order not found")
			raise
		return order

	"""@deprecated"""

	def get_actual_events(self, group):
		now = datetime.datetime.now()
		events = Event.objects.filter(date_from__lte=now, date_to__gte=now, products__group__name=group).order_by('id')
		logger.debug('get_actual_events - fetching %s data', events.count())
		logger.debug(events)
		return events
