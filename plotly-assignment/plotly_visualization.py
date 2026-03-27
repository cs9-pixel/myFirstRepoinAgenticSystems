# Import libraries
import pandas as pd
import plotly.express as px

# Step 1: Create dataset
epochs = list(range(1, 11))
training_loss = [0.9, 0.75, 0.6, 0.5, 0.42, 0.38, 0.35, 0.34, 0.33, 0.33]

# Step 2: Create DataFrame
df = pd.DataFrame({
    "Epoch": epochs,
    "Loss": training_loss
})

# Step 3: Create interactive line chart
fig = px.line(df, x="Epoch", y="Loss", title="Training Loss Over Epochs")

# Step 4: Add labels
fig.update_layout(
    xaxis_title="Epoch",
    yaxis_title="Training Loss"
)

# Step 5: Add annotation (where loss stabilizes)
fig.add_annotation(
    x=9,
    y=0.33,
    text="Loss Stabilizing",
    showarrow=True,
    arrowhead=2
)

# Step 6: Show chart
fig.show()
