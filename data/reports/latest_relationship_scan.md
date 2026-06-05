# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T05:22:24.855935+00:00`
- Price records: `672`
- Market context records: `2939`
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

- `market_context_high->crypto_alt_24h` score `16.3975` n `142` status `ready` deltaP `16.0701` edge `1.651` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.8482` n `142` status `ready` deltaP `18.2829` edge `0.7325` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.8646` n `142` status `ready` deltaP `16.1433` edge `0.5109` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.7466` n `142` status `ready` deltaP `13.884` edge `0.2344` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8017` n `142` status `ready` deltaP `15.378` edge `0.357` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.8418` n `143` status `ready` deltaP `8.5068` edge `0.1514` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.7275` n `143` status `ready` deltaP `14.9721` edge `0.0776` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.2621` n `143` status `ready` deltaP `4.6617` edge `0.0961` maxDD `-3.7602`
- `market_context_high->crypto_alt_4h` score `0.0949` n `143` status `ready` deltaP `16.5157` edge `0.3581` maxDD `-30.8239`
- `market_context_high->index_1h` score `0.0196` n `143` status `ready` deltaP `4.9967` edge `0.0186` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.3633` n `143` status `ready` deltaP `1.0532` edge `0.046` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4501` n `143` status `ready` deltaP `5.8949` edge `0.079` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5195` n `143` status `ready` deltaP `-0.3475` edge `0.0034` maxDD `-0.2164`
- `market_context_high->unknown_1h` score `-0.5699` n `143` status `ready` deltaP `2.9993` edge `0.0056` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.5969` n `143` status `ready` deltaP `6.0917` edge `0.0698` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6388` n `143` status `ready` deltaP `0.3967` edge `0.0042` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6898` n `143` status `ready` deltaP `-1.6948` edge `-0.0018` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.9954` n `143` status `ready` deltaP `-1.7217` edge `0.0064` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2943` n `143` status `ready` deltaP `1.2718` edge `0.0176` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3116` n `142` status `ready` deltaP `-1.7116` edge `-0.0107` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
