# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T07:52:25.626995+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5087`

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

- `market_context_high->unknown_24h` score `5691.0211` n `31` status `ready` deltaP `1.3889` edge `474.2425` maxDD `0.0`
- `market_context_high->unknown_4h` score `671.8697` n `36` status `ready` deltaP `8.8415` edge `55.9302` maxDD `0.0`
- `market_context_high->unknown_1h` score `176.5113` n `36` status `ready` deltaP `7.535` edge `14.6701` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.9734` n `31` status `ready` deltaP `41.3923` edge `1.4121` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `10.7639` n `101` status `ready` deltaP `28.9827` edge `0.9261` maxDD `-13.7862`
- `market_context_high->commodity_24h` score `7.3115` n `31` status `ready` deltaP `41.7563` edge `0.362` maxDD `-0.8203`
- `market_context_high->index_24h` score `7.0602` n `31` status `ready` deltaP `49.1319` edge `0.2608` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.0337` n `36` status `ready` deltaP `25.2202` edge `0.3641` maxDD `-1.6876`
- `market_context_high->equity_4h` score `5.9442` n `36` status `ready` deltaP `9.773` edge `0.5004` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `4.7246` n `36` status `ready` deltaP `22.8659` edge `0.2749` maxDD `-1.6901`
- `market_context_high->equity_1h` score `3.7097` n `36` status `ready` deltaP `13.4398` edge `0.2596` maxDD `-1.2043`
- `market_context_high->index_4h` score `2.6903` n `36` status `ready` deltaP `25.5251` edge `0.0767` maxDD `-0.1474`
- `news_risk_high->crypto_alt_4h` score `2.6209` n `126` status `ready` deltaP `10.5376` edge `0.2868` maxDD `-7.4246`
- `market_context_high->crypto_major_1h` score `2.5749` n `36` status `ready` deltaP `13.7392` edge `0.162` maxDD `-1.1219`
- `market_context_high->crypto_alt_1h` score `1.8128` n `36` status `ready` deltaP `11.5602` edge `0.1995` maxDD `-1.5324`
- `market_context_high->metal_4h` score `1.4061` n `36` status `ready` deltaP `16.5989` edge `0.049` maxDD `-0.7323`
- `market_context_high->fx_1h` score `1.2332` n `36` status `ready` deltaP `16.2176` edge `0.0118` maxDD `-0.0388`
- `market_context_high->crypto_alt_24h` score `1.1778` n `31` status `ready` deltaP `-9.2798` edge `0.3118` maxDD `-8.8096`
- `market_context_high->commodity_4h` score `1.0709` n `36` status `ready` deltaP `21.4261` edge `0.0357` maxDD `-1.633`
- `market_context_high->index_1h` score `0.7207` n `36` status `ready` deltaP `6.986` edge `0.0376` maxDD `-0.2628`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
