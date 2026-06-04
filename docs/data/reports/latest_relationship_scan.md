# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T13:22:25.554654+00:00`
- Price records: `672`
- Market context records: `2870`
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

- `market_context_high->crypto_alt_24h` score `6.5349` n `142` status `ready` deltaP `5.827` edge `0.8974` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `4.0908` n `142` status `ready` deltaP `7.81` edge `0.3353` maxDD `-1.7175`
- `market_context_high->equity_24h` score `3.6029` n `142` status `ready` deltaP `7.1718` edge `0.4528` maxDD `-12.6963`
- `market_context_high->index_24h` score `1.8539` n `142` status `ready` deltaP `9.3701` edge `0.1901` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.6282` n `142` status `ready` deltaP `15.2044` edge `0.3437` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.9418` n `142` status `ready` deltaP `6.0331` edge `0.1436` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.6843` n `142` status `ready` deltaP `15.2826` edge `0.07` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0217` n `142` status `ready` deltaP `4.1811` edge `0.0434` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0431` n `142` status `ready` deltaP `4.4974` edge `0.0139` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.137` n `142` status `ready` deltaP `4.4014` edge `0.0972` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-0.5061` n `142` status `ready` deltaP `14.4903` edge `0.2953` maxDD `-28.7261`
- `market_context_high->commodity_1h` score `-0.5914` n `142` status `ready` deltaP `-0.4322` edge `0.0024` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6784` n `142` status `ready` deltaP `-2.1843` edge `0.0024` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.7061` n `142` status `ready` deltaP `4.6471` edge `0.0545` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8164` n `142` status `ready` deltaP `-2.0009` edge `0.0286` maxDD `-2.6634`
- `market_context_high->metal_1h` score `-0.8172` n `142` status `ready` deltaP `-1.2145` edge `-0.0121` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.8687` n `142` status `ready` deltaP `4.2254` edge `0.0474` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1464` n `142` status `ready` deltaP `3.6671` edge `0.0206` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2783` n `142` status `ready` deltaP `-4.9725` edge `0.0045` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3903` n `142` status `ready` deltaP `-1.8852` edge `-0.0161` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
