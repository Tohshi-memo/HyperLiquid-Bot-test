# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T08:07:25.343748+00:00`
- Price records: `672`
- Market context records: `5962`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11184`

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

- `news_risk_high->fx_24h` score `7.0193` n `30` status `ready` deltaP `64.2361` edge `0.1567` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.2891` n `30` status `ready` deltaP `38.0556` edge `0.2076` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8442` n `30` status `ready` deltaP `39.8476` edge `0.0593` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.122` n `30` status `ready` deltaP `25.5788` edge `0.0202` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4687` n `230` status `ready` deltaP `9.4698` edge `0.1687` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8372` n `30` status `ready` deltaP `10.1896` edge `0.0861` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2029` n `30` status `ready` deltaP `5.3194` edge `0.0367` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1625` n `30` status `ready` deltaP `6.9791` edge `0.0198` maxDD `-2.3058`
- `market_context_high->equity_1h` score `-0.3594` n `240` status `ready` deltaP `4.6757` edge `0.0356` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.376` n `30` status `ready` deltaP `2.1357` edge `-0.0258` maxDD `-1.2643`
- `market_context_high->equity_24h` score `-0.4005` n `213` status `ready` deltaP `21.3102` edge `0.3142` maxDD `-31.2762`
- `market_context_high->metal_1h` score `-0.4739` n `240` status `ready` deltaP `2.5524` edge `0.0021` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5807` n `240` status `ready` deltaP `-2.7345` edge `-0.0005` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.6398` n `240` status `ready` deltaP `-0.2545` edge `-0.0005` maxDD `-0.756`
- `market_context_high->index_1h` score `-0.6412` n `240` status `ready` deltaP `0.6512` edge `0.0048` maxDD `-1.3078`
- `news_risk_high->index_1h` score `-1.117` n `30` status `ready` deltaP `-10.5988` edge `-0.0211` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1176` n `240` status `ready` deltaP `1.8563` edge `0.0211` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1249` n `240` status `ready` deltaP `1.986` edge `0.0178` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.525` n `230` status `ready` deltaP `-2.1859` edge `-0.0096` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.5839` n `230` status `ready` deltaP `-2.2243` edge `-0.025` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
