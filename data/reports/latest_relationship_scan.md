# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T17:52:49.804515+00:00`
- Price records: `672`
- Market context records: `4114`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10592`

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

- `risk_on_high->unknown_4h` score `144.7127` n `40` status `ready` deltaP `-9.1159` edge `12.3018` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.7127` n `40` status `ready` deltaP `-9.1159` edge `12.3018` maxDD `-10.864`
- `market_context_high->unknown_1h` score `41.5924` n `193` status `ready` deltaP `1.9043` edge `3.6111` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `34.5206` n `147` status `ready` deltaP `-9.258` edge `3.3413` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `14.5364` n `183` status `ready` deltaP `-1.0421` edge `1.7606` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.073` n `40` status `ready` deltaP `37.5915` edge `0.0102` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.073` n `40` status `ready` deltaP `37.5915` edge `0.0102` maxDD `-0.0446`
- `risk_on_high->crypto_major_4h` score `0.4519` n `40` status `ready` deltaP `17.9268` edge `-0.0153` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.4519` n `40` status `ready` deltaP `17.9268` edge `-0.0153` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.314` n `40` status `ready` deltaP `11.2126` edge `-0.0095` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.314` n `40` status `ready` deltaP `11.2126` edge `-0.0095` maxDD `-0.7937`
- `risk_on_high->commodity_24h` score `0.1614` n `40` status `ready` deltaP `-1.2153` edge `0.2497` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.1614` n `40` status `ready` deltaP `-1.2153` edge `0.2497` maxDD `-12.9187`
- `risk_on_high->fx_4h` score `0.0424` n `40` status `ready` deltaP `9.4817` edge `0.0013` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0424` n `40` status `ready` deltaP `9.4817` edge `0.0013` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0389` n `40` status `ready` deltaP `4.1018` edge `0.0006` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0389` n `40` status `ready` deltaP `4.1018` edge `0.0006` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.0019` n `40` status `ready` deltaP `10.509` edge `-0.0156` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0019` n `40` status `ready` deltaP `10.509` edge `-0.0156` maxDD `-2.3372`
- `market_context_high->fx_1h` score `-0.2467` n `193` status `ready` deltaP `2.4697` edge `0.0004` maxDD `-0.546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
