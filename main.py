import imgui
import glfw
import sys

import OpenGL.GL as gl
from imgui.integrations.glfw import GlfwRenderer

def main():
    window = impl_glfw_init()
    imgui.create_context()
    impl = GlfwRenderer(window)
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        impl.process_inputs()

        imgui.new_frame()
        
        imgui.begin("Your first window!")
        imgui.text("Hello world")
        imgui.end()

        # gl.glClearColor(1.0, 1.0, 1.0, 1) #Change background color
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.render()
        impl.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

    impl.shutdown()
    glfw.terminate()

def impl_glfw_init():
    width, height = 1280, 720
    window_name = "testing window"
    if not glfw.init():
        # TODO error handling
        print("Could not initialize OpenGL context")
        sys.exit(1)
    
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)

    window = glfw.create_window(int(width), int(height), window_name, None, None)
    glfw.make_context_current(window)

    if not window:
        glfw.terminate()
        print("Could not initialize Window")
        sys.exit()

    return window

if __name__ == "__main__":
    main()