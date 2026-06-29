# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T08:37:29.259131+00:00`
- Price records: `672`
- Market context records: `5127`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5560`

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

- `market_context_high->unknown_24h` score `29.1258` n `63` status `ready` deltaP `28.621` edge `2.2706` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.8913` n `126` status `ready` deltaP `9.9135` edge `0.739` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.2138` n `117` status `ready` deltaP `19.6008` edge `0.5727` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.9094` n `117` status `ready` deltaP `13.7599` edge `0.4773` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.4059` n `117` status `ready` deltaP `11.5007` edge `0.4364` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.3551` n `63` status `ready` deltaP `20.2381` edge `0.1482` maxDD `-5.418`
- `market_context_high->crypto_alt_1h` score `0.7618` n `126` status `ready` deltaP `5.2704` edge `0.1245` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.7439` n `126` status `ready` deltaP `8.0411` edge `0.0677` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.6859` n `126` status `ready` deltaP `7.6205` edge `0.1309` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.5384` n `117` status `ready` deltaP `7.3849` edge `0.1595` maxDD `-7.4425`
- `market_context_high->metal_1h` score `0.1642` n `126` status `ready` deltaP `7.3662` edge `0.0234` maxDD `-1.4501`
- `market_context_high->index_1h` score `0.0224` n `126` status `ready` deltaP `5.5556` edge `0.0152` maxDD `-1.0296`
- `market_context_high->metal_24h` score `-0.4853` n `63` status `ready` deltaP `0.9424` edge `0.1794` maxDD `-14.4989`
- `market_context_high->commodity_1h` score `-0.5651` n `126` status `ready` deltaP `0.853` edge `-0.0012` maxDD `-2.155`
- `market_context_high->index_4h` score `-0.6082` n `117` status `ready` deltaP `4.3581` edge `0.032` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.6254` n `126` status `ready` deltaP `-2.1267` edge `-0.0019` maxDD `-0.7944`
- `market_context_high->metal_4h` score `-0.6876` n `117` status `ready` deltaP `0.4169` edge `0.0501` maxDD `-4.6157`
- `market_context_high->fx_4h` score `-1.0075` n `117` status `ready` deltaP `-3.2964` edge `0.0001` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.3155` n `63` status `ready` deltaP `-1.1409` edge `-0.0081` maxDD `-1.1804`
- `market_context_high->crypto_alt_24h` score `-2.0603` n `63` status `ready` deltaP `12.9712` edge `0.4546` maxDD `-58.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
