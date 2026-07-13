# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T17:52:37.194850+00:00`
- Price records: `672`
- Market context records: `6626`
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

- `market_context_high->unknown_24h` score `2.3598` n `182` status `ready` deltaP `-0.6616` edge `0.4882` maxDD `-12.3047`
- `market_context_high->unknown_1h` score `2.1864` n `203` status `ready` deltaP `-6.0898` edge `0.3129` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.3183` n `182` status `ready` deltaP `8.9319` edge `0.1538` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0067` n `203` status `ready` deltaP `8.3648` edge `0.0377` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.2547` n `203` status `ready` deltaP `2.6363` edge `0.0005` maxDD `-0.7249`
- `market_context_high->crypto_alt_1h` score `-0.3017` n `203` status `ready` deltaP `5.6023` edge `0.0306` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.5108` n `203` status `ready` deltaP `0.222` edge `0.0048` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6248` n `203` status `ready` deltaP `-0.8399` edge `-0.0062` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8286` n `203` status `ready` deltaP `10.6264` edge `0.0109` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8634` n `203` status `ready` deltaP `3.0523` edge `0.0104` maxDD `-3.8827`
- `market_context_high->unknown_4h` score `-1.0299` n `203` status `ready` deltaP `-16.6436` edge `0.2657` maxDD `-10.5788`
- `market_context_high->metal_1h` score `-1.1269` n `203` status `ready` deltaP `-3.0574` edge `0.0006` maxDD `-1.5966`
- `market_context_high->commodity_4h` score `-1.3039` n `203` status `ready` deltaP `-0.8546` edge `-0.012` maxDD `-5.6246`
- `market_context_high->crypto_major_4h` score `-1.345` n `203` status `ready` deltaP `9.3476` edge `0.0967` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.556` n `203` status `ready` deltaP `3.3176` edge `-0.0004` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.7526` n `203` status `ready` deltaP `6.1929` edge `0.0742` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.0134` n `203` status `ready` deltaP `0.3026` edge `0.0259` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.4415` n `203` status `ready` deltaP `8.9834` edge `-0.0031` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-4.8037` n `182` status `ready` deltaP `-1.9811` edge `0.0365` maxDD `-18.4654`
- `market_context_high->fx_24h` score `-5.9382` n `182` status `ready` deltaP `-8.871` edge `-0.0035` maxDD `-9.9098`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
