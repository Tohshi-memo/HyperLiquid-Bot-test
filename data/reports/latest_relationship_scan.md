# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T08:22:26.382798+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10233`

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

- `risk_on_high->crypto_alt_24h` score `8.203` n `117` status `ready` deltaP `20.3793` edge `0.5707` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.203` n `117` status `ready` deltaP `20.3793` edge `0.5707` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.8148` n `117` status `ready` deltaP `31.5497` edge `0.3114` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.8148` n `117` status `ready` deltaP `31.5497` edge `0.3114` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.9919` n `117` status `ready` deltaP `21.1005` edge `0.9061` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.9919` n `117` status `ready` deltaP `21.1005` edge `0.9061` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8353` n `117` status `ready` deltaP `25.9811` edge `0.3156` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8353` n `117` status `ready` deltaP `25.9811` edge `0.3156` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.1555` n `241` status `ready` deltaP `13.0345` edge `0.2588` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `0.9118` n `117` status `ready` deltaP `3.7976` edge `0.0859` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9118` n `117` status `ready` deltaP `3.7976` edge `0.0859` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.7854` n `117` status `ready` deltaP `9.7623` edge `0.0046` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `0.7854` n `117` status `ready` deltaP `9.7623` edge `0.0046` maxDD `-0.0051`
- `risk_on_high->equity_1h` score `0.5204` n `117` status `ready` deltaP `14.672` edge `-0.0013` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.5204` n `117` status `ready` deltaP `14.672` edge `-0.0013` maxDD `-2.2516`
- `risk_on_high->metal_1h` score `0.259` n `117` status `ready` deltaP `9.6794` edge `0.0017` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.259` n `117` status `ready` deltaP `9.6794` edge `0.0017` maxDD `-0.3081`
- `risk_on_high->crypto_major_1h` score `0.2457` n `117` status `ready` deltaP `4.0343` edge `0.0663` maxDD `-3.1509`
- `risk_on_and_context->crypto_major_1h` score `0.2457` n `117` status `ready` deltaP `4.0343` edge `0.0663` maxDD `-3.1509`
- `risk_on_high->index_1h` score `0.1967` n `117` status `ready` deltaP `9.7178` edge `-0.0032` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
