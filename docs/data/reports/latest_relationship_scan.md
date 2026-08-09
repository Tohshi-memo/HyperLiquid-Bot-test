# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T09:37:30.125910+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8841`

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

- `market_context_high->equity_24h` score `3.7668` n `103` status `ready` deltaP `4.5729` edge `0.5894` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6409` n `103` status `ready` deltaP `12.3854` edge `0.1951` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.1596` n `143` status `ready` deltaP `14.8996` edge `0.0646` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7737` n `143` status `ready` deltaP `10.6916` edge `0.0275` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.772` n `103` status `ready` deltaP `21.575` edge `0.0418` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5618` n `103` status `ready` deltaP `9.1002` edge `0.1645` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.2954` n `143` status `ready` deltaP `4.2953` edge `-0.0037` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4151` n `143` status `ready` deltaP `-1.3933` edge `-0.005` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.4615` n `143` status `ready` deltaP `5.9803` edge `-0.003` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6729` n `143` status `ready` deltaP `-4.5883` edge `-0.0061` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.8636` n `143` status `ready` deltaP `-0.4583` edge `-0.0084` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.8725` n `143` status `ready` deltaP `0.2618` edge `0.0084` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9567` n `143` status `ready` deltaP `-0.7462` edge `-0.0168` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8581` n `143` status `ready` deltaP `-9.8342` edge `-0.0251` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5125` n `143` status `ready` deltaP `-1.2664` edge `-0.0672` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.0537` n `143` status `ready` deltaP `-9.9389` edge `-0.056` maxDD `-7.2436`
- `market_context_high->crypto_major_24h` score `-3.3829` n `103` status `ready` deltaP `5.178` edge `-0.067` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.5427` n `143` status `ready` deltaP `-6.4473` edge `-0.0866` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-5.1895` n `103` status `ready` deltaP `-14.1822` edge `-0.1936` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8065` n `143` status `ready` deltaP `-5.7944` edge `-0.5672` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
