-- Member
create table members_contact
(
    id                integer      not null
        primary key autoincrement,
    name              varchar(36)  not null,
    email             varchar(254) not null,
    phone             varchar(20)  not null,
    profile_image_url varchar(200),
    company           varchar(32),
    position          varchar(16),
    memo              text,
    address           text,
    birthday          date,
    website           varchar(256),
    created_at        datetime     not null,
    updated_at        datetime     not null
);

create index members_con_email_834d33_idx
    on members_contact (email);

create index members_con_name_811096_idx
    on members_contact (name);

create index members_con_phone_e234d2_idx
    on members_contact (phone);


-- Label
create table members_label
(
    id    integer     not null
        primary key autoincrement,
    label varchar(20) not null
);


-- Member-Label through table
create table members_contact_labels
(
    id         integer not null
        primary key autoincrement,
    contact_id bigint  not null
        references members_contact
            deferrable initially deferred,
    label_id   bigint  not null
        references members_label
            deferrable initially deferred
);

create index members_contact_labels_contact_id_d9d9af85
    on members_contact_labels (contact_id);

create unique index members_contact_labels_contact_id_label_id_9c4e1758_uniq
    on members_contact_labels (contact_id, label_id);

create index members_contact_labels_label_id_2909def7
    on members_contact_labels (label_id);

