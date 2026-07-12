# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T01:37:29.138426+00:00`
- Price records: `672`
- Market context records: `6450`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.6576` n `32` status `ready` deltaP `29.6875` edge `0.7883` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.3249` n `145` status `ready` deltaP `19.1056` edge `0.8964` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.307` n `32` status `ready` deltaP `52.2569` edge `0.1772` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1096` n `32` status `ready` deltaP `42.7591` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.8663` n `32` status `ready` deltaP `33.6806` edge `0.1182` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.3188` n `32` status `ready` deltaP `11.6319` edge `0.4259` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4697` n `32` status `ready` deltaP `29.7904` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5155` n `32` status `ready` deltaP `13.6789` edge `0.1498` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.2718` n `179` status `ready` deltaP `-5.8074` edge `0.2348` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8786` n `32` status `ready` deltaP `9.6744` edge `0.0943` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.0943` n `179` status `ready` deltaP `7.5887` edge `0.0249` maxDD `-0.4108`
- `market_context_high->metal_4h` score `-0.137` n `179` status `ready` deltaP `8.3552` edge `0.0417` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.2032` n `32` status `ready` deltaP `6.0816` edge `-0.023` maxDD `-0.7581`
- `market_context_high->unknown_4h` score `-0.2458` n `179` status `ready` deltaP `-15.3623` edge `0.3225` maxDD `-10.5788`
- `market_context_high->commodity_24h` score `-0.2837` n `145` status `ready` deltaP `3.0987` edge `0.1447` maxDD `-5.4536`
- `news_risk_high->metal_1h` score `-0.5059` n `32` status `ready` deltaP `1.3473` edge `-0.0241` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.567` n `179` status `ready` deltaP `6.1653` edge `0.0175` maxDD `-5.8368`
- `market_context_high->metal_1h` score `-0.5691` n `179` status `ready` deltaP `0.5093` edge `0.0014` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5802` n `179` status `ready` deltaP `6.7789` edge `0.0503` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.6052` n `32` status `ready` deltaP `2.6042` edge `-0.0078` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
