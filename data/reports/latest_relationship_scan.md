# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T19:22:28.392804+00:00`
- Price records: `672`
- Market context records: `6421`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->crypto_alt_24h` score `12.5025` n `32` status `ready` deltaP `32.1181` edge `0.8425` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6334` n `32` status `ready` deltaP `55.9028` edge `0.1801` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.4691` n `146` status `ready` deltaP `16.7285` edge `0.7576` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `4.2265` n `32` status `ready` deltaP `44.1311` edge `0.0626` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1125` n `32` status `ready` deltaP `35.2431` edge `0.1283` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.6642` n `32` status `ready` deltaP `13.7153` edge `0.4563` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4841` n `32` status `ready` deltaP `29.9401` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4773` n `32` status `ready` deltaP `13.9783` edge `0.1429` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8466` n `32` status `ready` deltaP `9.9738` edge `0.0882` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.6649` n `203` status `ready` deltaP `-6.7321` edge `0.2011` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3533` n `198` status `ready` deltaP `10.7492` edge `0.0416` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.2427` n `198` status `ready` deltaP `9.6837` edge `0.0233` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2273` n `32` status `ready` deltaP `6.8301` edge `-0.03` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2844` n `146` status `ready` deltaP `18.5978` edge `0.0964` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.5231` n `203` status `ready` deltaP `1.275` edge `0.0022` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5496` n `198` status `ready` deltaP `7.6528` edge `0.0484` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.6048` n `32` status `ready` deltaP `-0.4491` edge `-0.0248` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.6537` n `203` status `ready` deltaP `-1.98` edge `-0.0023` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7061` n `203` status `ready` deltaP `-3.2211` edge `0.0029` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.7192` n `203` status `ready` deltaP `-0.7249` edge `-0.0019` maxDD `-0.9225`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
