# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T15:07:17.292249+00:00`
- Price records: `672`
- Market context records: `1853`
- Flow alert records: `7234`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4500`

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

- `market_context_high->crypto_alt_4h` score `6.5289` n `199` status `ready` deltaP `21.4418` edge `0.5156` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `5.9382` n `199` status `ready` deltaP `24.8184` edge `0.454` maxDD `-4.9684`
- `market_context_high->metal_24h` score `5.6484` n `178` status `ready` deltaP `23.2503` edge `0.5583` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.2219` n `199` status `ready` deltaP `17.0433` edge `0.4406` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.8141` n `178` status `ready` deltaP `14.9169` edge `0.2579` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.5482` n `178` status `ready` deltaP `14.0391` edge `0.6508` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.205` n `199` status `ready` deltaP `14.4296` edge `0.197` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.7063` n `178` status `ready` deltaP `11.8952` edge `0.4694` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.4756` n `199` status `ready` deltaP `10.5504` edge `0.0782` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.1754` n `199` status `ready` deltaP `4.3993` edge `0.0839` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.1699` n `178` status `ready` deltaP `19.2065` edge `0.7447` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.0761` n `178` status `ready` deltaP `12.9975` edge `0.0246` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.0248` n `199` status `ready` deltaP `4.2601` edge `0.0809` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.2067` n `199` status `ready` deltaP `4.2383` edge `0.0339` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.4629` n `199` status `ready` deltaP `3.4371` edge `0.0337` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.6013` n `199` status `ready` deltaP `5.5329` edge `0.0196` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.649` n `199` status `ready` deltaP `12.3905` edge `0.1325` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6805` n `199` status `ready` deltaP `-0.4551` edge `0.0095` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7126` n `199` status `ready` deltaP `-4.1006` edge `-0.0008` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0184` n `199` status `ready` deltaP `-5.4962` edge `-0.0051` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
