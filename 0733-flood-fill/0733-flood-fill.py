class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # Start the flood fill by calling the helper function `fill`
        # It fills the starting pixel (sr, sc) with the target color.
        self.fill(image, sr, sc, color, image[sr][sc])

        # Return the modified image after completing the flood fill
        return image

    def fill(self, image, sr, sc, color, original):
        # Base case: Return if out of bounds of the image
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]):
            return

        # Base case: Return if the pixel is already the target color or not
        # the original color that needs to be changed.
        if image[sr][sc] == color or image[sr][sc] != original:
            return

        # Fill the current pixel with the target color
        image[sr][sc] = color

        # Recursively call `fill` on the four adjacent pixels (up, down, left, right)
        self.fill(image, sr - 1, sc, color, original)  # Move up
        self.fill(image, sr + 1, sc, color, original)  # Move down
        self.fill(image, sr, sc - 1, color, original)  # Move left
        self.fill(image, sr, sc + 1, color, original)  # Move right
