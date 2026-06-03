# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T17:07:24.525959+00:00`
- Price records: `672`
- Market context records: `2783`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `3.3894` n `141` status `ready` deltaP `6.6784` edge `0.2844` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.9391` n `141` status `ready` deltaP `3.9598` edge `0.6102` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.9026` n `142` status `ready` deltaP `6.338` edge `0.1383` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.3422` n `141` status `ready` deltaP `10.8229` edge `0.2811` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.2515` n `142` status `ready` deltaP `12.5387` edge `0.0328` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0697` n `142` status `ready` deltaP `3.732` edge `0.0424` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1093` n `142` status `ready` deltaP `3.8986` edge `0.0094` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5622` n `142` status `ready` deltaP `-0.837` edge `0.0031` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6497` n `142` status `ready` deltaP `0.2825` edge `-0.0006` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6709` n `142` status `ready` deltaP `-0.7316` edge `-0.0058` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6874` n `142` status `ready` deltaP `5.0962` edge `0.0539` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.9085` n `142` status `ready` deltaP `3.926` edge `0.0443` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0382` n `142` status `ready` deltaP `-3.3482` edge `0.0191` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.0959` n `142` status `ready` deltaP `-3.1432` edge `0.0075` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.3527` n `142` status `ready` deltaP `14.0329` edge `0.2278` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.3952` n `141` status `ready` deltaP `-1.1821` edge `-0.0212` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-1.4263` n `142` status `ready` deltaP `1.2002` edge `0.0111` maxDD `-5.7037`
- `market_context_high->commodity_4h` score `-1.5878` n `142` status `ready` deltaP `0.0086` edge `-0.0116` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.2022` n `142` status `ready` deltaP `-1.2281` edge `-0.0191` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4638` n `142` status `ready` deltaP `5.5822` edge `0.1375` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
