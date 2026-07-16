# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T21:22:31.934860+00:00`
- Price records: `672`
- Market context records: `6959`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11735`

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

- `market_context_high->fx_1h` score `-0.2593` n `237` status `ready` deltaP `2.0345` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3801` n `237` status `ready` deltaP `2.43` edge `0.0215` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.7263` n `237` status `ready` deltaP `-2.0901` edge `-0.0024` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7504` n `237` status `ready` deltaP `-0.6879` edge `-0.0005` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.9489` n `237` status `ready` deltaP `11.4779` edge `0.0082` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.1922` n `237` status `ready` deltaP `3.1785` edge `0.0147` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.3077` n `237` status `ready` deltaP `-3.1235` edge `-0.016` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.5769` n `237` status `ready` deltaP `-1.8312` edge `-0.0291` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6467` n `237` status `ready` deltaP `-4.2805` edge `-0.0336` maxDD `-5.5853`
- `market_context_high->unknown_24h` score `-1.6641` n `224` status `ready` deltaP `-9.1096` edge `0.3024` maxDD `-18.7342`
- `market_context_high->index_4h` score `-1.8371` n `237` status `ready` deltaP `7.3621` edge `-0.0147` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-2.0349` n `237` status `ready` deltaP `1.9391` edge `-0.0184` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.1041` n `237` status `ready` deltaP `3.8039` edge `0.0032` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-3.1763` n `237` status `ready` deltaP `-0.5512` edge `-0.025` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-3.3537` n `237` status `ready` deltaP `-8.8679` edge `0.0162` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.7435` n `224` status `ready` deltaP `-6.3359` edge `-0.0829` maxDD `-5.2791`
- `market_context_high->crypto_major_4h` score `-3.85` n `237` status `ready` deltaP `-1.8061` edge `-0.0531` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-4.4178` n `224` status `ready` deltaP `-7.2822` edge `-0.0149` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.7447` n `237` status `ready` deltaP `3.7061` edge `-0.0959` maxDD `-66.7371`
- `market_context_high->index_24h` score `-12.3643` n `224` status `ready` deltaP `-7.0306` edge `-0.1313` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
