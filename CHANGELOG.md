## v0.0.9
new support for `The Fisrt Descendant` :fire:

### Added
- add 15 apis for `The First Descendant`
  - `get_ouid`
  - `get_user_basic`
  - `get_user_descendant`
  - `get_user_weapon`
  - `get_user_reactor`
  - `get_user_external_component`
  - `get_descendant_metadata`
  - `get_weapon_metadata`
  - `get_module_metadata`
  - `get_reactor_metadata`
  - `get_external_config_metadata`
  - `get_reward_metadata`
  - `get_stat_metadata`
  - `get_void_battle_metadata`
  - `get_title_metadata`
- add `skill_effect_next` field to `MapleStoryCharacterSkill`
- new api endpoint `get_character_list` in MapleStory
-  add new fields `character_date_create`, `access_flag`, `liberation_quest_clear_flag` to `MapleStoryCharacterBasic`

### Deprecated
- `guild_mark` and `_guild_mark_custom` deprecated from `GuildBasic` in MapleStory

### Fixed
-  type mismatch in `MapleStoryCharacterLinkSkill`

## v0.0.8
### Added
- 메이플스토리 실시간 조회 적용

## v0.0.7
### Added
- 메이플스토리 1/19일 신규 업데이트 반영

### Fixed
- 메이플스토리 데이터 조회 시, 일부 필드명과 타입에서 오타를 수정하였습니다.
- 기존 명세와 다르게 반환되던 일부 필드명에 alias를 적용하였습니다.

## v0.0.6
### Added
- 메이플스토리 API 추가 연동 🍁
- ouid 조회
- 스타포스 히스토리 조회

## v0.0.5
### Added
- 메이플스토리 API 추가 연동
  - 유니온 조회
  - 길드 조회
  - 랭킹 조회

## v0.0.4
### Added
- 메이플스토리 API 최초 연동 (캐릭터 관련 20여종의 API)

## v0.0.3
### Added
- FC 온라인 API 최초 연동

## v0.0.2
### Added
- 비동기 클라이언트 (`NexonOpenAPIAsync`) 지원

## v0.0.1
### Added
- 바람의나라 API 최초 연동
- 바람의나라:연 API 최초 연동
- 메이플스토리M API 최초 연동
- 마비노기 영웅전 API 최초 연동
- 크레이지아케이드 API 최초 연동
- 히트2 API 최초 연동
- V4ㅓAPI 최초 연동
- 카트라이더 러쉬플러스 API 최초 연동

## Unreleased