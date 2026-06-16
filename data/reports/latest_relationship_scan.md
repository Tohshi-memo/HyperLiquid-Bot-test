# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T07:07:32.080398+00:00`
- Price records: `672`
- Market context records: `4069`
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

- `risk_on_high->unknown_4h` score `144.9977` n `40` status `ready` deltaP `-6.8293` edge `12.3103` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.9977` n `40` status `ready` deltaP `-6.8293` edge `12.3103` maxDD `-10.864`
- `market_context_high->unknown_1h` score `51.1172` n `172` status `ready` deltaP `2.0297` edge `4.404` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.3125` n `144` status `ready` deltaP `-8.1997` edge `3.5669` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `17.032` n `172` status `ready` deltaP `-0.9572` edge `1.968` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.753` n `40` status `ready` deltaP `38.2012` edge `0.0628` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.753` n `40` status `ready` deltaP `38.2012` edge `0.0628` maxDD `-0.0446`
- `risk_on_high->equity_24h` score `1.9693` n `40` status `ready` deltaP `30.6759` edge `-0.0404` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.9693` n `40` status `ready` deltaP `30.6759` edge `-0.0404` maxDD `0.0`
- `market_context_high->index_24h` score `1.6857` n `144` status `ready` deltaP `18.3709` edge `0.018` maxDD `0.0`
- `market_context_high->equity_4h` score `1.3777` n `172` status `ready` deltaP `15.1198` edge `0.1671` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `1.1535` n `40` status `ready` deltaP `19.4512` edge `0.033` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.1535` n `40` status `ready` deltaP `19.4512` edge `0.033` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.7981` n `172` status `ready` deltaP `6.0716` edge `0.082` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.5023` n `40` status `ready` deltaP `11.3623` edge `0.0052` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.5023` n `40` status `ready` deltaP `11.3623` edge `0.0052` maxDD `-0.7937`
- `risk_on_high->metal_4h` score `0.2206` n `40` status `ready` deltaP `11.7073` edge `-0.0162` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.2206` n `40` status `ready` deltaP `11.7073` edge `-0.0162` maxDD `-1.3516`
- `risk_on_high->crypto_major_1h` score `0.185` n `40` status `ready` deltaP `12.3054` edge `-0.0041` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.185` n `40` status `ready` deltaP `12.3054` edge `-0.0041` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
