# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T20:52:25.229516+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8478`

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

- `news_risk_high->crypto_major_24h` score `51.0968` n `72` status `ready` deltaP `27.0833` edge `4.1667` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.5904` n `72` status `ready` deltaP `33.507` edge `3.6304` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `32.8353` n `115` status `ready` deltaP `-4.0946` edge `2.7869` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.7899` n `72` status `ready` deltaP `36.9792` edge `0.4902` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.8701` n `115` status `ready` deltaP `40.089` edge `0.4411` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.5618` n `98` status `ready` deltaP `20.7037` edge `0.4464` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.3255` n `98` status `ready` deltaP `21.7707` edge `0.3411` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2412` n `98` status `ready` deltaP `18.624` edge `0.1925` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.7718` n `115` status `ready` deltaP `28.3059` edge `0.0832` maxDD `-0.274`
- `news_risk_high->crypto_major_1h` score `2.4007` n `98` status `ready` deltaP `19.9713` edge `0.1192` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7225` n `72` status `ready` deltaP `22.5694` edge `0.0775` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.5031` n `115` status `ready` deltaP `18.4887` edge `0.0272` maxDD `-0.3491`
- `market_context_high->fx_4h` score `0.9163` n `115` status `ready` deltaP `18.5498` edge `-0.0005` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7967` n `98` status `ready` deltaP `18.8246` edge `0.0463` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6955` n `98` status `ready` deltaP `15.3061` edge `0.0161` maxDD `-0.8144`
- `news_risk_high->equity_1h` score `0.457` n `98` status `ready` deltaP `7.1154` edge `0.0312` maxDD `-0.9112`
- `news_risk_high->fx_24h` score `0.4392` n `72` status `ready` deltaP `2.4306` edge `0.0386` maxDD `-0.1231`
- `market_context_high->fx_24h` score `0.2952` n `115` status `ready` deltaP `8.5054` edge `-0.0279` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.0773` n `115` status `ready` deltaP `4.6394` edge `0.0013` maxDD `-0.063`
- `news_risk_high->equity_4h` score `-0.0461` n `98` status `ready` deltaP `8.9037` edge `0.0812` maxDD `-5.2186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
