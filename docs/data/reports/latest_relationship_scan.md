# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T06:37:30.369748+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11430`

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

- `market_context_high->unknown_4h` score `37.8997` n `88` status `ready` deltaP `7.6774` edge `3.1519` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.1405` n `86` status `ready` deltaP `32.6448` edge `2.9512` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.5218` n `86` status `ready` deltaP `25.5612` edge `0.336` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `3.879` n `86` status `ready` deltaP `21.8613` edge `0.861` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.2031` n `86` status `ready` deltaP `16.1078` edge `-0.069` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.4759` n `88` status `ready` deltaP `0.8914` edge `0.0013` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.5019` n `88` status `ready` deltaP `2.4497` edge `0.0095` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.5765` n `88` status `ready` deltaP `1.275` edge `0.0282` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8264` n `88` status `ready` deltaP `0.3464` edge `-0.0105` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.1124` n `88` status `ready` deltaP `-9.4515` edge `0.0035` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2888` n `88` status `ready` deltaP `-3.3398` edge `-0.0046` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3436` n `88` status `ready` deltaP `-14.657` edge `-0.0061` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.8661` n `88` status `ready` deltaP `-9.7509` edge `0.0104` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-2.0137` n `88` status `ready` deltaP `0.034` edge `-0.0605` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1557` n `88` status `ready` deltaP `-7.2201` edge `-0.0101` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.8305` n `86` status `ready` deltaP `-6.7954` edge `-0.0306` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.2337` n `88` status `ready` deltaP `-5.5593` edge `-0.1152` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-5.8656` n `86` status `ready` deltaP `-23.141` edge `-0.0666` maxDD `-24.4901`
- `market_context_high->equity_4h` score `-7.5259` n `88` status `ready` deltaP `-2.7439` edge `-0.2277` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.2996` n `88` status `ready` deltaP `1.178` edge `-0.271` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
