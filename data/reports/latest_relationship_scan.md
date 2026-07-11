# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T19:07:29.248674+00:00`
- Price records: `672`
- Market context records: `6420`
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

- `news_risk_high->crypto_alt_24h` score `12.5848` n `32` status `ready` deltaP `32.2917` edge `0.8482` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6346` n `32` status `ready` deltaP `55.9028` edge `0.1802` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.2722` n `146` status `ready` deltaP `16.2172` edge `0.7446` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `4.2265` n `32` status `ready` deltaP `44.1311` edge `0.0626` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1125` n `32` status `ready` deltaP `35.2431` edge `0.1283` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.7021` n `32` status `ready` deltaP `13.8889` edge `0.46` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4721` n `32` status `ready` deltaP `29.7904` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4874` n `32` status `ready` deltaP `14.128` edge `0.1432` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8544` n `32` status `ready` deltaP `10.1235` edge `0.0882` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.6169` n `204` status `ready` deltaP `-6.9567` edge `0.1986` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3551` n `199` status `ready` deltaP `10.7872` edge `0.0415` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.2401` n `199` status `ready` deltaP `9.6811` edge `0.0231` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2273` n `32` status `ready` deltaP `6.8301` edge `-0.03` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2852` n `146` status `ready` deltaP `18.5978` edge `0.0963` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.5285` n `204` status `ready` deltaP `1.1712` edge `0.0022` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5578` n `199` status `ready` deltaP `7.4955` edge `0.0484` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.597` n `32` status `ready` deltaP `-0.2994` edge `-0.0248` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.6677` n `204` status `ready` deltaP `-2.2191` edge `-0.0025` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.7093` n `204` status `ready` deltaP `-0.6018` edge `-0.0019` maxDD `-0.9225`
- `market_context_high->index_1h` score `-0.72` n `204` status `ready` deltaP `-3.4578` edge `0.0027` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
