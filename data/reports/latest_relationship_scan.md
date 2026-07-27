# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T02:07:36.828237+00:00`
- Price records: `672`
- Market context records: `8047`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11848`

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

- `market_context_high->equity_24h` score `19.8945` n `75` status `ready` deltaP `34.6205` edge `1.5181` maxDD `-4.9489`
- `market_context_high->metal_24h` score `8.3624` n `75` status `ready` deltaP `35.8752` edge `0.4577` maxDD `0.0`
- `market_context_high->equity_4h` score `8.2426` n `88` status `ready` deltaP `32.1507` edge `0.5262` maxDD `-2.959`
- `market_context_high->commodity_24h` score `5.491` n `75` status `ready` deltaP `35.8868` edge `0.3338` maxDD `-6.2367`
- `market_context_high->index_4h` score `3.0975` n `88` status `ready` deltaP `30.3908` edge `0.0796` maxDD `-0.5928`
- `market_context_high->index_24h` score `2.4591` n `75` status `ready` deltaP `13.7932` edge `0.18` maxDD `-1.3621`
- `market_context_high->metal_4h` score `2.2929` n `88` status `ready` deltaP `21.092` edge `0.1127` maxDD `-0.979`
- `market_context_high->equity_1h` score `2.2738` n `88` status `ready` deltaP `16.0248` edge `0.1392` maxDD `-2.8575`
- `market_context_high->fx_24h` score `1.4423` n `75` status `ready` deltaP `30.0705` edge `0.0548` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.0428` n `88` status `ready` deltaP `14.8` edge `0.0206` maxDD `-0.5892`
- `market_context_high->metal_1h` score `0.7477` n `88` status `ready` deltaP `10.7921` edge `0.0282` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5947` n `88` status `ready` deltaP `9.3903` edge `0.028` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.4144` n `88` status `ready` deltaP `7.4002` edge `0.157` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.3031` n `88` status `ready` deltaP `3.6862` edge `0.1124` maxDD `-3.9374`
- `market_context_high->fx_4h` score `0.0496` n `88` status `ready` deltaP `7.6358` edge `0.0063` maxDD `-0.4012`
- `market_context_high->crypto_alt_1h` score `-0.2969` n `88` status `ready` deltaP `0.0612` edge `0.0181` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.4233` n `88` status `ready` deltaP `1.4018` edge `-0.0013` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.4359` n `88` status `ready` deltaP `-2.9872` edge `0.0004` maxDD `-0.2428`
- `market_context_high->commodity_4h` score `-0.8493` n `88` status `ready` deltaP `5.2799` edge `0.0061` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.2276` n `88` status `ready` deltaP `5.2667` edge `-0.1784` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
