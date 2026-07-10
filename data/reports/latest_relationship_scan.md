# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T22:37:25.862781+00:00`
- Price records: `672`
- Market context records: `6329`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.4734` n `32` status `ready` deltaP `43.2292` edge `1.016` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.068` n `32` status `ready` deltaP `50.6944` edge `0.1677` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4339` n `32` status `ready` deltaP `16.6667` edge `0.5353` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2045` n `32` status `ready` deltaP `43.8262` edge `0.0628` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.3911` n `32` status `ready` deltaP `30.0347` edge `0.1029` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4374` n `32` status `ready` deltaP `29.3413` edge `0.0214` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5201` n `32` status `ready` deltaP `14.8765` edge `0.1424` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9416` n `32` status `ready` deltaP `11.7702` edge `0.0884` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.1517` n `196` status `ready` deltaP `10.4343` edge `0.0394` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `-0.0542` n `208` status `ready` deltaP `-8.2508` edge `0.1513` maxDD `-3.7317`
- `market_context_high->index_4h` score `-0.2118` n `196` status `ready` deltaP `5.6962` edge `0.0206` maxDD `-0.8584`
- `market_context_high->metal_1h` score `-0.3324` n `208` status `ready` deltaP `4.9113` edge `0.0024` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.3443` n `147` status `ready` deltaP `18.3` edge `0.0907` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.5283` n `208` status `ready` deltaP `-1.9087` edge `-0.0021` maxDD `-0.8993`
- `market_context_high->index_1h` score `-0.5485` n `208` status `ready` deltaP `-3.1207` edge `0.0024` maxDD `-0.8198`
- `market_context_high->commodity_1h` score `-0.5897` n `208` status `ready` deltaP `-1.0796` edge `-0.0001` maxDD `-2.1314`
- `news_risk_high->index_24h` score `-0.6074` n `32` status `ready` deltaP `2.0833` edge `-0.0046` maxDD `-2.3058`
- `news_risk_high->unknown_1h` score `-0.7348` n `32` status `ready` deltaP `5.9319` edge `-0.0663` maxDD `-0.7581`
- `market_context_high->equity_4h` score `-0.7393` n `196` status `ready` deltaP `4.6043` edge `0.0444` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.7792` n `32` status `ready` deltaP `-3.7425` edge `-0.0252` maxDD `-1.6464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
