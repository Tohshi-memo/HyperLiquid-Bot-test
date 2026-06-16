# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T05:22:26.969120+00:00`
- Price records: `672`
- Market context records: `4061`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10440`

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

- `risk_on_high->unknown_4h` score `145.0589` n `40` status `ready` deltaP `-6.8293` edge `12.3154` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.0589` n `40` status `ready` deltaP `-6.8293` edge `12.3154` maxDD `-10.864`
- `market_context_high->unknown_1h` score `50.0541` n `172` status `ready` deltaP `1.7303` edge `4.3174` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.4884` n `144` status `ready` deltaP `-8.0264` edge `3.5804` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `18.1975` n `168` status `ready` deltaP `-0.6388` edge `2.063` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.863` n `40` status `ready` deltaP `38.811` edge `0.0679` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.863` n `40` status `ready` deltaP `38.811` edge `0.0679` maxDD `-0.0446`
- `risk_on_high->equity_24h` score `2.8211` n `40` status `ready` deltaP `31.8891` edge `0.0225` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.8211` n `40` status `ready` deltaP `31.8891` edge `0.0225` maxDD `0.0`
- `market_context_high->index_24h` score `2.1283` n `144` status `ready` deltaP `19.5841` edge `0.0468` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.4572` n `40` status `ready` deltaP `20.5183` edge `0.0512` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.4572` n `40` status `ready` deltaP `20.5183` edge `0.0512` maxDD `-2.6576`
- `market_context_high->equity_4h` score `1.4078` n `168` status `ready` deltaP `15.1205` edge `0.1696` maxDD `-6.9137`
- `market_context_high->equity_1h` score `0.8293` n `172` status `ready` deltaP `6.371` edge `0.0826` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.5335` n `40` status `ready` deltaP `11.6617` edge `0.0058` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.5335` n `40` status `ready` deltaP `11.6617` edge `0.0058` maxDD `-0.7937`
- `risk_on_high->crypto_major_1h` score `0.2629` n `40` status `ready` deltaP `13.0539` edge `0.0009` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2629` n `40` status `ready` deltaP `13.0539` edge `0.0009` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.2199` n `40` status `ready` deltaP `11.7073` edge `-0.0163` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.2199` n `40` status `ready` deltaP `11.7073` edge `-0.0163` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
