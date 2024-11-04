# Project Goal
This project uses the Python library **Manim** to create animations that illustrate concepts in planetary formation, tailored for studies in astronomy and astrophysics.

## Inventory

### Example Animation
Below is an embedded video demonstrating one of the animations on planetary formation.

<video width="1920" controls>
  <source src="dragEQ.mp4" type="video/mp4">
</video>

[![Watch the Animation](https://img.youtube.com/vi/qTuNCvHzRU0/0.jpg)](https://www.youtube.com/watch?v=qTuNCvHzRU0)

https://www.youtube.com/watch?v=qTuNCvHzRU0

## Compiling Videos
To render the animations, you can use the following compiler tags for quality control:

- **`-ql`**: Low quality rendering (faster, ideal for testing)
- **`-qh`**: High quality rendering (slower, ideal for final output)

### Example Command
To render the `dragEQ.py` animation in low quality, use:
```bash
manim -ql -p dragEQ.py DragEQ
```

---
