import yt_dlp
import os
import time

PASTA_BASE = "Musicas Baixadas"
ARQUIVO_LOCK = ".downloader.lock"

def encontrar_e_bloquear_pasta():
    """
    Encontra a primeira pasta 'Musicas Baixadas' (ou Musicas Baixadas X) que não 
    possui um arquivo de bloqueio e o cria, garantindo o uso exclusivo.
    """
    contador = 1
    while True:
        if contador == 1:
            pasta_atual = PASTA_BASE
        else:
            pasta_atual = f"{PASTA_BASE} {contador}"

        caminho_lock = os.path.join(pasta_atual, ARQUIVO_LOCK)

        if not os.path.exists(caminho_lock):
            print(f"Pasta '{pasta_atual}' está livre. Iniciando download aqui.")
            os.makedirs(pasta_atual, exist_ok=True)
            with open(caminho_lock, 'w') as f:
                f.write('locked')
            return pasta_atual, caminho_lock
        else:
            print(f"Pasta '{pasta_atual}' está em uso. Verificando a próxima...")
            contador += 1
            time.sleep(0.1)

def baixar_musicas(url):
    pasta_saida = None
    caminho_lock = None
    
    try:
        pasta_saida, caminho_lock = encontrar_e_bloquear_pasta()

        print(f"Iniciando download de: {url}")
        print("-" * 30)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            # Garante que o yt-dlp não falhe ao tentar renomear/salvar o arquivo temporário
            'outtmpl': {
                'default': os.path.join(pasta_saida, '%(title)s.%(ext)s'),
            },
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'ignoreerrors': True,
            'verbose': False,
            'quiet': False,
            
            # --- OPÇÕES DE ROBUSTEZ (Para resolver HTTP 403 Forbidden) ---
            # 1. Usa o arquivo de cookies para autenticação (RESOLUÇÃO PRINCIPAL)
            # Requer que o arquivo 'youtube_cookies.txt' esteja na mesma pasta do script
            'cookiefile': './youtube_cookies.txt',
            
            # 2. Tenta forçar o uso do manifesto DASH para uma abordagem de streaming mais robusta
            'youtube_include_dash_manifest': True,

            # 3. Limita a velocidade de download (comportamento humano)
            'ratelimit': 10000000,
            
            # 4. Faz pausas entre os downloads de playlist (comportamento humano)
            'sleep_interval': 5,
            'max_sleep_interval': 10,
        }
        # Nota: 'outtmpl' foi ligeiramente ajustado para o formato de dicionário preferido pelo yt-dlp moderno.

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("-" * 30)
        print(f"Download concluído! Músicas salvas em '{pasta_saida}'")

    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")
    
    finally:
        # Garante que a pasta seja liberada
        if caminho_lock and os.path.exists(caminho_lock):
            os.remove(caminho_lock)
            print(f"Processo finalizado. Pasta '{pasta_saida}' liberada.")

if __name__ == '__main__':
    print("Bem-vindo ao Music Downloader para DJs! (Versão Multi-Download)")
    print("Cole um link do YouTube ou SoundCloud (música ou playlist) e pressione Enter.")
    print("\n⚠️  Se o download falhar com erro 403, verifique se o arquivo 'youtube_cookies.txt' está atualizado e na mesma pasta.")
    
    link_usuario = input("Link: ")

    if "youtube.com" in link_usuario or "soundcloud.com" in link_usuario:
        baixar_musicas(link_usuario)
    else:
        print("URL inválida. Por favor, insira um link do YouTube ou SoundCloud.")