# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T11:22:23.378599+00:00`
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

- `market_context_high->unknown_4h` score `79.8786` n `88` status `ready` deltaP `8.1347` edge `6.6471` maxDD `-0.9161`
- `market_context_high->equity_24h` score `32.2147` n `88` status `ready` deltaP `28.4406` edge `2.7341` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.2681` n `52` status `ready` deltaP `36.9371` edge `0.8883` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.0799` n `88` status `ready` deltaP `37.279` edge `1.425` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.7754` n `88` status `ready` deltaP `28.5511` edge `0.3372` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.1953` n `88` status `ready` deltaP `31.2026` edge `0.1969` maxDD `-1.4245`
- `news_risk_high->equity_1h` score `3.7218` n `53` status `ready` deltaP `18.464` edge `0.2583` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.5181` n `52` status `ready` deltaP `35.7763` edge `0.0923` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.3129` n `52` status `ready` deltaP `26.9582` edge `0.1217` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1335` n `52` status `ready` deltaP `18.7617` edge `0.2848` maxDD `-9.2335`
- `news_risk_high->index_4h` score `2.3704` n `52` status `ready` deltaP `22.1037` edge `0.0938` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.6814` n `53` status `ready` deltaP `20.9496` edge `0.0259` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.6412` n `52` status `ready` deltaP `23.0652` edge `0.2205` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3712` n `53` status `ready` deltaP `17.7748` edge `0.0259` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.721` n `53` status `ready` deltaP `18.6419` edge `0.0661` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6404` n `53` status `ready` deltaP `18.6419` edge `0.063` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.1767` n `53` status `ready` deltaP `-2.6494` edge `0.0364` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3209` n `88` status `ready` deltaP `3.797` edge `0.0156` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4526` n `88` status `ready` deltaP `2.089` edge `-0.0037` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.6847` n `88` status `ready` deltaP `2.7855` edge `-0.0086` maxDD `-2.4871`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
