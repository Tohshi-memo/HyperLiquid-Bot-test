# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T05:22:22.075513+00:00`
- Price records: `672`
- Market context records: `3147`
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

- `market_context_high->commodity_24h` score `14.2493` n `110` status `ready` deltaP `47.6799` edge `0.9124` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.9693` n `110` status `ready` deltaP `22.3705` edge `0.8971` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.7002` n `110` status `ready` deltaP `12.6799` edge `2.4131` maxDD `-71.142`
- `market_context_high->index_24h` score `6.6556` n `110` status `ready` deltaP `31.4899` edge `0.8988` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.8266` n `110` status `ready` deltaP `12.9483` edge `1.3741` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.8118` n `146` status `ready` deltaP `18.3324` edge `0.1579` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.181` n `146` status `ready` deltaP `4.4316` edge `0.0278` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.386` n `110` status `ready` deltaP `6.2247` edge `-0.0009` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.4016` n `146` status `ready` deltaP `6.0557` edge `0.1211` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.5249` n `146` status `ready` deltaP `3.4021` edge `0.0163` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8231` n `146` status `ready` deltaP `3.4882` edge `0.0198` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9897` n `146` status `ready` deltaP `3.2257` edge `0.0779` maxDD `-15.1032`
- `market_context_high->index_4h` score `-1.1488` n `146` status `ready` deltaP `11.719` edge `0.0655` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.1508` n `146` status `ready` deltaP `-11.0676` edge `-0.0055` maxDD `-0.7941`
- `market_context_high->fx_4h` score `-1.4883` n `146` status `ready` deltaP `-14.0745` edge `-0.0085` maxDD `-1.4115`
- `market_context_high->unknown_4h` score `-1.5997` n `146` status `ready` deltaP `6.0015` edge `0.0489` maxDD `-14.7778`
- `market_context_high->metal_1h` score `-2.0696` n `146` status `ready` deltaP `-4.3044` edge `-0.0044` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.7761` n `146` status `ready` deltaP `13.9283` edge `0.0818` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.909` n `146` status `ready` deltaP `19.1196` edge `0.4346` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.2088` n `146` status `ready` deltaP `1.3104` edge `-0.0735` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
