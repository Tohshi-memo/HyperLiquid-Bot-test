# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T20:07:32.515736+00:00`
- Price records: `672`
- Market context records: `6317`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11133`

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

- `news_risk_high->crypto_alt_24h` score `15.3714` n `32` status `ready` deltaP `43.2292` edge `1.0075` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0205` n `32` status `ready` deltaP `50.5208` edge `0.1649` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3161` n `32` status `ready` deltaP `16.6667` edge `0.5202` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2021` n `32` status `ready` deltaP `43.8262` edge `0.0626` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.3407` n `32` status `ready` deltaP `30.0347` edge `0.0987` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4003` n `32` status `ready` deltaP `28.8922` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4756` n `32` status `ready` deltaP `14.5771` edge `0.1387` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9455` n `32` status `ready` deltaP `11.9199` edge `0.0879` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.4457` n `208` status `ready` deltaP `-5.2712` edge `0.1731` maxDD `-3.7317`
- `market_context_high->metal_4h` score `-0.0488` n `196` status `ready` deltaP `8.2877` edge `0.037` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1657` n `157` status `ready` deltaP `20.6398` edge `0.098` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4631` n `208` status `ready` deltaP `2.5939` edge `0.0011` maxDD `-1.8877`
- `market_context_high->fx_1h` score `-0.4711` n `208` status `ready` deltaP `-0.9155` edge `-0.002` maxDD `-0.8498`
- `news_risk_high->index_24h` score `-0.5015` n `32` status `ready` deltaP `3.8194` edge `-0.0026` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.5921` n `208` status `ready` deltaP `-1.0796` edge `-0.0004` maxDD `-2.1314`
- `news_risk_high->metal_1h` score `-0.72` n `32` status `ready` deltaP `-2.6946` edge `-0.0246` maxDD `-1.6464`
- `market_context_high->index_4h` score `-0.745` n `196` status `ready` deltaP `2.8341` edge `0.0185` maxDD `-1.2987`
- `market_context_high->index_1h` score `-0.8778` n `208` status `ready` deltaP `-4.1139` edge `0.0018` maxDD `-0.9531`
- `news_risk_high->unknown_1h` score `-0.9625` n `32` status `ready` deltaP `4.5846` edge `-0.0763` maxDD `-0.7581`
- `market_context_high->crypto_alt_1h` score `-1.0223` n `208` status `ready` deltaP `4.468` edge `0.0144` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
