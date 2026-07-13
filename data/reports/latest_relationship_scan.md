# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T01:52:25.026976+00:00`
- Price records: `672`
- Market context records: `6561`
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

- `market_context_high->unknown_24h` score `6.2789` n `144` status `ready` deltaP `11.2002` edge `0.7786` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.8119` n `210` status `ready` deltaP `-4.6806` edge `0.2723` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3827` n `144` status `ready` deltaP `13.4773` edge `0.2122` maxDD `-5.2791`
- `market_context_high->index_4h` score `-0.138` n `201` status `ready` deltaP `10.3681` edge `0.0197` maxDD `-2.1882`
- `market_context_high->fx_1h` score `-0.3464` n `210` status `ready` deltaP `1.008` edge `-0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4197` n `210` status `ready` deltaP `7.197` edge `0.0248` maxDD `-6.7936`
- `market_context_high->crypto_alt_4h` score `-0.4541` n `201` status `ready` deltaP `7.559` edge `0.0931` maxDD `-10.4705`
- `market_context_high->crypto_alt_1h` score `-0.4768` n `210` status `ready` deltaP `6.7893` edge `0.0249` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.588` n `210` status `ready` deltaP `-0.9795` edge `0.0031` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5907` n `210` status `ready` deltaP `-0.4092` edge `-0.0047` maxDD `-2.1314`
- `market_context_high->crypto_major_4h` score `-0.6909` n `201` status `ready` deltaP `10.2711` edge `0.0845` maxDD `-12.6576`
- `market_context_high->equity_1h` score `-1.1633` n `210` status `ready` deltaP `2.0816` edge `0.0002` maxDD `-4.2147`
- `market_context_high->unknown_4h` score `-1.1753` n `201` status `ready` deltaP `-16.5711` edge `0.2531` maxDD `-10.5788`
- `market_context_high->metal_1h` score `-1.2284` n `210` status `ready` deltaP `-3.128` edge `-0.0008` maxDD `-2.1239`
- `market_context_high->commodity_4h` score `-1.4059` n `201` status `ready` deltaP `-2.5907` edge `-0.0135` maxDD `-5.6246`
- `market_context_high->equity_4h` score `-1.4569` n `201` status `ready` deltaP `8.4334` edge `0.0266` maxDD `-11.0054`
- `market_context_high->metal_4h` score `-1.5064` n `201` status `ready` deltaP `0.2472` edge `0.0315` maxDD `-3.4353`
- `market_context_high->metal_24h` score `-1.9745` n `144` status `ready` deltaP `5.966` edge `0.0887` maxDD `-5.7746`
- `market_context_high->fx_4h` score `-2.8915` n `201` status `ready` deltaP `-1.9423` edge `-0.0068` maxDD `-3.3635`
- `market_context_high->index_24h` score `-3.8218` n `144` status `ready` deltaP `1.2914` edge `-0.005` maxDD `-10.7676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
