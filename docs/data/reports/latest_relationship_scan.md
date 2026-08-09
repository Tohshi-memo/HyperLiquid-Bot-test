# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T13:37:30.266340+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10809`

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

- `market_context_high->equity_24h` score `3.8544` n `103` status `ready` deltaP `4.5729` edge `0.5967` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4478` n `103` status `ready` deltaP `10.3021` edge `0.1929` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.1656` n `143` status `ready` deltaP `14.8996` edge `0.0651` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7666` n `143` status `ready` deltaP `10.5419` edge `0.0279` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7193` n `103` status `ready` deltaP `21.4013` edge `0.0362` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4629` n `103` status `ready` deltaP `7.3641` edge `0.1634` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3469` n `143` status `ready` deltaP `3.6965` edge `-0.004` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.3505` n `143` status `ready` deltaP `-0.1957` edge `-0.0047` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5199` n `143` status `ready` deltaP `5.3706` edge `-0.0038` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6651` n `143` status `ready` deltaP `-4.4386` edge `-0.0061` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.7746` n `143` status `ready` deltaP `0.6087` edge `-0.0081` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.8785` n `143` status `ready` deltaP `0.1121` edge `0.0089` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9821` n `143` status `ready` deltaP `-1.2035` edge `-0.017` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8881` n `143` status `ready` deltaP `-9.9839` edge `-0.0266` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.3691` n `143` status `ready` deltaP `0.1056` edge `-0.0644` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1471` n `143` status `ready` deltaP `-10.6874` edge `-0.0588` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.6383` n `143` status `ready` deltaP `-7.057` edge `-0.0905` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-3.9291` n `103` status `ready` deltaP `2.4003` edge `-0.094` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.1113` n `103` status `ready` deltaP `-16.96` edge `-0.2519` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7897` n `143` status `ready` deltaP `-5.7944` edge `-0.5658` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
