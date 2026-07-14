# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T01:22:25.582077+00:00`
- Price records: `672`
- Market context records: `6661`
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

- `market_context_high->unknown_1h` score `2.3978` n `202` status `ready` deltaP `-5.4114` edge `0.326` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.1631` n `202` status `ready` deltaP `12.1416` edge `0.2028` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0865` n `202` status `ready` deltaP `8.3121` edge `0.05` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0732` n `202` status `ready` deltaP `5.8828` edge `0.0436` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2256` n `202` status `ready` deltaP `3.1215` edge `0.001` maxDD `-0.7249`
- `market_context_high->unknown_24h` score `-0.2259` n `202` status `ready` deltaP `-3.9364` edge `0.3725` maxDD `-12.3511`
- `market_context_high->unknown_4h` score `-0.2707` n `202` status `ready` deltaP `-14.3534` edge `0.3137` maxDD `-10.5788`
- `market_context_high->index_1h` score `-0.4588` n `202` status `ready` deltaP `1.1635` edge `0.0052` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6805` n `202` status `ready` deltaP `-1.371` edge `-0.0098` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.7968` n `202` status `ready` deltaP `11.0435` edge `0.0122` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8448` n `202` status `ready` deltaP `3.615` edge `0.0082` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-1.0038` n `202` status `ready` deltaP `11.2745` edge `0.1276` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1241` n `202` status `ready` deltaP `-3.1882` edge `0.0017` maxDD `-1.5966`
- `market_context_high->crypto_alt_4h` score `-1.3069` n `202` status `ready` deltaP `8.5697` edge `0.1155` maxDD `-19.2145`
- `market_context_high->fx_4h` score `-1.3861` n `202` status `ready` deltaP `6.4055` edge `0.0008` maxDD `-3.3635`
- `market_context_high->commodity_4h` score `-1.4652` n `202` status `ready` deltaP `-1.3765` edge `-0.0292` maxDD `-5.6246`
- `market_context_high->metal_4h` score `-1.9674` n `202` status `ready` deltaP `0.6173` edge `0.0297` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.515` n `202` status `ready` deltaP `8.3042` edge `-0.0047` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.3908` n `202` status `ready` deltaP `-12.1895` edge `-0.0114` maxDD `-10.8591`
- `market_context_high->metal_24h` score `-6.7936` n `202` status `ready` deltaP `-4.5531` edge `0.0079` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
