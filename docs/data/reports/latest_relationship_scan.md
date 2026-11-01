# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T14:07:28.375181+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6597`

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

- `market_context_high->unknown_24h` score `7031.4014` n `55` status `ready` deltaP `1.5625` edge `585.9397` maxDD `0.0`
- `market_context_high->unknown_4h` score `379.5085` n `55` status `ready` deltaP `5.194` edge `31.5954` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `74.8083` n `55` status `ready` deltaP `3.7616` edge `6.22` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.1153` n `55` status `ready` deltaP `43.3207` edge `1.4944` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.055` n `98` status `ready` deltaP `30.4847` edge `1.0203` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.7958` n `55` status `ready` deltaP `55.3819` edge `0.1971` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.4363` n `55` status `ready` deltaP `45.442` edge `0.2645` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.9869` n `55` status `ready` deltaP `23.75` edge `0.37` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.5679` n `55` status `ready` deltaP `30.5876` edge `0.2937` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `3.8516` n `116` status `ready` deltaP `15.3017` edge `0.3576` maxDD `-7.4246`
- `market_context_high->equity_4h` score `3.398` n `55` status `ready` deltaP `5.5903` edge `0.3161` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3795` n `55` status `ready` deltaP `31.8293` edge `0.0945` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.4244` n `55` status `ready` deltaP `10.8586` edge `0.3061` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7317` n `55` status `ready` deltaP `-5.3409` edge `0.4094` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5678` n `55` status `ready` deltaP `18.3508` edge `0.0508` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4782` n `55` status `ready` deltaP `2.5776` edge `0.1585` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.346` n `55` status `ready` deltaP `7.7327` edge `0.1216` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.2672` n `55` status `ready` deltaP `3.3261` edge `0.1505` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.9247` n `55` status `ready` deltaP `11.4752` edge `0.0254` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.7209` n `128` status `ready` deltaP `9.1926` edge `0.0942` maxDD `-3.9659`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
