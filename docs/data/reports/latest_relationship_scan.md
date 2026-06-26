# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T17:52:33.335555+00:00`
- Price records: `672`
- Market context records: `4851`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7632`

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

- `market_context_high->unknown_1h` score `13.5053` n `110` status `ready` deltaP `10.6206` edge `1.0964` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.4904` n `101` status `ready` deltaP `28.7491` edge `0.819` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `5.6123` n `101` status `ready` deltaP `18.3923` edge `0.4803` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `5.5087` n `101` status `ready` deltaP `14.9662` edge `0.4817` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.2433` n `90` status `ready` deltaP `25.6945` edge `0.2999` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.6829` n `101` status `ready` deltaP `12.7611` edge `0.1214` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8358` n `101` status `ready` deltaP `11.3106` edge `0.1699` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5454` n `101` status `ready` deltaP `11.0827` edge `0.0423` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4336` n `110` status `ready` deltaP `6.1704` edge `0.1183` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4121` n `110` status `ready` deltaP `8.0212` edge `0.1016` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.1981` n `110` status `ready` deltaP `4.0855` edge `0.0579` maxDD `-2.779`
- `market_context_high->fx_4h` score `-0.2048` n `101` status `ready` deltaP `5.2176` edge `0.0082` maxDD `-0.8722`
- `market_context_high->commodity_1h` score `-0.2152` n `110` status `ready` deltaP `3.4322` edge `0.0155` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2227` n `110` status `ready` deltaP `-0.0545` edge `0.0298` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5266` n `110` status `ready` deltaP `-0.2885` edge `0.0099` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.7219` n `101` status `ready` deltaP `7.4333` edge `0.0075` maxDD `-4.377`
- `market_context_high->fx_1h` score `-1.331` n `110` status `ready` deltaP `-6.8672` edge `-0.0038` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-2.0164` n `90` status `ready` deltaP `-8.0555` edge `-0.0133` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.9017` n `90` status `ready` deltaP `-9.7569` edge `-0.1576` maxDD `-24.4619`
- `market_context_high->commodity_24h` score `-5.6186` n `90` status `ready` deltaP `9.4445` edge `-0.0203` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
