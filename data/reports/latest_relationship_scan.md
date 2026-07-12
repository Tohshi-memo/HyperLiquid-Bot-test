# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T00:52:25.900649+00:00`
- Price records: `672`
- Market context records: `6447`
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

- `news_risk_high->crypto_alt_24h` score `11.5981` n `32` status `ready` deltaP `29.5139` edge `0.7845` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.7932` n `145` status `ready` deltaP `20.6538` edge `0.9251` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3058` n `32` status `ready` deltaP `52.2569` edge `0.1771` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1096` n `32` status `ready` deltaP `42.7591` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.9428` n `32` status `ready` deltaP `34.2014` edge `0.1211` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.241` n `32` status `ready` deltaP `11.1111` edge `0.4194` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4566` n `32` status `ready` deltaP `29.6407` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.556` n `32` status `ready` deltaP `14.128` edge `0.152` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.1191` n `182` status `ready` deltaP `-6.141` edge `0.2243` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.9246` n `32` status `ready` deltaP `10.1235` edge `0.0972` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.062` n `182` status `ready` deltaP `7.3053` edge `0.0241` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.1445` n `32` status `ready` deltaP `6.5307` edge `-0.0211` maxDD `-0.7581`
- `market_context_high->metal_4h` score `-0.2206` n `182` status `ready` deltaP `7.416` edge `0.041` maxDD `-2.7056`
- `market_context_high->unknown_4h` score `-0.4423` n `182` status `ready` deltaP `-15.4483` edge `0.3067` maxDD `-10.5788`
- `news_risk_high->metal_1h` score `-0.5223` n `32` status `ready` deltaP `1.0479` edge `-0.0242` maxDD `-1.6464`
- `market_context_high->commodity_24h` score `-0.5477` n `145` status `ready` deltaP `1.5505` edge `0.136` maxDD `-5.6914`
- `market_context_high->metal_1h` score `-0.5697` n `182` status `ready` deltaP `0.4984` edge `0.0014` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5792` n `182` status `ready` deltaP `6.9938` edge `0.049` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.6386` n `32` status `ready` deltaP `2.0833` edge `-0.0086` maxDD `-2.3058`
- `market_context_high->crypto_alt_1h` score `-0.6426` n `182` status `ready` deltaP `5.6936` edge `0.0159` maxDD `-6.2331`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
