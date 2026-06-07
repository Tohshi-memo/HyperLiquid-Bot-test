# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T01:37:20.380018+00:00`
- Price records: `672`
- Market context records: `3132`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7125`

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

- `market_context_high->commodity_24h` score `14.2682` n `106` status `ready` deltaP `47.5858` edge `0.9146` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.7729` n `106` status `ready` deltaP `21.1314` edge `0.889` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `10.7714` n `106` status `ready` deltaP `10.0727` edge `2.3114` maxDD `-71.142`
- `market_context_high->index_24h` score `6.461` n `106` status `ready` deltaP `30.703` edge `0.8791` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.338` n `106` status `ready` deltaP `10.8556` edge `1.3254` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.0911` n `135` status `ready` deltaP `20.3083` edge `0.168` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.0959` n `146` status `ready` deltaP `3.5334` edge `0.0267` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.3953` n `146` status `ready` deltaP `5.906` edge `0.1229` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.4657` n `106` status `ready` deltaP `5.3328` edge `-0.0016` maxDD `-0.4876`
- `market_context_high->index_1h` score `-0.4688` n `146` status `ready` deltaP `4.1506` edge `0.0185` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8316` n `146` status `ready` deltaP `3.0391` edge `0.0217` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9577` n `146` status `ready` deltaP `3.076` edge `0.083` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1594` n `146` status `ready` deltaP `-11.2173` edge `-0.0056` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.3179` n `135` status `ready` deltaP `10.3264` edge `0.0531` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4912` n `135` status `ready` deltaP `-14.2277` edge `-0.0088` maxDD `-1.3359`
- `market_context_high->metal_1h` score `-1.9821` n `146` status `ready` deltaP `-3.5559` edge `-0.0021` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.1707` n `135` status `ready` deltaP `4.0549` edge `0.0143` maxDD `-14.7778`
- `market_context_high->crypto_alt_4h` score `-2.7759` n `135` status `ready` deltaP `17.4887` edge `0.332` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-2.993` n `146` status `ready` deltaP `2.508` edge `-0.0635` maxDD `-14.2111`
- `market_context_high->equity_4h` score `-3.3431` n `135` status `ready` deltaP `10.9146` edge `0.0292` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
