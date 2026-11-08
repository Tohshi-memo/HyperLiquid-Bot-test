# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T21:22:27.105127+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6549`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_4h` score `81.8662` n `39` status `ready` deltaP `-4.6591` edge `6.898` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.0778` n `37` status `ready` deltaP `11.4208` edge `0.7765` maxDD `-31.3588`
- `market_context_high->fx_4h` score `2.7184` n `39` status `ready` deltaP `29.0729` edge `0.0417` maxDD `-0.0521`
- `market_context_high->equity_1h` score `1.9849` n `50` status `ready` deltaP `7.0479` edge `0.1727` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8322` n `39` status `ready` deltaP `24.1792` edge `0.0385` maxDD `-2.4279`
- `market_context_high->index_24h` score `1.1628` n `37` status `ready` deltaP `14.6913` edge `0.1142` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8498` n `37` status `ready` deltaP `10.9422` edge `0.0067` maxDD `-0.0397`
- `market_context_high->crypto_alt_1h` score `0.2797` n `50` status `ready` deltaP `5.5389` edge `0.0679` maxDD `-3.1881`
- `market_context_high->commodity_1h` score `0.1901` n `50` status `ready` deltaP `10.4072` edge `0.0096` maxDD `-1.7019`
- `market_context_high->metal_1h` score `0.0945` n `50` status `ready` deltaP `4.4491` edge `0.011` maxDD `-0.6226`
- `market_context_high->index_1h` score `0.0486` n `50` status `ready` deltaP `1.3473` edge `0.0261` maxDD `-0.3084`
- `market_context_high->commodity_24h` score `0.0295` n `37` status `ready` deltaP `3.0875` edge `0.1027` maxDD `-6.5601`
- `market_context_high->commodity_4h` score `-0.0458` n `39` status `ready` deltaP `2.0169` edge `0.0261` maxDD `-1.633`
- `market_context_high->crypto_major_1h` score `-0.1171` n `50` status `ready` deltaP `3.1437` edge `0.0445` maxDD `-3.0172`
- `market_context_high->fx_1h` score `-0.3427` n `50` status `ready` deltaP `-1.5389` edge `0.0088` maxDD `-0.1681`
- `market_context_high->equity_4h` score `-0.642` n `39` status `ready` deltaP `22.5571` edge `0.0953` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.8103` n `39` status `ready` deltaP `-3.6664` edge `-0.0344` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.969` n `39` status `ready` deltaP `16.014` edge `0.0133` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.6632` n `37` status `ready` deltaP `7.0055` edge `-0.13` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.7782` n `39` status `ready` deltaP `2.4038` edge `-0.1059` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
