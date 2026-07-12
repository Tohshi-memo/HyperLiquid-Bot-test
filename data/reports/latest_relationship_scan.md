# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T08:37:27.742351+00:00`
- Price records: `672`
- Market context records: `6480`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5869`

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

- `news_risk_high->crypto_alt_24h` score `12.5574` n `32` status `ready` deltaP `33.8542` edge `0.8355` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.7369` n `157` status `ready` deltaP `16.0109` edge `0.7847` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.4481` n `32` status `ready` deltaP `53.6458` edge `0.1797` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.2712` n `32` status `ready` deltaP `16.4931` edge `0.5156` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9654` n `38` status `ready` deltaP `42.2176` edge `0.0536` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.0898` n `32` status `ready` deltaP `28.8194` edge `0.0859` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `1.8541` n `178` status `ready` deltaP `-4.9788` edge `0.2778` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.8311` n `38` status `ready` deltaP `22.9121` edge `0.0179` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.5543` n `38` status `ready` deltaP `4.751` edge `0.0931` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.4599` n `172` status `ready` deltaP `11.6492` edge `0.0283` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.2568` n `172` status `ready` deltaP `-15.5453` edge `0.3656` maxDD `-10.5788`
- `market_context_high->crypto_alt_4h` score `0.2548` n `172` status `ready` deltaP `8.5508` edge `0.1196` maxDD `-6.7632`
- `market_context_high->commodity_24h` score `0.2472` n `157` status `ready` deltaP `6.2278` edge `0.1659` maxDD `-5.2791`
- `market_context_high->metal_4h` score `0.1725` n `172` status `ready` deltaP `11.8938` edge `0.0439` maxDD `-2.7056`
- `news_risk_high->crypto_alt_1h` score `0.0446` n `38` status `ready` deltaP `1.1346` edge `0.0491` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.4579` n `32` status `ready` deltaP `4.6875` edge `-0.0028` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4713` n `172` status `ready` deltaP `8.1395` edge `0.0552` maxDD `-8.2573`
- `news_risk_high->unknown_1h` score `-0.4773` n `38` status `ready` deltaP `4.6013` edge `-0.0333` maxDD `-0.9718`
- `market_context_high->metal_1h` score `-0.533` n `178` status `ready` deltaP `1.2346` edge `0.0012` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5768` n `178` status `ready` deltaP `-0.4104` edge `-0.0029` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
