/*
 Navicat Premium Data Transfer

 Source Server         : mysql_localbase
 Source Server Type    : MySQL
 Source Server Version : 100322
 Source Host           : localhost:3306
 Source Schema         : bot_different_utilities

 Target Server Type    : MySQL
 Target Server Version : 100322
 File Encoding         : 65001

 Date: 14/07/2021 12:25:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;


CREATE DATABASE bot_different_utilities;
USE bot_different_utilities;

-- ----------------------------
-- Table structure for botmessages
-- ----------------------------
DROP TABLE IF EXISTS `botmessages`;
CREATE TABLE `botmessages`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `lang_id` int NOT NULL,
  `text` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `botmessages_lang_id`(`lang_id`) USING BTREE,
  CONSTRAINT `botmessages_ibfk_1` FOREIGN KEY (`lang_id`) REFERENCES `languages` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 81 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of botmessages
-- ----------------------------
INSERT INTO `botmessages` VALUES (1, 'get_lang', 1, '👅 Выберите удобный для вас язык');
INSERT INTO `botmessages` VALUES (2, 'get_lang', 2, '👅 Choose your prefferred language');
INSERT INTO `botmessages` VALUES (3, 'choise_from_key', 1, '😖 Выберите из <b>представленных</b> значений');
INSERT INTO `botmessages` VALUES (4, 'choise_from_key', 2, '😖 Choise from the <b>buttons</b>');
INSERT INTO `botmessages` VALUES (5, 'success_set_lang', 1, '😊 Язык <b>успешно</b> установлен');
INSERT INTO `botmessages` VALUES (6, 'success_set_lang', 2, '😊 Language <b>successfully</b> installed');
INSERT INTO `botmessages` VALUES (7, 'password_generator', 1, '🔑 Пароли');
INSERT INTO `botmessages` VALUES (8, 'password_generator', 2, '🔑 Passwords');
INSERT INTO `botmessages` VALUES (9, 'main_menu', 1, '🗂 Вы в главном меню');
INSERT INTO `botmessages` VALUES (10, 'main_menu', 2, '🗂 You are in main menu');
INSERT INTO `botmessages` VALUES (11, 'create_password', 1, '🎲 Сгенерировать пароль');
INSERT INTO `botmessages` VALUES (12, 'create_password', 2, '🎲 Generate password');
INSERT INTO `botmessages` VALUES (13, 'main_settings', 1, '⚙️ Настройки');
INSERT INTO `botmessages` VALUES (14, 'main_settings', 2, '⚙️ Settings');
INSERT INTO `botmessages` VALUES (15, 'language', 1, '👅 Язык');
INSERT INTO `botmessages` VALUES (16, 'language', 2, '👅 Language');
INSERT INTO `botmessages` VALUES (17, 'settings', 1, '⚙️ Вы в настройках');
INSERT INTO `botmessages` VALUES (18, 'settings', 2, '⚙️ You are in settings menu');
INSERT INTO `botmessages` VALUES (19, 'back', 1, '◀️ Назад');
INSERT INTO `botmessages` VALUES (20, 'back', 2, '◀️ Back');
INSERT INTO `botmessages` VALUES (21, 'check_passwords', 1, '👁 Посмотреть сохраненные пароли');
INSERT INTO `botmessages` VALUES (22, 'check_passwords', 2, '👁 Check saved passwords');
INSERT INTO `botmessages` VALUES (23, 'passwords', 1, '🔑 Вы в меню паролей');
INSERT INTO `botmessages` VALUES (24, 'passwords', 2, '🔑 You are in passwords menu');
INSERT INTO `botmessages` VALUES (25, 'to_main_menu', 1, '🗂 Главное меню');
INSERT INTO `botmessages` VALUES (26, 'to_main_menu', 2, '🗂 Main menu');
INSERT INTO `botmessages` VALUES (27, 'generate_password', 1, '🔑 Пароли');
INSERT INTO `botmessages` VALUES (28, 'generate_password', 2, '🔑 Passwords');
INSERT INTO `botmessages` VALUES (29, 'main_menu', 1, '🗂 Вы в главном меню');
INSERT INTO `botmessages` VALUES (30, 'main_menu', 2, '🗂 You are in main menu');
INSERT INTO `botmessages` VALUES (31, 'get_pass_len', 1, '📏 Введите длину генерируемого пароля (она может быть от 8 до 501) или выберите нужный вариант из предложенных.\\nИмейте ввиду, некоторые проекты не поддерживают пароли более чем 32 или 64 символа например');
INSERT INTO `botmessages` VALUES (32, 'get_pass_len', 2, '📏 Enter length of the generated password (it can be from 8 to 501) or select the desired option from the proposed.\\nPlease note that some projects do not support passwords longer than 32 or 64 characters for example');
INSERT INTO `botmessages` VALUES (33, 'len_not_in_range', 1, '😖 Введите <b>число в диапазоне от</b> <u>8</u> <b>до</b> <u>501</u>');
INSERT INTO `botmessages` VALUES (34, 'len_not_in_range', 2, '😖 Input <b>number in range from</b> <u>8</u> <b>to</b> <u>501</u>');
INSERT INTO `botmessages` VALUES (35, 'len_not_a_number', 1, '😖 Введите <b>число</b>');
INSERT INTO `botmessages` VALUES (36, 'len_not_a_number', 2, '😖 Input <b>number</b>');
INSERT INTO `botmessages` VALUES (37, 'with_cyr_and_lat', 1, '🔤 Использовать ли в пароле латиницу И <b>кириллицу</b> (не только английские но и русские буквы)? Некоторые проекты не поддерживают <b>кириллицу</b>.');
INSERT INTO `botmessages` VALUES (38, 'with_cyr_and_lat', 2, '🔤 Should I use Latin AND <b>Cyrillic</b> (not only English but also Russian letters) in the password? Some projects do not support <b>Cyrillic</b>.');
INSERT INTO `botmessages` VALUES (39, 'use_cyr', 1, 'Использовать кириллицу');
INSERT INTO `botmessages` VALUES (40, 'use_cyr', 2, 'Use Cyrillic');
INSERT INTO `botmessages` VALUES (41, 'no_cyr', 1, 'Не использовать кириллицу');
INSERT INTO `botmessages` VALUES (42, 'no_cyr', 2, 'Do not use Cyrillic');
INSERT INTO `botmessages` VALUES (43, 'with_spec', 1, '🔣 Использовать ли <b>специальные</b> (такие как #, ?, `, и так далее) символы? (Некоторые проекты не поддерживают специальные символы)');
INSERT INTO `botmessages` VALUES (44, 'with_spec', 2, '🔣 Should I use <b>special</b> (such as #, ?, `, and other) characters? (Some projects do not support special characters)');
INSERT INTO `botmessages` VALUES (45, 'use_spec', 1, 'Использовать спец. символы');
INSERT INTO `botmessages` VALUES (46, 'use_spec', 2, 'Use special symbols');
INSERT INTO `botmessages` VALUES (47, 'no_spec', 1, 'Не использовать спец. символы');
INSERT INTO `botmessages` VALUES (48, 'no_spec', 2, 'Do not use special symbols');
INSERT INTO `botmessages` VALUES (49, 'wanna_save', 1, '🧠 Хотите чтоб бот запомнил пароль?');
INSERT INTO `botmessages` VALUES (50, 'wanna_save', 2, '🧠 Do you want the bot to remember the password?');
INSERT INTO `botmessages` VALUES (51, 'do_save', 1, '✅ Запомнить');
INSERT INTO `botmessages` VALUES (52, 'do_save', 2, '✅ Save');
INSERT INTO `botmessages` VALUES (53, 'not_save', 1, '🚫 Просто сгенерировать');
INSERT INTO `botmessages` VALUES (54, 'not_save', 2, '🚫 Just generate');
INSERT INTO `botmessages` VALUES (55, 'password_was_created', 1, '✅ <b>Сгенерированный пароль: </b><code>\\t\\t{}</code>\\n\\n🔥 Это сообщение будет удалено через 10 секунд.');
INSERT INTO `botmessages` VALUES (56, 'password_was_created', 2, '✅ <b>Generated password: </b><code>\\t\\t{}</code>\\n\\n🔥 This message will be delete after 10 seconds.');
INSERT INTO `botmessages` VALUES (57, 'password_title', 1, '🔠 Введите название пароля (для быстрого поиска нужного пароля из общего вашего общего списка паролей)');
INSERT INTO `botmessages` VALUES (58, 'password_title', 2, '🔠 Input password title (for quick search from you passwords list)');
INSERT INTO `botmessages` VALUES (59, 'generate_key', 1, '🔑 <b>Ваш ключ для дешифровки пароля</b>:\\n\\n<code>{}</code>\\n\\n ⚠️ <b><u>Пожалуйста</u></b>, запишите его куда-нибудь и <b><u>не потеряйте</u></b>.\\nЭтот ключ нужен для получения созданных и сохраненных вами паролей в будущем.\\n🔥 Это сообщение будет удалено через 30 секунд.');
INSERT INTO `botmessages` VALUES (60, 'generate_key', 2, '🔑 <b>Your key to decrypt the password</b>:\\n\\n<code>{}</code>\\n\\n ⚠️ <b><u>Please</u></b>, write it down somewhere and <b><u>do not lose</u></b>.\\nThis key is needed to retrieve the passwords you created and saved in the future.\\n🔥 This message will be deleted after 30 seconds.');
INSERT INTO `botmessages` VALUES (61, 'get_pass_titles', 1, '🤔 <b>Выберите нужный пароль</b>');
INSERT INTO `botmessages` VALUES (62, 'get_pass_titles', 2, '🤔 <b>Choose need password</b>');
INSERT INTO `botmessages` VALUES (63, 'input_priv_key', 1, '🔑 <b>Введите приватный ключ</b>');
INSERT INTO `botmessages` VALUES (64, 'input_priv_key', 2, '🔑 <b>Input private key</b>');
INSERT INTO `botmessages` VALUES (65, 'error_in_getting_pass', 1, '😖 При получении пароля произошла <b>ошибка</b>.');
INSERT INTO `botmessages` VALUES (66, 'error_in_getting_pass', 2, '😖 <b>Error</b> occurred while retrieving the password.');
INSERT INTO `botmessages` VALUES (67, 'print_password', 1, '😊 <b>Ваш пароль:</b> <code>{}</code>\r\n\r\n🔥 Это сообщение будет удалено через 10 секунд.');
INSERT INTO `botmessages` VALUES (68, 'print_password', 2, '😊 <b>Your password:</b> <code>{}</code>\r\n\r\n🔥 This message will be deleted after 10 seconds.');
INSERT INTO `botmessages` VALUES (69, 'not_valid_key', 1, '😖 Неправильный ключ.');
INSERT INTO `botmessages` VALUES (70, 'not_valid_key', 2, '😖 Not valid key.');
INSERT INTO `botmessages` VALUES (71, 'security_key_gen', 1, '🔑 Генерация защитных ключей, подождите пожалуйста ...');
INSERT INTO `botmessages` VALUES (72, 'security_key_gen', 2, '🔑 Generation of security keys, please wait ...');
INSERT INTO `botmessages` VALUES (73, 'len_not_in_range', 1, '😖 Введите <b>число в диапазоне от</b> <u>8</u> <b>до</b> <u>501</u>');
INSERT INTO `botmessages` VALUES (74, 'len_not_in_range', 2, '😖 Input <b>number in range from</b> <u>8</u> <b>to</b> <u>501</u>');
INSERT INTO `botmessages` VALUES (75, 'len_not_a_number', 1, '😖 Введите <b>число</b>');
INSERT INTO `botmessages` VALUES (76, 'len_not_a_number', 2, '😖 Input <b>number</b>');
INSERT INTO `botmessages` VALUES (77, 'with_cyr_and_lat', 1, '🔤 Использовать ли в пароле латиницу И <b>кириллицу</b> (не только английские но и русские буквы)? Некоторые проекты не поддерживают <b>кириллицу</b>.');
INSERT INTO `botmessages` VALUES (78, 'with_cyr_and_lat', 2, '🔤 Should I use Latin AND <b>Cyrillic</b> (not only English but also Russian letters) in the password? Some projects do not support <b>Cyrillic</b>.');
INSERT INTO `botmessages` VALUES (79, 'use_cyr', 1, '◀️ Назад');
INSERT INTO `botmessages` VALUES (80, 'use_cyr', 2, '◀️ Back');

-- ----------------------------
-- Table structure for keys
-- ----------------------------
DROP TABLE IF EXISTS `keys`;
CREATE TABLE `keys`  (
  `user_id` int NOT NULL,
  `key` blob NOT NULL,
  PRIMARY KEY (`user_id`) USING BTREE,
  CONSTRAINT `keys_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of keys
-- ----------------------------
INSERT INTO `keys` VALUES (704369002, 0x2D2D2D2D2D424547494E20525341205055424C4943204B45592D2D2D2D2D0A4D49494343674B43416745416F35502F584C5A6F2B556D44566A374B474E367376465A746F6D506B4C793675785264673759756F7351634936493758616679330A6B39336638764C314C41634C6C4E623769424A5972584B576D2B6853466F50464978487A3568385954454D6F6F5575312B4B4B595734543538724D6C646154710A746C6E306A57687544342F4C304A456B3638736C6579537778394B555A5363583279622F57513834614764675957484E755846384151355469583477517A2B720A2F414B31456630774E4A654D724B455A70792F316F6A312F7871396261685579343370754E6A4A66635A484F584C65553464586A6B6631566F326E396C6F67380A447269766957554D2F2B3448706238676F5A794F5A696E6949782F7558413479436F362F31694F56622F7174656D57344641795139482F364270554F37374C330A5A4B356E4A717A574B394953414B327044634A623849582B64566F2B694666347A4561736C56687659394D3858644E375371536E42645369504555376D6A54300A4A3456474C6945374C6F384F4A372B6B516D776B6648427A70617150513134304159767A757743365949564E6A2B52497335544A5A6B5A597368486A415573320A325146316A336E345869663432586C5956354E314E353774687535362B5476456D484F6A7069414C4D6C544A6F454A4E7064674163557456495467374C585A450A2F5250654E625A344350513246674D39307465647563454E692B334B556258344A615A30452B3751416E4F5535376972375431705557717277575638436576320A6D454B4F647576695543396156723069477635326652584B6C6A4565586832345853465156503067565A6D70557343714934536773336B47482F2F4B50354C610A6B37535A694F61374A77696757652B4F58415054564F35732B6B424568736B73535A50773668616C2B74446566556F634B797139575545434177454141513D3D0A2D2D2D2D2D454E4420525341205055424C4943204B45592D2D2D2D2D0A);

-- ----------------------------
-- Table structure for languages
-- ----------------------------
DROP TABLE IF EXISTS `languages`;
CREATE TABLE `languages`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `code_in_tg` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `title` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `languages_code_in_tg`(`code_in_tg`) USING BTREE,
  UNIQUE INDEX `languages_title`(`title`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of languages
-- ----------------------------
INSERT INTO `languages` VALUES (1, 'ru', '🇷🇺 Русский');
INSERT INTO `languages` VALUES (2, 'en', '🏴󠁧󠁢󠁥󠁮󠁧󠁿 English');

-- ----------------------------
-- Table structure for passwords
-- ----------------------------
DROP TABLE IF EXISTS `passwords`;
CREATE TABLE `passwords`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `encrypted_password` blob NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `passwords_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `passwords_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of passwords
-- ----------------------------
INSERT INTO `passwords` VALUES (6, 704369002, 'VK', 0x02442ED7C027D2EB11274AF14DE804A0136E9BE46C9CCD9F1AE454A32B7E5605263C08B8889961C4A542CA1E489930FAC3AFBFCA246BE294FB6170CDDA67948F7B8748955877BAD809AB0A0258231F58A1942EC4FEA521B4BBFD165062D69160D711E34B2F391E34CFD5BBB6C752D40125C026489F7E53CE8517B971C8D16266B2C7E0F23D6A0487A840E7E5AEBAA40FEFEAFCF15301CADC580BD53F1492119C28351BCB57E622AABFD3AC0D3BDBEDF02A83128EA960DF18504CC1337A37A3CD10472F1886134544990CB02A42B890078320FEF002232C69EDFFB092EB5706AE69417B79C7E02C379E0AC9668AF63BD34AF9D9CC26D3908CF04756FA57D800EBD97E1D6683501FF4B619B876C6C019129897BB43DE45FA8B74411FB391C0B8C246473DFE690931F73133F4304CD34FB6B4DF09C6333C6AA1E54D84BE10980A86C8E75A42345D320130C0E6687F687FE173A5F31BBB9FE91201B10BABBEDCBEA49D58DC676E3E9D3CA4C16D6D3F5B416E495A7A7027BABD8C37182C593FF47F4150869906155AF84723B49FF2D732AE82228EE30599DE5D1377A5287D8E67629C490B54611E0473FD57D2763C46F5F140A844569AF990255A9CFED678D05825A52FD332202D218C9E1182A975E83D3A2DB4A220A0E417D9B86B1B2393E05FAB58660983E013F9A233DCEB845131FF3D7C58D4AE63D0D9BD8520D4D45B0E0EAFEB);
INSERT INTO `passwords` VALUES (8, 704369002, 'Instagram', 0x3EF4FBF134E0FF6DF0E34D0C7D13D5E340CB380D67258CBF39EDF0381C072D4CE9BC4495888F4F42F91EFA4EB7D1193B98725B7BEA3CB250DD539A59C550579A612EC2F1956A02FDDB471716B2EA848CE0AC9D450AE2E1994F47B53E2D1C54DFC35767F7D2B4ED85AC4F17576FBB34B2727D265869983BA399F51E007DEFBFC71D03E9CC8B30C42B0C7A81612F9B943E1AC43EE55B11152784B10AA92243094CB7BA7C2CEAB64329B51A6C0A1D2CCCA0F24C023C6E9E24EA606E8DE5EEBD047A5B9D0F13E9152D13D679D15119A2557AEC4A7BE2C538B90A8B84D663F1396FAF7126D9770711A78DD77825E8490BB02A24B6664ACC60FFAC5A4C07292D5CE16A6C3A5CDBACE10E68A08AB6E06E5F28E65175E811B73B7722531AAE891EC085AD64AA6AF3C96818438723848167F32858C59D3DCD8EA97797B4C8BBC5107DF9B3C959BF90F8E4B781466DA66F9EC40BD8A427168EE26186490D3354ADC561E9A3FD86104EEDD7E82BE60C7E0FD237677629BFDBDB9D44F7DE948168A9477436CE98CF08660E9F5AC49368AB1B2E0700AA34152FEE4B4600C9BB0AD8DDAC260EBEBEFE33FFFAA229BE56B3608F0C7BB4F040108AE3D02E0477BCEBF404A387A9FB1B0832E2CABFA654F9CBA06F4505427D71C786DDCE622496AD9D4101779AA748D9A1C9D806C6FD0AE6176B2FD5D9BC6EAB7570983D7C0ADEB11C23C04AA81FCE);

-- ----------------------------
-- Table structure for sessions
-- ----------------------------
DROP TABLE IF EXISTS `sessions`;
CREATE TABLE `sessions`  (
  `user_id` int NOT NULL,
  `session` blob NOT NULL,
  PRIMARY KEY (`user_id`) USING BTREE,
  CONSTRAINT `sessions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sessions
-- ----------------------------
INSERT INTO `sessions` VALUES (704369002, 0x7B226C616E67223A20227275222C202270617373776F72645F7469746C65223A2022496E7374616772616D227D);

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int NOT NULL,
  `name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (704369002, 'Никита');

SET FOREIGN_KEY_CHECKS = 1;
