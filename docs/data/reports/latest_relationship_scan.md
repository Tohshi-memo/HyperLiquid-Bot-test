# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T21:37:23.317945+00:00`
- Price records: `672`
- Market context records: `6542`
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

- `market_context_high->unknown_24h` score `6.3883` n `144` status `ready` deltaP `11.8934` edge `0.7831` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `3.7153` n `35` status `ready` deltaP `39.1812` edge `0.053` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3015` n `35` status `ready` deltaP `28.4773` edge `0.02` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.9992` n `196` status `ready` deltaP `-6.4493` edge `0.2997` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3615` n `144` status `ready` deltaP `12.9574` edge `0.2139` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5711` n `188` status `ready` deltaP `13.1292` edge `0.0277` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5315` n `35` status `ready` deltaP `5.3465` edge `0.0862` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.3268` n `188` status `ready` deltaP `9.7204` edge `0.1178` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `-0.1807` n `35` status `ready` deltaP `-1.4286` edge `0.0373` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.2684` n `188` status `ready` deltaP `11.0956` edge `0.0615` maxDD `-8.2573`
- `market_context_high->crypto_major_4h` score `-0.4049` n `188` status `ready` deltaP `12.2308` edge `0.0956` maxDD `-12.6576`
- `market_context_high->fx_1h` score `-0.429` n `196` status `ready` deltaP `-0.4002` edge `-0.0016` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.4606` n `196` status `ready` deltaP `1.5978` edge `-0.0014` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5107` n `196` status `ready` deltaP `6.6327` edge `0.0216` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5268` n `196` status `ready` deltaP `6.3669` edge `0.0166` maxDD `-6.7936`
- `market_context_high->equity_1h` score `-0.6698` n `196` status `ready` deltaP `3.1559` edge `0.0041` maxDD `-4.2147`
- `market_context_high->index_1h` score `-0.7435` n `196` status `ready` deltaP `0.8096` edge `0.0046` maxDD `-0.7564`
- `news_risk_high->metal_1h` score `-0.8482` n `35` status `ready` deltaP `-3.6998` edge `-0.0217` maxDD `-1.6568`
- `news_risk_high->unknown_1h` score `-0.8923` n `35` status `ready` deltaP `2.9384` edge `-0.0568` maxDD `-0.9718`
- `market_context_high->metal_4h` score `-0.9068` n `188` status `ready` deltaP `1.0865` edge `0.039` maxDD `-2.6662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
