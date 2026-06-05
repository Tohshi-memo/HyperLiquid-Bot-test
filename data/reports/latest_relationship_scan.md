# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T12:37:23.500707+00:00`
- Price records: `672`
- Market context records: `2969`
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

- `market_context_high->crypto_alt_24h` score `16.7475` n `113` status `ready` deltaP `10.0802` edge `1.7201` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `9.3068` n `113` status `ready` deltaP `16.2058` edge `0.714` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `8.9561` n `113` status `ready` deltaP `33.0967` edge `0.5816` maxDD `-1.8058`
- `market_context_high->equity_24h` score `7.3456` n `113` status `ready` deltaP `16.6805` edge `0.7013` maxDD `-12.6963`
- `market_context_high->index_24h` score `3.6505` n `113` status `ready` deltaP `15.118` edge `0.3015` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.1441` n `114` status `ready` deltaP `16.1773` edge `0.1931` maxDD `-0.7819`
- `market_context_high->index_4h` score `1.6521` n `114` status `ready` deltaP `17.5065` edge `0.0998` maxDD `-1.9733`
- `market_context_high->crypto_alt_4h` score `1.5225` n `114` status `ready` deltaP `23.4489` edge `0.495` maxDD `-30.8239`
- `market_context_high->equity_1h` score `0.9439` n `114` status `ready` deltaP `7.0412` edge `0.0652` maxDD `-1.012`
- `market_context_high->crypto_alt_1h` score `0.283` n `114` status `ready` deltaP `10.0772` edge `0.1326` maxDD `-10.747`
- `market_context_high->index_1h` score `0.2566` n `114` status `ready` deltaP `6.3977` edge `0.0217` maxDD `-1.104`
- `market_context_high->crypto_major_1h` score `0.0495` n `114` status `ready` deltaP `9.5624` edge `0.0962` maxDD `-9.622`
- `market_context_high->unknown_4h` score `0.0247` n `114` status `ready` deltaP `3.014` edge `0.0873` maxDD `-3.7602`
- `market_context_high->commodity_4h` score `0.0234` n `114` status `ready` deltaP `8.7773` edge `0.0612` maxDD `-6.3373`
- `market_context_high->fx_1h` score `-0.3533` n `114` status `ready` deltaP `-0.3624` edge `0.0037` maxDD `-0.1244`
- `market_context_high->commodity_1h` score `-0.5831` n `114` status `ready` deltaP `-1.518` edge `-0.0021` maxDD `-3.3365`
- `market_context_high->metal_1h` score `-0.8105` n `114` status `ready` deltaP `-1.8411` edge `-0.0029` maxDD `-3.4325`
- `market_context_high->unknown_1h` score `-1.0082` n `114` status `ready` deltaP `1.9908` edge `-0.0242` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-1.0385` n `114` status `ready` deltaP `10.7857` edge `0.3075` maxDD `-33.6701`
- `market_context_high->fx_4h` score `-1.2579` n `114` status `ready` deltaP `-4.6133` edge `0.0038` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
