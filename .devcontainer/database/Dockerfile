FROM python:3.9-bookworm as builder

# パッケージ更新
RUN apt-get update \
    && apt-get clean \
    && apt-get autoclean \
    && apt-get autoremove --purge  -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

FROM python:3.9-slim-bookworm
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib /usr/local/lib
COPY --from=builder /usr/local/include /usr/local/include

# 設定情報(UID,GIDについてはidコマンドでdockerの実行ユーザーと合わせた方がよい)
ARG USERNAME=pyuser
ARG GROUPNAME=pyuser
ARG UID=1000
ARG GID=1000
ARG WORKDIR=/usr/src/app
ARG MNTDIR=/usr/src/mnt

# ユーザー追加
RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME 

# フォルダ作成＆管理者設定
RUN mkdir -p $WORKDIR && chown -R $UID:$GID $WORKDIR \
    && mkdir -p $MNTDIR && chown -R $UID:$GID $MNTDIR

# ユーザーのbinaryディレクトリをパスに追加
ENV PATH /home/$USERNAME/.local/bin:$PATH

# ユーザー切り替え
USER $USERNAME

# 作業ディレクトリ設定
WORKDIR $WORKDIR


