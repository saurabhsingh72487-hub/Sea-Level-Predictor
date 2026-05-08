import unittest
import matplotlib.pyplot as plt
from sea_level_predictor import draw_plot


class SeaLevelPredictorTestCase(unittest.TestCase):

    def setUp(self):
        self.ax = draw_plot()

    def test_plot_title(self):
        self.assertEqual(self.ax.get_title(), 'Rise in Sea Level')

    def test_x_label(self):
        self.assertEqual(self.ax.get_xlabel(), 'Year')

    def test_y_label(self):
        self.assertEqual(self.ax.get_ylabel(), 'Sea Level (inches)')

    def test_number_of_lines(self):
        # There should be 2 regression lines
        self.assertEqual(len(self.ax.lines), 2)

    def test_first_line_x_data(self):
        x_data = self.ax.lines[0].get_xdata()
        self.assertEqual(x_data[0], 1880)
        self.assertEqual(x_data[-1], 2050)

    def test_second_line_x_data(self):
        x_data = self.ax.lines[1].get_xdata()
        self.assertEqual(x_data[0], 2000)
        self.assertEqual(x_data[-1], 2050)

    def tearDown(self):
        plt.close()


if __name__ == "__main__":
    unittest.main()