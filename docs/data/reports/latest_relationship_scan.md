# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T00:09:42.910726+00:00`
- Price records: `672`
- Market context records: `6444`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.5789` n `32` status `ready` deltaP `29.5139` edge `0.7829` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `9.0168` n `145` status `ready` deltaP `21.1698` edge `0.9403` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.351` n `32` status `ready` deltaP `52.7778` edge `0.1774` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1096` n `32` status `ready` deltaP `42.7591` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.9716` n `32` status `ready` deltaP `34.2014` edge `0.1235` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.2121` n `32` status `ready` deltaP `11.1111` edge `0.4157` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4206` n `32` status `ready` deltaP `29.1916` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.542` n `32` status `ready` deltaP `14.128` edge `0.1502` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.049` n `185` status `ready` deltaP `-5.8173` edge `0.2163` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.9215` n `32` status `ready` deltaP `10.1235` edge `0.0968` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.0297` n `185` status `ready` deltaP `7.0213` edge `0.0233` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.1493` n `32` status `ready` deltaP `6.5307` edge `-0.0215` maxDD `-0.7581`
- `market_context_high->metal_4h` score `-0.2372` n `185` status `ready` deltaP `7.2833` edge `0.0405` maxDD `-2.7056`
- `news_risk_high->metal_1h` score `-0.5309` n `32` status `ready` deltaP `0.8982` edge `-0.0243` maxDD `-1.6464`
- `market_context_high->unknown_4h` score `-0.5439` n `185` status `ready` deltaP `-15.1286` edge `0.2961` maxDD `-10.5788`
- `market_context_high->metal_1h` score `-0.5919` n `185` status `ready` deltaP `0.0874` edge `0.0013` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.6012` n `185` status `ready` deltaP `-0.7444` edge `-0.0038` maxDD `-2.1314`
- `market_context_high->equity_4h` score `-0.622` n `185` status `ready` deltaP `6.4107` edge `0.0474` maxDD `-8.2573`
- `market_context_high->commodity_24h` score `-0.6353` n `145` status `ready` deltaP `1.5505` edge `0.1287` maxDD `-5.6914`
- `news_risk_high->index_24h` score `-0.6719` n `32` status `ready` deltaP `1.5625` edge `-0.0094` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
