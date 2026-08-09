# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T15:07:32.469580+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10825`

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

- `market_context_high->equity_24h` score `3.7762` n `103` status `ready` deltaP `4.2257` edge `0.5925` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.3465` n `103` status `ready` deltaP `9.2604` edge `0.1914` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.2748` n `143` status `ready` deltaP `15.8142` edge `0.0681` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8181` n `143` status `ready` deltaP `11.1407` edge `0.0282` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7068` n `103` status `ready` deltaP `21.4013` edge `0.0346` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.3986` n `103` status `ready` deltaP `6.3224` edge `0.1621` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3457` n `143` status `ready` deltaP `3.6965` edge `-0.0039` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.3832` n `143` status `ready` deltaP `-0.7945` edge `-0.0049` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5053` n `143` status `ready` deltaP `5.523` edge `-0.0036` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6737` n `143` status `ready` deltaP `-4.5883` edge `-0.0062` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.8562` n `143` status `ready` deltaP `-0.3059` edge `-0.0088` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9217` n `143` status `ready` deltaP `-0.3371` edge `0.0083` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0082` n `143` status `ready` deltaP `-1.6608` edge `-0.0173` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9252` n `143` status `ready` deltaP `-10.2833` edge `-0.0277` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.4807` n `143` status `ready` deltaP `-0.8091` edge `-0.0676` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2226` n `143` status `ready` deltaP `-11.2862` edge `-0.0611` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.7847` n `143` status `ready` deltaP `-7.9717` edge `-0.0966` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.101` n `103` status `ready` deltaP `1.7058` edge `-0.1037` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.4862` n `103` status `ready` deltaP `-18.0017` edge `-0.2762` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7897` n `143` status `ready` deltaP `-5.7944` edge `-0.5658` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
