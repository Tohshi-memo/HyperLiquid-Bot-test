# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T04:22:28.059073+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11742`

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

- `market_context_high->unknown_4h` score `79.531` n `88` status `ready` deltaP `7.525` edge `6.6222` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.517` n `88` status `ready` deltaP `32.2601` edge `2.9005` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.1469` n `37` status `ready` deltaP `33.6314` edge `0.8169` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.8085` n `88` status `ready` deltaP `32.4179` edge `1.2944` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1605` n `88` status `ready` deltaP `31.8497` edge `0.3473` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.8869` n `47` status `ready` deltaP `20.6937` edge `0.2572` maxDD `-3.6997`
- `market_context_high->metal_24h` score `3.3673` n `88` status `ready` deltaP `28.7721` edge `0.1441` maxDD `-1.4245`
- `news_risk_high->commodity_4h` score `3.2523` n `37` status `ready` deltaP `23.8464` edge `0.1374` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4323` n `37` status `ready` deltaP `24.8723` edge `0.0805` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.2462` n `37` status `ready` deltaP `28.6544` edge `0.2608` maxDD `-10.1088`
- `news_risk_high->crypto_major_4h` score `1.8791` n `37` status `ready` deltaP `20.3939` edge `0.2537` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `1.6837` n `37` status `ready` deltaP `30.9287` edge `0.0473` maxDD `-1.0104`
- `news_risk_high->metal_1h` score `1.5949` n `47` status `ready` deltaP `20.6937` edge `0.0204` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4477` n `47` status `ready` deltaP `18.8655` edge `0.025` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.1134` n `47` status `ready` deltaP `22.9074` edge `0.0838` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7734` n `47` status `ready` deltaP `21.0791` edge `0.0638` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2084` n `47` status `ready` deltaP `-4.2075` edge `0.0348` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.416` n `88` status `ready` deltaP `2.5381` edge `-0.002` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4623` n `88` status `ready` deltaP `2.8988` edge `0.0098` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6737` n `88` status `ready` deltaP `1.5798` edge `0.0137` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
