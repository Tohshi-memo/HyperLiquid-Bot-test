# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T03:52:29.598410+00:00`
- Price records: `672`
- Market context records: `6567`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9904`

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

- `market_context_high->unknown_24h` score `6.2426` n `144` status `ready` deltaP `11.032` edge `0.7767` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.7028` n `210` status `ready` deltaP `-5.4291` edge `0.2682` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3941` n `144` status `ready` deltaP `13.3492` edge `0.214` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3549` n `210` status `ready` deltaP `0.8583` edge `-0.0005` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.3612` n `210` status `ready` deltaP `7.4964` edge `0.0303` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.43` n `210` status `ready` deltaP `6.939` edge `0.0299` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5475` n `210` status `ready` deltaP `-0.3807` edge `0.0043` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5985` n `210` status `ready` deltaP `-0.5589` edge `-0.0047` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9038` n `209` status `ready` deltaP `8.0751` edge `0.0076` maxDD `-5.1849`
- `market_context_high->equity_1h` score `-1.1285` n `210` status `ready` deltaP `2.0816` edge `0.0031` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2212` n `210` status `ready` deltaP `-3.128` edge `-0.0002` maxDD `-2.1239`
- `market_context_high->unknown_4h` score `-1.3287` n `209` status `ready` deltaP `-15.5786` edge `0.2337` maxDD `-10.5788`
- `market_context_high->commodity_4h` score `-1.3752` n `209` status `ready` deltaP `-2.2258` edge `-0.012` maxDD `-5.6246`
- `market_context_high->crypto_major_4h` score `-1.4643` n `209` status `ready` deltaP `8.1536` edge `0.06` maxDD `-14.8335`
- `market_context_high->crypto_alt_4h` score `-1.6368` n `209` status `ready` deltaP `5.5024` edge `0.0649` maxDD `-17.2473`
- `market_context_high->fx_4h` score `-1.7604` n `209` status `ready` deltaP `-0.1774` edge `-0.0033` maxDD `-3.3635`
- `market_context_high->metal_24h` score `-1.9369` n `144` status `ready` deltaP `6.0917` edge `0.091` maxDD `-5.7746`
- `market_context_high->metal_4h` score `-2.0385` n `209` status `ready` deltaP `-1.1911` edge `0.0237` maxDD `-4.8348`
- `market_context_high->index_24h` score `-3.7521` n `144` status `ready` deltaP `1.4429` edge `-0.0002` maxDD `-10.7676`
- `market_context_high->fx_24h` score `-3.8336` n `144` status `ready` deltaP `-4.8143` edge `-0.0059` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
