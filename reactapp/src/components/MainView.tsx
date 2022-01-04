import React, {Component} from 'react';
import {Button, Card, CardActions, CardContent, Grid, Typography} from "@mui/material";

export interface MainViewProps {
}

export interface MainViewState {

}

class MainView extends Component<MainViewProps, MainViewState> {


    render() {
        return (
            <div>
                <Grid
                    container
                    spacing={0}
                    direction="column"
                    alignItems="center"
                    justifyContent="center"
                    style={{minHeight: '100vh',backgroundColor:'#1e1e1e'}}>
                    <Card sx={{width: 275,height: 575,backgroundColor:'#0a1929'}}>
                        <CardContent>
                        </CardContent>
                        <CardActions>
                            <Button size="small">Learn More</Button>
                        </CardActions>
                    </Card>
                </Grid>

            </div>
        );
    }


}

export default MainView;