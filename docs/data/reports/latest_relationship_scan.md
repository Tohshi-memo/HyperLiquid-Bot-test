# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T18:52:26.357617+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2652`

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

- `market_context_high->unknown_1h` score `9988.3193` n `126` status `ready` deltaP `1.1643` edge `832.372` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6043.6433` n `126` status `ready` deltaP `-0.6194` edge `503.6716` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2771` n `126` status `ready` deltaP `2.754` edge `0.0126` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.384` n `126` status `ready` deltaP `1.3615` edge `0.0029` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.846` n `126` status `ready` deltaP `7.2227` edge `0.024` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4525` n `126` status `ready` deltaP `-9.5547` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8859` n `126` status `ready` deltaP `-6.2693` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.1392` n `126` status `ready` deltaP `3.5928` edge `0.0037` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3973` n `126` status `ready` deltaP `-9.569` edge `-0.0228` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.7838` n `126` status `ready` deltaP `-7.4526` edge `-0.019` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.2247` n `126` status `ready` deltaP `0.1639` edge `-0.038` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.9127` n `126` status `ready` deltaP `-6.4395` edge `-0.0554` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-6.2124` n `126` status `ready` deltaP `-5.529` edge `-0.0667` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4577` n `126` status `ready` deltaP `-13.1697` edge `-0.0044` maxDD `-7.0088`
- `market_context_high->commodity_4h` score `-7.1023` n `126` status `ready` deltaP `-21.1019` edge `-0.0819` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.8456` n `126` status `ready` deltaP `6.8701` edge `0.11` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.3587` n `126` status `ready` deltaP `-6.4436` edge `-0.139` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.5678` n `126` status `ready` deltaP `14.7073` edge `0.3507` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8039` n `126` status `ready` deltaP `-26.1409` edge `-0.1156` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.843` n `126` status `ready` deltaP `3.8194` edge `0.0616` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
