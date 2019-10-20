import React from 'react';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import './Website.css';

//var shell = require('shelljs');


const useStyles = makeStyles(theme => ({
  container: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  button: {
    margin: theme.spacing(1),
  },
  input: {
    margin: theme.spacing(1),
  },
}));

export default function Inputs() {
  const classes = useStyles();
  return (
    <div className={classes.container}>
      <AppBar position="static" >
        <Toolbar className={classes.toolbar}>
          <Typography 
              className={classes.title} variant="h5" noWrap
              style = {{margin: "0 auto"}}>
            SpaceLapse
          </Typography>
        </Toolbar>
      </AppBar>

      <iframe className = "frame" src="https://drive.google.com/file/d/1GwCH3ymJQUVm7JH06cqqcQi3KL-FTXrz/preview"></iframe>
{/* 
      <video id='my-video' className='video-js' controls autoPlay={true} preload='auto' width='auto' height='500'
        poster='MY_VIDEO_POSTER.jpg' data-setup='{}'  style = {{margin: "auto" }}>
        <source src='/mainvideo.mp4' type='video/mp4'/>
        <p className='vjs-no-js'>
          To view this video please enable JavaScript, and consider upgrading to a web browser that
          <a href='https://videojs.com/html5-video-support/' target='_blank'>supports HTML5 video</a>
        </p>
      </video>
      <script src='https://vjs.zencdn.net/7.6.5/video.js'></script>  */}
      
      <Input
        id="q1"
        placeholder="How long is your time lapse (seconds)"
        style = {{width:"100%", height:'50px', paddingTop: '5px'}}
        className={classes.input}
        inputProps={{
          'aria-label': 'description',
        }}
      />
      <Input
        id="q2"
        placeholder="Enter how long your interval is (greater than 2)"
        style = {{width:"100%", height:'50px'}}
        className={classes.input}
        inputProps={{
          'aria-label': 'description',
        }}
      />
      <Button
        variant="contained"
        color="primary"
        className={classes.button}
        style = {{margin: "0 auto"}}
      >
        Submit
      </Button>
    </div>

    
  
  );
}
