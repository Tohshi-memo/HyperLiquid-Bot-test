# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T17:07:33.113371+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5915`

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

- `news_risk_high->unknown_24h` score `5190.5202` n `60` status `ready` deltaP `34.2345` edge `432.3572` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.8646` n `53` status `ready` deltaP `54.4979` edge `1.0818` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.4846` n `60` status `ready` deltaP `23.6077` edge `0.4427` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.6386` n `60` status `ready` deltaP `23.1504` edge `0.0846` maxDD `-0.191`
- `market_context_high->commodity_24h` score `2.1163` n `53` status `ready` deltaP `30.4307` edge `0.2543` maxDD `-10.2019`
- `news_risk_high->crypto_major_4h` score `1.318` n `60` status `ready` deltaP `7.8963` edge `0.1939` maxDD `-3.5385`
- `news_risk_high->equity_1h` score `0.9722` n `65` status `ready` deltaP `10.4652` edge `0.0792` maxDD `-2.7692`
- `news_risk_high->crypto_alt_4h` score `0.553` n `60` status `ready` deltaP `11.9817` edge `0.1302` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.5385` n `53` status `ready` deltaP `8.5855` edge `0.1075` maxDD `-5.323`
- `news_risk_high->crypto_alt_1h` score `0.5038` n `65` status `ready` deltaP `9.21` edge `0.0584` maxDD `-2.0834`
- `news_risk_high->fx_4h` score `0.2401` n `60` status `ready` deltaP `13.689` edge `0.0245` maxDD `-0.6604`
- `market_context_high->fx_4h` score `0.1971` n `53` status `ready` deltaP `13.406` edge `0.0155` maxDD `-1.3685`
- `news_risk_high->crypto_major_1h` score `0.1942` n `65` status `ready` deltaP `4.2953` edge `0.051` maxDD `-2.3794`
- `news_risk_high->metal_4h` score `0.1455` n `60` status `ready` deltaP `4.6748` edge `0.0351` maxDD `-0.8085`
- `news_risk_high->fx_1h` score `0.0154` n `65` status `ready` deltaP `4.445` edge `0.0046` maxDD `-0.2475`
- `market_context_high->fx_1h` score `-0.0149` n `53` status `ready` deltaP `7.2026` edge `0.001` maxDD `-0.6874`
- `news_risk_high->metal_1h` score `-0.0276` n `65` status `ready` deltaP `4.3782` edge `0.0076` maxDD `-0.5599`
- `news_risk_high->index_1h` score `-0.0608` n `65` status `ready` deltaP `2.3906` edge `0.0084` maxDD `-0.5702`
- `market_context_high->commodity_1h` score `-0.094` n `53` status `ready` deltaP `3.8781` edge `0.0162` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `-0.2027` n `53` status `ready` deltaP `4.4869` edge `0.0316` maxDD `-3.0005`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
