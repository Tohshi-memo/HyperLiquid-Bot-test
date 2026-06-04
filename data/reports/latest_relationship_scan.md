# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T09:07:24.021672+00:00`
- Price records: `672`
- Market context records: `2852`
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

- `market_context_high->crypto_alt_24h` score `3.0948` n `142` status `ready` deltaP `2.8756` edge `0.6304` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `3.0099` n `142` status `ready` deltaP `4.8586` edge `0.2649` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `1.0955` n `142` status `ready` deltaP `13.1211` edge `0.3132` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.835` n `142` status `ready` deltaP `6.0331` edge `0.1347` maxDD `-3.7602`
- `market_context_high->equity_24h` score `0.5852` n `142` status `ready` deltaP `4.2204` edge `0.221` maxDD `-12.6963`
- `market_context_high->index_24h` score `0.5822` n `142` status `ready` deltaP `6.4187` edge `0.1038` maxDD `-2.5127`
- `market_context_high->index_4h` score `0.3071` n `142` status `ready` deltaP `12.8435` edge `0.0379` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.097` n `142` status `ready` deltaP `4.6302` edge `0.0503` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0742` n `142` status `ready` deltaP `4.198` edge `0.0119` maxDD `-1.2855`
- `market_context_high->crypto_alt_1h` score `-0.6281` n `142` status `ready` deltaP `5.2459` edge `0.0605` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6506` n `142` status `ready` deltaP `-0.8813` edge `-0.0022` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.67` n `142` status `ready` deltaP `-2.0346` edge `0.0021` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.7051` n `142` status `ready` deltaP `0.1328` edge `-0.0067` maxDD `-3.0996`
- `market_context_high->equity_1h` score `-0.832` n `142` status `ready` deltaP `-2.0009` edge `0.0273` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.8398` n `142` status `ready` deltaP `4.2254` edge `0.0511` maxDD `-9.622`
- `market_context_high->equity_4h` score `-0.9906` n `142` status `ready` deltaP `2.2673` edge `0.0403` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-1.2127` n `142` status `ready` deltaP `13.7281` edge `0.2415` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.2333` n `142` status `ready` deltaP `-4.5152` edge `0.0052` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.331` n `142` status `ready` deltaP `1.9903` edge `0.0081` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.4071` n `142` status `ready` deltaP `-1.8852` edge `-0.0175` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
