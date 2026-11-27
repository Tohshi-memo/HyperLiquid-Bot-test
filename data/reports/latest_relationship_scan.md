# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T09:37:26.600101+00:00`
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

- `news_risk_high->unknown_1h` score `3224.6017` n `31` status `ready` deltaP `1.6322` edge `268.7235` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3182.6758` n `31` status `ready` deltaP `3.7864` edge `265.2034` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `19.4959` n `31` status `ready` deltaP `29.5139` edge `1.4279` maxDD `0.0`
- `news_risk_high->equity_24h` score `17.4226` n `31` status `ready` deltaP `28.9931` edge `1.2586` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.5209` n `31` status `ready` deltaP `28.6458` edge `1.0191` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.6829` n `31` status `ready` deltaP `21.1201` edge `0.6698` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.4799` n `31` status `ready` deltaP `30.5173` edge `0.3846` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.522` n `31` status `ready` deltaP `14.1866` edge `0.7551` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.0014` n `31` status `ready` deltaP `16.9299` edge `0.3314` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6322` n `31` status `ready` deltaP `38.5865` edge `0.1416` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.1476` n `31` status `ready` deltaP `30.5556` edge `0.0586` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5616` n `31` status `ready` deltaP `29.9076` edge `0.0401` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.5405` n `31` status `ready` deltaP `15.9455` edge `0.1241` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3835` n `31` status `ready` deltaP `28.8488` edge `0.0148` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0379` n `31` status `ready` deltaP `6.4178` edge `0.2646` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8395` n `31` status `ready` deltaP `9.5615` edge `0.2078` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1309` n `31` status `ready` deltaP `24.6426` edge `0.0086` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3681` n `31` status `ready` deltaP `11.7476` edge `0.0246` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.0493` n `31` status `ready` deltaP `6.0828` edge `-0.0071` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6839` n `31` status `ready` deltaP `-5.056` edge `0.0029` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
