# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T20:07:18.974929+00:00`
- Price records: `672`
- Market context records: `1971`
- Flow alert records: `7567`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7583`

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

- `market_context_high->crypto_alt_4h` score `7.3726` n `234` status `ready` deltaP `22.7173` edge `0.5774` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7578` n `234` status `ready` deltaP `26.1987` edge `0.5131` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4457` n `234` status `ready` deltaP `13.5906` edge `0.3156` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.2958` n `234` status `ready` deltaP `14.5156` edge `0.204` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.5217` n `199` status `ready` deltaP `16.7627` edge `0.5471` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.2621` n `199` status `ready` deltaP `14.7269` edge `0.2496` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `0.986` n `234` status `ready` deltaP `9.252` edge `0.1191` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.8016` n `234` status `ready` deltaP `8.2451` edge `0.1232` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.7395` n `199` status `ready` deltaP `13.4053` edge `0.4621` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.4033` n `199` status `ready` deltaP `4.1922` edge `0.1285` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1946` n `234` status `ready` deltaP `7.9829` edge `0.0719` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0395` n `234` status `ready` deltaP `5.3982` edge `0.0401` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.1964` n `199` status `ready` deltaP `10.446` edge `0.0189` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.4205` n `199` status `ready` deltaP `17.9468` edge `0.7039` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.5825` n `234` status `ready` deltaP `0.6347` edge `0.0104` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6849` n `234` status `ready` deltaP `-3.612` edge `-0.0005` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.119` n `234` status `ready` deltaP `-7.6871` edge `-0.0034` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.2712` n `234` status `ready` deltaP `3.3971` edge `0.005` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.5024` n `234` status `ready` deltaP `0.8087` edge `-0.0354` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.8845` n `234` status `ready` deltaP `2.1585` edge `-0.0002` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
