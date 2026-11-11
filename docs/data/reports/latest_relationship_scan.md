# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T11:52:34.380015+00:00`
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

- `market_context_high->unknown_4h` score `78.4266` n `88` status `ready` deltaP `8.1347` edge `6.5261` maxDD `-0.9161`
- `market_context_high->equity_24h` score `31.9229` n `88` status `ready` deltaP `28.0934` edge `2.7121` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.1477` n `52` status `ready` deltaP `36.6322` edge `0.8803` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.1253` n `88` status `ready` deltaP `37.6262` edge `1.4285` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.7236` n `88` status `ready` deltaP `28.2039` edge `0.3352` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.2049` n `88` status `ready` deltaP `31.2026` edge `0.1977` maxDD `-1.4245`
- `news_risk_high->equity_1h` score `3.7146` n `53` status `ready` deltaP `18.464` edge `0.2577` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.489` n `52` status `ready` deltaP `35.4714` edge `0.0919` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.2645` n `52` status `ready` deltaP `26.6533` edge `0.1197` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.0815` n `52` status `ready` deltaP `18.4569` edge `0.2825` maxDD `-9.2335`
- `news_risk_high->index_4h` score `2.3424` n `52` status `ready` deltaP `21.7988` edge `0.0935` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.6814` n `53` status `ready` deltaP `20.9496` edge `0.0259` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.5996` n `52` status `ready` deltaP `22.7603` edge `0.2172` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3581` n `53` status `ready` deltaP `17.6251` edge `0.0258` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7397` n `53` status `ready` deltaP `18.7916` edge `0.0675` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6653` n `53` status `ready` deltaP `18.9413` edge `0.0642` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.148` n `53` status `ready` deltaP `-2.35` edge `0.0368` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3209` n `88` status `ready` deltaP `3.797` edge `0.0156` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4339` n `88` status `ready` deltaP `2.3884` edge `-0.0033` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.7029` n `88` status `ready` deltaP `2.4806` edge `-0.0089` maxDD `-2.4871`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
