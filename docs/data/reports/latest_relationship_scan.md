# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T07:37:28.519249+00:00`
- Price records: `672`
- Market context records: `5018`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10194`

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

- `market_context_high->unknown_1h` score `15.4927` n `93` status `ready` deltaP `4.2673` edge `1.3127` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0297` n `93` status `ready` deltaP `21.4496` edge `0.7117` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.7379` n `93` status `ready` deltaP `18.0141` edge `0.5165` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3771` n `93` status `ready` deltaP `14.7883` edge `0.4889` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.3511` n `93` status `ready` deltaP `14.4587` edge `0.1241` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.9171` n `93` status `ready` deltaP `8.6359` edge `0.0762` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.7961` n `93` status `ready` deltaP `6.2536` edge `0.1164` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.5326` n `93` status `ready` deltaP `4.3404` edge `0.1775` maxDD `-6.3852`
- `market_context_high->unknown_24h` score `0.4212` n `74` status `ready` deltaP `27.3836` edge `-0.1132` maxDD `-1.4072`
- `market_context_high->metal_1h` score `0.364` n `93` status `ready` deltaP `6.2536` edge `0.0383` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1944` n `93` status `ready` deltaP `5.4101` edge `0.0911` maxDD `-5.5126`
- `market_context_high->index_4h` score `-0.0413` n `93` status `ready` deltaP `4.7813` edge `0.0408` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.0835` n `74` status `ready` deltaP `8.8636` edge `0.0064` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3407` n `93` status `ready` deltaP `1.2588` edge `0.0139` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5323` n `93` status `ready` deltaP `2.5111` edge `0.013` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.8043` n `93` status `ready` deltaP `3.6979` edge `-0.0025` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.9919` n `93` status `ready` deltaP `-3.9158` edge `-0.0022` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7581` n `93` status `ready` deltaP `-11.9986` edge `-0.0055` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.9156` n `74` status `ready` deltaP `3.2986` edge `0.0215` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.418` n `74` status `ready` deltaP `3.1907` edge `-0.0768` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
