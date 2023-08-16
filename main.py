import array
import cmd_parser.command_manager as cm
import inventory.contents as inventory
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class GameState(BaseModel):
    Command: str
    Place: str
    Story: str | None = None
    Image: str | None = None
    Inventory: list


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"Command": "", "Place": "Forest", "Story": "You are in the Forest. To the north is the castle. To the south is the cave",
            "Image": "images/forest.png", "Inventory": []}


@app.post("/")
async def root(game_state: GameState):
    print(game_state)

    if game_state.Command == '' and game_state.Place == "Forest":
        return {"Command": "", "Place": "Forest", "Story": "You are in the Forest. To the north is the castle. To the south is the cave",
                "Image": "images/forest.png", "Inventory": []}
    else:
        # Set the game state
        cm.game_state = game_state.Place
        # Use our inventory
        for item in game_state.Inventory:
            inventory.collect_item(item)
        # Get the story
        story = cm.game_play(game_state.Command)
        # Inventory is updated by all_inventory

        return {"Command": "", "Place": cm.game_state, "Story": story, "Image": "images/"+cm.game_places[cm.game_state]
                ['Image'], "Inventory": inventory.all_inventory()}
