# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T07:22:24.364835+00:00`
- Price records: `672`
- Market context records: `6896`
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

- `market_context_high->unknown_24h` score `0.5003` n `185` status `ready` deltaP `-4.6485` edge `0.4825` maxDD `-13.3224`
- `market_context_high->fx_1h` score `-0.2214` n `224` status `ready` deltaP `2.6866` edge `0.0022` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5338` n `224` status `ready` deltaP `2.3605` edge `0.0162` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.5777` n `224` status `ready` deltaP `-0.2994` edge `-0.0036` maxDD `-2.1443`
- `market_context_high->crypto_major_1h` score `-0.6186` n `224` status `ready` deltaP `3.8468` edge `0.0132` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.8032` n `224` status `ready` deltaP `-1.3286` edge `-0.003` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.8358` n `224` status `ready` deltaP `13.6978` edge `0.0079` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.8799` n `224` status `ready` deltaP `-4.2932` edge `-0.0074` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3209` n `224` status `ready` deltaP `-1.8838` edge `-0.0078` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.75` n `224` status `ready` deltaP `-4.1595` edge `-0.028` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8191` n `224` status `ready` deltaP `1.636` edge `-0.0261` maxDD `-13.1084`
- `market_context_high->commodity_24h` score `-1.9864` n `185` status `ready` deltaP `1.1981` edge `0.0133` maxDD `-5.2791`
- `market_context_high->index_4h` score `-1.9953` n `224` status `ready` deltaP `3.7892` edge `-0.0231` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.296` n `224` status `ready` deltaP `1.4046` edge `-0.0054` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.9456` n `224` status `ready` deltaP `0.9909` edge `-0.0259` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-3.0117` n `224` status `ready` deltaP `-1.1542` edge `-0.0457` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0861` n `224` status `ready` deltaP `-8.7326` edge `0.0376` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.265` n `185` status `ready` deltaP `-6.7029` edge `-0.0071` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3537` n `224` status `ready` deltaP `1.1869` edge `-0.1562` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.4974` n `185` status `ready` deltaP `-14.3614` edge `-0.1351` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
