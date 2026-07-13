# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T16:52:26.655454+00:00`
- Price records: `672`
- Market context records: `6622`
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

- `market_context_high->unknown_24h` score `2.8839` n `178` status `ready` deltaP `-0.0447` edge `0.5111` maxDD `-12.3047`
- `market_context_high->unknown_1h` score `2.142` n `203` status `ready` deltaP `-6.3892` edge `0.3112` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.2216` n `178` status `ready` deltaP `8.2034` edge `0.1506` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0713` n `203` status `ready` deltaP `7.766` edge `0.0334` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.2469` n `203` status `ready` deltaP `2.786` edge `0.0005` maxDD `-0.7249`
- `market_context_high->crypto_alt_1h` score `-0.4264` n `203` status `ready` deltaP `5.0035` edge `0.0242` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.5381` n `203` status `ready` deltaP `-0.2271` edge `0.0043` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.61` n `203` status `ready` deltaP `-0.6902` edge `-0.0053` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8515` n `203` status `ready` deltaP `10.3215` edge `0.01` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.9725` n `203` status `ready` deltaP `2.4535` edge `0.0053` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.1568` n `203` status `ready` deltaP `-3.3568` edge `0.0001` maxDD `-1.5966`
- `market_context_high->commodity_4h` score `-1.2584` n `203` status `ready` deltaP `-0.5497` edge `-0.0082` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.2971` n `203` status `ready` deltaP `-17.2534` edge `0.2475` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.507` n `203` status `ready` deltaP `8.7379` edge `0.08` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.5901` n `203` status `ready` deltaP `2.7078` edge `-0.0007` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.9232` n `203` status `ready` deltaP `5.5831` edge `0.0564` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.0685` n `203` status `ready` deltaP `-0.3071` edge `0.0229` maxDD `-5.2172`
- `market_context_high->metal_24h` score `-4.413` n `178` status `ready` deltaP `-1.9322` edge `0.0419` maxDD `-16.2499`
- `market_context_high->equity_4h` score `-4.5451` n `203` status `ready` deltaP `8.6785` edge `-0.0097` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-5.795` n `178` status `ready` deltaP `-8.1178` edge `-0.0019` maxDD `-9.4851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
