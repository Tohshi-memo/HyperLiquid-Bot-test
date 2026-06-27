# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T02:37:28.353543+00:00`
- Price records: `672`
- Market context records: `4890`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8584`

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

- `market_context_high->unknown_1h` score `15.8743` n `110` status `ready` deltaP `9.5727` edge `1.3008` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5506` n `110` status `ready` deltaP `23.1624` edge `0.6946` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.4714` n `110` status `ready` deltaP `21.3609` edge `0.5321` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.3204` n `110` status `ready` deltaP `18.7971` edge `0.5238` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.1484` n `91` status `ready` deltaP `24.2541` edge `0.3016` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1041` n `110` status `ready` deltaP `7.9102` edge `0.1055` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8851` n `110` status `ready` deltaP `12.439` edge `0.1687` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5913` n `110` status `ready` deltaP `12.1452` edge `0.0411` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4508` n `110` status `ready` deltaP `6.3201` edge `0.1195` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.3965` n `110` status `ready` deltaP `7.8715` edge `0.1006` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.1942` n `110` status `ready` deltaP `3.9358` edge `0.0584` maxDD `-2.779`
- `market_context_high->commodity_1h` score `-0.195` n `110` status `ready` deltaP `3.7316` edge `0.0161` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2274` n `110` status `ready` deltaP `-0.2042` edge `0.0302` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5164` n `110` status `ready` deltaP `-0.2885` edge `0.0112` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6909` n `110` status `ready` deltaP `0.6098` edge `0.0044` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.8816` n `110` status `ready` deltaP `6.1197` edge `0.0044` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3106` n `110` status `ready` deltaP `-6.5678` edge `-0.0041` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.6823` n `91` status `ready` deltaP `-4.5998` edge `-0.0085` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.5157` n `91` status `ready` deltaP `-4.8879` edge `-0.1378` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.7657` n `91` status `ready` deltaP `15.0202` edge `0.0136` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
