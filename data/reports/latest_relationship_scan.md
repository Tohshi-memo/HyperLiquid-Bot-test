# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T12:22:33.304817+00:00`
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

- `market_context_high->unknown_4h` score `76.9698` n `88` status `ready` deltaP `8.1347` edge `6.4047` maxDD `-0.9161`
- `market_context_high->equity_24h` score `31.6239` n `88` status `ready` deltaP `27.7462` edge `2.6895` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.0574` n `52` status `ready` deltaP `36.3274` edge `0.8748` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.1589` n `88` status `ready` deltaP `37.9735` edge `1.4305` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.6731` n `88` status `ready` deltaP `27.8567` edge `0.3333` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.2265` n `88` status `ready` deltaP `31.2026` edge `0.1995` maxDD `-1.4245`
- `news_risk_high->equity_1h` score `3.6366` n `53` status `ready` deltaP `18.1646` edge `0.2532` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.4756` n `52` status `ready` deltaP `35.319` edge `0.0918` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.2185` n `52` status `ready` deltaP `26.3485` edge `0.1179` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1887` n `52` status `ready` deltaP `18.7617` edge `0.2894` maxDD `-9.2335`
- `news_risk_high->index_4h` score `2.3424` n `52` status `ready` deltaP `21.7988` edge `0.0935` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.6958` n `53` status `ready` deltaP `21.0993` edge `0.0261` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.6316` n `52` status `ready` deltaP `22.7603` edge `0.2213` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3317` n `53` status `ready` deltaP `17.3257` edge `0.0256` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7015` n `53` status `ready` deltaP `18.4922` edge `0.0646` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6497` n `53` status `ready` deltaP `18.9413` edge `0.0622` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.1791` n `53` status `ready` deltaP `-2.6494` edge `0.0362` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3065` n `88` status `ready` deltaP `3.9467` edge `0.0158` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4542` n `88` status `ready` deltaP `2.089` edge `-0.0039` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.7029` n `88` status `ready` deltaP `2.4806` edge `-0.0089` maxDD `-2.4871`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
