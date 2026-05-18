# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T12:22:18.827873+00:00`
- Price records: `672`
- Market context records: `1117`
- Flow alert records: `5119`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8704`

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

- `market_context_high->crypto_major_24h` score `18.3601` n `150` status `ready` deltaP `39.6389` edge `1.3121` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `7.9988` n `150` status `ready` deltaP `16.0` edge `0.6833` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.5997` n `150` status `ready` deltaP `16.5208` edge `0.4895` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.5655` n `150` status `ready` deltaP `-1.8889` edge `0.6431` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.2523` n `150` status `ready` deltaP `15.4791` edge `0.3653` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.5701` n `168` status `ready` deltaP `8.9649` edge `0.1374` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.8462` n `168` status `ready` deltaP `7.8324` edge `0.0866` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4881` n `168` status `ready` deltaP `7.6454` edge `0.0214` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2153` n `168` status `ready` deltaP `2.2811` edge `0.0405` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1352` n `168` status `ready` deltaP `8.3155` edge `0.0014` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.0071` n `168` status `ready` deltaP `7.9994` edge `0.1397` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.0098` n `168` status `ready` deltaP `6.8328` edge `0.0302` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.2364` n `168` status `ready` deltaP `6.8007` edge `-0.004` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3485` n `168` status `ready` deltaP `2.495` edge `0.0386` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.7057` n `168` status `ready` deltaP `1.2412` edge `0.0009` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7349` n `168` status `ready` deltaP `-1.9247` edge `-0.0006` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0498` n `168` status `ready` deltaP `5.3862` edge `0.126` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.4408` n `168` status `ready` deltaP `6.0903` edge `-0.0486` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.159` n `168` status `ready` deltaP `-11.1208` edge `-0.0141` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.3346` n `168` status `ready` deltaP `9.1609` edge `-0.2173` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
