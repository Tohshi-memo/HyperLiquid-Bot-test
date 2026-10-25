# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T12:22:33.893955+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_4h` score `38.7243` n `113` status `ready` deltaP `-0.2914` edge `3.2625` maxDD `-1.016`
- `market_context_high->unknown_1h` score `3.6421` n `113` status `ready` deltaP `4.1704` edge `0.3246` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `0.6323` n `55` status `ready` deltaP `15.1894` edge `0.0707` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0475` n `113` status `ready` deltaP `8.221` edge `0.009` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0731` n `113` status `ready` deltaP `3.41` edge `0.0028` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5194` n `113` status `ready` deltaP `-0.3325` edge `0.009` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6534` n `113` status `ready` deltaP `-1.8865` edge `-0.006` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6623` n `113` status `ready` deltaP `4.3347` edge `-0.0049` maxDD `-1.6682`
- `market_context_high->crypto_major_24h` score `-0.6926` n `55` status `ready` deltaP `-0.142` edge `0.0147` maxDD `-4.5369`
- `market_context_high->commodity_4h` score `-0.9154` n `113` status `ready` deltaP `-3.61` edge `0.0296` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.422` n `113` status `ready` deltaP `1.75` edge `-0.0359` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8734` n `113` status `ready` deltaP `4.9185` edge `-0.0179` maxDD `-5.3474`
- `market_context_high->fx_24h` score `-1.9875` n `55` status `ready` deltaP `-2.4148` edge `0.0077` maxDD `-1.2451`
- `market_context_high->index_4h` score `-2.1783` n `113` status `ready` deltaP `-8.2249` edge `-0.037` maxDD `-4.3282`
- `market_context_high->index_24h` score `-2.5356` n `55` status `ready` deltaP `-7.5063` edge `-0.1468` maxDD `-4.925`
- `market_context_high->crypto_alt_1h` score `-3.2025` n `113` status `ready` deltaP `-2.4588` edge `-0.0631` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.6823` n `55` status `ready` deltaP `-10.9753` edge `0.0067` maxDD `-7.2311`
- `market_context_high->equity_1h` score `-3.8715` n `113` status `ready` deltaP `-0.3895` edge `-0.0927` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-4.6902` n `55` status `ready` deltaP `2.6452` edge `-0.1126` maxDD `-33.5073`
- `market_context_high->crypto_major_4h` score `-10.0436` n `113` status `ready` deltaP `-12.7428` edge `-0.2522` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
