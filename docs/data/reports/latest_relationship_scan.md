# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T19:52:27.725541+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2804`

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

- `market_context_high->unknown_1h` score `10152.8993` n `126` status `ready` deltaP `1.4638` edge `846.085` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6197.7621` n `126` status `ready` deltaP `-0.3145` edge `516.5128` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.6978` n `108` status `ready` deltaP `26.794` edge `1.1022` maxDD `-57.8734`
- `market_context_high->crypto_alt_24h` score `-0.0475` n `108` status `ready` deltaP `13.8311` edge `0.8939` maxDD `-72.5383`
- `market_context_high->metal_1h` score `-0.1672` n `126` status `ready` deltaP `4.4007` edge `0.0157` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2493` n `126` status `ready` deltaP `3.7567` edge `0.0042` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5003` n `126` status `ready` deltaP `12.1007` edge `0.0358` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3975` n `126` status `ready` deltaP `-8.8062` edge `-0.0018` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.716` n `126` status `ready` deltaP `6.4371` edge `0.02` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9903` n `126` status `ready` deltaP `-7.9462` edge `-0.0006` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.238` n `126` status `ready` deltaP `-7.7726` edge `-0.0215` maxDD `-4.3877`
- `market_context_high->crypto_major_1h` score `-2.3096` n `126` status `ready` deltaP `3.0082` edge `0.0193` maxDD `-13.8788`
- `market_context_high->index_4h` score `-2.3406` n `126` status `ready` deltaP `-2.4221` edge `-0.0156` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.0216` n `126` status `ready` deltaP `-2.9964` edge `-0.0041` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.1649` n `126` status `ready` deltaP `1.0259` edge `0.1521` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.8586` n `108` status `ready` deltaP `12.963` edge `0.1147` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.7713` n `108` status `ready` deltaP `-18.8658` edge `-0.0112` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.8838` n `126` status `ready` deltaP `-20.0348` edge `-0.0708` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.0494` n `126` status `ready` deltaP `1.7881` edge `0.0819` maxDD `-46.5016`
- `market_context_high->index_24h` score `-13.1256` n `108` status `ready` deltaP `-26.3888` edge `-0.1549` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
