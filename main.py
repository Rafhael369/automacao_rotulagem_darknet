import argparse
import asone
from asone import ASOne
from modificado.variables_fixes import *
from modificado.rotular import *

i, x = 0, 0

def main(args):
    global i, x
    filter_classes = args.filter_classes

    if filter_classes:
        filter_classes = [filter_classes]

    dt_obj = ASOne(
        tracker=asone.BYTETRACK,
        detector=asone.YOLOV7_PYTORCH,
        weights=args.weights,
        use_cuda=args.use_cuda
        )
    # Get tracking function
    track_fn = dt_obj.track_video(args.video_path,
                                output_dir=args.output_dir,
                                save_result=args.save_result,
                                display=args.display,
                                draw_trails=args.draw_trails,
                                filter_classes=filter_classes,
                                class_names=None) # class_names=['License Plate'] for custom weights
    
    # Loop over track_fn to retrieve outputs of each frame 
    for bbox_details, frame_details in track_fn:
        bbox_xyxy, ids, scores, class_ids = bbox_details
        frame, frame_num, fps = frame_details
        print(frame_num)

        organizar(i, x, frame, class_ids, bbox_xyxy, filter_classes, caminho_carro_imagem, caminho_carro_voc, caminho_carro_yolo, id_carro)
        i += 1
        x += 1
        if x == 51:
            x = 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('video_path', help='Path to input video')
    parser.add_argument('--cpu', default=True, action='store_false', dest='use_cuda',
                        help='run on cpu if not provided the program will run on gpu.')
    parser.add_argument('--no_save', default=False, action='store_false',
                        dest='save_result', help='whether or not save results')
    parser.add_argument('--no_display', default=True, action='store_false',
                        dest='display', help='whether or not display results on screen')
    parser.add_argument('--output_dir', default='data/results',  help='Path to output directory')
    parser.add_argument('--draw_trails', action='store_true', default=False,
                        help='if provided object motion trails will be drawn.')
    parser.add_argument('--filter_classes', default=None, help='Filter class name')
    parser.add_argument('-w', '--weights', default=None, help='Path of trained weights')

    args = parser.parse_args()

    main(args)
