# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T07:22:26.198846+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11728`

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

- `market_context_high->unknown_4h` score `79.5674` n `88` status `ready` deltaP `7.8298` edge `6.6232` maxDD `-0.9161`
- `market_context_high->equity_24h` score `33.9657` n `88` status `ready` deltaP `31.2184` edge `2.8615` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `13.0165` n `47` status `ready` deltaP `37.0816` edge `0.9497` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.5494` n `88` status `ready` deltaP `34.5012` edge `1.3755` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1176` n `88` status `ready` deltaP `31.3289` edge `0.3472` maxDD `-2.3671`
- `market_context_high->metal_24h` score `3.9641` n `88` status `ready` deltaP `30.6818` edge `0.1811` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.7405` n `47` status `ready` deltaP `22.8237` edge `0.3083` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5889` n `52` status `ready` deltaP `17.7338` edge `0.2521` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.4956` n `47` status `ready` deltaP `34.954` edge `0.0959` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.315` n `47` status `ready` deltaP `26.8941` edge `0.1223` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.0727` n `47` status `ready` deltaP `29.4726` edge `0.1032` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.2105` n `47` status `ready` deltaP `27.3839` edge `0.2647` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.5767` n `52` status `ready` deltaP `19.9562` edge `0.0238` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3799` n `52` status `ready` deltaP `18.0332` edge `0.0249` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6866` n `52` status `ready` deltaP `17.5034` edge `0.0457` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.5385` n `52` status `ready` deltaP `17.6531` edge `0.0493` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `-0.1708` n `52` status `ready` deltaP `-2.5449` edge `0.0362` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3712` n `88` status `ready` deltaP `3.3479` edge `0.0144` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3716` n `88` status `ready` deltaP `3.1369` edge `-0.0003` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6558` n `88` status `ready` deltaP `1.5798` edge `0.016` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
