# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T17:37:36.891413+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8092`

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

- `market_context_high->unknown_1h` score `28.2205` n `153` status `ready` deltaP `1.1751` edge `2.3928` maxDD `-1.5807`
- `market_context_high->unknown_4h` score `22.6851` n `150` status `ready` deltaP `0.4018` edge `1.9213` maxDD `-1.0178`
- `market_context_high->metal_24h` score `0.4427` n `112` status `ready` deltaP `26.1884` edge `0.1448` maxDD `-7.0108`
- `market_context_high->fx_1h` score `0.2039` n `153` status `ready` deltaP `7.5163` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0952` n `150` status `ready` deltaP `8.9528` edge `0.0081` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0051` n `112` status `ready` deltaP `16.3051` edge `0.0145` maxDD `-4.5747`
- `market_context_high->fx_24h` score `-0.125` n `112` status `ready` deltaP `17.1453` edge `0.0269` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.1602` n `153` status `ready` deltaP `7.8813` edge `0.0061` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.2954` n `153` status `ready` deltaP `2.0029` edge `0.0121` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.586` n `153` status `ready` deltaP `0.0127` edge `-0.0015` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.7116` n `150` status `ready` deltaP `4.14` edge `0.036` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.9262` n `153` status `ready` deltaP `3.7846` edge `0.0141` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.0281` n `150` status `ready` deltaP `6.3896` edge `-0.0034` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8097` n `153` status `ready` deltaP `1.6046` edge `-0.0151` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0154` n `153` status `ready` deltaP `-0.725` edge `-0.0051` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.5262` n `150` status `ready` deltaP `-7.3364` edge `-0.0273` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.3665` n `112` status `ready` deltaP `-2.0983` edge `-0.0601` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.8382` n `150` status `ready` deltaP `-2.0395` edge `-0.1027` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.0137` n `112` status `ready` deltaP `-3.0438` edge `-0.2074` maxDD `-35.4638`
- `market_context_high->commodity_24h` score `-6.3631` n `112` status `ready` deltaP `-17.4238` edge `-0.1407` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
