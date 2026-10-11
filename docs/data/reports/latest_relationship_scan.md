# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T18:22:34.827456+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8174`

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

- `market_context_high->unknown_24h` score `1381.0703` n `40` status `ready` deltaP `-21.0069` edge `115.2656` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `58.8902` n `82` status `ready` deltaP `-5.9451` edge `5.0052` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `9.5601` n `94` status `ready` deltaP `-2.1149` edge `0.8444` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.7984` n `40` status `ready` deltaP `27.6736` edge `0.5916` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.388` n `40` status `ready` deltaP `52.4306` edge `0.1828` maxDD `0.0`
- `market_context_high->fx_24h` score `3.2679` n `40` status `ready` deltaP `36.9444` edge `0.039` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.5709` n `40` status `ready` deltaP `-20.5903` edge `0.583` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.8166` n `82` status `ready` deltaP `13.2622` edge `0.008` maxDD `-0.2692`
- `market_context_high->crypto_alt_1h` score `0.6307` n `94` status `ready` deltaP `6.9117` edge `0.1099` maxDD `-4.9401`
- `market_context_high->commodity_4h` score `0.2675` n `82` status `ready` deltaP `9.6037` edge `0.0116` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `-0.0359` n `94` status `ready` deltaP `1.8442` edge `0.0736` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.0379` n `94` status `ready` deltaP `3.1055` edge `0.0045` maxDD `-0.6025`
- `market_context_high->fx_1h` score `-0.0757` n `94` status `ready` deltaP `2.5067` edge `0.0012` maxDD `-0.271`
- `market_context_high->crypto_major_4h` score `-0.0912` n `82` status `ready` deltaP `-0.3048` edge `0.2009` maxDD `-11.1784`
- `market_context_high->metal_4h` score `-0.1995` n `82` status `ready` deltaP `5.183` edge `0.0211` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.2053` n `94` status `ready` deltaP `5.6663` edge `0.004` maxDD `-0.7107`
- `market_context_high->crypto_alt_4h` score `-0.403` n `82` status `ready` deltaP `-3.9634` edge `0.2306` maxDD `-13.8008`
- `market_context_high->index_1h` score `-0.636` n `94` status `ready` deltaP `-2.2455` edge `-0.0015` maxDD `-0.5392`
- `market_context_high->index_4h` score `-0.7283` n `82` status `ready` deltaP `-4.1158` edge `0.0041` maxDD `-0.9364`
- `market_context_high->equity_1h` score `-0.9093` n `94` status `ready` deltaP `-4.9082` edge `0.0031` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
