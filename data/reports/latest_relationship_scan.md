# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T19:37:27.129790+00:00`
- Price records: `672`
- Market context records: `6532`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `news_risk_high->crypto_alt_24h` score `13.5687` n `32` status `ready` deltaP `36.7309` edge `0.9006` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5964` n `32` status `ready` deltaP `54.4194` edge `0.1869` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.2875` n `144` status `ready` deltaP `11.8934` edge `0.7747` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.9391` n `32` status `ready` deltaP `21.4309` edge `0.5683` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.7121` n `38` status `ready` deltaP `39.3213` edge `0.0518` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.1749` n `192` status `ready` deltaP `-5.9631` edge `0.3111` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.0127` n `32` status `ready` deltaP `22.3299` edge `0.0394` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.7784` n `38` status `ready` deltaP `22.3133` edge `0.0175` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.5936` n `144` status `ready` deltaP `14.3438` edge `0.224` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.7253` n `180` status `ready` deltaP `14.8611` edge `0.029` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.58` n `38` status `ready` deltaP `5.2001` edge `0.0934` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.4223` n `180` status `ready` deltaP `10.8401` edge `0.1183` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0937` n `38` status `ready` deltaP `1.7334` edge `0.0514` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.2165` n `32` status `ready` deltaP `8.0698` edge `0.0056` maxDD `-2.3058`
- `market_context_high->crypto_major_4h` score `-0.361` n `180` status `ready` deltaP `13.4215` edge `0.0933` maxDD `-12.6576`
- `market_context_high->equity_4h` score `-0.382` n `180` status `ready` deltaP `9.3462` edge `0.0586` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.4232` n `192` status `ready` deltaP `-0.2745` edge `-0.0017` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.4641` n `192` status `ready` deltaP `1.6218` edge `-0.002` maxDD `-2.1314`
- `market_context_high->crypto_major_1h` score `-0.5563` n `192` status `ready` deltaP `6.1596` edge `0.0142` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.5783` n `192` status `ready` deltaP `5.8726` edge `0.018` maxDD `-5.8368`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
