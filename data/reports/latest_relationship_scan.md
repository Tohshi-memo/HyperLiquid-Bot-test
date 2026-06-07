# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T05:52:25.354731+00:00`
- Price records: `672`
- Market context records: `3149`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8008`

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

- `market_context_high->commodity_24h` score `14.2853` n `110` status `ready` deltaP `47.6799` edge `0.9154` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.9825` n `110` status `ready` deltaP `22.3705` edge `0.8982` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.5983` n `110` status `ready` deltaP `12.5063` edge `2.4012` maxDD `-71.142`
- `market_context_high->index_24h` score `6.6346` n `110` status `ready` deltaP `31.4899` edge `0.8961` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.7845` n `110` status `ready` deltaP `12.9483` edge `1.3687` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.8458` n `146` status `ready` deltaP `18.6372` edge `0.1587` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.181` n `146` status `ready` deltaP `4.4316` edge `0.0278` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.4035` n `110` status `ready` deltaP `6.0511` edge `-0.0012` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.4234` n `146` status `ready` deltaP `5.906` edge `0.1193` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.5265` n `146` status `ready` deltaP `3.4021` edge `0.0161` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.827` n `146` status `ready` deltaP `3.4882` edge `0.0193` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.024` n `146` status `ready` deltaP `2.9263` edge `0.0755` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1431` n `146` status `ready` deltaP `-10.9179` edge `-0.0055` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.1748` n `146` status `ready` deltaP `11.4142` edge `0.0642` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4804` n `146` status `ready` deltaP `-13.9221` edge `-0.0085` maxDD `-1.4115`
- `market_context_high->unknown_4h` score `-1.578` n `146` status `ready` deltaP `6.1539` edge `0.0497` maxDD `-14.7778`
- `market_context_high->metal_1h` score `-2.0983` n `146` status `ready` deltaP `-4.6038` edge `-0.0048` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.78` n `146` status `ready` deltaP `13.9283` edge `0.0813` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.9538` n `146` status `ready` deltaP `18.8147` edge `0.4329` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1932` n `146` status `ready` deltaP `1.3104` edge `-0.0722` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
