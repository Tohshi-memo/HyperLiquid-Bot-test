# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T09:37:31.716785+00:00`
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

- `market_context_high->unknown_4h` score `81.4192` n `88` status `ready` deltaP `7.9823` edge `6.7765` maxDD `-0.9161`
- `market_context_high->equity_24h` score `33.0607` n `88` status `ready` deltaP `29.6559` edge `2.7965` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.873` n `49` status `ready` deltaP `37.2978` edge `0.9363` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.8787` n `88` status `ready` deltaP `36.0637` edge `1.4073` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.9362` n `88` status `ready` deltaP `29.7664` edge `0.3425` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.1437` n `88` status `ready` deltaP `31.2026` edge `0.1926` maxDD `-1.4245`
- `news_risk_high->equity_1h` score `3.6117` n `52` status `ready` deltaP `17.8835` edge `0.253` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.5428` n `49` status `ready` deltaP `21.133` edge `0.3031` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `3.5166` n `49` status `ready` deltaP `35.5619` edge `0.0936` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.3089` n `49` status `ready` deltaP `26.8479` edge `0.1221` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.7961` n `49` status `ready` deltaP `26.3906` edge `0.1007` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.9663` n `49` status `ready` deltaP `25.672` edge `0.2448` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.6115` n `52` status `ready` deltaP `20.2556` edge `0.0247` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4374` n `52` status `ready` deltaP `18.632` edge `0.0257` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7896` n `52` status `ready` deltaP `18.2519` edge `0.0493` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.5822` n `52` status `ready` deltaP `17.9525` edge `0.0529` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `-0.1887` n `52` status `ready` deltaP `-2.6946` edge `0.0357` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3364` n `88` status `ready` deltaP `3.6473` edge `0.0153` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3833` n `88` status `ready` deltaP `2.9872` edge `-0.0008` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.7014` n `88` status `ready` deltaP `2.4806` edge `-0.0087` maxDD `-2.4871`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
