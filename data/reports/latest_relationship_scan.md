# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T01:22:26.422302+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8004`

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

- `market_context_high->unknown_4h` score `87.4877` n `153` status `ready` deltaP `1.1697` edge `7.3164` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `20.8824` n `153` status `ready` deltaP `1.6242` edge `1.7783` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.2901` n `153` status `ready` deltaP `8.5642` edge `0.0029` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.2578` n `153` status `ready` deltaP `10.8491` edge `0.009` maxDD `-0.4545`
- `market_context_high->metal_24h` score `0.1415` n `113` status `ready` deltaP `22.4214` edge `0.1313` maxDD `-7.0108`
- `market_context_high->index_24h` score `-0.1052` n `113` status `ready` deltaP `15.4` edge `0.0077` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1314` n `153` status `ready` deltaP `8.3304` edge `0.0068` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.1405` n `113` status `ready` deltaP `16.923` edge `0.0264` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.1803` n `153` status `ready` deltaP `2.9011` edge `0.0157` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.3437` n `153` status `ready` deltaP `6.6684` edge `0.0498` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6203` n `153` status `ready` deltaP `-0.5861` edge `-0.0019` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.899` n `153` status `ready` deltaP `4.5331` edge `0.0126` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9321` n `153` status `ready` deltaP `7.8172` edge `-0.0006` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8486` n `153` status `ready` deltaP `0.8561` edge `-0.0151` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0116` n `153` status `ready` deltaP `-0.4256` edge `-0.0066` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.4079` n `153` status `ready` deltaP `-6.232` edge `-0.0248` maxDD `-6.7447`
- `market_context_high->crypto_major_4h` score `-4.6414` n `153` status `ready` deltaP `-0.6108` edge `-0.087` maxDD `-32.9851`
- `market_context_high->crypto_major_24h` score `-4.7202` n `113` status `ready` deltaP `-3.5306` edge `-0.0959` maxDD `-29.1905`
- `market_context_high->commodity_24h` score `-5.8475` n `113` status `ready` deltaP `-11.7973` edge `-0.1121` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-6.9861` n `153` status `ready` deltaP `-0.8738` edge `-0.1674` maxDD `-45.4611`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
