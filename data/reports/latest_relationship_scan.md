# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T05:37:22.775008+00:00`
- Price records: `672`
- Market context records: `3148`
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

- `market_context_high->commodity_24h` score `14.2685` n `110` status `ready` deltaP `47.6799` edge `0.914` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.9837` n `110` status `ready` deltaP `22.3705` edge `0.8983` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.6366` n `110` status `ready` deltaP `12.5063` edge `2.4061` maxDD `-71.142`
- `market_context_high->index_24h` score `6.6431` n `110` status `ready` deltaP `31.4899` edge `0.8972` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.8032` n `110` status `ready` deltaP `12.9483` edge `1.3711` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.83` n `146` status `ready` deltaP `18.4848` edge `0.1584` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1822` n `146` status `ready` deltaP `4.4316` edge `0.0279` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.3872` n `110` status `ready` deltaP `6.2247` edge `-0.001` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.4187` n `146` status `ready` deltaP `5.906` edge `0.1199` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.5343` n `146` status `ready` deltaP `3.2524` edge `0.0161` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8262` n `146` status `ready` deltaP `3.4882` edge `0.0194` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.0084` n `146` status `ready` deltaP `3.076` edge `0.0765` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1508` n `146` status `ready` deltaP `-11.0676` edge `-0.0055` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.1622` n `146` status `ready` deltaP `11.5666` edge `0.0648` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4883` n `146` status `ready` deltaP `-14.0745` edge `-0.0085` maxDD `-1.4115`
- `market_context_high->unknown_4h` score `-1.5985` n `146` status `ready` deltaP `6.0015` edge `0.049` maxDD `-14.7778`
- `market_context_high->metal_1h` score `-2.0839` n `146` status `ready` deltaP `-4.4541` edge `-0.0046` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.7776` n `146` status `ready` deltaP `13.9283` edge `0.0816` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.9344` n `146` status `ready` deltaP `18.9671` edge `0.4335` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.2016` n `146` status `ready` deltaP `1.3104` edge `-0.0729` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
