# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T09:22:26.176797+00:00`
- Price records: `672`
- Market context records: `2853`
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

- `market_context_high->crypto_alt_24h` score `3.2958` n `142` status `ready` deltaP `3.0492` edge `0.646` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `3.0922` n `142` status `ready` deltaP `5.0322` edge `0.2706` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `1.1322` n `142` status `ready` deltaP `13.2947` edge `0.3151` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.835` n `142` status `ready` deltaP `6.0331` edge `0.1347` maxDD `-3.7602`
- `market_context_high->equity_24h` score `0.7707` n `142` status `ready` deltaP `4.394` edge `0.2353` maxDD `-12.6963`
- `market_context_high->index_24h` score `0.6561` n `142` status `ready` deltaP `6.5923` edge `0.1088` maxDD `-2.5127`
- `market_context_high->index_4h` score `0.3221` n `142` status `ready` deltaP `12.996` edge `0.0388` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.1078` n `142` status `ready` deltaP `4.6302` edge `0.0512` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0727` n `142` status `ready` deltaP `4.198` edge `0.0121` maxDD `-1.2855`
- `market_context_high->crypto_alt_1h` score `-0.618` n `142` status `ready` deltaP `5.2459` edge `0.0618` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6498` n `142` status `ready` deltaP `-0.8813` edge `-0.0021` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.67` n `142` status `ready` deltaP `-2.0346` edge `0.0021` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.716` n `142` status `ready` deltaP `-0.0169` edge `-0.0071` maxDD `-3.0996`
- `market_context_high->equity_1h` score `-0.8212` n `142` status `ready` deltaP `-2.0009` edge `0.0282` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.8243` n `142` status `ready` deltaP `4.3751` edge `0.0521` maxDD `-9.622`
- `market_context_high->equity_4h` score `-0.952` n `142` status `ready` deltaP `2.4197` edge `0.0425` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-1.1791` n `142` status `ready` deltaP `13.7281` edge `0.2443` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.2333` n `142` status `ready` deltaP `-4.5152` edge `0.0052` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.3177` n `142` status `ready` deltaP `2.1427` edge `0.0088` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.4059` n `142` status `ready` deltaP `-1.8852` edge `-0.0174` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
