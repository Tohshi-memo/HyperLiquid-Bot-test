# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T06:37:19.503372+00:00`
- Price records: `672`
- Market context records: `1921`
- Flow alert records: `7428`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6020`

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

- `market_context_high->crypto_alt_4h` score `7.6857` n `200` status `ready` deltaP `23.8415` edge `0.596` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.2051` n `200` status `ready` deltaP `29.1646` edge `0.5306` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.9356` n `200` status `ready` deltaP `17.6037` edge `0.413` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.6334` n `200` status `ready` deltaP `15.9146` edge `0.2228` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.9025` n `193` status `ready` deltaP `13.6118` edge `0.5165` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.8296` n `212` status `ready` deltaP `8.8578` edge `0.1087` maxDD `-3.2225`
- `market_context_high->metal_24h` score `0.7457` n `193` status `ready` deltaP `13.476` edge `0.2149` maxDD `-12.7414`
- `market_context_high->crypto_alt_1h` score `0.6623` n `212` status `ready` deltaP `8.0048` edge `0.1132` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.4981` n `200` status `ready` deltaP `10.3963` edge `0.0811` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.4725` n `193` status `ready` deltaP `5.4764` edge `0.1257` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.0843` n `212` status `ready` deltaP `5.3186` edge `0.0369` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.1063` n `193` status `ready` deltaP `11.3927` edge `0.0201` maxDD `-1.3925`
- `market_context_high->metal_1h` score `-0.6142` n `212` status `ready` deltaP `5.361` edge `0.0191` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.6248` n `212` status `ready` deltaP `0.3164` edge `0.009` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6691` n `212` status `ready` deltaP `-3.4742` edge `0.0006` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.7047` n `200` status `ready` deltaP `11.6341` edge `0.1329` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-0.8025` n `200` status `ready` deltaP `-2.2439` edge `0.0009` maxDD `-1.1056`
- `market_context_high->equity_24h` score `-1.1223` n `193` status `ready` deltaP `7.0227` edge `0.3495` maxDD `-33.1875`
- `market_context_high->unknown_1h` score `-1.1934` n `212` status `ready` deltaP `1.5959` edge `-0.0149` maxDD `-3.6151`
- `market_context_high->crypto_major_24h` score `-2.058` n `193` status `ready` deltaP `13.4679` edge `0.5973` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
