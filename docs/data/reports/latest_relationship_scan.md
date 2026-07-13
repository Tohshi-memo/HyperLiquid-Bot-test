# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T21:22:25.581394+00:00`
- Price records: `672`
- Market context records: `6643`
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

- `market_context_high->unknown_1h` score `2.4034` n `203` status `ready` deltaP `-4.8922` edge `0.323` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `0.7423` n `192` status `ready` deltaP `-1.5643` edge `0.4344` maxDD `-12.3047`
- `market_context_high->commodity_24h` score `0.6838` n `192` status `ready` deltaP `10.6203` edge `0.173` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.1111` n `203` status `ready` deltaP `8.8139` edge `0.0498` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1097` n `203` status `ready` deltaP `6.0514` edge `0.0436` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.222` n `203` status `ready` deltaP `3.2351` edge `0.0007` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.468` n `203` status `ready` deltaP `0.9705` edge `0.0053` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6731` n `203` status `ready` deltaP `-1.4387` edge `-0.0084` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.6935` n `203` status `ready` deltaP `-15.4241` edge `0.2856` maxDD `-10.5788`
- `market_context_high->index_4h` score `-0.7838` n `203` status `ready` deltaP `11.0837` edge `0.0136` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8766` n `203` status `ready` deltaP `3.0523` edge `0.0093` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-1.0035` n `203` status `ready` deltaP `11.0244` edge `0.1293` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.0909` n `203` status `ready` deltaP `-2.758` edge `0.0016` maxDD `-1.5966`
- `market_context_high->crypto_alt_4h` score `-1.3809` n `203` status `ready` deltaP `7.7173` edge `0.1117` maxDD `-19.2145`
- `market_context_high->commodity_4h` score `-1.4252` n `203` status `ready` deltaP `-1.3119` edge `-0.0245` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-1.4808` n `203` status `ready` deltaP `4.6895` edge `0.0001` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.8786` n `203` status `ready` deltaP `1.9795` edge `0.032` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3419` n `203` status `ready` deltaP `8.9834` edge `0.0052` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-5.8225` n `192` status `ready` deltaP `-3.0061` edge `0.0244` maxDD `-24.0668`
- `market_context_high->fx_24h` score `-6.2377` n `192` status `ready` deltaP `-10.6167` edge `-0.0079` maxDD `-10.624`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
