
-- Tabla de USUARIOS
-- =================
CREATE TABLE usuarios (
    usuario_id  INTEGER PRIMARY KEY,
    nombre      varchar NOT NULL,
    contraseña  varchar NOT NULL
);

-- Tabla de COMUNIDADES
-- ====================
CREATE TABLE comunidades (
    comunidad_id    INTEGER PRIMARY KEY,
    nombre          varchar NOT NULL,
    direc_social    varchar NOT NULL,
    fecha_creacion  date NOT NULL,
    creador_id      INTEGER NOT NULL,
    organizador_id  INTEGER NOT NULL,
    otros_datos     varchar NOT NULL,
    FOREIGN KEY (creador_id)
      REFERENCES usuarios (user_id),
    FOREIGN KEY (organizador_id)
      REFERENCES usuarios (user_id)
);

-- Tabla de EVENTOS
-- ================
CREATE TABLE eventos (
    evento_id     INTEGER PRIMARY KEY,
    nombre        varchar NOT NULL,
    descripcion   varchar NOT NULL,
    comunidad_id  INTEGER NOT NULL,
    fecha         date NOT NULL,
    FOREIGN KEY (comunidad_id)
      REFERENCES comunidades (comunidad_id)
);

-- Tabla de MIEMBROS_COMUNIDAD
-- ===========================
CREATE TABLE miembros_comunidad (
    comunidad_id  INTEGER NOT NULL,
    miembro_id    INTEGER NOT NULL,
    PRIMARY KEY (comunidad_id, usuario_id),
    FOREIGN KEY (comunidad_id)
      REFERENCES comunidades (comunidad_id),
    FOREIGN KEY (miembro_id)
      REFERENCES usuarios (user_id)
);

-- Tabla de ASISTENTES_EVENTOS
-- ===========================
CREATE TABLE asistentes_eventos (
    aistente_id INTEGER PRIMARY KEY,
    evento_id   INTEGER PRIMARY KEY,
    PRIMARY KEY (aistente_id, evento_id),
    FOREIGN KEY (aistente_id)
      REFERENCES usuarios (user_id),
    FOREIGN KEY (evento_id)
      REFERENCES eventos (evento_id)
);

