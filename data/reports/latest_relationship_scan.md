# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T13:07:24.043876+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `5558`

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

- `news_risk_high->unknown_1h` score `3400.2456` n `31` status `ready` deltaP `2.0813` edge `283.3575` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3248.659` n `31` status `ready` deltaP `3.7864` edge `270.702` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `23.8814` n `31` status `ready` deltaP `35.7019` edge `1.7521` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.6094` n `31` status `ready` deltaP `33.6222` edge `1.2433` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.8782` n `31` status `ready` deltaP `28.4229` edge `0.8837` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.1686` n `31` status `ready` deltaP `23.7116` edge `0.693` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.8388` n `31` status `ready` deltaP `17.9976` edge `0.7703` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.7253` n `31` status `ready` deltaP `31.5844` edge `0.3146` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0515` n `31` status `ready` deltaP `41.6224` edge `0.1563` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `4.0198` n `31` status `ready` deltaP `17.5603` edge `0.2454` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.578` n `31` status `ready` deltaP `31.432` edge `0.0313` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4279` n `31` status `ready` deltaP `26.3432` edge `0.0267` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3547` n `31` status `ready` deltaP `28.8488` edge `0.0124` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2287` n `31` status `ready` deltaP `14.7479` edge `0.1061` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.069` n `31` status `ready` deltaP `7.1663` edge `0.2636` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8777` n `31` status `ready` deltaP `10.1603` edge `0.2087` maxDD `-1.5232`
- `market_context_high->metal_4h` score `1.2082` n `45` status `ready` deltaP `16.8191` edge `0.0297` maxDD `-0.2914`
- `news_risk_high->metal_1h` score `1.1364` n `31` status `ready` deltaP `24.6426` edge `0.0093` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.4655` n `31` status `ready` deltaP `10.8084` edge `0.0274` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3522` n `31` status `ready` deltaP `11.4427` edge `0.0246` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
