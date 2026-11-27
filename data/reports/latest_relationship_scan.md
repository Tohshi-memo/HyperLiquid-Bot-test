# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T19:07:25.390571+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3286.5951` n `31` status `ready` deltaP `1.6201` edge `273.8897` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3183.7425` n `31` status `ready` deltaP `3.3191` edge `265.2954` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.3315` n `31` status `ready` deltaP `25.8232` edge `1.1888` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.6713` n `31` status `ready` deltaP `23.9168` edge `0.8965` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.9741` n `31` status `ready` deltaP `25.4766` edge `0.828` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.067` n `31` status `ready` deltaP `20.8916` edge `0.62` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4439` n `31` status `ready` deltaP `29.8375` edge `0.3028` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.9564` n `31` status `ready` deltaP `13.3451` edge `0.6882` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6538` n `31` status `ready` deltaP `38.6762` edge `0.1428` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.7904` n `31` status `ready` deltaP `12.1877` edge `0.2621` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3559` n `31` status `ready` deltaP `29.0765` edge `0.0285` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.258` n `31` status `ready` deltaP `27.7304` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.234` n `31` status `ready` deltaP `24.6101` edge `0.0221` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.2206` n `31` status `ready` deltaP `15.1261` edge `0.1029` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8548` n `31` status `ready` deltaP `6.0466` edge `0.2436` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6578` n `31` status `ready` deltaP `8.5877` edge `0.191` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1488` n `31` status `ready` deltaP `24.8661` edge `0.0094` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.415` n `31` status `ready` deltaP `10.2715` edge `0.0245` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3821` n `31` status `ready` deltaP `11.823` edge `0.0259` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3304` n `31` status `ready` deltaP `-1.8371` edge `0.0109` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
