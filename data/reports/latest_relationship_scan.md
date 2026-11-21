# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T23:37:27.271319+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `32`

- Symbol pattern count: `3600`

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

- `market_context_high->unknown_1h` score `9950.5733` n `126` status `ready` deltaP `1.1643` edge `829.2265` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6019.2577` n `126` status `ready` deltaP `-0.9243` edge `501.6415` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2631` n `126` status `ready` deltaP `3.2031` edge `0.0114` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4603` n `126` status `ready` deltaP `0.0142` edge `0.0021` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.9651` n `126` status `ready` deltaP `5.6983` edge `0.0189` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4406` n `126` status `ready` deltaP `-9.405` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.878` n `126` status `ready` deltaP `-6.1169` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.2914` n `126` status `ready` deltaP `2.3952` edge `-0.001` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3805` n `126` status `ready` deltaP `-9.4193` edge `-0.0224` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.9285` n `126` status `ready` deltaP `-8.977` edge `-0.0209` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.6265` n `126` status `ready` deltaP `-1.1834` edge `-0.0625` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-4.2749` n `126` status `ready` deltaP `-7.6371` edge `-0.0776` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-6.1856` n `126` status `ready` deltaP `-10.2183` edge `-0.0014` maxDD `-7.0088`
- `market_context_high->crypto_major_4h` score `-6.8619` n `126` status `ready` deltaP `-7.2058` edge `-0.1388` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-7.1013` n `126` status `ready` deltaP `-21.2543` edge `-0.0808` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-8.0548` n `126` status `ready` deltaP `4.9603` edge `0.1053` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.8921` n `126` status `ready` deltaP `-6.9009` edge `-0.1804` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.982` n `126` status `ready` deltaP `13.4921` edge `0.3057` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8483` n `126` status `ready` deltaP `-26.1409` edge `-0.1193` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.8704` n `126` status `ready` deltaP `3.4722` edge `0.0604` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
