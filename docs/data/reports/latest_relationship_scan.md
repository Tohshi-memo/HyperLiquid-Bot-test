# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T02:22:29.961518+00:00`
- Price records: `672`
- Market context records: `6665`
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

- `market_context_high->unknown_1h` score `2.4662` n `202` status `ready` deltaP `-5.112` edge `0.3297` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.1667` n `202` status `ready` deltaP `12.1416` edge `0.2031` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0507` n `202` status `ready` deltaP `7.863` edge `0.0484` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.108` n `202` status `ready` deltaP `5.5834` edge `0.0427` maxDD `-3.7803`
- `market_context_high->unknown_4h` score `-0.2119` n `202` status `ready` deltaP `-14.3534` edge `0.3186` maxDD `-10.5788`
- `market_context_high->unknown_24h` score `-0.2259` n `202` status `ready` deltaP `-3.9364` edge `0.3725` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2333` n `202` status `ready` deltaP `2.9718` edge `0.001` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4751` n `202` status `ready` deltaP `0.8641` edge `0.0051` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6432` n `202` status `ready` deltaP `-0.7722` edge `-0.009` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8267` n `202` status `ready` deltaP `10.7387` edge `0.0104` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8448` n `202` status `ready` deltaP `3.615` edge `0.0082` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-1.1158` n `202` status `ready` deltaP `10.6647` edge `0.1173` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1529` n `202` status `ready` deltaP `-3.4876` edge `0.0013` maxDD `-1.5966`
- `market_context_high->fx_4h` score `-1.3869` n `202` status `ready` deltaP `6.4055` edge `0.0007` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.4228` n `202` status `ready` deltaP `7.96` edge `0.1047` maxDD `-19.2145`
- `market_context_high->commodity_4h` score `-1.4691` n `202` status `ready` deltaP `-1.3765` edge `-0.0297` maxDD `-5.6246`
- `market_context_high->metal_4h` score `-1.9911` n `202` status `ready` deltaP `0.3124` edge `0.0287` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.6174` n `202` status `ready` deltaP `7.9993` edge `-0.0112` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.4028` n `202` status `ready` deltaP `-12.1895` edge `-0.0124` maxDD `-10.8591`
- `market_context_high->metal_24h` score `-6.8107` n `202` status `ready` deltaP `-4.5531` edge `0.0057` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
