# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T13:52:34.045565+00:00`
- Price records: `672`
- Market context records: `6924`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->fx_1h` score `-0.1872` n `224` status `ready` deltaP `3.2854` edge `0.0026` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.3411` n `205` status `ready` deltaP `-5.0547` edge `0.3916` maxDD `-14.4643`
- `market_context_high->crypto_alt_1h` score `-0.4067` n `224` status `ready` deltaP `2.9593` edge `0.0228` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4783` n `224` status `ready` deltaP `4.4456` edge `0.0209` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6292` n `224` status `ready` deltaP `-0.7485` edge `-0.0072` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7027` n `224` status `ready` deltaP `0.1684` edge `-0.0001` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7475` n `224` status `ready` deltaP `-2.6465` edge `-0.0014` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.7639` n `224` status `ready` deltaP `14.7649` edge `0.01` maxDD `-2.1765`
- `market_context_high->unknown_1h` score `-1.5103` n `224` status `ready` deltaP `-2.0637` edge `-0.022` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.5249` n `224` status `ready` deltaP `-3.4081` edge `-0.0238` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.583` n `224` status `ready` deltaP `3.8815` edge `-0.0108` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.7279` n `224` status `ready` deltaP `7.4478` edge `-0.0132` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-1.9883` n `224` status `ready` deltaP `4.6058` edge `0.0127` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.6903` n `224` status `ready` deltaP `2.2104` edge `-0.0013` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7438` n `224` status `ready` deltaP `0.2177` edge `-0.0205` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9173` n `224` status `ready` deltaP `-7.2082` edge `0.0415` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.0085` n `205` status `ready` deltaP `-2.8026` edge `-0.0452` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.0475` n `205` status `ready` deltaP `-4.1045` edge `-0.0063` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.7352` n `224` status `ready` deltaP `4.8454` edge `-0.1013` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.3919` n `205` status `ready` deltaP `-11.7936` edge `-0.1118` maxDD `-30.5032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
