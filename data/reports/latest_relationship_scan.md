# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T03:22:24.785915+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11504`

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

- `risk_on_high->unknown_4h` score `7.3912` n `64` status `ready` deltaP `22.3323` edge `0.5099` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `7.3912` n `64` status `ready` deltaP `22.3323` edge `0.5099` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6627` n `104` status `ready` deltaP `34.2414` edge `0.2622` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `4.523` n `166` status `ready` deltaP `18.6802` edge `0.2994` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `4.0459` n `64` status `ready` deltaP `22.904` edge `0.2204` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `4.0459` n `64` status `ready` deltaP `22.904` edge `0.2204` maxDD `-1.208`
- `risk_on_high->crypto_alt_4h` score `2.7922` n `64` status `ready` deltaP `16.1204` edge `0.2988` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.7922` n `64` status `ready` deltaP `16.1204` edge `0.2988` maxDD `-1.5298`
- `risk_on_high->equity_4h` score `2.6254` n `64` status `ready` deltaP `24.0473` edge `0.0834` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.6254` n `64` status `ready` deltaP `24.0473` edge `0.0834` maxDD `-0.3281`
- `risk_on_high->unknown_1h` score `2.0341` n `66` status `ready` deltaP `3.4568` edge `0.1904` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `2.0341` n `66` status `ready` deltaP `3.4568` edge `0.1904` maxDD `-1.5148`
- `market_context_high->unknown_1h` score `1.9462` n `168` status `ready` deltaP `9.4633` edge `0.1472` maxDD `-1.5148`
- `risk_on_high->metal_4h` score `1.7894` n `64` status `ready` deltaP `22.7134` edge `0.0274` maxDD `-0.0431`
- `risk_on_and_context->metal_4h` score `1.7894` n `64` status `ready` deltaP `22.7134` edge `0.0274` maxDD `-0.0431`
- `risk_on_high->index_4h` score `1.6573` n `64` status `ready` deltaP `23.7043` edge `0.011` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.6573` n `64` status `ready` deltaP `23.7043` edge `0.011` maxDD `-0.1405`
- `risk_on_high->metal_1h` score `1.1908` n `66` status `ready` deltaP `17.0024` edge `0.0073` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.1908` n `66` status `ready` deltaP `17.0024` edge `0.0073` maxDD `-0.0463`
- `news_risk_high->fx_4h` score `0.5757` n `36` status `ready` deltaP `17.9032` edge `0.0094` maxDD `-0.3953`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
