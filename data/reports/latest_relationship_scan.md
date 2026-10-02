# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T23:37:37.064169+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `364.1302` n `50` status `ready` deltaP `10.7246` edge `30.2776` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.8863` n `50` status `ready` deltaP `10.8232` edge `24.2517` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.6774` n `70` status `ready` deltaP `40.4663` edge `1.1409` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `10.6668` n `50` status `ready` deltaP `20.1806` edge `0.9247` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.1862` n `70` status `ready` deltaP `33.7351` edge `0.5891` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.045` n `50` status `ready` deltaP `31.8264` edge `0.6832` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.8275` n `50` status `ready` deltaP `19.2195` edge `0.5945` maxDD `-3.294`
- `news_risk_high->crypto_alt_4h` score `6.8365` n `111` status `ready` deltaP `26.6878` edge `0.5262` maxDD `-6.4195`
- `market_context_high->crypto_alt_4h` score `6.2981` n `50` status `ready` deltaP `17.4085` edge `0.5377` maxDD `-7.6465`
- `market_context_high->crypto_alt_1h` score `3.3357` n `50` status `ready` deltaP `15.2515` edge `0.2426` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.0696` n `50` status `ready` deltaP `13.8503` edge `0.2085` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `2.8875` n `111` status `ready` deltaP `24.3738` edge `0.1394` maxDD `-2.9013`
- `market_context_high->fx_4h` score `2.7909` n `50` status `ready` deltaP `31.1646` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->crypto_major_24h` score `2.7482` n `70` status `ready` deltaP `8.3978` edge `0.5374` maxDD `-11.6179`
- `news_risk_high->crypto_major_4h` score `2.3606` n `111` status `ready` deltaP `18.7871` edge `0.3656` maxDD `-8.7232`
- `news_risk_high->metal_24h` score `1.4548` n `70` status `ready` deltaP `14.6528` edge `0.2149` maxDD `-2.0853`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.3053` n `50` status `ready` deltaP `6.0208` edge `0.3134` maxDD `-11.8957`
- `news_risk_high->crypto_alt_1h` score `1.1578` n `111` status `ready` deltaP `5.1074` edge `0.1185` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.0146` n `50` status `ready` deltaP `20.6806` edge `0.094` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
