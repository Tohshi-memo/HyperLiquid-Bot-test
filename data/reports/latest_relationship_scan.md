# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T10:22:37.720309+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11488`

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

- `market_context_high->unknown_4h` score `82.035` n `88` status `ready` deltaP `8.1347` edge `6.8268` maxDD `-0.9161`
- `market_context_high->equity_24h` score `32.737` n `88` status `ready` deltaP `29.1351` edge `2.773` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.4657` n `52` status `ready` deltaP `37.5469` edge `0.9007` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.976` n `88` status `ready` deltaP `36.5846` edge `1.4163` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.873` n `88` status `ready` deltaP `29.2455` edge `0.3407` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.1713` n `88` status `ready` deltaP `31.2026` edge `0.1949` maxDD `-1.4245`
- `news_risk_high->equity_1h` score `3.6321` n `52` status `ready` deltaP `17.8835` edge `0.2547` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.5765` n `52` status `ready` deltaP `36.3861` edge `0.0931` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.4121` n `52` status `ready` deltaP `27.568` edge `0.1259` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.2579` n `52` status `ready` deltaP `19.3715` edge `0.2911` maxDD `-9.2335`
- `news_risk_high->index_4h` score `2.385` n `52` status `ready` deltaP `22.2561` edge `0.094` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7259` n `52` status `ready` deltaP `23.6749` edge `0.2273` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.6115` n `52` status `ready` deltaP `20.2556` edge `0.0247` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4674` n `52` status `ready` deltaP `18.9314` edge `0.0262` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7573` n `52` status `ready` deltaP `17.9525` edge `0.0486` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.5627` n `52` status `ready` deltaP `17.8028` edge `0.0514` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `-0.2403` n `52` status `ready` deltaP `-3.1437` edge `0.0344` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3364` n `88` status `ready` deltaP `3.6473` edge `0.0153` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4168` n `88` status `ready` deltaP `2.5381` edge `-0.0021` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.6752` n `88` status `ready` deltaP `2.9379` edge `-0.0084` maxDD `-2.4871`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
