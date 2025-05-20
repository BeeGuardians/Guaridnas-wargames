FROM php:8.2-apache

# Apache가 8000 포트로 리스닝하도록 설정 변경
RUN sed -i 's/80/8000/' /etc/apache2/ports.conf \
 && sed -i 's/:80/:8000/' /etc/apache2/sites-available/000-default.conf

# uploads 디렉토리 생성 및 권한 설정
RUN mkdir /var/www/html/uploads \
 && chown -R www-data:www-data /var/www/html/uploads \
 && chmod 755 /var/www/html/uploads

# 업로드 페이지 및 플래그 복사
COPY index.php /var/www/html/index.php
COPY upload.php /var/www/html/upload.php
COPY flag.txt /var/www/html/flag.txt

# 플래그 읽기 전용
RUN chmod 444 /var/www/html/flag.txt

# 컨테이너 포트 공개
EXPOSE 8000
