# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T18:37:27.291448+00:00`
- Price records: `672`
- Market context records: `2892`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `9.9633` n `142` status `ready` deltaP `9.4729` edge `1.1588` maxDD `-22.6673`
- `market_context_high->equity_24h` score `5.4354` n `142` status `ready` deltaP `10.8176` edge `0.5812` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.0616` n `142` status `ready` deltaP `10.2406` edge `0.4` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.2259` n `142` status `ready` deltaP `10.5854` edge `0.213` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7496` n `142` status `ready` deltaP `15.5516` edge `0.3515` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.5404` n `142` status `ready` deltaP `13.9106` edge `0.0607` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.4352` n `142` status `ready` deltaP `5.8807` edge `0.1024` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0718` n `142` status `ready` deltaP `3.7489` edge `0.0152` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.1838` n `142` status `ready` deltaP `4.4014` edge `0.0933` maxDD `-5.7037`
- `market_context_high->unknown_1h` score `-0.2486` n `142` status `ready` deltaP `4.4805` edge `0.0225` maxDD `-3.1801`
- `market_context_high->commodity_1h` score `-0.5789` n `142` status `ready` deltaP `-0.4322` edge `0.004` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6001` n `142` status `ready` deltaP `5.2459` edge `0.0641` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.6401` n `142` status `ready` deltaP `-1.7352` edge `0.0026` maxDD `-0.2164`
- `market_context_high->crypto_alt_4h` score `-0.6695` n `142` status `ready` deltaP `14.3378` edge `0.2827` maxDD `-28.7261`
- `market_context_high->metal_1h` score `-0.6933` n `142` status `ready` deltaP `-0.6157` edge `-0.0002` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.6996` n `142` status `ready` deltaP `5.423` edge `0.0611` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.7192` n `142` status `ready` deltaP `-1.7015` edge `0.0347` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.0717` n `142` status `ready` deltaP `4.2769` edge `0.0261` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2101` n `142` status `ready` deltaP `-4.2103` edge `0.0051` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3519` n `142` status `ready` deltaP `-1.8852` edge `-0.0129` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
