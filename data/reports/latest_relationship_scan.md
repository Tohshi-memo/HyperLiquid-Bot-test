# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T00:52:26.168210+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2736`

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

- `market_context_high->unknown_1h` score `10118.2817` n `126` status `ready` deltaP `1.314` edge `843.2012` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6162.8841` n `126` status `ready` deltaP `-0.3145` edge `513.6063` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.1315` n `108` status `ready` deltaP `26.794` edge `1.0296` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.2288` n `126` status `ready` deltaP `3.3528` edge `0.0148` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2571` n `126` status `ready` deltaP `3.607` edge `0.0042` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5621` n `126` status `ready` deltaP `11.0336` edge `0.035` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3963` n `126` status `ready` deltaP `-8.8062` edge `-0.0017` maxDD `-0.4757`
- `market_context_high->crypto_alt_24h` score `-1.4275` n `108` status `ready` deltaP `13.8311` edge `0.7789` maxDD `-72.5383`
- `market_context_high->equity_1h` score `-1.8886` n `126` status `ready` deltaP `5.3892` edge `0.0126` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9887` n `126` status `ready` deltaP `-7.9462` edge `-0.0004` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1985` n `126` status `ready` deltaP `-7.1738` edge `-0.0222` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.3641` n `126` status `ready` deltaP `-3.0318` edge `-0.0135` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.4955` n `126` status `ready` deltaP `2.7088` edge `0.0058` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.1908` n `126` status `ready` deltaP `-3.4455` edge `-0.0152` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.5336` n `126` status `ready` deltaP `-0.6509` edge `0.116` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.6642` n `108` status `ready` deltaP `12.963` edge `0.1309` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.8269` n `108` status `ready` deltaP `-19.5602` edge `-0.0112` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.9918` n `126` status `ready` deltaP `-20.0348` edge `-0.0798` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.7121` n `126` status `ready` deltaP `-0.3461` edge `0.0409` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.894` n `108` status `ready` deltaP `-26.3888` edge `-0.1356` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
