# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T02:22:27.669605+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3230`

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

- `news_risk_high->unknown_1h` score `3309.5845` n `31` status `ready` deltaP `1.6322` edge `275.8054` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3173.6359` n `31` status `ready` deltaP `3.4815` edge `264.4521` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.8144` n `31` status `ready` deltaP `28.2496` edge `1.2962` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.3609` n `31` status `ready` deltaP `26.5165` edge `0.8533` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.3537` n `31` status `ready` deltaP `23.9168` edge `0.7867` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.1785` n `31` status `ready` deltaP `18.6811` edge `0.5607` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.0636` n `31` status `ready` deltaP `28.3832` edge `0.2808` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.7126` n `31` status `ready` deltaP `38.6762` edge `0.1477` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.481` n `31` status `ready` deltaP `13.5769` edge `0.6257` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.35` n `31` status `ready` deltaP `12.1877` edge `0.2254` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.2045` n `31` status `ready` deltaP `27.4686` edge `0.0266` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2014` n `31` status `ready` deltaP `27.0524` edge `0.0116` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.1664` n `31` status `ready` deltaP `14.4485` edge `0.1029` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.162` n `31` status `ready` deltaP `24.6101` edge `0.0161` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.7799` n `31` status `ready` deltaP `4.7711` edge `0.2425` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6213` n `31` status `ready` deltaP `7.9148` edge `0.1908` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1006` n `31` status `ready` deltaP `24.0438` edge `0.0087` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3508` n `31` status `ready` deltaP `8.8267` edge `0.0259` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2213` n `31` status `ready` deltaP `9.7659` edge `0.019` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3567` n `31` status `ready` deltaP `-2.3614` edge `0.0122` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
