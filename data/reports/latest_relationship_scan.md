# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T10:52:23.291298+00:00`
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

- `news_risk_high->unknown_1h` score `3384.7524` n `31` status `ready` deltaP `2.0813` edge `282.0664` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3255.0274` n `31` status `ready` deltaP `3.7864` edge `271.2327` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `22.5338` n `31` status `ready` deltaP `34.1421` edge `1.6502` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.305` n `31` status `ready` deltaP `32.0624` edge `1.145` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.4597` n `31` status `ready` deltaP `27.5563` edge `0.8546` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.6328` n `31` status `ready` deltaP `22.3397` edge `0.6575` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.4656` n `31` status `ready` deltaP `16.6257` edge `0.7316` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.4631` n `31` status `ready` deltaP `30.2125` edge `0.3019` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0069` n `31` status `ready` deltaP `41.2758` edge `0.1549` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.8398` n `31` status `ready` deltaP `16.0005` edge `0.2408` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.4514` n `31` status `ready` deltaP `30.06` edge `0.0299` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3653` n `31` status `ready` deltaP `25.9965` edge `0.0238` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2996` n `31` status `ready` deltaP `28.25` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.1041` n `31` status `ready` deltaP `13.8497` edge `0.1017` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.9325` n `31` status `ready` deltaP `6.7172` edge `0.2491` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7241` n `31` status `ready` deltaP `8.9627` edge `0.197` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1309` n `31` status `ready` deltaP `24.6426` edge `0.0086` maxDD `-0.2315`
- `market_context_high->metal_4h` score `0.6051` n `36` status `ready` deltaP `8.4857` edge `0.035` maxDD `-0.2914`
- `news_risk_high->commodity_4h` score `0.4038` n `31` status `ready` deltaP `9.7413` edge `0.0266` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3421` n `31` status `ready` deltaP `11.4427` edge `0.0233` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
