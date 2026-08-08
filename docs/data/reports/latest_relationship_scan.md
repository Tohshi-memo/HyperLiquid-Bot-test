# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T21:07:27.821522+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11607`

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

- `market_context_high->equity_24h` score `2.9712` n `103` status `ready` deltaP `4.5729` edge `0.5231` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4218` n `103` status `ready` deltaP `12.2118` edge `0.178` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.6293` n `107` status `ready` deltaP `15.7453` edge `0.0981` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0623` n `114` status `ready` deltaP `12.5591` edge `0.0391` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8967` n `103` status `ready` deltaP `22.443` edge `0.052` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4253` n `103` status `ready` deltaP `9.1002` edge `0.147` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5055` n `114` status `ready` deltaP `-2.9073` edge `-0.0065` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5389` n `114` status `ready` deltaP `1.476` edge `-0.0052` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.6123` n `114` status `ready` deltaP `-3.3774` edge `-0.0064` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.6244` n `114` status `ready` deltaP `2.2088` edge `0.0161` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.6913` n `107` status `ready` deltaP `-2.4618` edge `-0.0117` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8755` n `107` status `ready` deltaP `1.1497` edge `-0.0053` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.1023` n `107` status `ready` deltaP `-3.9064` edge `-0.0144` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.1128` n `114` status `ready` deltaP `-12.5775` edge `-0.0293` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.2556` n `107` status `ready` deltaP `0.3092` edge `-0.0563` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.7049` n `114` status `ready` deltaP `-9.1344` edge `-0.0575` maxDD `-5.2274`
- `market_context_high->crypto_major_24h` score `-3.6391` n `103` status `ready` deltaP `6.2197` edge `-0.0953` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.111` n `103` status `ready` deltaP `-12.4461` edge `-0.1153` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.7264` n `107` status `ready` deltaP `-14.0215` edge `-0.1352` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.1862` n `114` status `ready` deltaP `-3.7005` edge `-0.6128` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
