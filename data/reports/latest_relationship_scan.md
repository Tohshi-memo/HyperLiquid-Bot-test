# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T13:07:27.727555+00:00`
- Price records: `672`
- Market context records: `6605`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `3.5958` n `168` status `ready` deltaP `3.0318` edge `0.58` maxDD `-13.7118`
- `market_context_high->unknown_1h` score `2.0756` n `207` status `ready` deltaP `-5.719` edge `0.3012` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.3827` n `168` status `ready` deltaP `8.3415` edge `0.1631` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2894` n `207` status `ready` deltaP `1.9837` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4329` n `207` status `ready` deltaP `6.8074` edge `0.0257` maxDD `-6.7936`
- `market_context_high->index_1h` score `-0.5415` n `207` status `ready` deltaP `-0.1598` edge `0.0036` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5554` n `207` status `ready` deltaP `0.1801` edge `-0.0041` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.6678` n `207` status `ready` deltaP `4.2422` edge `0.0174` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9174` n `207` status `ready` deltaP `9.2186` edge `0.0089` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1728` n `207` status `ready` deltaP `1.9085` edge `-0.0001` maxDD `-4.1619`
- `market_context_high->commodity_4h` score `-1.2153` n `207` status `ready` deltaP `-0.1856` edge `-0.0051` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3272` n `207` status `ready` deltaP `-4.1605` edge `-0.0027` maxDD `-2.0797`
- `market_context_high->unknown_4h` score `-1.576` n `207` status `ready` deltaP `-17.3795` edge `0.2251` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.6352` n `207` status `ready` deltaP `1.9162` edge `-0.0012` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.7563` n `207` status `ready` deltaP `7.183` edge `0.0584` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.1186` n `207` status `ready` deltaP `4.2093` edge `0.0405` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1688` n `207` status `ready` deltaP `-1.545` edge `0.0183` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.1631` n `207` status `ready` deltaP `6.9276` edge `-0.0248` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-3.2116` n `168` status `ready` deltaP `-0.0227` edge `0.0579` maxDD `-10.8923`
- `market_context_high->fx_24h` score `-3.7362` n `168` status `ready` deltaP `-6.078` edge `-0.0002` maxDD `-9.0624`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
