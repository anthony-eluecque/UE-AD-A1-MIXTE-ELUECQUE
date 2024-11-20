
# UE-AD-A1-MIXTE-ELUECQUE

Projet réalisé dans le cadre de ma première année à l'IMT Atlantique en architecture distribuée

## Authors

- [@anthony-eluecque](https://www.github.com/anthony-eluecque)

## Pré-requis

- Docker
- Insomnia ou Postman ou équivalent.
- Pour un environnement locale, python >= 3.10


## Déploiment du projet

⚠️ Il est important d'ajouter des .env dans les dossiers suivants : 
Exemple de .env à ajouter pour configurer le projet
### - User 

```env
MOVIE_CLIENT = "http://movie:3001"
BOOKING_CLIENT = "booking:3003"
```

### - Booking 

```env
SHOWTIME_CLIENT = "showtime:3002"
```

Puis exécuter le script qui permet de lancer le projet

```bash
  ./start.bat
```
P.S : Tout est automatiquement configuré pour vous



## Fonctionnalités clées ajoutées 

- User

| Méthode | Description              | URL d'accès         |
|---------|--------------------------|---------------------|
| GET     |  Page d'accueil                       | http://localhost:3203/                    |
| GET    |  Récupérer l'utilisateur depuis son id                         | http://localhost:3203/{user_id}                    |
| GET     | Récupérer la liste des réservations d'un utilisateur                         | http://localhost:3203/{user_id}/bookings                    |
| GET  |  Récupérer la liste détaillés des réservations avec le détail de chaque film pour un utilisateur                         |  http://localhost:3203/{user_id}/bookings/{date}/movies                   |
| POST  | Créer une nouvelle réservation pour un utilisateur                          |  http://localhost:3203/{user_id}/bookings                   |



- Booking

| Méthode | Description              | Méthode         |
|---------|--------------------------|---------------------|
| gRPC     |  Récupérer les réservations depuis l'id de l'utilisateur                         |             /Booking/GetBookingFromUserId        |
| gRPC    |  Récupérer toutes les réservations                        |             /Booking/GetBookings        |
| gRPC    |  Ajouter une nouvelle réservation                        |             /Booking/AddBookingByUser        |

- Showtime

| Méthode | Description              | Méthode         |
|---------|--------------------------|---------------------|
| gRPC     |  Récupérer la date de diffusion                         |             /ShowTime/GetShowTimeByDate        |
| gRPC    |  Récupérer toutes les dates de diffusions                        |             /ShowTime/GetShowTimes        |

- Movie

Une seule route est disponible pour cette API :

POST http://127.0.0.1:3001/graphql (voir les fichiers .graphql)

## Modifications apportés supplémentaires

- Système de .env pour faciliter le déploiement dans un environnement de prod ou locale

- Architecture revisité pour chaque micro services afin de rendre le code + maintenable et + lisible (Orienté objet)