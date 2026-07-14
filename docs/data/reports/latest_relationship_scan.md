# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T09:22:32.080473+00:00`
- Price records: `672`
- Market context records: `6695`
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

- `market_context_high->unknown_24h` score `0.6638` n `187` status `ready` deltaP `-0.2813` edge `0.4622` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.3279` n `187` status `ready` deltaP `9.1662` edge `0.0522` maxDD `-4.2122`
- `market_context_high->commodity_24h` score `0.2887` n `187` status `ready` deltaP `9.9423` edge `0.1446` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `0.1193` n `187` status `ready` deltaP `6.1289` edge `0.0455` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3673` n `187` status `ready` deltaP `0.3946` edge `0.0005` maxDD `-0.6845`
- `market_context_high->unknown_1h` score `-0.4932` n `187` status `ready` deltaP `-6.1497` edge `0.09` maxDD `-3.2083`
- `market_context_high->index_1h` score `-0.5178` n `187` status `ready` deltaP `0.2458` edge `0.0034` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.5323` n `187` status `ready` deltaP `-2.7491` edge `0.0026` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.6311` n `187` status `ready` deltaP `-0.1809` edge `-0.0114` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-0.9553` n `187` status `ready` deltaP `3.2838` edge `0.0012` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.9863` n `187` status `ready` deltaP `9.4382` edge `-0.0014` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.3599` n `187` status `ready` deltaP `6.8173` edge `-0.0014` maxDD `-3.1385`
- `market_context_high->crypto_major_4h` score `-1.5944` n `187` status `ready` deltaP `7.4467` edge `0.0774` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.7621` n `187` status `ready` deltaP `-4.9107` edge `-0.0437` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.8453` n `187` status `ready` deltaP `5.2351` edge `0.0687` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.2501` n `187` status `ready` deltaP `-3.0332` edge `0.0178` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-4.1936` n `187` status `ready` deltaP `-17.6992` edge `0.0091` maxDD `-10.5788`
- `market_context_high->fx_24h` score `-4.9412` n `187` status `ready` deltaP `-9.9144` edge `-0.0041` maxDD `-7.992`
- `market_context_high->equity_4h` score `-5.4995` n `187` status `ready` deltaP `5.6875` edge `-0.0693` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-7.0612` n `187` status `ready` deltaP `-6.6854` edge `-0.0122` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
