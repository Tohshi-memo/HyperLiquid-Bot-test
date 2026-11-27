# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T04:37:35.693086+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3552`

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

- `news_risk_high->unknown_1h` score `3220.2865` n `31` status `ready` deltaP `1.6322` edge `268.3639` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3190.9774` n `31` status `ready` deltaP `3.7864` edge `265.8952` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `23.9737` n `31` status `ready` deltaP `32.9861` edge `1.7779` maxDD `0.0`
- `news_risk_high->equity_24h` score `21.3892` n `31` status `ready` deltaP `32.4653` edge `1.566` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.2714` n `31` status `ready` deltaP `32.1181` edge `1.3085` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.2414` n `31` status `ready` deltaP `23.4067` edge `0.7011` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.5154` n `31` status `ready` deltaP `33.2612` edge `0.4526` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.0075` n `31` status `ready` deltaP `16.4732` edge `0.8021` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.8358` n `31` status `ready` deltaP `20.0549` edge `0.3801` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.7884` n `31` status `ready` deltaP `40.149` edge `0.1442` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.783` n `31` status `ready` deltaP `34.0278` edge `0.0884` maxDD `0.0`
- `news_risk_high->index_4h` score `2.7388` n `31` status `ready` deltaP `31.432` edge `0.0447` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.7192` n `31` status `ready` deltaP `16.694` edge `0.134` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3966` n `31` status `ready` deltaP `28.9985` edge `0.0149` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0628` n `31` status `ready` deltaP `6.8669` edge `0.2648` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8512` n `31` status `ready` deltaP `10.0106` edge `0.2063` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1761` n `31` status `ready` deltaP `25.5408` edge `0.0084` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4833` n `31` status `ready` deltaP `12.5098` edge `0.0343` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.0499` n `31` status `ready` deltaP `7.1499` edge `-0.0015` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5952` n `31` status `ready` deltaP `-4.3075` edge `0.0053` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
