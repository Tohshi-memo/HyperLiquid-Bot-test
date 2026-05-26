# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T18:22:27.925721+00:00`
- Price records: `672`
- Market context records: `1963`
- Flow alert records: `7545`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7565`

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

- `market_context_high->crypto_alt_4h` score `7.121` n `234` status `ready` deltaP `22.1075` edge `0.5605` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.5701` n `234` status `ready` deltaP `25.7414` edge `0.5005` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.3953` n `234` status `ready` deltaP `13.5906` edge `0.3114` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.2944` n `234` status `ready` deltaP `14.3632` edge `0.2049` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.2627` n `199` status `ready` deltaP `16.4203` edge `0.5278` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.9452` n `234` status `ready` deltaP `9.1023` edge `0.1167` maxDD `-3.2225`
- `market_context_high->metal_24h` score `0.8662` n `199` status `ready` deltaP `13.5282` edge `0.2246` maxDD `-12.7414`
- `market_context_high->crypto_alt_1h` score `0.7488` n `234` status `ready` deltaP `8.0954` edge `0.1198` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.382` n `199` status `ready` deltaP `12.2066` edge `0.4403` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.3301` n `199` status `ready` deltaP `4.1922` edge `0.1224` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.2916` n `234` status `ready` deltaP `8.7451` edge `0.0749` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1474` n `234` status `ready` deltaP `4.9491` edge `0.0341` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2531` n `199` status `ready` deltaP `9.9323` edge `0.0176` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6101` n `234` status `ready` deltaP `0.6347` edge `0.0081` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6857` n `234` status `ready` deltaP `-3.612` edge `-0.0006` maxDD `-0.3914`
- `market_context_high->crypto_major_24h` score `-0.9903` n `199` status `ready` deltaP `16.7482` edge `0.6644` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.119` n `234` status `ready` deltaP `-7.6871` edge `-0.0034` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.1849` n `234` status `ready` deltaP `3.9959` edge `0.0082` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.6762` n `234` status `ready` deltaP `-0.0895` edge `-0.0439` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.8192` n `234` status `ready` deltaP `6.9276` edge `0.0714` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
