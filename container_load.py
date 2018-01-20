import traceback
import sys
import unittest

""" Challenge Statement
For a given collection of container sizes and a required load, write an algorithm
(simple console app will suffice), that will select sufficient containers for
the load, such that:

1. the overcapacity is minimized, and
2. the smallest number of containers are used
"""

class ContainerLoader:

	def __init__(self):
		pass

	def perform_loading(self, container_sizes, capacity):
		""" Function performs the job of loading.

		@param: container_sizes: Pass the list of container sizes
		@param: capacity: Pass the required optimal capacity value

		Algoritm to solve the container loading:
		* f(w) = min<i to n> {1 + f(w-w<i>)} where w<i> <= w
		* In above computation if there is no w<i> <= w, then return 1

		@returns: Number of containers required to reach capacity and list of container sizes which
		can be used to perform loading.
		"""
		try:
			container_sizes.sort()
			min_occupancy = [sys.maxsize]*(capacity+1)
			min_occupancy[0] = 0

			arrangement_arr = [0]*(capacity+1)
			for i in range(1, capacity+1):
				if (self.is_any_smaller_container_exist(i, container_sizes)):
					containers_num = 0
					for j in range(0, len(container_sizes)):
						if (i - container_sizes[j] >= 0):
							containers_num = 1 + min_occupancy[i - container_sizes[j]];
						if (min_occupancy[i] > containers_num):
							min_occupancy[i] = containers_num;
							arrangement_arr[i] = j;
				else:
					min_occupancy[i] = 1
					arrangement_arr[i] = self.get_min_container_index(container_sizes)

			no_of_containers = min_occupancy[capacity]
			print("Number of Containers required to load with minimum Over capacity:", no_of_containers)

			path_index = capacity
			selected_container_sizes = list()
			while(path_index > 0):
				selected_container_sizes.append(container_sizes[arrangement_arr[path_index]])
				path_index = path_index - container_sizes[arrangement_arr[path_index]]
			print("Selected Container sizes:", selected_container_sizes)

			selected_container_sizes.sort()

			return no_of_containers, selected_container_sizes

		except:
			print(traceback.format_exc())

	def get_min_container_index(self, container_sizes):
		""" Get Minimum container index 

		@param: container_sizes: Pass lis of container sizes
		@return: Index of element in the container size list which has minimum size.
		"""
		min_container_index = -1
		min_container_size = sys.maxsize
		array_length = len(container_sizes)
		for index in range(array_length):
			if(container_sizes[index] < min_container_size):
				min_container_size = container_sizes[index]
				min_container_index = index
		return min_container_index


	def is_any_smaller_container_exist(self, load, container_sizes):
		""" Check smaller container exist than a given load.

		@param: load: Pass the value of load which is upper bound of size.
		@param: container_sizes: Pass the list of container_sizes 

		@return: Boolean value if any container is found than the specified load.
		"""
		exist = False
		for container_size in container_sizes:
			if(container_size <=load):
				exist = True
				return exist
		return exist


class ContainerLoaderTest(unittest.TestCase):
	def setUp(self):
		self.loader_obj = ContainerLoader()

	def test_data_set_1(self):
		container_sizes = [2, 3 ,5]
		container_capacity = 6
		no_of_containers, selected_container_sizes = self.loader_obj.perform_loading(container_sizes, container_capacity)
		self.assertEqual(no_of_containers, 2)
		self.assertEqual(selected_container_sizes, [3, 3])

	def test_data_set_2(self):
		container_sizes = [2, 3 ,5]
		container_capacity = 9
		no_of_containers, selected_container_sizes = self.loader_obj.perform_loading(container_sizes, container_capacity)
		self.assertEqual(no_of_containers, 3)
		self.assertEqual(selected_container_sizes, [2, 2, 5])

	def test_data_set_3(self):
		container_sizes = [2, 3 ,5]
		container_capacity = 11
		no_of_containers, selected_container_sizes = self.loader_obj.perform_loading(container_sizes, container_capacity)
		self.assertEqual(no_of_containers, 3)
		self.assertEqual(selected_container_sizes, [3, 3, 5])

	def test_data_set_4(self):
		container_sizes = [2, 4]
		container_capacity = 5
		no_of_containers, selected_container_sizes = self.loader_obj.perform_loading(container_sizes, container_capacity)
		self.assertEqual(no_of_containers, 2)
		self.assertEqual(selected_container_sizes, [2, 4])

	def test_data_set_5(self):
		container_sizes = [2, 4]
		container_capacity = 8
		no_of_containers, selected_container_sizes = self.loader_obj.perform_loading(container_sizes, container_capacity)
		self.assertEqual(no_of_containers, 2)
		self.assertEqual(selected_container_sizes, [4, 4])

	def tearDown(self):
		del self.loader_obj

if __name__ == "__main__":
	unittest.main()