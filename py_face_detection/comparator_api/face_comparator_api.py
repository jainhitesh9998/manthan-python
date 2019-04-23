from threading import Thread
import cv2
import imutils
import numpy as np

from py_tensorflow_runner.session_utils import SessionRunner
from py_face_detection.facenet_api.face_embeddings_api import FNEmbeddingsGenerator
from py_face_detection.mtcnn_api.face_detector_api import FaceDetectorMTCNN

session_runner = SessionRunner()

generator = FNEmbeddingsGenerator()
generator.use_threading()
generator_ip = generator.get_in_pipe()
generator_op = generator.get_out_pipe()
generator.use_session_runner(session_runner)
session_runner.start()
generator.run()

detector = FaceDetectorMTCNN()
detector.use_threading()
detector_ip = detector.get_in_pipe()
detector_op = detector.get_out_pipe()
detector.use_session_runner(session_runner)
session_runner.start()
detector.run()

cap = cv2.VideoCapture(-1)
tj = [[2.23548692e-02, 5.77721037e-02, 4.61106636e-02, 4.53545293e-03,
            -3.74390837e-03, -1.32961553e-02, -3.12063415e-02, 7.66125023e-02,
            -1.32210078e-02, -2.90533323e-02, -2.63388120e-02, 1.28994407e-02,
            -6.29901215e-02, -2.11355742e-02, -1.57538266e-03, 1.36568556e-02,
            -2.49111727e-02, 4.16561514e-02, -2.63515841e-02, 6.04607798e-02,
            -7.18228146e-02, 5.74262626e-03, -3.55179869e-02, 2.23863460e-02,
            2.57176403e-02, 9.32490528e-02, -5.27182743e-02, -2.27406211e-02,
            -5.73287392e-03, -2.97082234e-02, -1.38547532e-02, 7.24130422e-02,
            -6.41347840e-02, 3.43024060e-02, 1.82470232e-02, 6.39981776e-02,
            6.09304640e-04, -8.48823413e-03, 3.15180942e-02, -3.48445103e-02,
            4.47011180e-02, -4.87530529e-02, -2.73970794e-02, 3.73562537e-02,
            -3.10523212e-02, 8.43791850e-03, -4.75900620e-02, -1.74047947e-02,
            1.15768248e-02, 1.46074779e-02, 3.97459194e-02, -7.06442967e-02,
            -1.33801030e-03, 2.93418765e-03, 8.87346268e-02, 6.78246766e-02,
            1.91893410e-02, 3.65162008e-02, -4.33763675e-02, -4.60666269e-02,
            5.29050529e-02, -2.10028049e-02, 2.97191963e-02, -8.01478997e-02,
            6.98358193e-02, -7.49527384e-03, -4.03643139e-02, 2.12984197e-02,
            -8.42759609e-02, 9.11785010e-03, 1.49886170e-02, -3.98369543e-02,
            -8.54999125e-02, -4.61268388e-02, -2.17927434e-02, 3.16310748e-02,
            1.77744497e-02, 2.60734092e-02, 1.80165637e-02, 9.67958942e-03,
            7.59374176e-04, 7.43685886e-02, -9.25391614e-02, -2.80897338e-02,
            -5.74475750e-02, -3.00814901e-02, 1.99671797e-02, 2.44216248e-02,
            -5.87709658e-02, 1.42747918e-02, 5.04111964e-03, 8.79119486e-02,
            -1.89078841e-02, -4.85766008e-02, 2.80019492e-02, 1.47860041e-02,
            5.76025918e-02, 1.68160740e-02, 3.11499573e-02, -6.88605681e-02,
            1.71392821e-02, 3.48988883e-02, 1.49817904e-02, 3.70170884e-02,
            4.60740663e-02, 1.04603566e-01, 2.35754959e-02, 7.37056732e-02,
            -5.48564680e-02, -2.93816067e-02, -1.97927207e-02, -2.26056054e-02,
            9.28073376e-02, 5.83724864e-02, 6.59428537e-03, -3.28663923e-02,
            -4.22723629e-02, 4.40966226e-02, -2.28345450e-02, 2.70202756e-02,
            -5.76677099e-02, 2.02970803e-02, 1.62888132e-02, 6.08108379e-02,
            1.02491617e-01, -9.93115082e-03, 2.63020750e-02, -1.66967679e-02,
            4.11572233e-02, 9.61303059e-03, 2.46421676e-02, -3.54528576e-02,
            7.83233941e-02, -2.71899272e-02, 7.22401869e-03, 3.51428986e-02,
            -4.69564833e-02, -6.03046343e-02, 1.81792118e-02, -2.50823144e-02,
            -8.08840543e-02, -8.00452605e-02, 2.59925611e-02, 7.30456337e-02,
            1.27549330e-02, -1.37884002e-02, 1.91791877e-02, 1.58020090e-02,
            -2.26361994e-02, 3.59580778e-02, -2.48411689e-02, 4.10666689e-02,
            2.94203721e-02, 3.64924669e-02, -8.26925486e-02, -4.50222706e-03,
            5.35612702e-02, 2.66882181e-02, 7.89120235e-03, -3.17796133e-02,
            1.03085496e-01, -6.45913258e-02, -2.08701603e-02, -1.34310825e-03,
            1.20093795e-02, -3.73504348e-02, -3.65281478e-02, -1.06196487e-02,
            2.26116925e-02, -9.25054774e-02, -3.05850506e-02, 8.53107721e-02,
            3.90893407e-02, 3.22171859e-02, -9.78427590e-04, -3.99058014e-02,
            -3.66063267e-02, 5.39528839e-02, -7.41102733e-03, 3.44507024e-02,
            8.93437564e-02, 1.00932218e-01, 4.00462896e-02, 4.43643853e-02,
            -4.00687084e-02, 1.04765622e-02, 2.87067704e-02, -6.52471557e-02,
            -2.50039492e-02, 1.23383533e-02, 8.23538303e-02, -9.09731761e-02,
            -3.10136378e-02, 5.61834089e-02, 8.72212742e-03, -1.27186300e-02,
            3.79166864e-02, 1.94913372e-02, -1.71868559e-02, -4.41405289e-02,
            -1.25173414e-02, -5.14625153e-03, -3.04158498e-02, 3.35797593e-02,
            1.26740173e-01, 2.47171298e-02, -7.55879679e-04, -6.60942867e-02,
            2.15464402e-02, 5.78211583e-02, 4.80994806e-02, 1.36718936e-02,
            2.16772823e-04, -6.07637735e-03, -1.17208302e-01, 7.11914105e-03,
            -3.52427810e-02, -7.42146000e-02, -7.92546198e-02, 5.18831499e-02,
            -1.01093436e-02, -3.73735763e-02, 1.82559267e-02, 5.46565466e-03,
            -1.98831391e-02, -3.34370248e-02, -9.98747349e-02, 8.89318585e-02,
            -2.47723721e-02, -3.00440900e-02, -1.00092918e-01, 4.26355517e-03,
            -1.05457762e-02, -2.79833507e-02, -2.36600507e-02, 3.10411546e-02,
            -2.88139954e-02, 2.16043391e-03, -6.98332069e-03, -2.35085525e-02,
            1.13573140e-02, 5.38893789e-02, 4.16231677e-02, 2.91680731e-03,
            -1.43448068e-02, 2.20122114e-02, 2.99991644e-03, 6.98511228e-02,
            -6.07472472e-03, -7.30403513e-02, 2.74565034e-02, -6.64447099e-02,
            -2.31508948e-02, 4.60245181e-03, 2.45241746e-02, -2.47655567e-02,
            -3.24330442e-02, 2.04077158e-02, -2.36261860e-02, -2.18466111e-02,
            1.70448497e-02, 1.99973360e-02, 6.41374500e-04, -2.84430292e-02,
            4.22013700e-02, -5.53579628e-03, -4.20934930e-02, 7.55495057e-02,
            3.83567698e-02, 5.15369400e-02, 5.79874776e-03, -3.16267945e-02,
            -5.03619611e-02, -3.50381657e-02, -4.01582532e-02, 6.40168563e-02,
            2.55335066e-02, 3.66544500e-02, -5.19502796e-02, 2.32840683e-02,
            2.38887519e-02, -8.68443307e-03, 2.07877997e-02, 3.95019613e-02,
            7.30604108e-04, 4.13419865e-02, -1.46194380e-02, -3.93039547e-02,
            -8.27763975e-02, -3.90869594e-04, -1.91931762e-02, -4.84004356e-02,
            1.45250037e-02, -4.96953353e-02, -5.28015606e-02, -1.56055549e-02,
            -1.95131712e-02, 3.49977538e-02, 2.22846977e-02, -2.61137355e-02,
            4.69080061e-02, 1.05957929e-02, 1.07487086e-02, 2.54529994e-04,
            -1.34187629e-02, -3.66036035e-02, -6.47042915e-02, 4.41298373e-02,
            7.55677819e-02, 6.91088266e-04, 9.28881988e-02, -4.12919670e-02,
            -8.61179084e-02, -2.96015274e-02, -1.37375174e-02, -5.25181331e-02,
            -7.19553307e-02, -5.15588969e-02, 1.75609495e-02, 1.47803323e-02,
            5.27690314e-02, 1.55185750e-02, -1.78004671e-02, 2.01209113e-02,
            -4.55548838e-02, -6.37974665e-02, -1.19348094e-02, 7.16634002e-03,
            4.07415964e-02, 6.55718371e-02, -1.68393236e-02, -3.97121087e-02,
            -2.94531044e-02, 6.42537475e-02, -6.71269447e-02, 1.89322922e-02,
            2.59297192e-02, -4.04554717e-02, -5.35308160e-02, -1.08788125e-02,
            2.57867053e-02, 6.40599523e-03, 1.70911942e-03, 3.55555415e-02,
            -8.32390264e-02, -3.77982147e-02, 4.59720828e-02, -1.26752043e-02,
            2.70726066e-02, 3.44592482e-02, 6.50878623e-02, -2.17928179e-02,
            9.77999158e-03, -2.00967286e-02, -4.12449613e-03, 1.36079211e-02,
            1.64541882e-03, -4.81888317e-02, 8.33331198e-02, -3.05843540e-02,
            -4.40664962e-02, 2.49853358e-02, 4.62490991e-02, 1.41332084e-02,
            -2.18486004e-02, -2.48905085e-02, 2.29562912e-02, -7.37780929e-02,
            1.47116100e-02, 2.45891046e-02, 1.83617510e-02, -6.85683340e-02,
            3.61693688e-02, 1.00151852e-01, -7.34628886e-02, 6.17242269e-02,
            5.49817309e-02, 1.95741821e-02, 2.77388860e-02, 3.78557332e-02,
            -2.00547166e-02, -1.17639191e-02, 1.94162782e-02, 3.38962325e-03,
            1.61679164e-02, 7.25301802e-02, -5.73767759e-02, 6.28688112e-02,
            8.47159177e-02, -1.48947919e-02, -8.62418115e-02, 2.21579242e-02,
            -3.03084613e-04, -6.33068848e-03, 1.68742845e-03, 5.03492123e-03,
            -3.14508267e-02, 3.57932113e-02, -1.77485030e-02, 1.01713486e-01,
            7.66298594e-03, 6.64628223e-02, 7.99929202e-02, -2.61246059e-02,
            -4.76968847e-03, 4.84447293e-02, 2.10749600e-02, -7.43388140e-04,
            7.27116168e-02, 6.56829652e-05, -5.31959198e-02, 6.90778717e-02,
            -3.57031226e-02, 1.64057910e-02, -9.48393159e-03, -2.05648690e-02,
            -4.83636260e-02, -1.10076956e-01, 2.32240390e-02, 3.05575300e-02,
            2.95266975e-02, -5.97071946e-02, -4.45711575e-02, -4.84542595e-03,
            -6.54420722e-03, -3.52052599e-02, -5.70358709e-03, -3.79948206e-02,
            1.87376756e-02, -6.43242747e-02, -3.45047452e-02, -4.32016887e-02,
            1.21703614e-02, -4.83682901e-02, 5.06115481e-02, -5.25021665e-02,
            1.43073881e-02, 2.99212374e-02, -2.66657537e-03, -3.85100953e-02,
            9.93809626e-02, -8.67454708e-03, 1.11378163e-01, -1.10122249e-01,
            -3.49238031e-02, -7.21529722e-02, 4.01850641e-02, -1.84274418e-03,
            -1.14254374e-02, -2.92739496e-02, 5.68821914e-02, -5.66952415e-02,
            9.25681833e-03, -3.96256289e-03, 2.80046295e-02, -6.77813292e-02,
            -4.60554957e-02, 1.30924331e-02, -7.29192570e-02, 7.67614618e-02,
            4.75514084e-02, -8.64221901e-03, 1.81962028e-02, -1.42256049e-02,
            3.96576226e-02, -1.52998166e-02, -8.35621133e-02, 1.15105032e-03,
            -4.13638614e-02, -4.73559238e-02, -5.10173067e-02, -9.74637363e-03,
            2.56087705e-02, -4.44743149e-02, 7.51362229e-03, 2.30588894e-02,
            6.93093985e-04, 4.00245190e-02, -1.18196220e-03, 9.87473503e-02,
            -6.77237436e-02, 7.53682107e-03, -6.42902032e-02, -6.52946206e-03,
            8.43799263e-02, 1.14359958e-02, -2.99284533e-02, 6.85750544e-02,
            4.40615043e-02, -4.20022644e-02, 1.00476980e-01, -2.76962537e-02,
            1.24714719e-02, 3.76618430e-02, 1.79980714e-02, 4.45620157e-02,
            8.61868355e-03, 7.82059729e-02, 5.61006293e-02, 8.27737432e-03,
            1.99089311e-02, 6.45592436e-03, 2.01086532e-02, 1.44403270e-02,
            1.31199723e-02, 2.93658883e-03, -1.42480638e-02, -2.33084504e-02,
            2.24296264e-02, 3.54810692e-02, -6.06880849e-03, 1.64817479e-02]]




def step_1():
    while True:
        detector_ip.push_wait()
        ret, image = cap.read()
        if not ret:
            continue
        image = imutils.resize(image, width=1080)
        inference = FaceDetectorMTCNN.Inference(image)
        detector_ip.push(inference)


def step_2():
    while True:
        generator_ip.push_wait()
        detector_op.pull_wait()
        ret, inference = detector_op.pull(True)
        if ret:
            faces = inference.get_result()
            if faces:
                face_image = faces[0]['face']
                inference = FNEmbeddingsGenerator.Inference(input=face_image)
                generator_ip.push(inference)


def step_3():
    while True:
        generator_op.pull_wait()
        ret, inference = generator_op.pull(True)
        if ret:
            embedding = inference.get_result()
            face = inference.get_input()
            # cv2.imshow("face", face)
            # cv2.waitKey(1)
            # print(embedding)
            dist = np.sqrt(np.sum(np.square(np.subtract(embedding, tj))))





Thread(target=step_1).start()
Thread(target=step_2).start()
Thread(target=step_3).start()
