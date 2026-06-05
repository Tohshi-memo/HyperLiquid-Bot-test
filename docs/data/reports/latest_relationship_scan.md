# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T05:07:25.434426+00:00`
- Price records: `672`
- Market context records: `2938`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6940`

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

- `market_context_high->crypto_alt_24h` score `16.2684` n `142` status `ready` deltaP `15.8965` edge `1.6414` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.7935` n `142` status `ready` deltaP `18.1093` edge `0.7291` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.8088` n `142` status `ready` deltaP `15.9697` edge `0.5074` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.7231` n `142` status `ready` deltaP `13.7104` edge `0.2336` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8017` n `142` status `ready` deltaP `15.378` edge `0.357` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.8684` n `143` status `ready` deltaP `8.6592` edge `0.1526` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.729` n `143` status `ready` deltaP `14.9721` edge `0.0778` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.2259` n `143` status `ready` deltaP `4.5093` edge `0.0941` maxDD `-3.7602`
- `market_context_high->crypto_alt_4h` score `0.0539` n `143` status `ready` deltaP `16.3633` edge `0.3557` maxDD `-30.8239`
- `market_context_high->index_1h` score `0.0204` n `143` status `ready` deltaP `4.9967` edge `0.0187` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.3573` n `143` status `ready` deltaP `1.0532` edge `0.0465` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4493` n `143` status `ready` deltaP `5.8949` edge `0.0791` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5326` n `143` status `ready` deltaP `-0.4972` edge `0.0033` maxDD `-0.2164`
- `market_context_high->unknown_1h` score `-0.5651` n `143` status `ready` deltaP `2.9993` edge `0.006` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.5977` n `143` status `ready` deltaP `6.0917` edge `0.0697` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6388` n `143` status `ready` deltaP `0.3967` edge `0.0042` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6804` n `143` status `ready` deltaP `-1.5451` edge `-0.0016` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.9954` n `143` status `ready` deltaP `-1.7217` edge `0.0064` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2848` n `143` status `ready` deltaP `1.4242` edge `0.0178` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3104` n `142` status `ready` deltaP `-1.7116` edge `-0.0106` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
