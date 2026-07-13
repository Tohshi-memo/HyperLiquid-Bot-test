# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T14:37:36.453012+00:00`
- Price records: `672`
- Market context records: `6612`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9810`

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

- `market_context_high->unknown_24h` score `3.1376` n `173` status `ready` deltaP `1.4491` edge `0.543` maxDD `-13.2952`
- `market_context_high->unknown_1h` score `2.0788` n `206` status `ready` deltaP `-5.9793` edge `0.3032` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.2266` n `173` status `ready` deltaP `7.6505` edge `0.1547` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2689` n `206` status `ready` deltaP `2.3632` edge `0.0005` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4006` n `206` status `ready` deltaP `7.2045` edge `0.0272` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5372` n `206` status `ready` deltaP `0.4404` edge `-0.0035` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5544` n `206` status `ready` deltaP `-0.4084` edge `0.0036` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6664` n `206` status `ready` deltaP `4.3282` edge `0.017` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.8624` n `206` status `ready` deltaP `10.1261` edge `0.0099` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.16` n `206` status `ready` deltaP `1.8284` edge `0.0015` maxDD `-4.1619`
- `market_context_high->commodity_4h` score `-1.2003` n `206` status `ready` deltaP `0.0888` edge `-0.005` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3158` n `206` status `ready` deltaP `-4.1379` edge `-0.0019` maxDD `-2.0797`
- `market_context_high->unknown_4h` score `-1.5984` n `206` status `ready` deltaP `-17.9893` edge `0.2273` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.6223` n `206` status `ready` deltaP `2.1179` edge `-0.0009` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.7137` n `206` status `ready` deltaP `7.4621` edge `0.062` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0826` n `206` status `ready` deltaP `4.4814` edge `0.0433` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1493` n `206` status `ready` deltaP `-1.2003` edge `0.0185` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.04` n `206` status `ready` deltaP `7.9593` edge `-0.0159` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-3.6931` n `173` status `ready` deltaP `-1.0721` edge `0.0513` maxDD `-12.7431`
- `market_context_high->fx_24h` score `-5.8217` n `173` status `ready` deltaP `-7.1274` edge `-0.001` maxDD `-9.2637`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
