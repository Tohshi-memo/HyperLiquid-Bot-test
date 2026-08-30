# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T02:22:20.476236+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11498`

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

- `risk_on_high->unknown_4h` score `5.4049` n `60` status `ready` deltaP `21.4431` edge `0.3503` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `5.4049` n `60` status `ready` deltaP `21.4431` edge `0.3503` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `4.7363` n `60` status `ready` deltaP `26.4939` edge `0.254` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `4.7363` n `60` status `ready` deltaP `26.4939` edge `0.254` maxDD `-1.208`
- `market_context_high->metal_24h` score `4.6778` n `104` status `ready` deltaP `34.415` edge `0.2623` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `3.8372` n `162` status `ready` deltaP `18.3567` edge `0.2444` maxDD `-1.0945`
- `risk_on_high->crypto_alt_4h` score `3.2152` n `60` status `ready` deltaP `17.5711` edge `0.3374` maxDD `-1.3869`
- `risk_on_and_context->crypto_alt_4h` score `3.2152` n `60` status `ready` deltaP `17.5711` edge `0.3374` maxDD `-1.3869`
- `risk_on_high->equity_4h` score `2.6186` n `60` status `ready` deltaP `23.3028` edge `0.0878` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.6186` n `60` status `ready` deltaP `23.3028` edge `0.0878` maxDD `-0.3281`
- `risk_on_high->metal_4h` score `2.0035` n `60` status `ready` deltaP `25.1016` edge `0.0292` maxDD `-0.0336`
- `risk_on_and_context->metal_4h` score `2.0035` n `60` status `ready` deltaP `25.1016` edge `0.0292` maxDD `-0.0336`
- `risk_on_high->unknown_1h` score `1.9537` n `66` status `ready` deltaP `3.3071` edge `0.1847` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `1.9537` n `66` status `ready` deltaP `3.3071` edge `0.1847` maxDD `-1.5148`
- `market_context_high->unknown_1h` score `1.8659` n `168` status `ready` deltaP `9.3136` edge `0.1415` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.8267` n `60` status `ready` deltaP `25.7317` edge `0.0116` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.8267` n `60` status `ready` deltaP `25.7317` edge `0.0116` maxDD `-0.1405`
- `risk_on_high->metal_1h` score `1.1789` n `66` status `ready` deltaP `16.8527` edge `0.0073` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.1789` n `66` status `ready` deltaP `16.8527` edge `0.0073` maxDD `-0.0463`
- `news_risk_high->unknown_1h` score `0.6829` n `40` status `ready` deltaP `-15.3293` edge `0.1948` maxDD `-0.8558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
