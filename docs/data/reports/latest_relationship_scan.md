# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T19:37:24.657651+00:00`
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

- `news_risk_high->unknown_1h` score `3285.2449` n `31` status `ready` deltaP `1.6322` edge `273.7771` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3181.5585` n `31` status `ready` deltaP `3.3191` edge `265.1134` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.4383` n `31` status `ready` deltaP `25.8232` edge `1.1977` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.5549` n `31` status `ready` deltaP `23.9168` edge `0.8868` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.0324` n `31` status `ready` deltaP `25.6499` edge `0.8317` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.0946` n `31` status `ready` deltaP `20.8916` edge `0.6223` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4017` n `31` status `ready` deltaP `29.6853` edge `0.3003` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.9854` n `31` status `ready` deltaP `13.4973` edge `0.6909` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6562` n `31` status `ready` deltaP `38.6762` edge `0.143` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.764` n `31` status `ready` deltaP `12.1877` edge `0.2599` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.339` n `31` status `ready` deltaP `28.9243` edge `0.0281` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2349` n `31` status `ready` deltaP `27.5015` edge `0.0114` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.2232` n `31` status `ready` deltaP `24.6101` edge `0.0212` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.1603` n `31` status `ready` deltaP `14.8976` edge `0.0994` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8429` n `31` status `ready` deltaP `5.9687` edge `0.2426` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6407` n `31` status `ready` deltaP `8.5136` edge `0.1893` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1426` n `31` status `ready` deltaP `24.7923` edge `0.0091` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.4425` n `31` status `ready` deltaP `10.5759` edge `0.026` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3742` n `31` status `ready` deltaP `11.6708` edge `0.0259` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3076` n `31` status `ready` deltaP `-1.6129` edge `0.0113` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
