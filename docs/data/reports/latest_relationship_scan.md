# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T12:07:33.443698+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->commodity_4h` score `1.0345` n `169` status `ready` deltaP `13.061` edge `0.0706` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7707` n `136` status `ready` deltaP `18.7634` edge `0.0199` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.6745` n `169` status `ready` deltaP `9.4214` edge `0.0277` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.0684` n `169` status `ready` deltaP `8.4717` edge `0.0092` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1156` n `169` status `ready` deltaP `4.4166` edge `0.0009` maxDD `-0.613`
- `market_context_high->equity_24h` score `-0.5452` n `136` status `ready` deltaP `1.3432` edge `0.259` maxDD `-21.0709`
- `market_context_high->index_24h` score `-0.5871` n `136` status `ready` deltaP `1.6528` edge `0.0932` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7524` n `169` status `ready` deltaP `-1.978` edge `-0.0018` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.7681` n `169` status `ready` deltaP `-3.9099` edge `-0.0088` maxDD `-2.0884`
- `market_context_high->metal_24h` score `-1.062` n `136` status `ready` deltaP `-1.0411` edge `0.0466` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.1931` n `169` status `ready` deltaP `-1.6068` edge `-0.0022` maxDD `-4.5876`
- `market_context_high->index_4h` score `-1.2025` n `169` status `ready` deltaP `-1.8843` edge `-0.0094` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.5949` n `169` status `ready` deltaP `-9.2779` edge `-0.0405` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9226` n `169` status `ready` deltaP `-6.0002` edge `-0.0301` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.2152` n `169` status `ready` deltaP `-11.4059` edge `-0.1245` maxDD `-7.9331`
- `market_context_high->crypto_major_1h` score `-3.6582` n `169` status `ready` deltaP `-10.5401` edge `-0.0612` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-4.0391` n `169` status `ready` deltaP `-12.9122` edge `-0.156` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.3787` n `136` status `ready` deltaP `-11.9075` edge `-0.1412` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.4222` n `136` status `ready` deltaP `-2.0236` edge `-0.1056` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.601` n `136` status `ready` deltaP `-5.3752` edge `-0.1953` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
