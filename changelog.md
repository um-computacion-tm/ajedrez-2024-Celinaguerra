# CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.24] - 2024-09-29
### Changed

- modified get_possible_positions_eat so next_col doesnt surprass board limits

## [0.1.23] - 2024-09-28
### Changed

- board move method to include pawn promotion (not working)

## [0.1.22] - 2024-09-26
### Added

- pawn tests
- promotion of pawn to queen (not tested)


## [0.1.21] - 2024-09-25
### Changed

- fixing duplications in code

## [0.1.20] - 2024-09-24
### Added

- pawn tests

### Changed

- fixed knight tests
- fixed duplication on pawn methods

## [0.1.19] - 2024-09-23
### Added

- knight tests

## [0.1.18] - 2024-09-22
### Added

- king tests

### Changed

- bishop tests

## [0.1.17] - 2024-09-17
### Changed

- piece orthogonal and diagonal method to avoid similar code
- updated tests

## [0.1.16] - 2024-09-16
### Added

- pawn and knight movement

## [0.1.15] - 2024-09-15
### Changed

- optimized movement methods

## [0.1.14] - 2024-09-14
### Added

- added king start movement

## [0.1.13] - 2024-09-10
### Added

- valid_positions_diagonal to bishop
- movement tests
- tested exceptions

## [0.1.12] - 2024-09-09
### Added

- all directions to bishop, with validation of color of pieces

### Changed

- adapted tests of exceptions

## [0.1.11] - 2024-09-08
### Added

- exceptions.py, where all exceptions are defined

- applied exceptions to chess

## [0.1.10] - 2024-09-07
### Added

- ortogonal verifications for color of pieces in rook

## [0.1.9] - 2024-09-04
### Added

- Differentation between enemy and own color for eating pieces.
- tests

## [0.1.8] - 2024-09-03
### Changed

- changed atribute board to pieces
- fixed tests


## [0.1.7] - 2024-09-02
### Added

- diagonal right movements to bishop and tests

## [0.1.6] - 2024-09-01
### Added

- valid_possitions to rook and queen
- added tests

## [0.1.5] - 2024-08-29
### Added

- possible_positions_hl to rook

### Changed

- updated board.__str__ and tests (not working)
- added white_str and black_str to all pieces

## [0.1.4] - 2024-08-28
### Added

- added possible_positions_vd and hr to rook
- added test
- white_str and black_str to piece and rook


###################

## [0.1.3] - 2024-08-27
### Added

- added possible_positions_vd to rook
- added tests

## [0.1.2] - 2024-08-26
### Added

- pawn movement and fixed board str

## [0.1.1] - 2024-08-25
### Added

- knight.py, bishop.py, king.py and queen.py
- new pieces positions

## [0.1.0] - 2024-08-24
### Added

- show_board
- str of board, pawn and rook

## [0.0.9] - 2024-08-23
### Changed

- modified cli tests, added method show_board to chess.

- modified changelog formatting

- move_piece now working

## [0.0.8] - 2024-08-21
### Changed
- modified tests

### Added
- added cli tests

## [0.0.7] - 2024-08-20
### Added
- added cli.py

## [0.0.6] - 2024-08-19
### Changed
- updated Pawn to board

### Added
- added tests to test_chess

## [0.0.5] - 2024-08-18
### Added
- added class Chess, move, change_turn. Tests

## [0.0.4] - 2024-08-17
### Added
- added InvalidMoveError, InvalidCoordError and are_valid_coords

## [0.0.3] - 2024-08-16
### Changed
- Updated board

### Added
- added move_piece method and test

## [0.0.2] - 2024-08-15
### Added
- Added board and tested.

## [0.0.1] - 2024-08-14
### Added
- Added basic piece, pawn and rook class. Basic piece tests.