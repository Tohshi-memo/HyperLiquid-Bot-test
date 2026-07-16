# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T08:07:27.889385+00:00`
- Price records: `672`
- Market context records: `6899`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11702`

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

- `market_context_high->unknown_24h` score `0.5399` n `185` status `ready` deltaP `-4.1285` edge `0.4841` maxDD `-13.3224`
- `market_context_high->fx_1h` score `-0.2207` n `224` status `ready` deltaP `2.6866` edge `0.0023` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4463` n `224` status `ready` deltaP `2.8096` edge `0.0205` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.5238` n `224` status `ready` deltaP `4.2959` edge `0.0181` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.5964` n `224` status `ready` deltaP `-0.5988` edge `-0.004` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7853` n `224` status `ready` deltaP `-1.0292` edge `-0.0027` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.8066` n `224` status `ready` deltaP `14.1551` edge `0.0086` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.8503` n `224` status `ready` deltaP `-3.8441` edge `-0.0066` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3318` n `224` status `ready` deltaP `-1.8838` edge `-0.0092` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6445` n `224` status `ready` deltaP `-3.7104` edge `-0.0222` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.7949` n `224` status `ready` deltaP `1.7857` edge `-0.024` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9622` n `224` status `ready` deltaP `4.2466` edge `-0.0219` maxDD `-11.3047`
- `market_context_high->commodity_24h` score `-2.0344` n `185` status `ready` deltaP `1.1981` edge `0.0093` maxDD `-5.2791`
- `market_context_high->metal_4h` score `-2.2426` n `224` status `ready` deltaP `1.8619` edge `-0.0016` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.8664` n `224` status `ready` deltaP `1.4482` edge `-0.0188` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.9419` n `224` status `ready` deltaP `-0.6969` edge `-0.0398` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0825` n `224` status `ready` deltaP `-8.7326` edge `0.0379` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.265` n `185` status `ready` deltaP `-6.7029` edge `-0.0071` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.2745` n `224` status `ready` deltaP `1.6442` edge `-0.1491` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.429` n `185` status `ready` deltaP `-13.8414` edge `-0.1298` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
