# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T13:07:36.664869+00:00`
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

- `market_context_high->unknown_4h` score `75.5694` n `88` status `ready` deltaP `8.1347` edge `6.288` maxDD `-0.9161`
- `market_context_high->equity_24h` score `31.1851` n `88` status `ready` deltaP `27.2253` edge `2.6564` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.8912` n `52` status `ready` deltaP `35.87` edge `0.864` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.2133` n `88` status `ready` deltaP `38.4943` edge `1.434` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.5942` n `88` status `ready` deltaP `27.3358` edge `0.3302` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.2529` n `88` status `ready` deltaP `31.2026` edge `0.2017` maxDD `-1.4245`
- `news_risk_high->equity_1h` score `3.5431` n `53` status `ready` deltaP `17.8652` edge `0.2474` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.5036` n `52` status `ready` deltaP `35.6239` edge `0.0921` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.3015` n `52` status `ready` deltaP `18.7617` edge `0.2988` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1291` n `52` status `ready` deltaP `25.8912` edge `0.1135` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.301` n `52` status `ready` deltaP `21.3415` edge `0.0931` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.6826` n `53` status `ready` deltaP `20.9496` edge `0.026` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.6729` n `52` status `ready` deltaP `22.7603` edge `0.2266` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.303` n `53` status `ready` deltaP `17.0263` edge `0.0252` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6594` n `53` status `ready` deltaP `18.0431` edge `0.0622` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6263` n `53` status `ready` deltaP `18.7916` edge `0.0602` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2067` n `53` status `ready` deltaP `-2.9488` edge `0.0359` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3197` n `88` status `ready` deltaP `3.797` edge `0.0157` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4721` n `88` status `ready` deltaP `1.7896` edge `-0.0042` maxDD `-1.7935`
- `market_context_high->crypto_major_24h` score `-0.6805` n `88` status `ready` deltaP `16.3511` edge `0.9968` maxDD `-80.6681`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
