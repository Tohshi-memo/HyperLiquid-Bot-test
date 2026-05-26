# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T18:37:21.834308+00:00`
- Price records: `672`
- Market context records: `1964`
- Flow alert records: `7548`
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

- `market_context_high->crypto_alt_4h` score `7.18` n `234` status `ready` deltaP `22.26` edge `0.5644` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.6194` n `234` status `ready` deltaP `25.8938` edge `0.5036` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.3893` n `234` status `ready` deltaP `13.5906` edge `0.3109` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.3186` n `234` status `ready` deltaP `14.5156` edge `0.2059` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.31` n `199` status `ready` deltaP `16.5915` edge `0.5306` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.9512` n `234` status `ready` deltaP `9.1023` edge `0.1172` maxDD `-3.2225`
- `market_context_high->metal_24h` score `0.9327` n `199` status `ready` deltaP `13.6995` edge `0.229` maxDD `-12.7414`
- `market_context_high->crypto_alt_1h` score `0.7608` n `234` status `ready` deltaP `8.0954` edge `0.1208` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.4485` n `199` status `ready` deltaP `12.3779` edge `0.4447` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.3493` n `199` status `ready` deltaP `4.1922` edge `0.124` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.2976` n `234` status `ready` deltaP `8.7451` edge `0.0754` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1294` n `234` status `ready` deltaP `4.9491` edge `0.0356` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2519` n `199` status `ready` deltaP `9.9323` edge `0.0177` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6017` n `234` status `ready` deltaP `0.6347` edge `0.0088` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6934` n `234` status `ready` deltaP `-3.7617` edge `-0.0006` maxDD `-0.3914`
- `market_context_high->crypto_major_24h` score `-0.8986` n `199` status `ready` deltaP `16.9194` edge `0.6709` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.1198` n `234` status `ready` deltaP `-7.6871` edge `-0.0035` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.1825` n `234` status `ready` deltaP `3.9959` edge `0.0084` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.6558` n `234` status `ready` deltaP `0.0602` edge `-0.0432` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.8192` n `234` status `ready` deltaP `6.9276` edge `0.0714` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
