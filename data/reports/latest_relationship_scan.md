# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T06:52:34.488003+00:00`
- Price records: `672`
- Market context records: `4068`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10216`

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

- `risk_on_high->unknown_4h` score `145.0157` n `40` status `ready` deltaP `-6.8293` edge `12.3118` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.0157` n `40` status `ready` deltaP `-6.8293` edge `12.3118` maxDD `-10.864`
- `market_context_high->unknown_1h` score `51.122` n `172` status `ready` deltaP `2.0297` edge `4.4044` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.3497` n `144` status `ready` deltaP `-8.1997` edge `3.57` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `17.05` n `172` status `ready` deltaP `-0.9572` edge `1.9695` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.7796` n `40` status `ready` deltaP `38.3537` edge `0.064` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.7796` n `40` status `ready` deltaP `38.3537` edge `0.064` maxDD `-0.0446`
- `risk_on_high->equity_24h` score `2.0863` n `40` status `ready` deltaP `30.8492` edge `-0.0318` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.0863` n `40` status `ready` deltaP `30.8492` edge `-0.0318` maxDD `0.0`
- `market_context_high->index_24h` score `1.7439` n `144` status `ready` deltaP `18.5442` edge `0.0217` maxDD `0.0`
- `market_context_high->equity_4h` score `1.4043` n `172` status `ready` deltaP `15.2723` edge `0.1683` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `1.2149` n `40` status `ready` deltaP `19.6037` edge `0.0371` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.2149` n `40` status `ready` deltaP `19.6037` edge `0.0371` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.8173` n `172` status `ready` deltaP `6.2213` edge `0.0826` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.5215` n `40` status `ready` deltaP `11.512` edge `0.0058` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.5215` n `40` status `ready` deltaP `11.512` edge `0.0058` maxDD `-0.7937`
- `risk_on_high->metal_4h` score `0.2199` n `40` status `ready` deltaP `11.7073` edge `-0.0163` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.2199` n `40` status `ready` deltaP `11.7073` edge `-0.0163` maxDD `-1.3516`
- `risk_on_high->crypto_major_1h` score `0.2029` n `40` status `ready` deltaP `12.4551` edge `-0.0028` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2029` n `40` status `ready` deltaP `12.4551` edge `-0.0028` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
