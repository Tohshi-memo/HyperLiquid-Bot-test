# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T16:01:09.330144+00:00`
- Price records: `672`
- Market context records: `6618`
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

- `market_context_high->unknown_24h` score `3.2484` n `175` status `ready` deltaP `0.8413` edge `0.5314` maxDD `-12.3047`
- `market_context_high->unknown_1h` score `2.1923` n `203` status `ready` deltaP `-5.9401` edge `0.3124` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.1822` n `175` status `ready` deltaP `7.6352` edge `0.1511` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.1072` n `203` status `ready` deltaP `7.4666` edge `0.0308` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.2633` n `203` status `ready` deltaP `2.4866` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_alt_1h` score `-0.4959` n `203` status `ready` deltaP `4.7041` edge `0.0204` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.5599` n `203` status `ready` deltaP `-0.5265` edge `0.0035` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.5999` n `203` status `ready` deltaP `-0.5405` edge `-0.005` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8823` n `203` status `ready` deltaP `9.8642` edge `0.0091` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.0541` n `203` status `ready` deltaP `2.1541` edge `0.0005` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.2072` n `203` status `ready` deltaP `-3.8059` edge `-0.0011` maxDD `-1.5966`
- `market_context_high->commodity_4h` score `-1.2514` n `203` status `ready` deltaP `-0.5497` edge `-0.0073` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.4393` n `203` status `ready` deltaP `-17.7107` edge `0.2387` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.6162` n `203` status `ready` deltaP `2.2505` edge `-0.001` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.6337` n `203` status `ready` deltaP `8.2805` edge `0.0668` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0562` n `203` status `ready` deltaP `5.1258` edge `0.0424` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1` n `203` status `ready` deltaP `-0.612` edge `0.0209` maxDD `-5.2172`
- `market_context_high->metal_24h` score `-4.1332` n `175` status `ready` deltaP `-1.8735` edge `0.0453` maxDD `-14.683`
- `market_context_high->equity_4h` score `-4.6728` n `203` status `ready` deltaP `8.2212` edge `-0.0173` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-5.6961` n `175` status `ready` deltaP `-7.5304` edge `-0.0009` maxDD `-9.2193`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
