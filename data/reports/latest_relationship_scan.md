# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T07:22:29.909131+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4007`

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

- `news_risk_high->unknown_4h` score `3236.3143` n `31` status `ready` deltaP `3.4815` edge `269.6753` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3217.4581` n `31` status `ready` deltaP `1.6322` edge `268.1282` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `87.1662` n `31` status `ready` deltaP `1.6322` edge `7.2624` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `40.3181` n `31` status `ready` deltaP `46.7014` edge `3.0485` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `38.6716` n `31` status `ready` deltaP `47.5694` edge `2.9055` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.0648` n `31` status `ready` deltaP `46.875` edge `2.4429` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.9177` n `31` status `ready` deltaP `27.0653` edge `0.8164` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.535` n `31` status `ready` deltaP `38.2917` edge `0.6707` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.7054` n `31` status `ready` deltaP `33.2494` edge `0.6146` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.8629` n `31` status `ready` deltaP `17.9976` edge `0.9016` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.6264` n `31` status `ready` deltaP `48.0903` edge `0.2316` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3504` n `31` status `ready` deltaP `45.7045` edge `0.154` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7554` n `31` status `ready` deltaP `20.4365` edge `0.1954` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.459` n `31` status `ready` deltaP `37.2247` edge `0.0661` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7321` n `31` status `ready` deltaP `32.2919` edge `0.0209` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5` n `31` status `ready` deltaP `10.1603` edge `0.2989` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2931` n `31` status `ready` deltaP `13.304` edge `0.241` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.1372` n `31` status `ready` deltaP `27.1145` edge `0.0258` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5087` n `31` status `ready` deltaP `29.433` edge `0.0251` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1054` n `31` status `ready` deltaP `16.7781` edge `0.0856` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
