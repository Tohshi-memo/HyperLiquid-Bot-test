# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T00:22:28.872473+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7985`

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

- `market_context_high->unknown_4h` score `89.9367` n `153` status `ready` deltaP `1.0172` edge `7.5215` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `20.8632` n `153` status `ready` deltaP `1.6242` edge `1.7767` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.2782` n `153` status `ready` deltaP `8.4145` edge `0.0029` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.2188` n `153` status `ready` deltaP `10.3917` edge `0.0088` maxDD `-0.4545`
- `market_context_high->metal_24h` score `0.2052` n `112` status `ready` deltaP `23.2421` edge `0.134` maxDD `-7.0108`
- `market_context_high->index_24h` score `-0.0734` n `112` status `ready` deltaP `15.7852` edge `0.0092` maxDD `-4.5747`
- `market_context_high->fx_24h` score `-0.1191` n `112` status `ready` deltaP `17.3186` edge `0.0265` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.1338` n `153` status `ready` deltaP `8.3304` edge `0.0065` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.2139` n `153` status `ready` deltaP `2.6017` edge `0.0149` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.3535` n `153` status `ready` deltaP `6.516` edge `0.05` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6195` n `153` status `ready` deltaP `-0.5861` edge `-0.0018` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.853` n `153` status `ready` deltaP `4.8325` edge `0.0165` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9297` n `153` status `ready` deltaP `7.8172` edge `-0.0003` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.858` n `153` status `ready` deltaP `0.7064` edge `-0.0153` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9827` n `153` status `ready` deltaP `-0.2759` edge `-0.0039` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3861` n `153` status `ready` deltaP `-6.0796` edge `-0.024` maxDD `-6.7447`
- `market_context_high->crypto_major_4h` score `-4.5535` n `153` status `ready` deltaP `-0.001` edge `-0.0798` maxDD `-32.9851`
- `market_context_high->crypto_major_24h` score `-4.6277` n `112` status `ready` deltaP `-3.3114` edge `-0.0855` maxDD `-29.1905`
- `market_context_high->commodity_24h` score `-5.9311` n `112` status `ready` deltaP `-12.7444` edge `-0.1165` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.9629` n `112` status `ready` deltaP `-7.7231` edge `-0.2979` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
