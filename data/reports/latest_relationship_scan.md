# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T09:22:28.857355+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2674`

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

- `market_context_high->unknown_1h` score `10040.5661` n `126` status `ready` deltaP `1.0146` edge `836.7269` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6121.3053` n `126` status `ready` deltaP `-0.3145` edge `510.1414` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `0.0276` n `111` status `ready` deltaP `24.9672` edge `0.9255` maxDD `-79.4062`
- `market_context_high->metal_1h` score `-0.1649` n `126` status `ready` deltaP `4.5504` edge `0.015` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2913` n `126` status `ready` deltaP `3.0082` edge `0.0038` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5115` n `126` status `ready` deltaP `11.7958` edge `0.0364` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3879` n `126` status `ready` deltaP `-8.8062` edge `-0.001` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7856` n `126` status `ready` deltaP `6.2874` edge `0.0152` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.8907` n `126` status `ready` deltaP `-6.4218` edge `0.002` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1913` n `126` status `ready` deltaP `-7.1738` edge `-0.0216` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.3945` n `126` status `ready` deltaP `-3.3367` edge `-0.014` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.5159` n `126` status `ready` deltaP `2.7088` edge `0.0041` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.2279` n `126` status `ready` deltaP `-4.0443` edge `-0.0143` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.3593` n `126` status `ready` deltaP `-1.1082` edge `0.1414` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-6.187` n `111` status `ready` deltaP `11.7164` edge `0.1146` maxDD `-46.6635`
- `market_context_high->fx_24h` score `-6.3529` n `111` status `ready` deltaP `-14.405` edge `-0.0057` maxDD `-5.5474`
- `market_context_high->commodity_4h` score `-6.8078` n `126` status `ready` deltaP `-17.9007` edge `-0.0787` maxDD `-15.5426`
- `market_context_high->crypto_alt_24h` score `-6.8513` n `111` status `ready` deltaP `12.4297` edge `0.5887` maxDD `-91.7339`
- `market_context_high->crypto_alt_4h` score `-7.5929` n `126` status `ready` deltaP `-1.8704` edge `0.061` maxDD `-46.5016`
- `market_context_high->index_24h` score `-13.0833` n `111` status `ready` deltaP `-26.539` edge `-0.1158` maxDD `-33.4706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
