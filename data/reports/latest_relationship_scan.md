# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T14:46:44.311221+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11696`

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

- `market_context_high->commodity_4h` score `0.876` n `169` status `ready` deltaP `11.9939` edge `0.0645` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7323` n `136` status `ready` deltaP `18.7634` edge `0.0167` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.6709` n `172` status `ready` deltaP `9.1805` edge `0.029` maxDD `-0.7439`
- `market_context_high->equity_24h` score `0.4701` n `136` status `ready` deltaP `3.2496` edge `0.3309` maxDD `-21.0709`
- `market_context_high->fx_4h` score `0.0015` n `169` status `ready` deltaP `7.7095` edge `0.0087` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.0759` n `172` status `ready` deltaP `5.1803` edge `0.0009` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.4192` n `136` status `ready` deltaP `2.866` edge `0.0991` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7174` n `172` status `ready` deltaP `-1.6014` edge `-0.0014` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.773` n `172` status `ready` deltaP `-4.0941` edge `-0.0082` maxDD `-2.0884`
- `market_context_high->metal_24h` score `-0.87` n `136` status `ready` deltaP `0.5187` edge `0.0522` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.1553` n `172` status `ready` deltaP `-1.1941` edge `-0.0018` maxDD `-4.5876`
- `market_context_high->index_4h` score `-1.2217` n `169` status `ready` deltaP `-1.8843` edge `-0.011` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.5848` n `172` status `ready` deltaP `-9.1143` edge `-0.0403` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9588` n `169` status `ready` deltaP `-6.3051` edge `-0.0327` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.2713` n `169` status `ready` deltaP `-11.4059` edge `-0.1317` maxDD `-7.9331`
- `market_context_high->crypto_major_1h` score `-3.6147` n `172` status `ready` deltaP `-10.5521` edge `-0.0575` maxDD `-10.5372`
- `market_context_high->crypto_major_24h` score `-3.893` n `136` status `ready` deltaP `-0.4638` edge `-0.0719` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.9927` n `169` status `ready` deltaP `-12.4549` edge `-0.1531` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.2323` n `136` status `ready` deltaP `-11.9075` edge `-0.129` maxDD `-4.5445`
- `market_context_high->commodity_24h` score `-8.686` n `136` status `ready` deltaP `-5.3752` edge `-0.2062` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
