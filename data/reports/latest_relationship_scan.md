# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T19:07:34.153041+00:00`
- Price records: `672`
- Market context records: `6632`
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

- `market_context_high->unknown_1h` score `2.2979` n `203` status `ready` deltaP `-5.6407` edge `0.3192` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `1.7228` n `187` status `ready` deltaP `-1.1481` edge `0.4592` maxDD `-12.3047`
- `market_context_high->commodity_24h` score `0.5004` n `187` status `ready` deltaP `9.7987` edge `0.1632` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0892` n `203` status `ready` deltaP `8.8139` edge `0.047` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1398` n `203` status `ready` deltaP `6.2011` edge `0.0401` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2383` n `203` status `ready` deltaP `2.9357` edge `0.0006` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4921` n `203` status `ready` deltaP `0.5214` edge `0.0052` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6537` n `203` status `ready` deltaP `-1.1393` edge `-0.0079` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.7841` n `203` status `ready` deltaP `-15.8814` edge `0.2811` maxDD `-10.5788`
- `market_context_high->index_4h` score `-0.8113` n `203` status `ready` deltaP `10.7788` edge `0.0121` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8215` n `203` status `ready` deltaP `3.3517` edge `0.0119` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.1269` n `203` status `ready` deltaP `-3.0574` edge `0.0006` maxDD `-1.5966`
- `market_context_high->crypto_major_4h` score `-1.1439` n `203` status `ready` deltaP `10.1098` edge `0.1174` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.3666` n `203` status `ready` deltaP `-1.1595` edge `-0.018` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-1.5133` n `203` status `ready` deltaP `4.0798` edge `0.0` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.5422` n `203` status `ready` deltaP `6.9551` edge `0.0961` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-1.9512` n `203` status `ready` deltaP `1.0648` edge `0.0288` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3911` n `203` status `ready` deltaP `8.9834` edge `0.0011` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-5.3314` n `187` status `ready` deltaP `-2.5165` edge `0.0285` maxDD `-21.2858`
- `market_context_high->fx_24h` score `-6.0883` n `187` status `ready` deltaP `-9.7672` edge `-0.0051` maxDD `-10.3047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
