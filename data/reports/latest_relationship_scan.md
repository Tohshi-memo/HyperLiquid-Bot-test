# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T02:22:23.999996+00:00`
- Price records: `672`
- Market context records: `6563`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9872`

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

- `market_context_high->unknown_24h` score `6.2296` n `144` status `ready` deltaP `10.8536` edge `0.7768` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.7628` n `210` status `ready` deltaP `-4.98` edge `0.2702` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3899` n `144` status `ready` deltaP `13.4773` edge `0.2128` maxDD `-5.2791`
- `market_context_high->index_4h` score `-0.3242` n `203` status `ready` deltaP `9.7358` edge `0.0168` maxDD `-2.8613`
- `market_context_high->fx_1h` score `-0.3456` n `210` status `ready` deltaP `1.008` edge `-0.0003` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.408` n `210` status `ready` deltaP `7.197` edge `0.0263` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.4636` n `210` status `ready` deltaP `6.7893` edge `0.0266` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5678` n `210` status `ready` deltaP `-0.6801` edge `0.0037` maxDD `-0.7564`
- `market_context_high->crypto_alt_4h` score `-0.5835` n `203` status `ready` deltaP `6.9905` edge `0.089` maxDD `-11.1666`
- `market_context_high->commodity_1h` score `-0.5915` n `210` status `ready` deltaP `-0.4092` edge `-0.0048` maxDD `-2.1314`
- `market_context_high->crypto_major_4h` score `-0.8097` n `203` status `ready` deltaP `9.6878` edge `0.0815` maxDD `-12.6576`
- `market_context_high->equity_1h` score `-1.1489` n `210` status `ready` deltaP `2.0816` edge `0.0014` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.244` n `210` status `ready` deltaP `-3.2777` edge `-0.0011` maxDD `-2.1239`
- `market_context_high->unknown_4h` score `-1.3205` n `203` status `ready` deltaP `-16.8554` edge `0.2429` maxDD `-10.5788`
- `market_context_high->commodity_4h` score `-1.417` n `203` status `ready` deltaP `-2.7897` edge `-0.0136` maxDD `-5.6246`
- `market_context_high->metal_4h` score `-1.6235` n `203` status `ready` deltaP `-0.1547` edge `0.0298` maxDD `-3.6196`
- `market_context_high->metal_24h` score `-1.9757` n `144` status `ready` deltaP `5.966` edge `0.0886` maxDD `-5.7746`
- `market_context_high->equity_4h` score `-2.1226` n `203` status `ready` deltaP `7.8697` edge `0.0122` maxDD `-13.9904`
- `market_context_high->fx_4h` score `-2.8368` n `203` status `ready` deltaP `-1.408` edge `-0.0058` maxDD `-3.3635`
- `market_context_high->index_24h` score `-3.8062` n `144` status `ready` deltaP `1.2914` edge `-0.0037` maxDD `-10.7676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
