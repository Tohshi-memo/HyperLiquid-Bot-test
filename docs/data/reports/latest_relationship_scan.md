# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T04:52:29.392575+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `2643.6438` n `43` status `ready` deltaP `21.0796` edge `220.2052` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.5831` n `40` status `ready` deltaP `51.4583` edge `0.8286` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0826` n `40` status `ready` deltaP `51.3194` edge `0.5942` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `2.1252` n `43` status `ready` deltaP `0.7445` edge `0.2485` maxDD `-3.4427`
- `news_risk_high->index_4h` score `0.8525` n `43` status `ready` deltaP `8.0261` edge `0.0556` maxDD `-0.3783`
- `market_context_high->commodity_1h` score `0.3743` n `47` status `ready` deltaP `7.7143` edge `0.034` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3294` n `47` status `ready` deltaP `5.0338` edge `0.0933` maxDD `-2.7703`
- `news_risk_high->metal_1h` score `0.1559` n `43` status `ready` deltaP `6.3431` edge `0.0097` maxDD `-0.5599`
- `market_context_high->fx_4h` score `0.0596` n `47` status `ready` deltaP `14.1801` edge `-0.0039` maxDD `-1.8531`
- `news_risk_high->commodity_1h` score `0.0567` n `43` status `ready` deltaP `10.5347` edge `-0.0151` maxDD `-1.496`
- `news_risk_high->metal_4h` score `0.0231` n `43` status `ready` deltaP `4.8994` edge `0.0054` maxDD `-0.8085`
- `market_context_high->fx_1h` score `-0.0007` n `47` status `ready` deltaP `7.1155` edge `-0.0086` maxDD `-0.7804`
- `news_risk_high->crypto_alt_1h` score `-0.1502` n `43` status `ready` deltaP `6.8619` edge `0.0032` maxDD `-3.1233`
- `news_risk_high->index_1h` score `-0.1671` n `43` status `ready` deltaP `1.3926` edge `0.0016` maxDD `-0.5845`
- `market_context_high->crypto_alt_4h` score `-0.2048` n `47` status `ready` deltaP `2.2963` edge `0.049` maxDD `-4.9116`
- `news_risk_high->fx_1h` score `-0.2956` n `43` status `ready` deltaP `0.6336` edge `0.0034` maxDD `-0.2475`
- `news_risk_high->equity_1h` score `-0.4389` n `43` status `ready` deltaP `-0.4038` edge `0.0484` maxDD `-2.916`
- `news_risk_high->fx_4h` score `-0.5375` n `43` status `ready` deltaP `0.1276` edge `0.026` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `-0.5678` n `43` status `ready` deltaP `2.9592` edge `-0.0205` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.6911` n `40` status `ready` deltaP `0.6597` edge `0.036` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
