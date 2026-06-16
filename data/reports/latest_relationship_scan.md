# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T05:52:31.340624+00:00`
- Price records: `672`
- Market context records: `4064`
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

- `risk_on_high->unknown_4h` score `145.0952` n `40` status `ready` deltaP `-6.5244` edge `12.3164` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.0952` n `40` status `ready` deltaP `-6.5244` edge `12.3164` maxDD `-10.864`
- `market_context_high->unknown_1h` score `51.152` n `172` status `ready` deltaP `2.0297` edge `4.4069` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.4728` n `144` status `ready` deltaP `-8.0264` edge `3.5791` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `17.5703` n `170` status `ready` deltaP `-1.0832` edge `2.0137` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.857` n `40` status `ready` deltaP `38.811` edge `0.0674` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.857` n `40` status `ready` deltaP `38.811` edge `0.0674` maxDD `-0.0446`
- `risk_on_high->equity_24h` score `2.5786` n `40` status `ready` deltaP `31.5425` edge `0.0046` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.5786` n `40` status `ready` deltaP `31.5425` edge `0.0046` maxDD `0.0`
- `market_context_high->index_24h` score `1.9998` n `144` status `ready` deltaP `19.2374` edge `0.0384` maxDD `0.0`
- `market_context_high->equity_4h` score `1.4384` n `170` status `ready` deltaP `15.4286` edge `0.1701` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `1.4184` n `40` status `ready` deltaP `20.2134` edge `0.05` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.4184` n `40` status `ready` deltaP `20.2134` edge `0.05` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.8389` n `172` status `ready` deltaP `6.371` edge `0.0834` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.5431` n `40` status `ready` deltaP `11.6617` edge `0.0066` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.5431` n `40` status `ready` deltaP `11.6617` edge `0.0066` maxDD `-0.7937`
- `risk_on_high->crypto_major_1h` score `0.2567` n `40` status `ready` deltaP `13.0539` edge `0.0001` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2567` n `40` status `ready` deltaP `13.0539` edge `0.0001` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.2269` n `40` status `ready` deltaP `11.7073` edge `-0.0154` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.2269` n `40` status `ready` deltaP `11.7073` edge `-0.0154` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
