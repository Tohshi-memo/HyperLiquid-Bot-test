# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T14:37:33.985166+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2588`

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

- `market_context_high->unknown_1h` score `12703.8366` n `103` status `ready` deltaP `1.0741` edge `1058.6657` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `8042.089` n `102` status `ready` deltaP `-0.3736` edge `670.205` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `25.2256` n `88` status `ready` deltaP `46.1489` edge `1.8538` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.5943` n `88` status `ready` deltaP `23.3586` edge `1.47` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.8553` n `102` status `ready` deltaP `3.4194` edge `0.4137` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.1964` n `102` status `ready` deltaP `4.1816` edge `0.2794` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5013` n `102` status `ready` deltaP `18.5348` edge `0.0472` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.3583` n `88` status `ready` deltaP `18.7184` edge `0.2139` maxDD `-14.7068`
- `market_context_high->metal_1h` score `-0.1475` n `103` status `ready` deltaP `4.7497` edge `0.0159` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.1896` n `103` status `ready` deltaP `4.2236` edge `0.0872` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.3476` n `103` status `ready` deltaP `1.7601` edge `0.0049` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.67` n `103` status `ready` deltaP `-1.2296` edge `0.0445` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.0212` n `103` status `ready` deltaP `4.6727` edge `0.0158` maxDD `-10.8962`
- `market_context_high->index_4h` score `-1.273` n `102` status `ready` deltaP `-3.8349` edge `-0.0033` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.489` n `103` status `ready` deltaP `-10.3352` edge `-0.0007` maxDD `-0.3584`
- `market_context_high->fx_4h` score `-2.3677` n `102` status `ready` deltaP `-14.7537` edge `-0.0036` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4701` n `103` status `ready` deltaP `-10.1898` edge `-0.0301` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-7.0472` n `88` status `ready` deltaP `-22.5537` edge `-0.0096` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.383` n `102` status `ready` deltaP `-31.0049` edge `-0.13` maxDD `-14.9509`
- `market_context_high->equity_4h` score `-9.508` n `102` status `ready` deltaP `-8.5426` edge `-0.0677` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
