# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T10:07:26.435989+00:00`
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

- `market_context_high->unknown_4h` score `81.7146` n `88` status `ready` deltaP `8.1347` edge `6.8001` maxDD `-0.9161`
- `market_context_high->equity_24h` score `32.8505` n `88` status `ready` deltaP `29.3087` edge `2.7813` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.6002` n `51` status `ready` deltaP `37.4731` edge `0.9124` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.9474` n `88` status `ready` deltaP `36.411` edge `1.4138` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.8941` n `88` status `ready` deltaP `29.4192` edge `0.3413` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.1617` n `88` status `ready` deltaP `31.2026` edge `0.1941` maxDD `-1.4245`
- `news_risk_high->equity_1h` score `3.6213` n `52` status `ready` deltaP `17.8835` edge `0.2538` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.565` n `51` status `ready` deltaP `36.1221` edge `0.0939` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.3761` n `51` status `ready` deltaP `27.3434` edge `0.1244` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1875` n `51` status `ready` deltaP `18.732` edge `0.2895` maxDD `-9.2335`
- `news_risk_high->index_4h` score `2.5204` n `51` status `ready` deltaP `23.5743` edge `0.0965` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.6685` n `51` status `ready` deltaP `23.111` edge `0.2237` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.6103` n `52` status `ready` deltaP `20.2556` edge `0.0246` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.465` n `52` status `ready` deltaP `18.9314` edge `0.026` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7621` n `52` status `ready` deltaP `17.9525` edge `0.049` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.5674` n `52` status `ready` deltaP `17.8028` edge `0.052` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `-0.2247` n `52` status `ready` deltaP `-2.994` edge `0.0347` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3376` n `88` status `ready` deltaP `3.6473` edge `0.0152` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4066` n `88` status `ready` deltaP `2.6878` edge `-0.0018` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.6839` n `88` status `ready` deltaP `2.7855` edge `-0.0085` maxDD `-2.4871`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
