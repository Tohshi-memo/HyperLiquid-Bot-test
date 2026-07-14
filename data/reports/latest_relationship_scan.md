# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T23:52:25.259051+00:00`
- Price records: `672`
- Market context records: `6761`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `1.0589` n `176` status `ready` deltaP `0.5366` edge `0.5074` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `-0.0341` n `176` status `ready` deltaP `7.5021` edge `0.0316` maxDD `-4.2122`
- `market_context_high->commodity_24h` score `-0.0694` n `176` status `ready` deltaP `7.9704` edge `0.1279` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.1627` n `176` status `ready` deltaP `5.1987` edge `0.0282` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3641` n `176` status `ready` deltaP `0.1837` edge `0.0006` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.5783` n `176` status `ready` deltaP `0.296` edge `-0.0078` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5905` n `176` status `ready` deltaP `-0.7179` edge `0.0005` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.7152` n `176` status `ready` deltaP `-5.2906` edge `-0.0039` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.104` n `176` status `ready` deltaP `3.7051` edge `-0.014` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.2003` n `176` status `ready` deltaP `7.8437` edge `0.0002` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.2389` n `176` status `ready` deltaP `6.2916` edge `-0.0128` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.4061` n `176` status `ready` deltaP `-1.4689` edge `-0.0215` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7957` n `176` status `ready` deltaP `-7.1754` edge `-0.0117` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.5363` n `176` status `ready` deltaP `3.6585` edge `-0.0181` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.6571` n `176` status `ready` deltaP `2.6746` edge `-0.0183` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.6896` n `176` status `ready` deltaP `-6.7766` edge `-0.0136` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.5577` n `176` status `ready` deltaP `-15.2578` edge `0.0418` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.2151` n `176` status `ready` deltaP `2.7023` edge `-0.1315` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.2325` n `176` status `ready` deltaP `-7.1812` edge `-0.0012` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.4811` n `176` status `ready` deltaP `-13.6364` edge `-0.1479` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
