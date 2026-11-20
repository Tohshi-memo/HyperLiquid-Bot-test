# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T14:22:31.277395+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2650`

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

- `market_context_high->unknown_1h` score `10459.7716` n `123` status `ready` deltaP `1.7916` edge `871.6555` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `6927.8561` n `115` status `ready` deltaP `0.9703` edge `577.3433` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `5.573` n `106` status `ready` deltaP `28.0693` edge `1.1825` maxDD `-46.411`
- `market_context_high->crypto_alt_24h` score `2.797` n `106` status `ready` deltaP `14.8094` edge `0.9854` maxDD `-62.0837`
- `market_context_high->crypto_major_4h` score `0.9664` n `115` status `ready` deltaP `3.754` edge `0.3374` maxDD `-16.2179`
- `market_context_high->metal_4h` score `0.3115` n `115` status `ready` deltaP `16.6556` edge `0.0552` maxDD `-6.8892`
- `market_context_high->crypto_alt_4h` score `0.1007` n `115` status `ready` deltaP `4.8211` edge `0.2443` maxDD `-16.749`
- `market_context_high->metal_1h` score `-0.1286` n `123` status `ready` deltaP `4.7685` edge `0.0182` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2685` n `123` status `ready` deltaP `3.3567` edge `0.0044` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.9887` n `123` status `ready` deltaP `3.4212` edge `0.0514` maxDD `-7.8611`
- `market_context_high->fx_1h` score `-1.2564` n `123` status `ready` deltaP `-7.1479` edge `-0.0011` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.3095` n `123` status `ready` deltaP `6.2448` edge `0.0354` maxDD `-11.559`
- `market_context_high->crypto_alt_1h` score `-1.7739` n `123` status `ready` deltaP `-2.2699` edge `0.0269` maxDD `-8.4343`
- `market_context_high->index_4h` score `-1.8414` n `115` status `ready` deltaP `-1.5536` edge `-0.0083` maxDD `-4.7832`
- `market_context_high->commodity_1h` score `-1.9556` n `123` status `ready` deltaP `-5.3077` edge `-0.0144` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.1372` n `115` status `ready` deltaP `-10.786` edge `-0.0005` maxDD `-1.794`
- `market_context_high->metal_24h` score `-5.6619` n `106` status `ready` deltaP `13.4696` edge `0.0967` maxDD `-42.6658`
- `market_context_high->fx_24h` score `-6.6266` n `106` status `ready` deltaP `-17.4463` edge `-0.0086` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.1254` n `115` status `ready` deltaP `-22.4403` edge `-0.0749` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-10.2926` n `115` status `ready` deltaP `-4.959` edge `-0.0746` maxDD `-49.6711`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
