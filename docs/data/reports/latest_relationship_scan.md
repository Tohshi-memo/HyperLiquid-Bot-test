# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T10:37:22.873377+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3242.8237` n `31` status `ready` deltaP `1.6322` edge `270.242` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3196.7974` n `31` status `ready` deltaP `3.7864` edge `266.3802` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `18.6808` n `31` status `ready` deltaP `28.8194` edge `1.3646` maxDD `0.0`
- `news_risk_high->equity_24h` score `16.6675` n `31` status `ready` deltaP `28.2986` edge `1.2003` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.8473` n `31` status `ready` deltaP `27.9514` edge `0.9676` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.6011` n `31` status `ready` deltaP `20.9677` edge `0.664` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.5019` n `31` status `ready` deltaP `30.8222` edge `0.3844` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.442` n `31` status `ready` deltaP `13.5769` edge `0.7489` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `4.8114` n `31` status `ready` deltaP `16.2355` edge `0.3202` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6346` n `31` status `ready` deltaP `38.5865` edge `0.1418` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.0249` n `31` status `ready` deltaP `29.8611` edge `0.053` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.5909` n `31` status `ready` deltaP `16.2449` edge `0.1263` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.5884` n `31` status `ready` deltaP `30.2125` edge `0.0403` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.3966` n `31` status `ready` deltaP `28.9985` edge `0.0149` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0223` n `31` status `ready` deltaP `6.2681` edge `0.2636` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8356` n `31` status `ready` deltaP `9.5615` edge `0.2073` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1644` n `31` status `ready` deltaP `25.0917` edge `0.0099` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3539` n `31` status `ready` deltaP `11.5952` edge `0.0238` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.0136` n `31` status `ready` deltaP `6.6925` edge `-0.0031` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.63` n `31` status `ready` deltaP `-4.6069` edge `0.0044` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
