import gradio as gr 
import matplotlib.pyplot as plt #To draw the chart 
import time #To slow down the code for the user to see

def insertion_sort(text_input):
    #Try Catch statement to avoid an error, when user enters invalid list
    try:
        if not text_input:
            return None
        array = [int(x) for x in text_input.split(',')] #Convert string input to a list of integars
    except ValueError:
        return None 

    #To draw the chart
    def draw_chart(data, highlight_index=None):
        fig, ax = plt.subplots(figsize=(6, 4)) #Size of frame of output
        
        #Make the background black
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        
        #Make the bars cyan
        colors = ['#00E5FF'] * len(data) 
        #Paint the current moving bar red.
        if highlight_index is not None:
            colors[highlight_index] = '#FF204E' 
            

        # Find the minimum value. If it's negative, shift everything up.
        # We add +2 extra so the smallest bar isn't invisible.
        min_val = min(data)
        if min_val < 0:
            visual_heights = [x + abs(min_val) + 2 for x in data]
        else:
            visual_heights = data # If all positive, just use normal heights

        # Draw the bars
        bars = ax.bar(range(len(data)), visual_heights, color=colors, width=0.8)
        
        # Add Numbers to the bars
        for bar, real_value in zip(bars, data):
            ax.text(
                bar.get_x() + bar.get_width() / 2, 
                0.5,             # Position at bottom
                str(real_value), # Turn the number into a str so we can print it
                ha='center',     # Center the text horizontally
                va='bottom',     # Center the text vertically                    
                color='black',   
                fontweight='bold',
                fontsize=12
            )

        ax.axis('off')  #Remove the grid
        return fig

    #Logic of the app
    for i in range(1, len(array)):
        value = array[i]  
        j = i - 1         

        while j >= 0 and value < array[j]: 
            array[j+1] = array[j]
            array[j] = value 
            
            # Show the red bar moving
            yield draw_chart(array, highlight_index=j)
            #Slow down so the user can the output
            time.sleep(0.9) 
            
            j -= 1
        
        array[j+1] = value
            
    yield draw_chart(array) #repaint

  #The starting UI
with gr.Blocks() as demo:
    gr.Markdown("# Insertion Sort")
    
    inp = gr.Textbox(label="Enter Numbers")
    out = gr.Plot(label="Animation")
    btn = gr.Button("Sort", variant="primary")
    btn.click(fn=insertion_sort, inputs=inp, outputs=out)

demo.launch()
