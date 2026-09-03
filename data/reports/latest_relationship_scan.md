# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T23:31:06.294734+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11523`

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

- `risk_on_high->unknown_4h` score `23.1351` n `133` status `ready` deltaP `10.5229` edge `1.9196` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `23.1351` n `133` status `ready` deltaP `10.5229` edge `1.9196` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `16.37` n `167` status `ready` deltaP `12.1212` edge `1.3529` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `14.7378` n `133` status `ready` deltaP `-0.0057` edge `1.2859` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `14.7378` n `133` status `ready` deltaP `-0.0057` edge `1.2859` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.258` n `167` status `ready` deltaP `0.4491` edge `0.9149` maxDD `-2.0446`
- `market_context_high->equity_24h` score `0.3256` n `127` status `ready` deltaP `15.435` edge `0.3588` maxDD `-20.7654`
- `news_risk_high->commodity_4h` score `0.3216` n `67` status `ready` deltaP `5.9474` edge `0.0375` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0782` n `133` status `ready` deltaP `11.9637` edge `0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0782` n `133` status `ready` deltaP `11.9637` edge `0.0015` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0508` n `67` status `ready` deltaP `4.7748` edge `-0.003` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.089` n `133` status `ready` deltaP `5.19` edge `-0.0015` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.089` n `133` status `ready` deltaP `5.19` edge `-0.0015` maxDD `-0.5605`
- `news_risk_high->fx_4h` score `-0.099` n `67` status `ready` deltaP `8.1271` edge `0.0032` maxDD `-1.2507`
- `risk_on_high->fx_24h` score `-0.1283` n `107` status `ready` deltaP `25.7075` edge `0.0819` maxDD `-4.2453`
- `risk_on_and_context->fx_24h` score `-0.1283` n `107` status `ready` deltaP `25.7075` edge `0.0819` maxDD `-4.2453`
- `risk_on_high->equity_24h` score `-0.1573` n `107` status `ready` deltaP `10.6812` edge `0.3302` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `-0.1573` n `107` status `ready` deltaP `10.6812` edge `0.3302` maxDD `-19.828`
- `news_risk_high->commodity_24h` score `-0.1822` n `67` status `ready` deltaP `4.4517` edge `-0.0256` maxDD `-0.2074`
- `news_risk_high->commodity_1h` score `-0.1873` n `67` status `ready` deltaP `4.3078` edge `0.0003` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
