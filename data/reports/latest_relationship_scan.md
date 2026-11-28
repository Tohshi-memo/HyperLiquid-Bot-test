# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T08:37:37.500827+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3756`

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

- `news_risk_high->unknown_1h` score `3365.6161` n `31` status `ready` deltaP `1.6322` edge `280.4747` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3238.1733` n `31` status `ready` deltaP `3.634` edge `269.8292` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `21.089` n `31` status `ready` deltaP `32.5823` edge `1.5402` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.0114` n `31` status `ready` deltaP `30.5026` edge `1.0476` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.9437` n `31` status `ready` deltaP `25.9965` edge `0.822` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.1311` n `31` status `ready` deltaP `21.2726` edge `0.6228` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.2687` n `31` status `ready` deltaP `29.2978` edge `0.2918` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.0175` n `31` status `ready` deltaP `15.2537` edge `0.6833` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.8931` n `31` status `ready` deltaP `40.0626` edge `0.1535` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.6299` n `31` status `ready` deltaP `14.4407` edge `0.2337` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3237` n `31` status `ready` deltaP `28.6881` edge `0.0284` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.2739` n `31` status `ready` deltaP `25.3033` edge `0.0208` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2624` n `31` status `ready` deltaP `27.8009` edge `0.0117` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.0909` n `31` status `ready` deltaP `13.8497` edge `0.1006` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8086` n `31` status `ready` deltaP `5.5196` edge `0.2412` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6579` n `31` status `ready` deltaP `8.5136` edge `0.1915` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.106` n `31` status `ready` deltaP `24.1935` edge `0.0084` maxDD `-0.2315`
- `market_context_high->equity_1h` score `0.3745` n `39` status `ready` deltaP `10.2104` edge `0.0208` maxDD `-1.2685`
- `news_risk_high->commodity_4h` score `0.3326` n `31` status `ready` deltaP `8.5218` edge `0.0256` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3217` n `31` status `ready` deltaP `11.2903` edge `0.0217` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
