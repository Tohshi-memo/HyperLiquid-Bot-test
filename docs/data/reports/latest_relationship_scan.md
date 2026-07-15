# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T08:52:26.317114+00:00`
- Price records: `672`
- Market context records: `6800`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11656`

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

- `market_context_high->unknown_24h` score `0.8336` n `176` status `ready` deltaP `-1.5467` edge `0.4924` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.2505` n `176` status `ready` deltaP `9.3592` edge `0.1453` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2731` n `185` status `ready` deltaP `6.3489` edge `0.0209` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.4021` n `185` status `ready` deltaP `3.6462` edge `0.0186` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.4519` n `185` status `ready` deltaP `-1.3845` edge `-0.0002` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.6611` n `185` status `ready` deltaP `-1.8587` edge `-0.0008` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.6847` n `185` status `ready` deltaP `-1.5261` edge `-0.0093` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7039` n `185` status `ready` deltaP `-5.1432` edge `-0.0031` maxDD `-1.2285`
- `market_context_high->equity_1h` score `-1.2906` n `185` status `ready` deltaP `2.2326` edge `-0.018` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3975` n `185` status `ready` deltaP `4.4553` edge `-0.0025` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4393` n `185` status `ready` deltaP `-2.7505` edge `-0.0172` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5323` n `185` status `ready` deltaP `-4.9935` edge `-0.0043` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.6256` n `185` status `ready` deltaP `1.8375` edge `-0.0246` maxDD `-6.3515`
- `market_context_high->metal_4h` score `-2.699` n `185` status `ready` deltaP `-5.3997` edge `-0.0117` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.1898` n `185` status `ready` deltaP `-0.2003` edge `-0.0745` maxDD `-16.9823`
- `market_context_high->crypto_alt_4h` score `-3.3597` n `185` status `ready` deltaP `-1.0597` edge `-0.0654` maxDD `-20.6608`
- `market_context_high->unknown_4h` score `-3.4629` n `185` status `ready` deltaP `-14.1175` edge `0.0421` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.5032` n `176` status `ready` deltaP `-9.7853` edge `-0.0064` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.8778` n `185` status `ready` deltaP `-0.6576` edge `-0.1664` maxDD `-29.3663`
- `market_context_high->metal_24h` score `-9.4044` n `176` status `ready` deltaP `-19.8864` edge `-0.2246` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
