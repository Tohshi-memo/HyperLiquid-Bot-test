# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T15:22:35.018980+00:00`
- Price records: `672`
- Market context records: `7681`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->index_1h` score `0.0671` n `142` status `ready` deltaP `6.4777` edge `0.0126` maxDD `-0.7743`
- `market_context_high->crypto_major_1h` score `0.0616` n `142` status `ready` deltaP `9.1549` edge `0.0277` maxDD `-3.4671`
- `market_context_high->equity_1h` score `-0.0794` n `142` status `ready` deltaP `5.6804` edge `0.0625` maxDD `-5.8444`
- `market_context_high->crypto_alt_1h` score `-0.1547` n `142` status `ready` deltaP `2.8612` edge `0.0238` maxDD `-2.6829`
- `market_context_high->fx_24h` score `-0.1971` n `141` status `ready` deltaP `10.7458` edge `0.0207` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4215` n `142` status `ready` deltaP `1.4972` edge `0.0008` maxDD `-0.6722`
- `market_context_high->crypto_major_4h` score `-0.4949` n `142` status `ready` deltaP `11.42` edge `0.0949` maxDD `-9.9818`
- `market_context_high->commodity_4h` score `-0.5335` n `142` status `ready` deltaP `1.1845` edge `0.007` maxDD `-1.0817`
- `market_context_high->index_4h` score `-0.5384` n `142` status `ready` deltaP `9.002` edge `0.0334` maxDD `-2.6614`
- `market_context_high->fx_1h` score `-0.5695` n `142` status `ready` deltaP `-0.8649` edge `-0.0015` maxDD `-0.5484`
- `market_context_high->metal_1h` score `-0.6192` n `142` status `ready` deltaP `1.3304` edge `0.0163` maxDD `-1.0307`
- `market_context_high->crypto_alt_4h` score `-0.6494` n `142` status `ready` deltaP `4.6827` edge `0.074` maxDD `-7.747`
- `market_context_high->equity_24h` score `-0.7231` n `141` status `ready` deltaP `14.0769` edge `0.1186` maxDD `-19.7451`
- `market_context_high->equity_4h` score `-0.8942` n `142` status `ready` deltaP `0.7366` edge `0.2097` maxDD `-15.0064`
- `market_context_high->commodity_24h` score `-1.3897` n `141` status `ready` deltaP `6.8463` edge `-0.0031` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-1.442` n `142` status `ready` deltaP `-1.1533` edge `-0.0524` maxDD `-1.1399`
- `market_context_high->metal_4h` score `-1.4864` n `142` status `ready` deltaP `-1.2925` edge `0.0545` maxDD `-3.9156`
- `market_context_high->metal_24h` score `-1.6858` n `142` status `ready` deltaP `-1.56` edge `0.078` maxDD `-5.3653`
- `market_context_high->fx_4h` score `-2.5362` n `142` status `ready` deltaP `-6.2863` edge `-0.0041` maxDD `-1.894`
- `market_context_high->index_24h` score `-3.3241` n `141` status `ready` deltaP `-20.8231` edge `-0.0312` maxDD `-5.8251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
