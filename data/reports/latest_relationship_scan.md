# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T06:37:24.420472+00:00`
- Price records: `672`
- Market context records: `2841`
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

- `market_context_high->unknown_24h` score `2.456` n `142` status `ready` deltaP `3.4697` edge `0.228` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `1.4619` n `142` status `ready` deltaP `1.1395` edge `0.5059` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8452` n `142` status `ready` deltaP `6.4904` edge `0.1325` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.7394` n `142` status `ready` deltaP `11.385` edge `0.2951` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3278` n `142` status `ready` deltaP `13.3009` edge `0.0375` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0682` n `142` status `ready` deltaP `4.4805` edge `0.0489` maxDD `-3.1801`
- `market_context_high->index_24h` score `-0.0619` n `142` status `ready` deltaP `4.6826` edge `0.0617` maxDD `-2.5127`
- `market_context_high->index_1h` score `-0.0945` n `142` status `ready` deltaP `4.0483` edge `0.0103` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5766` n `142` status `ready` deltaP `-0.9867` edge `0.0029` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6093` n `142` status `ready` deltaP `-0.2825` edge `-0.0009` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6949` n `142` status `ready` deltaP `0.2825` edge `-0.0064` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7529` n `142` status `ready` deltaP `4.6471` edge `0.0485` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.9662` n `142` status `ready` deltaP `-2.8991` edge `0.0221` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9693` n `142` status `ready` deltaP `3.6266` edge `0.0385` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.0582` n `142` status `ready` deltaP `1.9624` edge `0.0367` maxDD `-5.7037`
- `market_context_high->equity_24h` score `-1.1173` n `142` status `ready` deltaP `2.4843` edge `0.0907` maxDD `-12.6963`
- `market_context_high->fx_4h` score `-1.1567` n `142` status `ready` deltaP `-3.753` edge `0.0065` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.3798` n `142` status `ready` deltaP `1.5329` edge `0.0049` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.4589` n `142` status `ready` deltaP `-2.2325` edge `-0.0195` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.4909` n `142` status `ready` deltaP `13.8805` edge `0.2173` maxDD `-28.7261`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
