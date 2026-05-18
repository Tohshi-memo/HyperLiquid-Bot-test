# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T01:37:15.079967+00:00`
- Price records: `672`
- Market context records: `1071`
- Flow alert records: `4988`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8669`

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

- `market_context_high->crypto_major_24h` score `15.8412` n `166` status `ready` deltaP `34.7484` edge `1.1348` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.4227` n `166` status `ready` deltaP `11.9394` edge `0.4957` maxDD `-9.5387`
- `market_context_high->equity_24h` score `4.8084` n `166` status `ready` deltaP `13.6439` edge `0.3594` maxDD `-3.6396`
- `market_context_high->index_24h` score `4.096` n `166` status `ready` deltaP `14.1798` edge `0.2776` maxDD `-2.1308`
- `market_context_high->metal_24h` score `3.8809` n `166` status `ready` deltaP `-3.1913` edge `0.5114` maxDD `-6.3373`
- `market_context_high->equity_4h` score `1.1633` n `168` status `ready` deltaP `6.671` edge `0.1313` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `0.6772` n `168` status `ready` deltaP `11.3603` edge `0.1493` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.5436` n `168` status `ready` deltaP `5.2047` edge `0.0789` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.2673` n `170` status `ready` deltaP `6.5058` edge `0.0207` maxDD `-1.3437`
- `market_context_high->fx_1h` score `-0.1009` n `170` status `ready` deltaP `5.5301` edge `0.0003` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.2001` n `170` status `ready` deltaP `7.7545` edge `0.024` maxDD `-5.3898`
- `market_context_high->equity_1h` score `-0.2412` n `170` status `ready` deltaP `1.1905` edge `0.038` maxDD `-3.6162`
- `market_context_high->metal_1h` score `-0.4347` n `170` status `ready` deltaP `5.627` edge `-0.0186` maxDD `-3.3044`
- `market_context_high->fx_4h` score `-0.7091` n `168` status `ready` deltaP `0.9799` edge `0.0022` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.8735` n `170` status `ready` deltaP `-0.5565` edge `0.0117` maxDD `-3.7959`
- `market_context_high->crypto_alt_1h` score `-0.9264` n `170` status `ready` deltaP `1.9479` edge `0.0184` maxDD `-5.3538`
- `market_context_high->crypto_alt_4h` score `-1.0744` n `168` status `ready` deltaP `5.1756` edge `0.1264` maxDD `-13.0347`
- `market_context_high->metal_4h` score `-2.1238` n `168` status `ready` deltaP `3.0342` edge `-0.0971` maxDD `-9.2991`
- `market_context_high->fx_24h` score `-3.0345` n `166` status `ready` deltaP `5.8951` edge `-0.0207` maxDD `-19.2774`
- `market_context_high->unknown_4h` score `-4.0341` n `168` status `ready` deltaP `7.2662` edge `-0.2325` maxDD `-6.8363`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
