# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T18:37:33.249291+00:00`
- Price records: `672`
- Market context records: `4543`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_1h` score `56.0362` n `171` status `ready` deltaP `7.3993` edge `4.6704` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `30.1104` n `169` status `ready` deltaP `8.3093` edge `2.6104` maxDD `-7.5275`
- `market_context_high->fx_4h` score `-0.4563` n `169` status `ready` deltaP `7.1015` edge `0.0024` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6305` n `171` status `ready` deltaP `-0.3161` edge `0.0132` maxDD `-3.0206`
- `market_context_high->fx_1h` score `-0.6823` n `171` status `ready` deltaP `0.2407` edge `-0.003` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-0.9709` n `169` status `ready` deltaP `3.7821` edge `0.0708` maxDD `-8.8203`
- `market_context_high->index_4h` score `-1.0521` n `169` status `ready` deltaP `0.6089` edge `-0.01` maxDD `-5.9823`
- `market_context_high->index_1h` score `-1.0638` n `171` status `ready` deltaP `-3.5578` edge `-0.0118` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.068` n `171` status `ready` deltaP `-1.8454` edge `0.022` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.4003` n `169` status `ready` deltaP `1.8663` edge `0.0213` maxDD `-9.3943`
- `market_context_high->unknown_24h` score `-2.7016` n `169` status `ready` deltaP `2.4901` edge `-0.1494` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.562` n `171` status `ready` deltaP `-4.6434` edge `-0.0813` maxDD `-18.0993`
- `market_context_high->crypto_alt_1h` score `-5.3622` n `171` status `ready` deltaP `-3.1087` edge `-0.0974` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.4407` n `169` status `ready` deltaP `-13.0445` edge `-0.0152` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.6866` n `169` status `ready` deltaP `-8.8593` edge `-0.1325` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.3277` n `171` status `ready` deltaP `-4.5637` edge `-0.1216` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-8.3728` n `169` status `ready` deltaP `4.48` edge `0.011` maxDD `-46.4215`
- `market_context_high->crypto_alt_4h` score `-13.2843` n `169` status `ready` deltaP `-1.5154` edge `-0.2312` maxDD `-63.9243`
- `market_context_high->equity_24h` score `-13.4226` n `169` status `ready` deltaP `-0.8834` edge `-0.247` maxDD `-102.1031`
- `market_context_high->metal_4h` score `-15.5669` n `169` status `ready` deltaP `-6.7866` edge `-0.3171` maxDD `-68.4587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
