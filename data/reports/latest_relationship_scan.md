# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T19:22:28.033252+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8226`

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

- `market_context_high->unknown_24h` score `1380.9307` n `40` status `ready` deltaP `-21.7014` edge `115.2586` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `55.9625` n `86` status `ready` deltaP `-4.9808` edge `4.7548` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.7924` n `40` status `ready` deltaP `27.6736` edge `0.5911` maxDD `-1.0977`
- `market_context_high->unknown_1h` score `7.8956` n `98` status `ready` deltaP `-2.1172` edge `0.7057` maxDD `-1.0231`
- `market_context_high->index_24h` score `6.3916` n `40` status `ready` deltaP `52.4306` edge `0.1831` maxDD `0.0`
- `market_context_high->fx_24h` score `3.2016` n `40` status `ready` deltaP `36.25` edge `0.0381` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.4831` n `40` status `ready` deltaP `-20.9375` edge `0.578` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.7461` n `86` status `ready` deltaP `12.4114` edge `0.0078` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.4284` n `86` status `ready` deltaP `11.1352` edge `0.0148` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `0.3405` n `98` status `ready` deltaP `5.4137` edge `0.0957` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.2765` n `86` status `ready` deltaP `2.1909` edge `0.2314` maxDD `-11.1784`
- `market_context_high->commodity_1h` score `0.0986` n `98` status `ready` deltaP `4.6927` edge `0.0053` maxDD `-0.6025`
- `market_context_high->fx_1h` score `0.0285` n `98` status `ready` deltaP `3.7945` edge `0.0013` maxDD `-0.271`
- `market_context_high->metal_4h` score `-0.0346` n `86` status `ready` deltaP `7.1682` edge `0.0216` maxDD `-1.1153`
- `market_context_high->crypto_alt_4h` score `-0.0432` n `86` status `ready` deltaP `-1.6945` edge `0.2616` maxDD `-13.8008`
- `market_context_high->crypto_major_1h` score `-0.2237` n `98` status `ready` deltaP `0.2719` edge `0.0584` maxDD `-3.7778`
- `market_context_high->metal_1h` score `-0.286` n `98` status `ready` deltaP `4.7477` edge `0.0034` maxDD `-0.7107`
- `market_context_high->index_4h` score `-0.5935` n `86` status `ready` deltaP `-1.7335` edge `0.0055` maxDD `-0.9364`
- `market_context_high->index_1h` score `-0.7429` n `98` status `ready` deltaP `-4.2863` edge `-0.0016` maxDD `-0.5392`
- `market_context_high->equity_1h` score `-1.0075` n `98` status `ready` deltaP `-6.5868` edge `0.0017` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
