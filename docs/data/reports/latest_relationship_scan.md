# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T18:52:49.466705+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11794`

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

- `market_context_high->unknown_4h` score `73.5939` n `88` status `ready` deltaP `8.8969` edge `6.1183` maxDD `-0.9161`
- `market_context_high->equity_24h` score `25.5808` n `88` status `ready` deltaP `23.2323` edge `2.216` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `10.9993` n `53` status `ready` deltaP `33.4963` edge `0.8055` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.8791` n `88` status `ready` deltaP `37.1054` edge `1.2722` maxDD `-33.4213`
- `market_context_high->index_24h` score `4.724` n `88` status `ready` deltaP `23.3428` edge `0.2843` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.4161` n `88` status `ready` deltaP `31.2026` edge `0.2153` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.903` n `53` status `ready` deltaP `38.6218` edge `0.1054` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.3775` n `53` status `ready` deltaP `17.7155` edge `0.2346` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.2649` n `53` status `ready` deltaP `18.3042` edge `0.2988` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.608` n `53` status `ready` deltaP `23.9675` edge `0.0829` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2114` n `53` status `ready` deltaP `20.7461` edge `0.0896` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.9258` n `53` status `ready` deltaP `23.3448` edge `0.0303` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.5667` n `53` status `ready` deltaP `21.468` edge `0.2216` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2862` n `53` status `ready` deltaP `16.8766` edge `0.0248` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6576` n `53` status `ready` deltaP `18.3425` edge `0.0672` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6408` n `53` status `ready` deltaP `16.9952` edge `0.0668` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.0765` n `88` status `ready` deltaP `6.1922` edge `0.02` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.3386` n `53` status `ready` deltaP `-3.3979` edge `0.0279` maxDD `-0.3438`
- `market_context_high->fx_24h` score `-0.4288` n `88` status `ready` deltaP `14.9306` edge `0.0247` maxDD `-3.4642`
- `market_context_high->commodity_1h` score `-0.5578` n `88` status `ready` deltaP `1.3405` edge `-0.0122` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
