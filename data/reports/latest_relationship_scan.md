# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T02:07:27.412067+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `32388.0565` n `45` status `ready` deltaP `2.465` edge `2698.9977` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22235.5748` n `45` status `ready` deltaP `3.6349` edge `1852.9542` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1178.5272` n `31` status `ready` deltaP `2.6801` edge `98.2103` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1000.2216` n `31` status `ready` deltaP `4.8535` edge `83.3251` maxDD `-0.119`
- `news_risk_high->equity_24h` score `37.3074` n `31` status `ready` deltaP `43.4028` edge `2.8196` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.8929` n `31` status `ready` deltaP `45.4861` edge `2.6045` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.8496` n `31` status `ready` deltaP `45.6597` edge `2.2664` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.0282` n `31` status `ready` deltaP `43.1452` edge `0.7422` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.6664` n `31` status `ready` deltaP `23.864` edge `0.8168` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6551` n `31` status `ready` deltaP `30.8222` edge `0.564` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6219` n `31` status `ready` deltaP `56.4684` edge `0.1882` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.5246` n `31` status `ready` deltaP `13.5769` edge `0.8877` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.7654` n `31` status `ready` deltaP `40.9722` edge `0.2073` maxDD `0.0`
- `market_context_high->fx_4h` score `3.2623` n `45` status `ready` deltaP `38.9295` edge `0.0408` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.2049` n `31` status `ready` deltaP `17.8916` edge `0.1665` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.8458` n `31` status `ready` deltaP `31.5844` edge `0.0526` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4745` n `31` status `ready` deltaP `29.5973` edge `0.0174` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4368` n `31` status `ready` deltaP `10.6094` edge `0.2878` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0634` n `31` status `ready` deltaP `9.8609` edge `0.2345` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.564` n `31` status `ready` deltaP `30.1815` edge `0.0272` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
