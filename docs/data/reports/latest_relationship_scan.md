# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T13:37:20.751099+00:00`
- Price records: `672`
- Market context records: `2146`
- Flow alert records: `8074`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9158`

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

- `market_context_high->crypto_alt_4h` score `13.49` n `155` status `ready` deltaP `37.9052` edge `0.9651` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9892` n `155` status `ready` deltaP `41.9994` edge `0.7721` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.4794` n `155` status `ready` deltaP `25.2252` edge `0.4467` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.231` n `33` status `ready` deltaP `28.1966` edge `0.3984` maxDD `-3.0367`
- `market_context_high->equity_4h` score `5.0796` n `155` status `ready` deltaP `26.5431` edge `0.3558` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.8787` n `154` status `ready` deltaP `15.4289` edge `0.3432` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.4157` n `155` status `ready` deltaP `18.0983` edge `0.2117` maxDD `-1.817`
- `market_context_high->equity_24h` score `3.3223` n `154` status `ready` deltaP `26.9255` edge `0.5872` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `3.2088` n `155` status `ready` deltaP `16.6013` edge `0.2431` maxDD `-4.9097`
- `market_context_high->metal_4h` score `3.1947` n `155` status `ready` deltaP `21.7762` edge `0.2598` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.1509` n `155` status `ready` deltaP `22.8954` edge `0.1783` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.949` n `154` status `ready` deltaP `27.523` edge `0.5943` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.3713` n `33` status `ready` deltaP `30.8851` edge `0.0101` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.2914` n `154` status `ready` deltaP `21.9381` edge `1.0061` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.5044` n `33` status `ready` deltaP `18.3435` edge `0.1429` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.4073` n `40` status `ready` deltaP `21.6018` edge `0.0202` maxDD `-1.7548`
- `market_context_high->equity_1h` score `0.9016` n `155` status `ready` deltaP `10.706` edge `0.0826` maxDD `-2.6402`
- `news_risk_high->commodity_1h` score `0.7081` n `40` status `ready` deltaP `10.1497` edge `0.0911` maxDD `-2.1052`
- `market_context_high->metal_1h` score `0.6763` n `155` status `ready` deltaP `9.6079` edge `0.0593` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.6733` n `40` status `ready` deltaP `10.4491` edge `0.0121` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
