# TEE PELI TÄHÄN
import pygame
import numpy as np
from noise import pnoise2, snoise2
import math
import base64
import zipfile
from io import BytesIO

# base64 zip tiedosto spriteille. 3x golffari ja lippu
zippi = str("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")

class kartta():
    def __init__(self, leveys: int, korkeus: int):
        self._leveys = leveys
        self._korkeus = korkeus

        self.luo_korkeuskartta()
        self.luo_varianssikartta()
        self.uusi_lippu()

    @property
    def leveys(self):
        return self._leveys

    @property
    def korkeus(self):
        return self._korkeus

    @property
    def lippu_paikka(self):
        return (self._lippu_x, self._lippu_y)

    @property
    def lippu_x(self):
        return self._lippu_x

    @property
    def lippu_y(self):
        return self._lippu_y

    def uusi_lippu(self):
        self._lippu_x = np.random.randint(0, self._leveys)
        self._lippu_y = np.random.randint(0, self._korkeus)

    def value(self, coords:tuple):
        return max(self._korkeuskartta[coords[1], coords[0]], 0.2) # 0.2 = piirretään tasainen vesi

    def luo_korkeuskartta(self, scale:float=100):
        korkeuskartta = np.zeros((self._korkeus, self._leveys))
        for y in range(self._korkeus):
            for x in range(self._leveys):
                korkeuskartta[y][x] = pnoise2(x / scale, y / scale, octaves=6, persistence=0.5, lacunarity=2.0, repeatx=self._leveys, repeaty=self._korkeus, base=42)
        self._korkeuskartta = (korkeuskartta - np.min(korkeuskartta)) / (np.max(korkeuskartta) - np.min(korkeuskartta))

    def luo_varianssikartta(self, scale:float=0.1):
        self._varianssi = np.zeros((self._korkeus, self._leveys))
        for y in range(self._korkeus):
            for x in range(self._leveys):
                noise = snoise2(x * scale, y * scale, octaves=1)
                self._varianssi[y][x] = int(noise * 10)  # 0..10 varianssi 

    def kartan_vari(self, arvo:float, coords:tuple):
        varianssi = self._varianssi[coords[1], coords[0]]

        if arvo <= 0.2:
            return [0, 0, 128]  # Vesi
        elif arvo < 0.4:
            return [244 + varianssi, 164 + varianssi, 96 + varianssi]  # Hiekka
        elif arvo < 0.6:
            return [34 + varianssi, 139 + varianssi, 34 + varianssi]  # väylä
        elif arvo < 0.8:
            return [24 + varianssi, 119 + varianssi, 19 + varianssi]  # rifruff
        else:
            return [139 + varianssi, 69 + varianssi, 19 + varianssi]  # dirt

class spritet():
    def __init__(self, ziptiedosto:str):
        zip_file = BytesIO(base64.b64decode(ziptiedosto))
        self._golffari = []
        with zipfile.ZipFile(zip_file, 'r') as z:
            self._lippu_sprite = pygame.transform.scale(pygame.image.load(BytesIO(z.read("lippu2.png"))), (28, 48))
            self._golffari.append(pygame.transform.scale(pygame.image.load(BytesIO(z.read("golffaaja1.png"))), (132, 256)))
            self._golffari.append(pygame.transform.scale(pygame.image.load(BytesIO(z.read("golffaaja2.png"))), (132, 256)))
            self._golffari.append(pygame.transform.scale(pygame.image.load(BytesIO(z.read("golffaaja3.png"))), (132, 256)))

    @property
    def lippu_sprite(self):
        return self._lippu_sprite

    def golffari(self, index:int):
        return self._golffari[index]
    
    @property
    def golffari_max_index(self):
        return len(self._golffari)

class golfviewport():
    def __init__(self, koko:tuple=None):

        if koko is None:
            self._koko = (640, 480)
        else:
            self._koko = koko

        self._rendaus_array = np.full((self._koko[1], self._koko[0], 3), [135, 206, 235])
        self._terrain_surface = pygame.surfarray.make_surface(np.transpose(self._rendaus_array, (1, 0, 2)).astype(np.uint8))
        self._screen = pygame.display.set_mode(self._koko)

        self._font = pygame.font.Font(None, 74)
        self._small_font = pygame.font.Font(None, 30)
        self._small_font2 = pygame.font.Font(None, 36)
        self._text = self._font.render("Yhden holen golf course!", True, (0, 0, 0))
        self._subtext = self._small_font.render("Paina välilyönti aloittaaksesi pelin", True, (0, 0, 0))
        self._ohjeet = self._small_font.render("Nuoli vasen/oikea kääntää lyöntisuuntaa", True, (0, 0, 0))
        self._ohjeet2 = self._small_font.render("Nuoli alaspäin lyö", True, (0, 0, 0))
        self._ohjeet3 = self._small_font.render("Tavoitteena on osua kentällä lipulla merkittyyn paikkaan", True, (0, 0, 0))
        self._text_rect = self._text.get_rect(center=(self._koko[0] / 2, self._koko[1] / 2 - 100))
        self._subtext_rect = self._subtext.get_rect(center=(self._koko[0] / 2, self._koko[1] / 2 - 50))
        self._ohjeet_rect = self._ohjeet.get_rect(center=(self._koko[0] / 2, self._koko[1] / 2))
        self._ohjeet2_rect = self._ohjeet2.get_rect(center=(self._koko[0] / 2, self._koko[1] / 2 + 50))
        self._ohjeet3_rect = self._ohjeet3.get_rect(center=(self._koko[0] / 2, self._koko[1] / 2 + 100))
        self._subtext2 = self._small_font2.render("Paina välilyönti palataksesi alkunäyttöön", True, (0, 0, 0))

    @property
    def koko(self):
        return self._koko

    def alkuruutu(self):
        self._screen.fill((135, 206, 235))  # taivas tausta
        self._screen.blit(self._text, self._text_rect)
        self._screen.blit(self._subtext, self._subtext_rect)
        self._screen.blit(self._ohjeet, self._ohjeet_rect)
        self._screen.blit(self._ohjeet2, self._ohjeet2_rect)
        self._screen.blit(self._ohjeet3, self._ohjeet3_rect)
        pygame.display.flip()

    def lopetusruutu(self, voitto, lyonnit):
        if voitto:
            text = self._font.render("Voitit pelin!", True, (0, 0, 0))
            hits_text = self._small_font2.render(f"Lyönnit: {lyonnit}", True, (0, 0, 0))
        else:
            text = self._font.render("Hävisit pelin!", True, (0, 0, 0))
            hits_text = self._small_font2.render("", True, (0, 0, 0))  # Ei näytetä lyöntejä hävitessä
        self._screen.fill((135, 206, 235))  # taivas tausta

        text_rect = text.get_rect(center=(self._koko[0] / 2, self._koko[1] / 2 - 50))
        hits_text_rect = hits_text.get_rect(center=(self._koko[0] / 2, self._koko[1] / 2))
        subtext_rect = self._subtext2.get_rect(center=(self._koko[0] / 2, self._koko[1] / 2 + 50))
        self._screen.blit(text, text_rect)
        self._screen.blit(hits_text, hits_text_rect)
        self._screen.blit(self._subtext2, subtext_rect)
        pygame.display.flip()

    def piirra_maailma(self, greeni, sprite, maxz, direction, pointy2):
        self._rendaus_array[:] = [135, 206, 235]  # taivas tausta

        # ruudun x suunta, 0.2 skaala tuo 'ok' perspektiivin
        perp_vector = np.array([-direction[1], direction[0]])
        perp_vector /= np.linalg.norm(perp_vector)
        perp_vector *= 0.2

        piirtopuskuri = []
        lippu_screen_x, lippu_screen_y = None, None
        target_scale = 1.0

        for x in range(self._koko[0]):
            # thispoint ruudun x suhteen alareunassa
            thispoint = np.array([pointy2[0] + perp_vector[0] * (x - self._koko[0] / 2),
                                pointy2[1] + perp_vector[1] * (x - self._koko[0] / 2)])

            maxheight = self._koko[1]

            for z in range(maxz):
                thispoint += direction
                coords = tuple(map(int, thispoint))

                if not (0 <= coords[0] < greeni.leveys and 0 <= coords[1] < greeni.korkeus):
                    continue

                value = greeni.value(coords)

                # experimentaalisti löydetyt taikavakiot projektiota varten, korkeus pidetään yli 0
                height = max(int((((1 - value) * 32768 + 12288) * 1 / (50 + z * 3))), 0)

                # laitetaanko lipun paikka talteen
                if coords == greeni.lippu_paikka:
                    lippu_screen_x = x
                    lippu_screen_y = height
                    distance = math.dist(coords, pointy2)
                    target_scale = max(0.5, min(4.0, 400 / (distance*2 + 1)))

                # tarviiko tämä kierros piirtää?
                if height < maxheight:
                    color = greeni.kartan_vari(value, coords)
                    piirtopuskuri.append((x, height, maxheight, color))
                    maxheight = height

        # piirrä maasto
        for x, height, maxheight, color in piirtopuskuri:
            self._rendaus_array[height:maxheight, x] = color

        # käännä kuva oikein päin ja piirrä surface
        pygame.surfarray.blit_array(self._terrain_surface, np.transpose(self._rendaus_array, (1, 0, 2)).astype(np.uint8))

        # jos löytyi lipun paikka piirretään se lippu
        if lippu_screen_x is not None and lippu_screen_y is not None:
            scaled_sprite = pygame.transform.scale(sprite.lippu_sprite, (int(sprite.lippu_sprite.get_width() * target_scale), int(sprite.lippu_sprite.get_height() * target_scale)))
            self._terrain_surface.blit(scaled_sprite, (lippu_screen_x - scaled_sprite.get_width() // 2, lippu_screen_y - scaled_sprite.get_height()))

    def palauta_terrain(self):
        self._screen.blit(self._terrain_surface, (0, 0))

    def pikku_kartta(self, greeni, camera_x, camera_y, angle):
        pikkukartta_koko = 128
        surface = pygame.Surface((pikkukartta_koko, pikkukartta_koko))
        surface.fill((50, 50, 50))

        # Pelaaja
        player_x = int((camera_x / greeni.leveys) * pikkukartta_koko)
        player_y = int((camera_y / greeni.korkeus) * pikkukartta_koko)
        pygame.draw.circle(surface, (255, 0, 0), (player_x, player_y), 5)

        # suunta
        direction_x = player_x + int(20 * math.cos(math.radians(angle - 90)))
        direction_y = player_y + int(20 * math.sin(math.radians(angle - 90)))
        pygame.draw.line(surface, (255, 255, 255), (player_x, player_y), (direction_x, direction_y), 2)

        # lippu
        lippu_map_x = int((greeni.lippu_x / greeni.leveys) * pikkukartta_koko)
        lippu_map_y = int((greeni.lippu_y / greeni.korkeus) * pikkukartta_koko)
        pygame.draw.circle(surface, (0, 255, 0), (lippu_map_x, lippu_map_y), 5)

        self._screen.blit(surface, (self._koko[0] - pikkukartta_koko - 10, 10))
        
    def voima_ja_lyonnit(self, swing_power:int):
        pygame.draw.rect(self._screen, (0, 255, 0), (10, self._koko[1] - 30, swing_power, 20))
        pygame.draw.rect(self._screen, (0, 0, 0), (10, self._koko[1] - 30, 100, 20), 2)
        font = pygame.font.Font(None, 36)
        text = font.render(f"Lyönnit: {lyonnit}", True, (0, 0, 0))
        self._screen.blit(text, (10, self._koko[1] - 60))

    def piirra_sprite(self, sprite, pos:tuple=None):
        if sprite is not None:
            self._screen.blit(sprite, (self._koko[0] // 2 - sprite.get_width() // 2, self._koko[1] - sprite.get_height()))
        else:
            pygame.draw.circle(self._screen, (255, 255, 255), pos, 5)

# Tästä lähtee!
pygame.init()
sprite = spritet(zippi)

# parametrit
maxz = 100 # maksimi piirtoetäisyys
move_speed = 5
camera_x, camera_y = 128, 128 # golffaajan paikka
angle = 180  # aloitus katselukulma
pointy2 = np.array([0, 0])

clock = pygame.time.Clock()
kuva = golfviewport()
greeni = kartta(1024, 1024)

# Pelin muuttujat
swing_power = 0
swinging = False
max_swing_power = 100
ball_pos = [camera_x, camera_y]
ball_moving = False
ball_velocity = [0, 0]
ball_initial_pos = [kuva.koko[0] // 2 + 60, kuva.koko[1] - 20]  # Alustava pallon sijainti golffarin vieressä
ball_animation_frames = 30  # n framet pallon lennolle
ball_animation_count = 0  # laskuri pallon lennolle
golffari_frame = 1  # default golffarin kuva
golffari_frame_viive = 0  # viive golffarin animaatiolle
lyonnit = 0  # lyönnit

# Pelin tilat
peli_kaynnissa = False
game_over = False
peli_voitto = False

kuva.alkuruutu()

running = True
tarviipiirtaa = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not peli_kaynnissa:
                # Alusta peli
                camera_x, camera_y = 128, 128
                greeni.uusi_lippu()
                ball_pos = [camera_x, camera_y]

                lyonnit = 0
                swing_power = 0
                swinging = False
                ball_moving = False
                game_over = False
                peli_voitto = False
                golffari_frame = 1
                peli_kaynnissa = True
                tarviipiirtaa = True
                angle = 135

    if peli_kaynnissa and not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not swinging and not ball_moving:
            angle -= 2
            tarviipiirtaa = True
        if keys[pygame.K_RIGHT] and not swinging and not ball_moving:
            angle += 2  
            tarviipiirtaa = True
        if keys[pygame.K_DOWN]:
            swinging = True
            swing_power = min(swing_power + 5, max_swing_power)
        if not keys[pygame.K_DOWN] and swinging:
            swinging = False
            ball_moving = True
            ball_animation_count = 0  # Animaation laskurin nollaus
            ball_initial_pos = [kuva.koko[0] // 2 + 60, kuva.koko[1] - 20]  # Alku pallon sijainti golffarin vieressä
            rad_angle = math.radians(angle)
            power_factor = swing_power / max_swing_power
            ball_velocity = [power_factor * 220 * direction[0], -power_factor * 10, power_factor * 220 * direction[1]]
            swing_power = 0
            golffari_frame = 0  # aloita swing animaatio
            golffari_frame_viive = 5  # viive framet
            lyonnit += 1  # lyöntien laskuri

        if ball_moving:
            if ball_animation_count < ball_animation_frames:
                if golffari_frame > 0:
                    ball_animation_count += 1
                    t = ball_animation_count / ball_animation_frames
                    ball_initial_pos[0] += ball_velocity[0] / ball_animation_frames
                    ball_initial_pos[1] += (ball_velocity[1] * t * (1 - t)) * 10  # pallon lentorata ruudulla
            else:
                ball_moving = False
                ball_pos[0] += ball_velocity[0]
                ball_pos[1] += ball_velocity[2]
                camera_x, camera_y = ball_pos  # Siirrä pelaaja pallon uuteen sijaintiin
                golffari_frame = 1  # Palauta oletus golffari kuvaaan
                ball_initial_pos = [kuva.koko[0] // 2 + 60, kuva.koko[1] - 20]  # Pallo mailaan

                # Tarkista, osuuko pallo reikään
                distance_to_flag = math.sqrt((ball_pos[0] - greeni.lippu_x) ** 2 + (ball_pos[1] - greeni.lippu_y) ** 2)
                if distance_to_flag <= 25:
                    peli_voitto = True
                    game_over = True
                    peli_kaynnissa = False
                elif ball_pos[0] < 0 or ball_pos[0] >= greeni.leveys or ball_pos[1] < 0 or ball_pos[1] >= greeni.korkeus:
                    peli_voitto = False
                    game_over = True
                    peli_kaynnissa = False

            tarviipiirtaa = True

        if golffari_frame_viive > 0:
            golffari_frame_viive -= 1
            if golffari_frame_viive == 0 and golffari_frame < sprite.golffari_max_index - 1:
                golffari_frame += 1
                golffari_frame_viive = 5  # Nollaa viive seuraavaa kuvaa varten

        if tarviipiirtaa:
            # suunta kameran kulmasta
            rad = angle * math.pi / 180
            direction = np.array([ 1.5 * math.sin(rad), -1.5 * math.cos(rad)])
            direction /= np.linalg.norm(direction)

            kuva.piirra_maailma(greeni, sprite, maxz, direction, np.array([camera_x, camera_y]))
            tarviipiirtaa = False

        # piirrä kaikki ruutuun
        kuva.palauta_terrain()
        kuva.pikku_kartta(greeni, camera_x, camera_y, angle)
        kuva.piirra_sprite(None, (int(ball_initial_pos[0]), int(ball_initial_pos[1])))
        kuva.piirra_sprite(sprite.golffari(golffari_frame))
        kuva.voima_ja_lyonnit(swing_power)
        pygame.display.flip()
    
        # kello, jos kone sattuisi olemaan liian nopea..
        clock.tick(30)
    
    if game_over:
        kuva.lopetusruutu(voitto=peli_voitto, lyonnit=lyonnit)
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_over = False
                    kuva.alkuruutu()

pygame.quit()
