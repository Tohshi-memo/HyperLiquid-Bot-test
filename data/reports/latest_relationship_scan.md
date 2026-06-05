# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T03:22:21.123388+00:00`
- Price records: `672`
- Market context records: `2931`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6927`

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

- `market_context_high->crypto_alt_24h` score `15.0528` n `142` status `ready` deltaP `14.6812` edge `1.5482` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.3291` n `142` status `ready` deltaP `16.894` edge `0.6985` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.3791` n `142` status `ready` deltaP `14.7545` edge `0.4797` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.5462` n `142` status `ready` deltaP `12.6687` edge `0.2258` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8101` n `142` status `ready` deltaP `15.378` edge `0.3577` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.8692` n `142` status `ready` deltaP `8.6697` edge `0.1526` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.7285` n `142` status `ready` deltaP `14.9777` edge `0.0777` maxDD `-2.3986`
- `market_context_high->crypto_alt_4h` score `0.1747` n `142` status `ready` deltaP `15.7098` edge `0.3439` maxDD `-28.7261`
- `market_context_high->unknown_4h` score `0.0161` n `142` status `ready` deltaP `3.7465` edge `0.0817` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0279` n `143` status `ready` deltaP `4.2482` edge `0.0175` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.41` n `143` status `ready` deltaP `0.7538` edge `0.0441` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.482` n `143` status `ready` deltaP `5.5955` edge `0.0769` maxDD `-10.747`
- `market_context_high->unknown_1h` score `-0.4931` n `143` status `ready` deltaP `3.2987` edge `0.01` maxDD `-3.1801`
- `market_context_high->fx_1h` score `-0.559` n `143` status `ready` deltaP `-0.7966` edge `0.0031` maxDD `-0.2164`
- `market_context_high->crypto_major_1h` score `-0.646` n `143` status `ready` deltaP `5.6426` edge `0.0665` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6512` n `143` status `ready` deltaP `0.247` edge `0.0036` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6882` n `143` status `ready` deltaP `-1.6948` edge `-0.0016` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-1.0164` n `142` status `ready` deltaP `-1.9237` edge `0.006` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2946` n `142` status `ready` deltaP `1.6854` edge `0.0148` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.296` n `142` status `ready` deltaP `-1.7116` edge `-0.0094` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
