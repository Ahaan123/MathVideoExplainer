import anthropic


API_KEY = "not available"



# from manim import *

# '''
# Prompt:
# Create Manim code for explaining this code with intuitive visuals and lots of animations and shapes with multiple scenes making up the full tutorial like explanation (give just the manim code and nothing else):

# # Python program for Linear Search using iterative approach
# def linear_search(arr, target):
#     # Traverse through all elements in the array
#     for index in range(len(arr)):
#         # If the element is found, return its index
#         if arr[index] == target:
#             return index
#     # If the element is not found, return -1
#     return -1

# # Example usage:
# arr = [10, 23, 45, 70, 11, 15]
# target = 70

# # Function call
# result = linear_search(arr, target)

# if result != -1:
#     print(f"Element found at index: {result}")
# else:
#     print("Element not found in the array")
# '''



# class LinearSearchTutorial(MovingCameraScene):
#     def construct(self):
#         self.intro_scene()
#         self.array_creation_scene()
#         self.linear_search_explanation_scene()
#         self.search_process_scene()
#         self.result_scene()
#         self.recap_scene()

#     def intro_scene(self):
#         title = Text("Understanding Linear Search", font_size=48, color=BLUE)
#         self.play(Write(title))
#         self.wait(1)
#         self.play(FadeOut(title))

#         code = '''
# # Python program for Linear Search
# def linear_search(arr, target):
#     for index in range(len(arr)):
#         if arr[index] == target:
#             return index
#     return -1

# # Example usage:
# arr = [10, 23, 45, 70, 11, 15]
# target = 70
# result = linear_search(arr, target)

# if result != -1:
#     print(f"Element found at index: {result}")
# else:
#     print("Element not found")
# '''
#         code_text = Code(
#             code=code,
#             tab_width=4,
#             background="rectangle",
#             language="python",
#             font="Monospace",
#             font_size=24,
#             line_spacing=0.8,
#             insert_line_no=False,
#             style="monokai",
#         )
#         code_text.to_edge(UP)
#         self.play(Write(code_text))
#         self.wait(2)
#         self.play(FadeOut(code_text))

#     def array_creation_scene(self):
#         step1 = Text("Step 1: Create the Array", font_size=36, color=YELLOW)
#         step1.to_edge(UP)
#         self.play(Write(step1))
#         self.wait(1)

#         arr = [10, 23, 45, 70, 11, 15]
#         boxes = VGroup(*[Square(side_length=1, color=BLUE) for _ in arr])
#         boxes.arrange(RIGHT, buff=0.5)
#         boxes.next_to(step1, DOWN)

#         labels = VGroup(*[Text(str(num), font_size=24).move_to(box) for num, box in zip(arr, boxes)])
#         self.play(Create(boxes), Write(labels))
#         self.wait(2)

#         self.play(FadeOut(step1), FadeOut(boxes), FadeOut(labels))

#     def linear_search_explanation_scene(self):
#         step2 = Text("Step 2: Define the Linear Search Function", font_size=36, color=YELLOW)
#         step2.to_edge(UP)
#         self.play(Write(step2))
#         self.wait(1)

#         code = '''
# def linear_search(arr, target):
#     for index in range(len(arr)):
#         if arr[index] == target:
#             return index
#     return -1
# '''
#         code_text = Code(
#             code=code,
#             tab_width=4,
#             background="rectangle",
#             language="python",
#             font="Monospace",
#             font_size=24,
#             line_spacing=0.8,
#             insert_line_no=False,
#             style="monokai",
#         )
#         code_text.next_to(step2, DOWN)
#         self.play(Write(code_text))
#         self.wait(2)
#         self.play(FadeOut(step2), FadeOut(code_text))

#     def search_process_scene(self):
#         step3 = Text("Step 3: Perform Linear Search", font_size=36, color=YELLOW)
#         step3.to_edge(UP)
#         self.play(Write(step3))
#         self.wait(1)

#         arr = [10, 23, 45, 70, 11, 15]
#         target = 70
#         boxes = VGroup(*[Square(side_length=1, color=BLUE) for _ in arr])
#         boxes.arrange(RIGHT, buff=0.5)
#         boxes.next_to(step3, DOWN)

#         labels = VGroup(*[Text(str(num), font_size=24).move_to(box) for num, box in zip(arr, boxes)])
#         self.play(Create(boxes), Write(labels))
#         self.wait(1)

#         target_text = Text(f"Target: {target}", font_size=36, color=RED).next_to(boxes, DOWN)
#         self.play(Write(target_text))
#         self.wait(1)

#         for i, box in enumerate(boxes):
#             self.play(box.animate.set_color(YELLOW))
#             if arr[i] == target:
#                 self.play(box.animate.set_color(GREEN))
#                 break
#             else:
#                 self.play(box.animate.set_color(RED))
#         self.wait(2)
#         self.play(FadeOut(step3), FadeOut(boxes), FadeOut(labels), FadeOut(target_text))

#     def result_scene(self):
#         step4 = Text("Step 4: Display the Result", font_size=36, color=YELLOW)
#         step4.to_edge(UP)
#         self.play(Write(step4))
#         self.wait(1)

#         result_text = Text("Element found at index: 3", font_size=36, color=GREEN)
#         result_text.next_to(step4, DOWN)
#         self.play(Write(result_text))
#         self.wait(2)
#         self.play(FadeOut(step4), FadeOut(result_text))

#     def recap_scene(self):
#         recap = Text("Recap:", font_size=48, color=BLUE)
#         self.play(Write(recap))
#         self.wait(1)

#         point1 = Text("1. Create an array", font_size=36).next_to(recap, DOWN)
#         point2 = Text("2. Define the linear search function", font_size=36).next_to(point1, DOWN)
#         point3 = Text("3. Traverse the array to find the target", font_size=36).next_to(point2, DOWN)
#         point4 = Text("4. Return the index if found, else return -1", font_size=36).next_to(point3, DOWN)

#         self.play(Write(point1))
#         self.wait(1)
#         self.play(Write(point2))
#         self.wait(1)
#         self.play(Write(point3))
#         self.wait(1)
#         self.play(Write(point4))
#         self.wait(2)
#         self.play(FadeOut(recap), FadeOut(point1), FadeOut(point2), FadeOut(point3), FadeOut(point4))
