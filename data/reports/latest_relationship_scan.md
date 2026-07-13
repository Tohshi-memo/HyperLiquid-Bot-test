# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T23:52:30.250527+00:00`
- Price records: `672`
- Market context records: `6655`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_1h` score `2.3726` n `202` status `ready` deltaP `-5.4114` edge `0.3239` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.1166` n `201` status `ready` deltaP `11.9963` edge `0.1999` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0974` n `202` status `ready` deltaP `8.6115` edge `0.0494` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0409` n `202` status `ready` deltaP `6.1822` edge `0.0443` maxDD `-3.7803`
- `market_context_high->unknown_24h` score `-0.0974` n `201` status `ready` deltaP `-3.7099` edge `0.3782` maxDD `-11.9426`
- `market_context_high->fx_1h` score `-0.2435` n `202` status `ready` deltaP `2.8221` edge `0.0007` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4712` n `202` status `ready` deltaP `0.8641` edge `0.0056` maxDD `-0.7417`
- `market_context_high->unknown_4h` score `-0.4933` n `202` status `ready` deltaP `-14.8107` edge `0.2982` maxDD `-10.5788`
- `market_context_high->commodity_1h` score `-0.693` n `202` status `ready` deltaP `-1.6704` edge `-0.0094` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.7574` n `202` status `ready` deltaP `11.5009` edge `0.0142` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8076` n `202` status `ready` deltaP `3.4653` edge `0.0123` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-0.9481` n `202` status `ready` deltaP `11.5793` edge `0.1327` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1397` n `202` status `ready` deltaP `-3.3379` edge `0.0014` maxDD `-1.5966`
- `market_context_high->crypto_alt_4h` score `-1.252` n `202` status `ready` deltaP `8.8746` edge `0.1205` maxDD `-19.2145`
- `market_context_high->fx_4h` score `-1.4202` n `202` status `ready` deltaP `5.7957` edge `0.0005` maxDD `-3.3635`
- `market_context_high->commodity_4h` score `-1.4457` n `202` status `ready` deltaP `-1.3765` edge `-0.0267` maxDD `-5.6246`
- `market_context_high->metal_4h` score `-1.9486` n `202` status `ready` deltaP `0.7697` edge `0.0311` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.357` n `202` status `ready` deltaP `8.9139` edge `0.0044` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.3521` n `201` status `ready` deltaP `-12.0392` edge `-0.0099` maxDD `-10.8013`
- `market_context_high->metal_24h` score `-6.6672` n `201` status `ready` deltaP `-4.4054` edge `0.0119` maxDD `-27.6509`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
