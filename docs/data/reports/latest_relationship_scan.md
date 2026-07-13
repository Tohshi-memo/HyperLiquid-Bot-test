# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T23:07:23.422176+00:00`
- Price records: `672`
- Market context records: `6652`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11766`

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

- `market_context_high->unknown_1h` score `2.4278` n `202` status `ready` deltaP `-4.9623` edge `0.3255` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.9491` n `198` status `ready` deltaP `11.5515` edge `0.1889` maxDD `-5.2791`
- `market_context_high->unknown_24h` score `0.175` n `198` status `ready` deltaP `-3.0164` edge `0.396` maxDD `-11.9426`
- `market_context_high->crypto_major_1h` score `0.1224` n `202` status `ready` deltaP `8.9109` edge `0.0506` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0073` n `202` status `ready` deltaP `6.4816` edge `0.0451` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2349` n `202` status `ready` deltaP `2.9718` edge `0.0008` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4813` n `202` status `ready` deltaP `0.7144` edge `0.0053` maxDD `-0.7417`
- `market_context_high->unknown_4h` score `-0.6163` n `202` status `ready` deltaP `-15.268` edge `0.291` maxDD `-10.5788`
- `market_context_high->commodity_1h` score `-0.672` n `202` status `ready` deltaP `-1.371` edge `-0.0087` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.7574` n `202` status `ready` deltaP `11.5009` edge `0.0142` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8448` n `202` status `ready` deltaP `3.3156` edge `0.0102` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-0.9481` n `202` status `ready` deltaP `11.5793` edge `0.1327` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1541` n `202` status `ready` deltaP `-3.4876` edge `0.0012` maxDD `-1.5966`
- `market_context_high->crypto_alt_4h` score `-1.2819` n `202` status `ready` deltaP `8.5697` edge `0.1187` maxDD `-19.2145`
- `market_context_high->commodity_4h` score `-1.4372` n `202` status `ready` deltaP `-1.3765` edge `-0.0256` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-1.4447` n `202` status `ready` deltaP `5.3384` edge `0.0004` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.9391` n `202` status `ready` deltaP `0.9222` edge `0.0313` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3534` n `202` status `ready` deltaP `8.9139` edge `0.0047` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.2843` n `198` status `ready` deltaP `-11.5794` edge `-0.009` maxDD `-10.666`
- `market_context_high->metal_24h` score `-6.4178` n `198` status `ready` deltaP `-3.9531` edge `0.0159` maxDD `-26.6542`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
