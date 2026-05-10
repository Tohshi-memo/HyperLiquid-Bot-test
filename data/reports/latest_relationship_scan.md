# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T08:52:19.935155+00:00`
- Price records: `672`
- Market context records: `958`
- Flow alert records: `2686`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `14.8713` n `157` status `ready` deltaP `33.1` edge `1.052` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `8.8531` n `157` status `ready` deltaP `9.5486` edge `0.6741` maxDD `0.0`
- `market_context_high->equity_24h` score `1.1547` n `157` status `ready` deltaP `2.0701` edge `0.3429` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.4096` n `157` status `ready` deltaP `0.6215` edge `0.2295` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.3277` n `204` status `ready` deltaP `2.3805` edge `0.0376` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3926` n `204` status `ready` deltaP `1.0098` edge `0.001` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.5752` n `204` status `ready` deltaP `1.8199` edge `0.0168` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.7291` n `204` status `ready` deltaP `2.8942` edge `0.0053` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-1.0345` n `192` status `ready` deltaP `1.7149` edge `0.002` maxDD `-1.6381`
- `market_context_high->equity_4h` score `-1.2159` n `192` status `ready` deltaP `2.6677` edge `0.0961` maxDD `-10.5498`
- `market_context_high->unknown_1h` score `-1.3581` n `204` status `ready` deltaP `-2.9412` edge `-0.0164` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.5035` n `192` status `ready` deltaP `-0.0635` edge `0.0274` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.5954` n `204` status `ready` deltaP `6.4283` edge `-0.0035` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.8804` n `204` status `ready` deltaP `1.5704` edge `-0.0232` maxDD `-8.1842`
- `market_context_high->metal_1h` score `-1.8962` n `204` status `ready` deltaP `-2.5155` edge `-0.0304` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-2.3827` n `192` status `ready` deltaP `-0.7749` edge `0.0817` maxDD `-13.0076`
- `market_context_high->crypto_major_4h` score `-2.4461` n `192` status `ready` deltaP `8.9939` edge `0.1068` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-3.3024` n `192` status `ready` deltaP `-2.2485` edge `0.0176` maxDD `-15.2248`
- `market_context_high->unknown_4h` score `-3.3564` n `192` status `ready` deltaP `6.2881` edge `-0.1338` maxDD `-8.3588`
- `market_context_high->unknown_24h` score `-4.1497` n `157` status `ready` deltaP `6.6393` edge `-0.0257` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
