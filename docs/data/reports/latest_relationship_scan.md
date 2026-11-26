# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T08:52:32.297643+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3419`

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

- `news_risk_high->unknown_4h` score `3264.4279` n `31` status `ready` deltaP `3.4815` edge `272.0181` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3237.1561` n `31` status `ready` deltaP `1.6322` edge `269.7697` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `106.8642` n `31` status `ready` deltaP `1.6322` edge `8.9039` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `39.018` n `31` status `ready` deltaP `45.6597` edge `2.9471` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.8622` n `31` status `ready` deltaP `46.5278` edge `2.845` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.2207` n `31` status `ready` deltaP `45.8333` edge `2.3795` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.0326` n `31` status `ready` deltaP `27.8275` edge `0.8209` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.7438` n `31` status `ready` deltaP `39.2064` edge `0.682` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.364` n `31` status `ready` deltaP `32.2077` edge `0.5931` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.9627` n `31` status `ready` deltaP `18.9123` edge `0.9083` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.4375` n `31` status `ready` deltaP `47.0486` edge `0.2228` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2491` n `31` status `ready` deltaP `44.6629` edge `0.1525` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7782` n `31` status `ready` deltaP `20.5862` edge `0.1963` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5514` n `31` status `ready` deltaP `38.1393` edge `0.0677` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7465` n `31` status `ready` deltaP `32.4416` edge `0.0211` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5` n `31` status `ready` deltaP `10.1603` edge `0.2989` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.3087` n `31` status `ready` deltaP `13.4537` edge `0.242` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.1104` n `31` status `ready` deltaP `26.8096` edge `0.0256` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5149` n `31` status `ready` deltaP `29.5827` edge `0.0249` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1093` n `31` status `ready` deltaP `16.7781` edge `0.0861` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
