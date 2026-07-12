# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T07:37:32.874135+00:00`
- Price records: `672`
- Market context records: `6476`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5863`

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

- `news_risk_high->crypto_alt_24h` score `12.4672` n `32` status `ready` deltaP `33.5069` edge `0.8303` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.1429` n `153` status `ready` deltaP `17.065` edge `0.8115` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.4155` n `32` status `ready` deltaP `53.2986` edge `0.1793` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.1361` n `32` status `ready` deltaP `15.7986` edge `0.5029` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9288` n `34` status `ready` deltaP `40.9792` edge `0.0588` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.2018` n `32` status `ready` deltaP `29.5139` edge `0.0906` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `2.0398` n `174` status `ready` deltaP `-4.5925` edge `0.2907` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.8071` n `38` status `ready` deltaP `22.6127` edge `0.0179` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.5808` n `38` status `ready` deltaP `5.0504` edge `0.0945` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.4465` n `172` status `ready` deltaP `11.4968` edge `0.0282` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.3089` n `172` status `ready` deltaP `-15.0879` edge `0.3669` maxDD `-10.5788`
- `market_context_high->crypto_alt_4h` score `0.1956` n `172` status `ready` deltaP `8.2459` edge `0.1167` maxDD `-6.7632`
- `market_context_high->commodity_24h` score `0.1916` n `153` status `ready` deltaP `5.9232` edge `0.1633` maxDD `-5.2791`
- `market_context_high->metal_4h` score `0.1201` n `172` status `ready` deltaP `11.284` edge `0.0436` maxDD `-2.7056`
- `news_risk_high->crypto_alt_1h` score `0.0921` n `38` status `ready` deltaP `1.7334` edge `0.0512` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.4602` n `32` status `ready` deltaP `4.6875` edge `-0.0031` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4895` n `174` status `ready` deltaP `2.0717` edge `0.0012` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.4957` n `172` status `ready` deltaP `7.8346` edge `0.0541` maxDD `-8.2573`
- `news_risk_high->unknown_1h` score `-0.5012` n `38` status `ready` deltaP `4.4516` edge `-0.0343` maxDD `-0.9718`
- `market_context_high->commodity_1h` score `-0.5732` n `174` status `ready` deltaP `-0.222` edge `-0.0037` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
