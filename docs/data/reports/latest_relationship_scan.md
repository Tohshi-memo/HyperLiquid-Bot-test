# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T18:07:29.573340+00:00`
- Price records: `672`
- Market context records: `2787`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `3.2055` n `142` status `ready` deltaP `6.0739` edge `0.2731` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.6146` n `142` status `ready` deltaP `3.7437` edge `0.5846` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8508` n `142` status `ready` deltaP `6.1856` edge `0.135` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.5473` n `142` status `ready` deltaP `11.0377` edge `0.2814` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.2955` n `142` status `ready` deltaP `12.996` edge `0.0354` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0898` n `142` status `ready` deltaP `4.198` edge `0.0099` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.0937` n `142` status `ready` deltaP `3.732` edge `0.0404` maxDD `-3.1801`
- `market_context_high->fx_1h` score `-0.549` n `142` status `ready` deltaP `-0.6873` edge `0.0032` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6271` n `142` status `ready` deltaP `0.5819` edge `0.0003` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.7044` n `142` status `ready` deltaP `-1.031` edge `-0.0081` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.735` n `142` status `ready` deltaP `4.7968` edge `0.0498` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.9498` n `142` status `ready` deltaP `3.6266` edge `0.041` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0262` n `142` status `ready` deltaP `-3.1985` edge `0.0191` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1069` n `142` status `ready` deltaP `-3.2957` edge `0.0076` maxDD `-0.5631`
- `market_context_high->equity_4h` score `-1.278` n `142` status `ready` deltaP `1.8099` edge `0.0194` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-1.3297` n `142` status `ready` deltaP `14.1854` edge `0.2287` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.4436` n `142` status `ready` deltaP `-1.7116` edge `-0.0217` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.653` n `142` status `ready` deltaP `-0.6012` edge `-0.0159` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.1323` n `142` status `ready` deltaP `-0.6183` edge `-0.0142` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4184` n `142` status `ready` deltaP `5.7347` edge `0.1423` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
