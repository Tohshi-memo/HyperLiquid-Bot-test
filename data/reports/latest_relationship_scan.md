# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T15:07:24.973820+00:00`
- Price records: `672`
- Market context records: `1949`
- Flow alert records: `7506`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7547`

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

- `market_context_high->crypto_alt_4h` score `7.0372` n `232` status `ready` deltaP `21.7796` edge `0.5557` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4806` n `232` status `ready` deltaP `25.4636` edge `0.4949` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4276` n `232` status `ready` deltaP `13.6785` edge `0.3135` maxDD `-9.8581`
- `market_context_high->equity_4h` score `1.9773` n `232` status `ready` deltaP `13.9689` edge `0.1811` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.857` n `199` status `ready` deltaP `15.5641` edge `0.4997` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.7546` n `234` status `ready` deltaP `8.0544` edge `0.1078` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.5845` n `234` status `ready` deltaP `7.3469` edge `0.1111` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.233` n `199` status `ready` deltaP `11.9871` edge `0.1821` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1273` n `199` status `ready` deltaP `4.1922` edge `0.1055` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1014` n `232` status `ready` deltaP `8.1519` edge `0.063` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.2205` n `234` status `ready` deltaP `4.5` edge `0.031` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2663` n `199` status `ready` deltaP `9.9323` edge `0.0165` maxDD `-1.3925`
- `market_context_high->equity_24h` score `-0.4681` n `199` status `ready` deltaP `9.9806` edge `0.3843` maxDD `-33.1875`
- `market_context_high->index_1h` score `-0.6029` n `234` status `ready` deltaP `0.6347` edge `0.0087` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6421` n `234` status `ready` deltaP `-2.8635` edge `0.0` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0514` n `232` status `ready` deltaP `-6.4915` edge `-0.0027` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.2256` n `234` status `ready` deltaP `3.3971` edge `0.0088` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.5047` n `234` status `ready` deltaP `0.5093` edge `-0.0336` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.7978` n `232` status `ready` deltaP `6.9408` edge `0.0731` maxDD `-12.5349`
- `market_context_high->crypto_major_24h` score `-1.868` n `199` status `ready` deltaP `14.5221` edge `0.6061` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
