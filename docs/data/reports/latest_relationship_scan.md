# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T11:22:27.583771+00:00`
- Price records: `672`
- Market context records: `2861`
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

- `market_context_high->crypto_alt_24h` score `5.033` n `142` status `ready` deltaP `4.4381` edge `0.7815` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `3.5957` n `142` status `ready` deltaP `6.4211` edge `0.3033` maxDD `-1.7175`
- `market_context_high->equity_24h` score `2.2402` n `142` status `ready` deltaP `5.7829` edge `0.3485` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `1.4142` n `142` status `ready` deltaP `14.51` edge `0.3305` maxDD `-12.4171`
- `market_context_high->index_24h` score `1.2568` n `142` status `ready` deltaP `7.9812` edge `0.1496` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `0.9104` n `142` status `ready` deltaP `5.8807` edge `0.142` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.4806` n `142` status `ready` deltaP `14.2155` edge `0.051` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0718` n `142` status `ready` deltaP `4.3308` edge `0.0502` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0516` n `142` status `ready` deltaP `4.4974` edge `0.0128` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.528` n `142` status `ready` deltaP `3.6392` edge `0.0697` maxDD `-5.7037`
- `market_context_high->crypto_alt_1h` score `-0.5876` n `142` status `ready` deltaP `5.0962` edge `0.0667` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6038` n `142` status `ready` deltaP `-0.4322` edge `0.0008` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6688` n `142` status `ready` deltaP `-2.0346` edge `0.0022` maxDD `-0.2164`
- `market_context_high->crypto_major_1h` score `-0.758` n `142` status `ready` deltaP `4.6745` edge `0.0586` maxDD `-9.622`
- `market_context_high->crypto_alt_4h` score `-0.7661` n `142` status `ready` deltaP `13.8805` edge `0.2777` maxDD `-28.7261`
- `market_context_high->equity_1h` score `-0.784` n `142` status `ready` deltaP `-1.8512` edge `0.0303` maxDD `-2.6634`
- `market_context_high->metal_1h` score `-0.7845` n `142` status `ready` deltaP `-0.7654` edge `-0.0109` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-1.2381` n `142` status `ready` deltaP `-4.5152` edge `0.0048` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2541` n `142` status `ready` deltaP `2.6` edge `0.0139` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3903` n `142` status `ready` deltaP `-1.8852` edge `-0.0161` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
