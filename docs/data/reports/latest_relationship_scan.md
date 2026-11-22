# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T04:52:31.410169+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4576`

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

- `market_context_high->unknown_1h` score `9960.616` n `124` status `ready` deltaP `1.1927` edge `830.0632` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `5993.863` n `124` status `ready` deltaP `-0.7474` edge `499.5241` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.3458` n `124` status `ready` deltaP `3.8342` edge `0.0121` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.5526` n `124` status `ready` deltaP `0.6326` edge `0.0026` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8579` n `124` status `ready` deltaP `7.4891` edge `0.0207` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.409` n `124` status `ready` deltaP `-9.011` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8024` n `124` status `ready` deltaP `-4.6961` edge `0.0018` maxDD `-1.7927`
- `market_context_high->equity_1h` score `-1.9938` n `124` status `ready` deltaP `3.9502` edge `0.0051` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3529` n `124` status `ready` deltaP `-9.0448` edge `-0.0226` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.8382` n `124` status `ready` deltaP `-7.8924` edge `-0.0206` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.2073` n `124` status `ready` deltaP `-0.3236` edge `-0.0333` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.9444` n `124` status `ready` deltaP `-7.0166` edge `-0.0542` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.8543` n `124` status `ready` deltaP `-4.2535` edge `-0.0293` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-5.9028` n `124` status `ready` deltaP `-8.1037` edge `-0.0006` maxDD `-6.9819`
- `market_context_high->crypto_alt_4h` score `-6.3246` n `124` status `ready` deltaP `-4.406` edge `-0.1002` maxDD `-46.5016`
- `market_context_high->commodity_4h` score `-6.9492` n `124` status `ready` deltaP `-19.4728` edge `-0.08` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-8.1541` n `124` status `ready` deltaP `3.7186` edge `0.1053` maxDD `-52.1012`
- `market_context_high->crypto_major_24h` score `-13.0407` n `124` status `ready` deltaP `12.8137` edge `0.3027` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.0504` n `124` status `ready` deltaP `-27.677` edge `-0.1259` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.7241` n `124` status `ready` deltaP `3.5562` edge `0.0786` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
