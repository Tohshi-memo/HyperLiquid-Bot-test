# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T07:37:22.476880+00:00`
- Price records: `672`
- Market context records: `2845`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->unknown_24h` score `2.5641` n `142` status `ready` deltaP `3.817` edge `0.2347` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.0706` n `142` status `ready` deltaP `1.834` edge `0.552` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `0.8466` n `142` status `ready` deltaP `12.0794` edge `0.2994` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.815` n `142` status `ready` deltaP `6.338` edge `0.131` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.2836` n `142` status `ready` deltaP `12.6911` edge `0.0359` maxDD `-2.3986`
- `market_context_high->index_24h` score `0.1893` n `142` status `ready` deltaP `5.3771` edge `0.078` maxDD `-2.5127`
- `market_context_high->unknown_1h` score `0.079` n `142` status `ready` deltaP `4.4805` edge `0.0498` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0953` n `142` status `ready` deltaP `4.0483` edge `0.0102` maxDD `-1.2855`
- `market_context_high->equity_24h` score `-0.4353` n `142` status `ready` deltaP `3.1788` edge `0.1429` maxDD `-12.6963`
- `market_context_high->fx_1h` score `-0.6161` n `142` status `ready` deltaP `-1.4358` edge `0.0026` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6179` n `142` status `ready` deltaP `-0.4322` edge `-0.001` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6918` n `142` status `ready` deltaP `0.2825` edge `-0.006` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7014` n `142` status `ready` deltaP `4.7968` edge `0.0541` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.8983` n `142` status `ready` deltaP `3.926` edge `0.0456` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.9183` n `142` status `ready` deltaP `-2.45` edge `0.0231` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-1.0944` n `142` status `ready` deltaP `1.8099` edge `0.0347` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.2127` n `142` status `ready` deltaP `-4.3627` edge `0.0059` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.3648` n `142` status `ready` deltaP `1.6854` edge `0.0058` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.4167` n `142` status `ready` deltaP `-1.8852` edge `-0.0183` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.4347` n `142` status `ready` deltaP `13.7281` edge `0.223` maxDD `-28.7261`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
