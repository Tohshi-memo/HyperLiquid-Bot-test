# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T14:22:33.364627+00:00`
- Price records: `672`
- Market context records: `6611`
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

- `market_context_high->unknown_24h` score `3.2476` n `172` status `ready` deltaP `1.7583` edge `0.5501` maxDD `-13.2952`
- `market_context_high->unknown_1h` score `2.0956` n `206` status `ready` deltaP `-5.8296` edge `0.3036` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.217` n `172` status `ready` deltaP `7.4556` edge `0.1552` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2689` n `206` status `ready` deltaP `2.3632` edge `0.0005` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4006` n `206` status `ready` deltaP `7.2045` edge `0.0272` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5357` n `206` status `ready` deltaP `0.4404` edge `-0.0033` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5536` n `206` status `ready` deltaP `-0.4084` edge `0.0037` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6555` n `206` status `ready` deltaP `4.4779` edge `0.0174` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.8624` n `206` status `ready` deltaP `10.1261` edge `0.0099` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1576` n `206` status `ready` deltaP `1.8284` edge `0.0017` maxDD `-4.1619`
- `market_context_high->commodity_4h` score `-1.2011` n `206` status `ready` deltaP `0.0888` edge `-0.0051` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3194` n `206` status `ready` deltaP `-4.1379` edge `-0.0022` maxDD `-2.0797`
- `market_context_high->unknown_4h` score `-1.579` n `206` status `ready` deltaP `-17.8368` edge `0.2279` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.6231` n `206` status `ready` deltaP `2.1179` edge `-0.001` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.7051` n `206` status `ready` deltaP `7.4621` edge `0.0631` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0787` n `206` status `ready` deltaP `4.4814` edge `0.0438` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1485` n `206` status `ready` deltaP `-1.2003` edge `0.0186` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.0542` n `206` status `ready` deltaP `7.8069` edge `-0.0167` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-3.5913` n `172` status `ready` deltaP `-0.8671` edge `0.0532` maxDD `-12.2936`
- `market_context_high->fx_24h` score `-5.7918` n `172` status `ready` deltaP `-6.9224` edge `-0.0008` maxDD `-9.1896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
