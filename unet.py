# -*- coding:utf-8 -*-
from data import *

class myUnet(object):
    def __init__(self):
        self.old_best = 500
        self.val_loss = 500
        self.fail_counter = 0
        self.img_rows = 512
        self.img_cols = 512
        if snap == True:
            self.bands = 3
        else:
            self.bands = 2

    def get_unet(self):

        inputs = tf.keras.layers.Input((self.img_rows, self.img_cols, self.bands))
        conv1 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(inputs)
        conv1 = tf.keras.layers.BatchNormalization(trainable=True)(conv1)
        conv1 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv1)
        conv1 = tf.keras.layers.BatchNormalization(trainable=True)(conv1)
        pool1 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(conv1)

        conv2 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(pool1)
        conv2 = tf.keras.layers.BatchNormalization(trainable=True)(conv2)
        conv2 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv2)
        conv2 = tf.keras.layers.BatchNormalization(trainable=True)(conv2)
        drop2 = tf.keras.layers.Dropout(0.1)(conv2, training=True)
        pool2 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(drop2)

        conv3 = tf.keras.layers.Conv2D(256, 3, activation=activation, padding='same', kernel_initializer='he_normal')(pool2)
        conv3 = tf.keras.layers.BatchNormalization(trainable=True)(conv3)
        conv3 = tf.keras.layers.Conv2D(256, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv3)
        conv3 = tf.keras.layers.BatchNormalization(trainable=True)(conv3)
        drop3 = tf.keras.layers.Dropout(0.1)(conv3, training=True)
        pool3 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(drop3)

        conv4 = tf.keras.layers.Conv2D(512, 3, activation=activation, padding='same', kernel_initializer='he_normal')(pool3)
        conv4 = tf.keras.layers.BatchNormalization(trainable=True)(conv4)
        conv4 = tf.keras.layers.Conv2D(512, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv4)
        conv4 = tf.keras.layers.BatchNormalization(trainable=True)(conv4)
        drop4 = tf.keras.layers.Dropout(0.1)(conv4, training=True)
        pool4 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(drop4)

        conv5 = tf.keras.layers.Conv2D(1024, 3, activation=activation, padding='same', kernel_initializer='he_normal')(pool4)
        conv5 = tf.keras.layers.BatchNormalization(trainable=True)(conv5)
        conv5 = tf.keras.layers.Conv2D(1024, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv5)
        conv5 = tf.keras.layers.BatchNormalization(trainable=True)(conv5)
        drop5 = tf.keras.layers.Dropout(0.5)(conv5, training=True)

        up6 = tf.keras.layers.Conv2D(512, 2, activation=activation, padding='same', kernel_initializer='he_normal')(
            tf.keras.layers.UpSampling2D(size=(2, 2))(drop5))
        merge6 = tf.keras.layers.concatenate([drop4, up6], axis=3)

        conv6 = tf.keras.layers.Conv2D(512, 3, activation=activation, padding='same', kernel_initializer='he_normal')(merge6)
        conv6 = tf.keras.layers.BatchNormalization(trainable=True)(conv6)
        conv6 = tf.keras.layers.Conv2D(512, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv6)
        conv6 = tf.keras.layers.BatchNormalization(trainable=True)(conv6)
        drop6 = tf.keras.layers.Dropout(0.1)(conv6, training=True)

        up7 = tf.keras.layers.Conv2D(256, 2, activation=activation, padding='same', kernel_initializer='he_normal')(
            tf.keras.layers.UpSampling2D(size=(2, 2))(drop6))
        merge7 = tf.keras.layers.concatenate([drop3, up7], axis=3)

        conv7 = tf.keras.layers.Conv2D(256, 3, activation=activation, padding='same', kernel_initializer='he_normal')(merge7)
        conv7 = tf.keras.layers.BatchNormalization(trainable=True)(conv7)
        conv7 = tf.keras.layers.Conv2D(256, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv7)
        conv7 = tf.keras.layers.BatchNormalization(trainable=True)(conv7)
        drop7 = tf.keras.layers.Dropout(0.1)(conv7, training=True)

        up8 = tf.keras.layers.Conv2D(filters, 2, activation=activation, padding='same', kernel_initializer='he_normal')(
            tf.keras.layers.UpSampling2D(size=(2, 2))(drop7))
        merge8 = tf.keras.layers.concatenate([drop2, up8], axis=3)

        conv8 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(merge8)
        conv8 = tf.keras.layers.BatchNormalization(trainable=True)(conv8)
        conv8 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv8)
        conv8 = tf.keras.layers.BatchNormalization(trainable=True)(conv8)
        drop8 = tf.keras.layers.Dropout(0.1)(conv8, training=True)

        up9 = tf.keras.layers.Conv2D(filters, 2, activation=activation, padding='same', kernel_initializer='he_normal')(
            tf.keras.layers.UpSampling2D(size=(2, 2))(drop8))
        merge9 = tf.keras.layers.concatenate([conv1, up9], axis=3)

        conv9 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(merge9)
        conv9 = tf.keras.layers.BatchNormalization(trainable=True)(conv9)
        conv9 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv9)

        conv9 = tf.keras.layers.Conv2D(1, 3, activation=None, padding='same', kernel_initializer='he_normal')(conv9)

        conv10 = tf.keras.layers.Conv2D(1, 1, activation=None)(conv9)

        model = keras.models.Model(inputs=inputs, outputs=conv10)
        model.compile(optimizer=optimizer, loss=loss, metrics=[absolute_error, pred_max, pred_min])

        model.summary()
        return model

    def get_newnet(self):

        #512
        inputs = tf.keras.layers.Input((self.img_rows, self.img_cols, self.bands))
        conv1 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(inputs)
        conv1 = tf.keras.layers.BatchNormalization(trainable=True)(conv1)
        conv1 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv1)
        conv1 = tf.keras.layers.BatchNormalization(trainable=True)(conv1)
        pool1 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(conv1)

        #256
        conv2 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(pool1)
        conv2 = tf.keras.layers.BatchNormalization(trainable=True)(conv2)
        conv2 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv2)
        conv2 = tf.keras.layers.BatchNormalization(trainable=True)(conv2)
        conv2 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv2)
        conv2 = tf.keras.layers.BatchNormalization(trainable=True)(conv2)
        drop2 = tf.keras.layers.Dropout(0.1)(conv2, training=True)
        pool2 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(drop2)

        #filters
        conv3 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(pool2)
        conv3 = tf.keras.layers.BatchNormalization(trainable=True)(conv3)
        conv3 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv3)
        conv3 = tf.keras.layers.BatchNormalization(trainable=True)(conv3)
        conv3 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv3)
        conv3 = tf.keras.layers.BatchNormalization(trainable=True)(conv3)
        drop3 = tf.keras.layers.Dropout(0.1)(conv3, training=True)
        pool3 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(drop3)

        #filters
        conv4 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(pool3)
        conv4 = tf.keras.layers.BatchNormalization(trainable=True)(conv4)
        conv4 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv4)
        conv4 = tf.keras.layers.BatchNormalization(trainable=True)(conv4)
        conv4 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv4)
        conv4 = tf.keras.layers.BatchNormalization(trainable=True)(conv4)
        drop4 = tf.keras.layers.Dropout(0.1)(conv4, training=True)
        pool4 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(drop4)

        #32
        conv5 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(pool4)
        conv5 = tf.keras.layers.BatchNormalization(trainable=True)(conv5)
        conv5 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv5)
        conv5 = tf.keras.layers.BatchNormalization(trainable=True)(conv5)
        conv5 = tf.keras.layers.Conv2DTranspose(filters, 3, (2, 2), activation=activation, padding='same',
                                              kernel_initializer='he_normal')((conv5))
        conv5 = tf.keras.layers.BatchNormalization(trainable=True)(conv5)
        drop5 = tf.keras.layers.Dropout(0.5)(conv5, training=True)
        merge6 = tf.keras.layers.concatenate([drop4, drop5], axis=3)

        #filters
        conv6 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(merge6)
        conv6 = tf.keras.layers.BatchNormalization(trainable=True)(conv6)
        conv6 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv6)
        conv6 = tf.keras.layers.BatchNormalization(trainable=True)(conv6)
        conv6 = tf.keras.layers.Conv2DTranspose(filters, 3, (2, 2), activation=activation, padding='same',
                                                kernel_initializer='he_normal')((conv6))
        conv6 = tf.keras.layers.BatchNormalization(trainable=True)(conv6)
        drop6 = tf.keras.layers.Dropout(0.1)(conv6, training=True)

        #filters
        merge7 = tf.keras.layers.concatenate([drop3, drop6], axis=3)
        conv7 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(merge7)
        conv7 = tf.keras.layers.BatchNormalization(trainable=True)(conv7)
        conv7 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv7)
        conv7 = tf.keras.layers.BatchNormalization(trainable=True)(conv7)
        conv7 = tf.keras.layers.Conv2DTranspose(filters, 3, (2, 2), activation=activation, padding='same',
                                                kernel_initializer='he_normal')((conv7))
        conv7 = tf.keras.layers.BatchNormalization(trainable=True)(conv7)
        drop7 = tf.keras.layers.Dropout(0.1)(conv7, training=True)

        #256
        merge8 = tf.keras.layers.concatenate([drop2, drop7], axis=3)
        conv8 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(merge8)
        conv8 = tf.keras.layers.BatchNormalization(trainable=True)(conv8)
        conv8 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv8)
        conv8 = tf.keras.layers.BatchNormalization(trainable=True)(conv8)
        conv8 = tf.keras.layers.Conv2DTranspose(filters, 3, (2, 2), activation=activation, padding='same',
                                                kernel_initializer='he_normal')((conv8))
        conv8 = tf.keras.layers.BatchNormalization(trainable=True)(conv8)
        drop8 = tf.keras.layers.Dropout(0.1)(conv8, training=True)

        #512
        merge9 = tf.keras.layers.concatenate([conv1, drop8], axis=3)
        conv9 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(merge9)
        conv9 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv9)
        conv9 = tf.keras.layers.Conv2D(filters, 3, activation=activation, padding='same', kernel_initializer='he_normal')(conv9)
        conv9 = tf.keras.layers.Conv2D(1, 3, activation=None, padding='same', kernel_initializer='he_normal')(conv9)
        conv10 = tf.keras.layers.Conv2D(1, 1, activation=None)(conv9)

        model = keras.models.Model(inputs=inputs, outputs=conv10)
        model.compile(optimizer=optimizer, loss=loss, metrics=[absolute_error, pred_max, pred_min])

        model.summary()
        return model

    def get_batch(self, timex_dataset, train_flag):

        if train_flag == 'train':
            imgdatas = np.ndarray((batch_size, self.img_rows, self.img_cols, self.bands), dtype=np.float32)
            imglabels = np.ndarray((batch_size, self.img_rows, self.img_cols, 1), dtype=np.float32)
            for j in range(batch_size):
                random_index = np.random.uniform(0, len(timex_dataset)-(.1*len(timex_dataset)))
                random_index = int(random_index)
                sample = timex_dataset[random_index]
                sample['label'] = np.expand_dims(sample['label'], axis=-1)
                imgdatas[j] = sample['image']
                imglabels[j] = sample['label']
        if train_flag == 'val':
            imgdatas = np.ndarray((val_size, self.img_rows, self.img_cols, self.bands), dtype=np.float32)
            imglabels = np.ndarray((val_size, self.img_rows, self.img_cols, 1), dtype=np.float32)
            for j in range(val_size):
                random_index = np.random.uniform(len(timex_dataset)-val_size, len(timex_dataset))
                random_index = int(random_index)
                sample = timex_dataset[random_index]
                sample['label'] = np.expand_dims(sample['label'], axis=-1)
                imgdatas[j] = sample['image']
                imglabels[j] = sample['label']
        if train_flag == 'test':
            imgdatas = np.ndarray((test_size, self.img_rows, self.img_cols, self.bands), dtype=np.float32)
            imglabels = np.ndarray((test_size, self.img_rows, self.img_cols, 1), dtype=np.float32)
            l = 0
            t = 0
            while l < cuts:
                j = 0
                while j < test_set_length:
                    random_index = j + test_id_offset
                    #random_index = np.random.uniform(0, test_size)
                    sample = timex_dataset[random_index]
                    sample['label'] = np.expand_dims(sample['label'], axis=-1)
                    """if j % 100 == 0:
                        image = sample['image']
                        label = sample['label']
                        print(l)
                        print(j)
                        fig = plt.figure()
                        X = np.linspace(0, img_cols, img_cols)
                        Y = np.linspace(0, img_rows, img_rows)
                        cs_labels = ["-8m", "-7.5m", "-7m", "-6.5m", "-6m", "-5.5m", "-5m", "-4.5m", "-4m", "-3.5m",
                                     "-3m", "-2.5m", "-2m", "-1.5m", "-1m", "-.5m", "0m"]
                        fmt = {}
                        for f, s in zip(
                                [-8, -7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -.5, -.01],
                                cs_labels):
                            fmt[f] = s
                        ax0 = fig.add_subplot(1, 2, 1), plt.imshow(image[0, :, :img_cols, 0])
                        cs = ax0[0].contour(X, Y, np.where(label[:, :img_cols, 0] > .1, 0, label[:, :img_cols, 0]), vmin=-6,
                                            vmax=2, alpha=.5,
                                            colors=['white', 'white', 'white', 'white', 'white', 'white', 'white',
                                                    'white', 'white', 'white', 'white', 'white', 'white', 'white',
                                                    'white', 'white', 'black'],
                                            levels=[-8, -7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2,
                                                    -1.5, -1, -.5, -.01],
                                            linestyles=['solid', 'dashed', 'solid', 'dashed', 'solid', 'dashed',
                                                        'solid', 'dashed', 'solid', 'dashed', 'solid', 'dashed',
                                                        'solid', 'dashed', 'solid', 'dashed', 'solid'],
                                            linewidths=[1.5, .5, 1.5, .5, 1.5, .5, 1.5, .5, 1.5, .5, 1.5, .5, 1.5, .5,
                                                        1.5, .5, 2])
                        ax0[0].clabel(cs,
                                      [-8, -7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -.5,
                                       -.01], fmt=fmt, inline_spacing=2, fontsize='small', )
                        ax1 = fig.add_subplot(1, 2, 2), plt.imshow(label[:, :img_cols, 0], cmap='gist_earth', vmin=-6,
                                                                   vmax=1)
                        cs = ax1[0].contour(X, Y, np.where(label[:, :img_cols, 0] > .1, 0, label[:, :img_cols, 0]), vmin=-6,
                                            vmax=2, alpha=1,
                                            colors=['white', 'white', 'white', 'white', 'white', 'white', 'white',
                                                    'white', 'white', 'white', 'white', 'white', 'white', 'white',
                                                    'white', 'white', 'black'],
                                            levels=[-8, -7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2,
                                                    -1.5, -1, -.5, -.01],
                                            linestyles=['solid', 'dashed', 'solid', 'dashed', 'solid', 'dashed',
                                                        'solid', 'dashed', 'solid', 'dashed', 'solid', 'dashed',
                                                        'solid', 'dashed', 'solid', 'dashed', 'solid'],
                                            linewidths=[1.5, .5, 1.5, .5, 1.5, .5, 1.5, .5, 1.5, .5, 1.5, .5, 1.5, .5,
                                                        1.5, .5, 2])
                        ax1[0].clabel(cs,
                                      [-8, -7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -.5,
                                       -.01], fmt=fmt, inline_spacing=2, fontsize='small', )
                        plt.show()"""
                    imgdatas[t] = sample['image']
                    imglabels[t] = sample['label']
                    j+=1
                    t+=1
                l = l + 1

        return imgdatas, imglabels

    def load_model(self):
        try:
            my_model = keras.models.load_model('./results/'+ name+ 'iter.h5', custom_objects={
                'absolute_error': absolute_error,
                'pred_max': pred_max,
                'pred_min': pred_min,})
            print("loaded chk")
        except:
            my_model = self.get_newnet()
            print("couldnt load chk")
        i=0
        if __name__ == '__main__':
            if args.finetune:
                for layer in my_model.layers:
                    if i >= 34:
                        continue
                    layer.trainable = False
                    i=i+1
                    print(i, layer.name)
                my_model.compile(optimizer=optimizer, loss=loss, metrics=[absolute_error, pred_max, pred_min,])
                tf.keras.backend.set_value(my_model.optimizer.lr, .00001)
                print("New LR for finetuning: " + str(tf.keras.backend.get_value(my_model.optimizer.lr)))

        my_model.summary()
        return my_model

    def validate(self, epoch, timex_dataset, model):
        val_train, val_mask_train = self.get_batch(timex_dataset, train_flag='val')
        val_history = model.evaluate(val_train, val_mask_train, verbose=1, batch_size=10)
        self.val_loss = float(val_history[0])
        writer = tf.summary.create_file_writer(logs_path)
        with writer.as_default():
            tf.summary.scalar("Val_Loss", val_history[0], step=1)
        writer.flush()
        if self.val_loss < self.old_best:
            print(str(self.old_best) + ' was the old best val_loss. ' + str(
                self.val_loss) + ' is the new best val loss!')
            self.old_best = self.val_loss
            model.save('./results/'+ name+ 'val_loss.h5', overwrite=True)
            self.fail_counter = 0
        else:
            self.fail_counter += 1
            print("val better fails in a row: " + str(self.fail_counter))
            if self.fail_counter % 1 == 0:
                print("val loss failed to improve 1 epochs in a row")
                print("Current LR: " + str(model.optimizer.lr) + "reducing learning rate by 1%")
                # yo this actually works and carries the lr across load models!
                tf.keras.backend.set_value(model.optimizer.lr, model.optimizer.lr * .99)
                print("New LR: " + str(tf.keras.backend.get_value(model.loss)))

    def train(self):
        timex_dataset = TimexDataset(Dataset)
        model = self.load_model()
        loss = []
        #train model for an epoch
        self.validate(0, timex_dataset, model)
        for epoch in range(epoch_no):
            print(epoch)
            epoch_mean_loss = []
            writer = tf.summary.create_file_writer(logs_path)
            for i in range(int((len(timex_dataset)-val_size) / batch_size)):
                imgdatas, imglabels = self.get_batch(timex_dataset, train_flag='train')
                train_history = model.train_on_batch(imgdatas, imglabels)
                epoch_mean_loss = np.append(epoch_mean_loss, train_history[0])
                with writer.as_default():
                    tf.summary.scalar("Loss", train_history[0], step=i)
                    tf.summary.scalar("Absolute Loss", train_history[1], step=i)
                    tf.summary.scalar("LR", model.optimizer.lr, step=i)
                print("Batch " + str(i) + "/" + str((len(timex_dataset)-val_size)/batch_size) +
                    " Loss: " + str(train_history[0]) + 
                    " Absolute: " + str(train_history[1]) + 
                    " Max: " + str(train_history[2]) + 
                    " Min: " + str(train_history[3]))
            print(" Epoch Loss: " + str(np.mean(epoch_mean_loss)))
            writer.flush()
            loss = np.append(loss, train_history)
            model.save('./results/'+ name+ 'iter.h5', overwrite=True)
            self.validate(epoch, timex_dataset, model)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-ft', '--finetune', action='store_true',
                        help="print full stats and uncertainty of test set with N passes")

    args = parser.parse_args()
    myunet = myUnet()
    myunet.train()
