# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T12:37:29.238569+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7893`

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

- `market_context_high->unknown_24h` score `482.5614` n `51` status `ready` deltaP `-14.0522` edge `40.3435` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `44.8919` n `83` status `ready` deltaP `-7.3428` edge `3.848` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.9715` n `51` status `ready` deltaP `33.0473` edge `0.5702` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `4.0658` n `51` status `ready` deltaP `-3.9931` edge `0.8627` maxDD `-17.8526`
- `market_context_high->index_24h` score `3.6482` n `51` status `ready` deltaP `32.5981` edge `0.1411` maxDD `-0.6858`
- `market_context_high->fx_4h` score `1.2129` n `83` status `ready` deltaP `18.0062` edge `0.0094` maxDD `-0.2692`
- `market_context_high->fx_24h` score `0.8649` n `51` status `ready` deltaP `20.9865` edge `0.0237` maxDD `-0.5518`
- `market_context_high->commodity_1h` score `0.281` n `85` status `ready` deltaP `5.8084` edge `0.0098` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `0.1584` n `83` status `ready` deltaP `8.7809` edge `0.008` maxDD `-1.6002`
- `market_context_high->fx_1h` score `-0.1766` n `85` status `ready` deltaP `1.2311` edge `0.0013` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.3772` n `85` status `ready` deltaP `1.2945` edge `0.0021` maxDD `-0.7275`
- `market_context_high->metal_4h` score `-0.5132` n `83` status `ready` deltaP `-1.5023` edge `0.0165` maxDD `-1.1153`
- `market_context_high->unknown_1h` score `-0.6945` n `85` status `ready` deltaP `-7.448` edge `0.0254` maxDD `-1.0231`
- `market_context_high->crypto_alt_1h` score `-0.8024` n `85` status `ready` deltaP `-0.2025` edge `0.0379` maxDD `-4.9401`
- `market_context_high->crypto_major_1h` score `-0.9444` n `85` status `ready` deltaP `-1.3367` edge `0.0191` maxDD `-3.7778`
- `market_context_high->index_1h` score `-1.137` n `85` status `ready` deltaP `-8.3956` edge `-0.0036` maxDD `-0.5627`
- `market_context_high->crypto_major_4h` score `-1.2674` n `83` status `ready` deltaP `-5.0727` edge `0.0819` maxDD `-11.1784`
- `market_context_high->index_4h` score `-1.418` n `83` status `ready` deltaP `-13.8554` edge `-0.0004` maxDD `-1.1221`
- `market_context_high->equity_1h` score `-1.8208` n `85` status `ready` deltaP `-8.5012` edge `-0.0081` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-1.8382` n `83` status `ready` deltaP `-6.2279` edge `0.0617` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
