# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T18:07:21.213358+00:00`
- Price records: `672`
- Market context records: `1962`
- Flow alert records: `7542`
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

- `market_context_high->crypto_alt_4h` score `7.068` n `234` status `ready` deltaP `21.9551` edge `0.5571` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.5195` n `234` status `ready` deltaP `25.5889` edge `0.4973` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4337` n `234` status `ready` deltaP `13.5906` edge `0.3146` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.2824` n `234` status `ready` deltaP `14.3632` edge `0.2039` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.2579` n `199` status `ready` deltaP `16.4203` edge `0.5274` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.9404` n `234` status `ready` deltaP `9.1023` edge `0.1163` maxDD `-3.2225`
- `market_context_high->metal_24h` score `0.7949` n `199` status `ready` deltaP `13.357` edge `0.2198` maxDD `-12.7414`
- `market_context_high->crypto_alt_1h` score `0.7272` n `234` status `ready` deltaP `7.9457` edge `0.119` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.3167` n `199` status `ready` deltaP `12.0354` edge `0.436` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.3061` n `199` status `ready` deltaP `4.1922` edge `0.1204` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.2856` n `234` status `ready` deltaP `8.7451` edge `0.0744` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1606` n `234` status `ready` deltaP `4.9491` edge `0.033` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2543` n `199` status `ready` deltaP `9.9323` edge `0.0175` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6185` n `234` status `ready` deltaP `0.6347` edge `0.0074` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6841` n `234` status `ready` deltaP `-3.612` edge `-0.0004` maxDD `-0.3914`
- `market_context_high->crypto_major_24h` score `-1.0724` n `199` status `ready` deltaP `16.5769` edge `0.6587` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.119` n `234` status `ready` deltaP `-7.6871` edge `-0.0034` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.2053` n `234` status `ready` deltaP `3.8462` edge `0.0075` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.6486` n `234` status `ready` deltaP `0.0602` edge `-0.0426` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.8228` n `234` status `ready` deltaP `6.9276` edge `0.0711` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
