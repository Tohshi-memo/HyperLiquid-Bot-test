# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T03:37:29.330652+00:00`
- Price records: `672`
- Market context records: `5002`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10290`

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

- `market_context_high->unknown_1h` score `15.1567` n `93` status `ready` deltaP `3.9679` edge `1.2867` maxDD `-1.674`
- `market_context_high->unknown_4h` score `6.5375` n `90` status `ready` deltaP `21.9613` edge `0.5006` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.8695` n `90` status `ready` deltaP `17.754` edge `0.5292` maxDD `-8.3416`
- `market_context_high->unknown_24h` score `5.4709` n `74` status `ready` deltaP `29.8142` edge `0.2914` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.1275` n `90` status `ready` deltaP `12.8523` edge `0.481` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.2203` n `90` status `ready` deltaP `12.5678` edge `0.1258` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8764` n `93` status `ready` deltaP `8.1868` edge `0.0758` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.856` n `93` status `ready` deltaP `6.553` edge `0.1194` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.5988` n `90` status `ready` deltaP `4.9221` edge `0.1821` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3604` n `93` status `ready` deltaP `6.2536` edge `0.038` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.1935` n `90` status `ready` deltaP `5.4438` edge `0.0422` maxDD `-0.9895`
- `market_context_high->crypto_alt_1h` score `0.1734` n `93` status `ready` deltaP `5.1107` edge `0.0904` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.1824` n `74` status `ready` deltaP `7.1275` edge `0.0053` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.2808` n `93` status `ready` deltaP `2.3067` edge `0.0146` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5563` n `93` status `ready` deltaP `2.2117` edge `0.013` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7654` n `90` status `ready` deltaP `4.5495` edge `-0.0032` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.9108` n `90` status `ready` deltaP `-2.5271` edge `-0.0019` maxDD `-1.1746`
- `market_context_high->fx_1h` score `-1.7473` n `93` status `ready` deltaP `-11.8489` edge `-0.0056` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-4.138` n `74` status `ready` deltaP `0.5208` edge `0.0115` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.1464` n `74` status `ready` deltaP `5.9684` edge `-0.0605` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
