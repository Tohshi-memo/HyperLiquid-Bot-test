# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T05:37:29.685946+00:00`
- Price records: `672`
- Market context records: `5010`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10274`

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

- `market_context_high->unknown_1h` score `15.416` n `93` status `ready` deltaP `3.8182` edge `1.3093` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.9149` n `93` status `ready` deltaP `22.0594` edge `0.7814` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.6627` n `93` status `ready` deltaP `17.4043` edge `0.5143` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.2274` n `93` status `ready` deltaP `14.0261` edge `0.4815` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `3.2011` n `74` status `ready` deltaP `28.7725` edge `0.1092` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3413` n `93` status `ready` deltaP `14.3063` edge `0.1243` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.9303` n `93` status `ready` deltaP `8.7856` edge `0.0763` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8345` n `93` status `ready` deltaP `6.4033` edge `0.1186` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.535` n `93` status `ready` deltaP `4.3404` edge `0.1778` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.364` n `93` status `ready` deltaP `6.2536` edge `0.0383` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1469` n `93` status `ready` deltaP `4.8113` edge `0.089` maxDD `-5.5126`
- `market_context_high->index_4h` score `-0.0547` n `93` status `ready` deltaP `4.6289` edge `0.0407` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.1333` n `74` status `ready` deltaP `7.9955` edge `0.0058` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.294` n `93` status `ready` deltaP `2.0073` edge `0.0149` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5575` n `93` status `ready` deltaP `2.2117` edge `0.0129` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7923` n `93` status `ready` deltaP `4.0028` edge `-0.003` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.984` n `93` status `ready` deltaP `-3.7634` edge `-0.0022` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7581` n `93` status `ready` deltaP `-11.9986` edge `-0.0055` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-4.0439` n `74` status `ready` deltaP `1.9097` edge `0.0143` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.281` n `74` status `ready` deltaP `4.5795` edge `-0.0685` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
