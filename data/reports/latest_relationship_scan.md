# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T11:52:23.669183+00:00`
- Price records: `672`
- Market context records: `2966`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.0095` n `116` status `ready` deltaP `10.9555` edge `1.7361` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `9.248` n `116` status `ready` deltaP `16.5948` edge `0.7065` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `8.2584` n `116` status `ready` deltaP `31.0045` edge `0.5577` maxDD `-2.4294`
- `market_context_high->equity_24h` score `7.5509` n `116` status `ready` deltaP `16.8462` edge `0.7173` maxDD `-12.6963`
- `market_context_high->index_24h` score `3.5381` n `116` status `ready` deltaP `14.9426` edge `0.2933` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.3159` n `117` status `ready` deltaP `16.5247` edge `0.2051` maxDD `-0.7819`
- `market_context_high->crypto_alt_4h` score `2.7521` n `117` status `ready` deltaP `23.8913` edge `0.5262` maxDD `-30.8239`
- `market_context_high->index_4h` score `1.464` n `117` status `ready` deltaP `15.9045` edge `0.0948` maxDD `-1.9733`
- `market_context_high->equity_1h` score `0.8245` n `117` status `ready` deltaP `6.1493` edge `0.0612` maxDD `-1.012`
- `market_context_high->unknown_4h` score `0.2959` n `117` status `ready` deltaP `4.1836` edge `0.1021` maxDD `-3.7602`
- `market_context_high->crypto_alt_1h` score `0.1516` n `117` status `ready` deltaP `8.5253` edge `0.1193` maxDD `-10.747`
- `market_context_high->index_1h` score `0.1136` n `117` status `ready` deltaP `6.3233` edge `0.0205` maxDD `-1.1802`
- `market_context_high->crypto_major_1h` score `-0.0804` n `117` status `ready` deltaP `8.1005` edge `0.0893` maxDD `-9.622`
- `market_context_high->fx_1h` score `-0.2621` n `117` status `ready` deltaP `0.7025` edge `0.0042` maxDD `-0.1244`
- `market_context_high->commodity_4h` score `-0.3432` n `117` status `ready` deltaP `7.3953` edge `0.051` maxDD `-7.5445`
- `market_context_high->commodity_1h` score `-0.6112` n `117` status `ready` deltaP `-1.9678` edge `-0.0027` maxDD `-3.3365`
- `market_context_high->unknown_1h` score `-0.6962` n `117` status `ready` deltaP `2.4554` edge `-0.0013` maxDD `-3.1801`
- `market_context_high->metal_1h` score `-0.699` n `117` status `ready` deltaP `-0.5963` edge `0.0031` maxDD `-3.4325`
- `market_context_high->crypto_major_4h` score `-0.7253` n `117` status `ready` deltaP `11.588` edge `0.3423` maxDD `-33.6701`
- `market_context_high->fx_4h` score `-1.126` n `117` status `ready` deltaP `-3.2638` edge `0.0058` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
