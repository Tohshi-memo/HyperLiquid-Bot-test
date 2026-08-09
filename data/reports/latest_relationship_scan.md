# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T04:52:27.570811+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8811`

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

- `market_context_high->equity_24h` score `3.5256` n `103` status `ready` deltaP `4.5729` edge `0.5693` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6923` n `103` status `ready` deltaP `13.2535` edge `0.1936` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4146` n `133` status `ready` deltaP `15.3723` edge `0.0827` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.9299` n `141` status `ready` deltaP `11.6236` edge `0.0343` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7999` n `103` status `ready` deltaP `21.2277` edge `0.0477` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5368` n `103` status `ready` deltaP `9.1002` edge `0.1613` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.2953` n `141` status `ready` deltaP `4.3105` edge `-0.0038` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.3085` n `133` status `ready` deltaP `7.7732` edge `-0.0022` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6646` n `141` status `ready` deltaP `-4.2935` edge `-0.007` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.702` n `133` status `ready` deltaP `-2.5926` edge `-0.0122` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.8192` n `141` status `ready` deltaP `-3.3953` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.9786` n `141` status `ready` deltaP `-0.3133` edge `0.0034` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0774` n `133` status `ready` deltaP `-2.7966` edge `-0.0186` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0459` n `141` status `ready` deltaP `-11.0863` edge `-0.0324` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.6537` n `133` status `ready` deltaP `-2.2075` edge `-0.0727` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2611` n `141` status `ready` deltaP `-11.2604` edge `-0.0646` maxDD `-7.2335`
- `market_context_high->crypto_major_24h` score `-3.3415` n `103` status `ready` deltaP `6.2197` edge `-0.0705` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.0491` n `133` status `ready` deltaP `-8.8919` edge `-0.1125` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.5442` n `103` status `ready` deltaP `-12.4461` edge `-0.1514` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-8.292` n `141` status `ready` deltaP `-6.1781` edge `-0.6051` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
