
FROM node:21-bookworm-slim as base



# パッケージ更新
RUN apt-get update \
    && apt-get clean \
    && apt-get autoclean \ 
    && apt-get autoremove --purge -y \
    && apt-get install -y git less vim sudo
# && rm -rf /var/lib/apt/lists/*


FROM base as main

# 設定情報
ARG USERNAME=dev
ARG GROUPNAME=dev
ARG UID=1001
ARG GID=1001
ARG WORKDIR=/usr/src/app/frontend
ARG MNTDIR=/usr/src/mnt

# ユーザー追加
RUN groupadd -g $GID $GROUPNAME && \
    # useradd -m -s /bin/bash -u $UID -g $GID $USERNAME  && \
    useradd --uid $UID  -g $GID -s /bin/bash -G sudo,root $USERNAME && \
    # usermod -aG sudo $USERNAME && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers


# フォルダ作成＆管理者設定
RUN mkdir -p $WORKDIR && chown -R $UID:$GID $WORKDIR \
    && mkdir -p $MNTDIR && chown -R $UID:$GID $MNTDIR \
    && mkdir -p /home/$USERNAME && chown -R $UID:$GID /home/$USERNAME \ 
    && mkdir -p $WORKDIR/node_modules && chown -R $UID:$GID $WORKDIR/node_modules

# ボリュームマウントすると owner が root になってしまう対策
# RUN mkdir node_modules && \
#     chown node:node node_modules

# USER node:node

WORKDIR $WORKDIR
USER $USERNAME
# RUN npm install

# ユーザー切り替え
# USER $USERNAME

# 作業ディレクトリ設定
WORKDIR $WORKDIR


# CMD ["sudo",  "npm", "run" ,"dev" ]