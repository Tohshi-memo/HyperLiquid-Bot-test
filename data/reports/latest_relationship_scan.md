# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T08:07:30.281414+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3516`

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

- `news_risk_high->unknown_1h` score `3224.8465` n `31` status `ready` deltaP `1.6322` edge `268.7439` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3182.3014` n `31` status `ready` deltaP `3.7864` edge `265.1722` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `20.7804` n `31` status `ready` deltaP `30.5556` edge `1.528` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.6484` n `31` status `ready` deltaP `30.0347` edge `1.3538` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.6326` n `31` status `ready` deltaP `29.6875` edge `1.1048` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.9312` n `31` status `ready` deltaP `22.0348` edge `0.6844` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.7727` n `31` status `ready` deltaP `31.432` edge `0.4029` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.6802` n `31` status `ready` deltaP `14.9488` edge `0.7703` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.2983` n `31` status `ready` deltaP `17.9716` edge `0.3492` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6322` n `31` status `ready` deltaP `38.5865` edge `0.1416` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.3438` n `31` status `ready` deltaP `31.5972` edge `0.068` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.7036` n `31` status `ready` deltaP `16.694` edge `0.1327` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.6284` n `31` status `ready` deltaP `30.5173` edge `0.0416` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.441` n `31` status `ready` deltaP `29.4476` edge `0.0156` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0682` n `31` status `ready` deltaP `6.7172` edge `0.2665` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8816` n `31` status `ready` deltaP `10.0106` edge `0.2102` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1613` n `31` status `ready` deltaP `25.0917` edge `0.0095` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4317` n `31` status `ready` deltaP `12.3574` edge `0.0287` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.1296` n `31` status `ready` deltaP `5.1682` edge `-0.0113` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6947` n `31` status `ready` deltaP `-5.2057` edge `0.003` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
