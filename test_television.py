import unittest
import 



class MyTest(unittest.TestCase):
    def test_with_string(self):
        #Circle
        with self.assertRaises(ValueError):
            area.circle('x')
        with self.assertRaises(TypeError):
            area.circle(-2)
        with self.assertRaises(TypeError):
            area.circle(0)
        self.assertAlmostEqual(area.circle(4), 12.56)
        self.assertAlmostEqual(area.circle(4.2), 13.188)
        #Square
        with self.assertRaises(ValueError):
            area.square('x')
        with self.assertRaises(TypeError):
            area.square(-2)
        with self.assertRaises(TypeError):
            area.square(0)
        self.assertAlmostEqual(area.square(4), 16)
        self.assertAlmostEqual(area.square(4.2), 17.64)
        #Rectangle
        with self.assertRaises(ValueError):
            area.rectangle('x', 'x')
            area.rectangle('x',2)
            area.rectangle(2, '2')
        with self.assertRaises(TypeError):
            area.rectangle(-2, -2)
            area.rectangle(2, -2)
            area.rectangle(-2, 2)
        with self.assertRaises(TypeError):
            area.rectangle(0,0)
            area.rectangle(1, 0)
            area.rectangle(0, 1)
        self.assertAlmostEqual(area.rectangle(2,3), 6)
        self.assertAlmostEqual(area.rectangle(2,2.1), 4.2)
        self.assertAlmostEqual(area.rectangle(2.1, 2.1), 4.41)
        self.assertAlmostEqual(area.rectangle(2.5, 2), 5.0)
        #triangle
        with self.assertRaises(ValueError):
            area.triangle('x', 'x')
            area.triangle('x', 2)
            area.triangle(2, '2')
        with self.assertRaises(TypeError):
            area.triangle(-2, -2)
            area.triangle(2, -2)
            area.triangle(-2, 2)
        with self.assertRaises(TypeError):
            area.triangle(0, 0)
            area.triangle(1, 0)
            area.triangle(0, 1)
        self.assertAlmostEqual(area.triangle(2, 3), 3)
        self.assertAlmostEqual(area.triangle(2, 2.1), 2.1)
        self.assertAlmostEqual(area.triangle(2.1, 2.1), 2.205)
        self.assertAlmostEqual(area.triangle(2.5, 2), 2.5)
if __name__ == '__main__':
    unittest.main()
