# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T01:07:31.089405+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7987`

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

- `market_context_high->unknown_4h` score `87.5057` n `153` status `ready` deltaP `1.1697` edge `7.3179` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `20.9016` n `153` status `ready` deltaP `1.6242` edge `1.7799` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.2901` n `153` status `ready` deltaP `8.5642` edge `0.0029` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.2578` n `153` status `ready` deltaP `10.8491` edge `0.009` maxDD `-0.4545`
- `market_context_high->metal_24h` score `0.1755` n `112` status `ready` deltaP `22.8955` edge `0.1325` maxDD `-7.0108`
- `market_context_high->index_24h` score `-0.1169` n `112` status `ready` deltaP `15.2653` edge `0.0071` maxDD `-4.5747`
- `market_context_high->fx_24h` score `-0.1176` n `112` status `ready` deltaP `17.3186` edge `0.0267` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.133` n `153` status `ready` deltaP `8.3304` edge `0.0066` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.1815` n `153` status `ready` deltaP `2.9011` edge `0.0156` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.3425` n `153` status `ready` deltaP `6.6684` edge `0.0499` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6288` n `153` status `ready` deltaP `-0.7358` edge `-0.002` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.8935` n `153` status `ready` deltaP `4.5331` edge `0.0133` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9313` n `153` status `ready` deltaP `7.8172` edge `-0.0005` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8642` n `153` status `ready` deltaP `0.7064` edge `-0.0161` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0092` n `153` status `ready` deltaP `-0.4256` edge `-0.0063` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3921` n `153` status `ready` deltaP `-6.0796` edge `-0.0245` maxDD `-6.7447`
- `market_context_high->crypto_major_4h` score `-4.6187` n `153` status `ready` deltaP `-0.4583` edge `-0.0851` maxDD `-32.9851`
- `market_context_high->crypto_major_24h` score `-4.7405` n `112` status `ready` deltaP `-3.8314` edge `-0.0965` maxDD `-29.1905`
- `market_context_high->commodity_24h` score `-5.8982` n `112` status `ready` deltaP `-12.3978` edge `-0.1146` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-6.9814` n `153` status `ready` deltaP `-0.8738` edge `-0.1668` maxDD `-45.4611`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
