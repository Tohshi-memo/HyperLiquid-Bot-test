# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T00:52:20.757300+00:00`
- Price records: `672`
- Market context records: `2817`
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

- `market_context_high->unknown_24h` score `2.4486` n `142` status `ready` deltaP `3.1225` edge `0.2297` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `0.9158` n `142` status `ready` deltaP `6.338` edge `0.1394` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.6895` n `142` status `ready` deltaP `11.2114` edge `0.2921` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.327` n `142` status `ready` deltaP `13.3009` edge `0.0374` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.2025` n `142` status `ready` deltaP `5.3787` edge `0.0541` maxDD `-3.1801`
- `market_context_high->crypto_alt_24h` score `0.1681` n `142` status `ready` deltaP `-0.423` edge `0.4085` maxDD `-22.6673`
- `market_context_high->index_1h` score `-0.0485` n `142` status `ready` deltaP `4.6471` edge `0.0122` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5107` n `142` status `ready` deltaP `-0.2382` edge `0.0034` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6296` n `142` status `ready` deltaP `-0.1328` edge `-0.0045` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.649` n `142` status `ready` deltaP `0.5819` edge `-0.0025` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7708` n `142` status `ready` deltaP `4.7968` edge `0.0452` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8655` n `142` status `ready` deltaP `-2.45` edge `0.0275` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9342` n `142` status `ready` deltaP `3.7763` edge `0.042` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.035` n `142` status `ready` deltaP `2.2673` edge `0.0366` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1727` n `142` status `ready` deltaP `-4.0579` edge `0.0072` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.4487` n `142` status `ready` deltaP `1.2281` edge `-0.0019` maxDD `-10.0279`
- `market_context_high->index_24h` score `-1.5297` n `142` status `ready` deltaP `0.6896` edge `-0.034` maxDD `-2.5127`
- `market_context_high->fx_24h` score `-1.7236` n `142` status `ready` deltaP `-4.8366` edge `-0.0242` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-2.0295` n `142` status `ready` deltaP `13.1183` edge `0.1775` maxDD `-28.7261`
- `market_context_high->metal_4h` score `-2.2891` n `142` status `ready` deltaP `-0.6183` edge `-0.0343` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
