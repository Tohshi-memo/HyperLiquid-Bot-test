# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T21:07:28.032937+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `170.1573` n `116` status `ready` deltaP `-28.0598` edge `14.6517` maxDD `-9.1222`
- `risk_on_high->unknown_24h` score `33.8472` n `32` status `ready` deltaP `-36.3572` edge `4.6568` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.8472` n `32` status `ready` deltaP `-36.3572` edge `4.6568` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9719` n `36` status `ready` deltaP `26.6609` edge `0.9412` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7419` n `36` status `ready` deltaP `39.939` edge `0.3789` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.3539` n `116` status `ready` deltaP `36.2308` edge `0.2937` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.4376` n `32` status `ready` deltaP `37.9549` edge `0.2001` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.4376` n `32` status `ready` deltaP `37.9549` edge `0.2001` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.0703` n `32` status `ready` deltaP `27.6809` edge `0.4529` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.0703` n `32` status `ready` deltaP `27.6809` edge `0.4529` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.7359` n `36` status `ready` deltaP `31.3692` edge `0.1022` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.939` n `32` status `ready` deltaP `21.1128` edge `0.1224` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.939` n `32` status `ready` deltaP `21.1128` edge `0.1224` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0784` n `116` status `ready` deltaP `19.7119` edge `0.0889` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9778` n `36` status `ready` deltaP `22.815` edge `0.0259` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.761` n `36` status `ready` deltaP `8.4332` edge `0.1224` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3737` n `32` status `ready` deltaP `14.7081` edge `0.0397` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3737` n `32` status `ready` deltaP `14.7081` edge `0.0397` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `0.7856` n `32` status `ready` deltaP `15.2026` edge `0.1773` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.7856` n `32` status `ready` deltaP `15.2026` edge `0.1773` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
