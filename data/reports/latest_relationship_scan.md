# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T10:07:25.579425+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3714`

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

- `news_risk_high->unknown_1h` score `3391.1496` n `31` status `ready` deltaP `2.0813` edge `282.5995` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3252.0286` n `31` status `ready` deltaP `3.7864` edge `270.9828` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `22.0122` n `31` status `ready` deltaP `33.6222` edge `1.6102` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.8506` n `31` status `ready` deltaP `31.5425` edge `1.1106` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.2765` n `31` status `ready` deltaP `27.0364` edge `0.8428` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.4282` n `31` status `ready` deltaP `21.8823` edge `0.6435` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.3847` n `31` status `ready` deltaP `29.9076` edge `0.2974` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.2889` n `31` status `ready` deltaP `16.1683` edge `0.712` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9883` n `31` status `ready` deltaP `41.1025` edge `0.1545` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.7719` n `31` status `ready` deltaP `15.4806` edge `0.2386` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.4076` n `31` status `ready` deltaP `29.6027` edge `0.0293` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3383` n `31` status `ready` deltaP `25.8232` edge `0.0227` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2996` n `31` status `ready` deltaP `28.25` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.11` n `31` status `ready` deltaP `13.9994` edge `0.1012` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8827` n `31` status `ready` deltaP `6.2681` edge `0.2457` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7039` n `31` status `ready` deltaP `8.813` edge `0.1954` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1309` n `31` status `ready` deltaP `24.6426` edge `0.0086` maxDD `-0.2315`
- `market_context_high->fx_4h` score `0.5969` n `33` status `ready` deltaP `10.6061` edge `0.0174` maxDD `-0.0693`
- `news_risk_high->commodity_4h` score `0.3856` n `31` status `ready` deltaP `9.4365` edge `0.0263` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3382` n `31` status `ready` deltaP `11.4427` edge `0.0228` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
