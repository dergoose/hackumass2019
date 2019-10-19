import json
import ffmpeg

def lambda_handler(event, context):
    # TODO implement
    (
    ffmpeg
    .input('/path/to/jpegs/*.jpg', pattern_type='glob', framerate=25)
    .output('movie.mp4')
    .run()
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
