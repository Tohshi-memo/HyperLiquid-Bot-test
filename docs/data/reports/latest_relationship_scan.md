# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T19:52:27.272556+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8222`

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

- `market_context_high->unknown_24h` score `1380.8549` n `40` status `ready` deltaP `-22.0486` edge `115.2546` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `54.2284` n `88` status `ready` deltaP `-4.5316` edge `4.6073` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.7876` n `40` status `ready` deltaP `27.6736` edge `0.5907` maxDD `-1.0977`
- `market_context_high->unknown_1h` score `7.1682` n `100` status `ready` deltaP `-2.6886` edge `0.6489` maxDD `-1.0231`
- `market_context_high->index_24h` score `6.394` n `40` status `ready` deltaP `52.4306` edge `0.1833` maxDD `0.0`
- `market_context_high->fx_24h` score `3.169` n `40` status `ready` deltaP `35.9028` edge `0.0377` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.444` n `40` status `ready` deltaP `-21.1111` edge `0.5759` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.7797` n `88` status `ready` deltaP `12.8464` edge `0.0077` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.4757` n `88` status `ready` deltaP `11.6962` edge `0.015` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `0.4186` n `100` status `ready` deltaP `6.0599` edge `0.0979` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.3783` n `88` status `ready` deltaP `3.3537` edge `0.2367` maxDD `-11.1784`
- `market_context_high->commodity_1h` score `0.1687` n `100` status `ready` deltaP `5.509` edge `0.0057` maxDD `-0.6025`
- `market_context_high->crypto_alt_4h` score `0.0664` n `88` status `ready` deltaP `-0.6374` edge `0.2686` maxDD `-13.8008`
- `market_context_high->metal_4h` score `0.043` n `88` status `ready` deltaP `8.0932` edge `0.0219` maxDD `-1.1153`
- `market_context_high->fx_1h` score `-0.0674` n `100` status `ready` deltaP `2.6108` edge `0.0012` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.2162` n `100` status `ready` deltaP `5.6048` edge `0.0035` maxDD `-0.7107`
- `market_context_high->crypto_major_1h` score `-0.2248` n `100` status `ready` deltaP `0.4012` edge `0.0574` maxDD `-3.7778`
- `market_context_high->index_4h` score `-0.5304` n `88` status `ready` deltaP `-0.6236` edge `0.0062` maxDD `-0.9364`
- `market_context_high->index_1h` score `-0.7315` n `100` status `ready` deltaP `-4.0958` edge `-0.0014` maxDD `-0.5392`
- `market_context_high->equity_1h` score `-0.995` n `100` status `ready` deltaP `-6.4371` edge `0.0023` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
