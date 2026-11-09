# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T06:22:37.109357+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8736`

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

- `market_context_high->equity_24h` score `9.7832` n `32` status `ready` deltaP `16.4931` edge `0.9426` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.5025` n `32` status `ready` deltaP `7.8125` edge `0.2152` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3849` n `32` status `ready` deltaP `16.6667` edge `0.1127` maxDD `-2.3671`
- `market_context_high->commodity_4h` score `0.8658` n `69` status `ready` deltaP `6.144` edge `0.0784` maxDD `-1.1102`
- `market_context_high->metal_4h` score `0.7896` n `69` status `ready` deltaP `11.8593` edge `0.0747` maxDD `-1.2025`
- `market_context_high->fx_24h` score `0.7102` n `32` status `ready` deltaP `10.9375` edge `-0.0049` maxDD `-0.0397`
- `market_context_high->metal_1h` score `0.6786` n `81` status `ready` deltaP `9.2593` edge `0.0276` maxDD `-0.6226`
- `market_context_high->index_4h` score `0.1622` n `69` status `ready` deltaP `12.3961` edge `0.031` maxDD `-2.4279`
- `market_context_high->equity_1h` score `-0.1428` n `81` status `ready` deltaP `-1.6264` edge `0.1164` maxDD `-5.5762`
- `market_context_high->commodity_1h` score `-0.1774` n `81` status `ready` deltaP `4.7683` edge `0.0122` maxDD `-1.7019`
- `market_context_high->index_1h` score `-0.4132` n `81` status `ready` deltaP `-1.4767` edge `0.0152` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-1.0322` n `81` status `ready` deltaP `6.1562` edge `0.0159` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-1.2024` n `81` status `ready` deltaP `-14.8721` edge `-0.0053` maxDD `-0.6429`
- `market_context_high->equity_4h` score `-1.5789` n `69` status `ready` deltaP `9.1132` edge `0.1148` maxDD `-24.9053`
- `market_context_high->metal_24h` score `-1.6784` n `32` status `ready` deltaP `-0.5208` edge `-0.1564` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.0834` n `69` status `ready` deltaP `-11.7046` edge `-0.011` maxDD `-1.9126`
- `market_context_high->crypto_major_1h` score `-2.1959` n `81` status `ready` deltaP `-0.5785` edge `-0.0642` maxDD `-12.0777`
- `market_context_high->crypto_major_24h` score `-4.6006` n `32` status `ready` deltaP `-4.8611` edge `0.0133` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-6.9338` n `69` status `ready` deltaP `4.9885` edge `-0.1442` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.193` n `32` status `ready` deltaP `-18.75` edge `-0.1832` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
