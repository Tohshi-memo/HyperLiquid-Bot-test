# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T17:52:36.989123+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8092`

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

- `market_context_high->unknown_4h` score `59.1645` n `151` status `ready` deltaP `0.499` edge `4.9606` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `28.2133` n `153` status `ready` deltaP `1.1751` edge `2.3922` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.4298` n `112` status `ready` deltaP `26.0151` edge `0.1443` maxDD `-7.0108`
- `market_context_high->fx_1h` score `0.2159` n `153` status `ready` deltaP `7.666` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.118` n `151` status `ready` deltaP `9.2221` edge `0.0082` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0043` n `112` status `ready` deltaP `16.3051` edge `0.0146` maxDD `-4.5747`
- `market_context_high->fx_24h` score `-0.1348` n `112` status `ready` deltaP `16.972` edge `0.0268` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.1595` n `153` status `ready` deltaP `7.8813` edge `0.0062` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.2786` n `153` status `ready` deltaP `2.1526` edge `0.0125` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5852` n `153` status `ready` deltaP `0.0127` edge `-0.0014` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.7037` n `151` status `ready` deltaP `4.2527` edge `0.0359` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.9301` n `153` status `ready` deltaP `3.7846` edge `0.0136` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.0006` n `151` status `ready` deltaP `6.7384` edge `-0.0022` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8074` n `153` status `ready` deltaP `1.6046` edge `-0.0148` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0271` n `153` status `ready` deltaP `-0.8747` edge `-0.0056` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.48` n `151` status `ready` deltaP `-6.939` edge `-0.0261` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.3735` n `112` status `ready` deltaP `-2.0983` edge `-0.061` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.7738` n `151` status `ready` deltaP `-1.6863` edge `-0.0968` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.0368` n `112` status `ready` deltaP `-3.2171` edge `-0.2092` maxDD `-35.4638`
- `market_context_high->commodity_24h` score `-6.3495` n `112` status `ready` deltaP `-17.2505` edge `-0.1401` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
