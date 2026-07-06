# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T11:37:31.030805+00:00`
- Price records: `672`
- Market context records: `5874`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10178`

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

- `news_risk_high->fx_4h` score `3.7728` n `30` status `ready` deltaP `39.3902` edge `0.0564` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0501` n `30` status `ready` deltaP `24.8303` edge `0.0192` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4253` n `234` status `ready` deltaP `8.0702` edge `0.175` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9236` n `30` status `ready` deltaP `11.8363` edge `0.0862` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2793` n `30` status `ready` deltaP `5.4691` edge `0.0455` maxDD `-1.6923`
- `news_risk_high->metal_1h` score `-0.4196` n `30` status `ready` deltaP `1.6866` edge `-0.0284` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4376` n `238` status `ready` deltaP `4.7288` edge `0.0327` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.4398` n `238` status `ready` deltaP `-1.024` edge `-0.0007` maxDD `-0.5751`
- `market_context_high->metal_1h` score `-0.4807` n `238` status `ready` deltaP `3.3953` edge `0.0044` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5307` n `238` status `ready` deltaP `-1.3863` edge `-0.0017` maxDD `-1.9006`
- `market_context_high->index_1h` score `-0.6095` n `238` status `ready` deltaP `0.4252` edge `0.0038` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.8456` n `238` status `ready` deltaP `3.545` edge `0.038` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9399` n `238` status `ready` deltaP `2.5839` edge `0.0379` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.178` n `234` status `ready` deltaP `0.4052` edge `0.015` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2167` n `30` status `ready` deltaP `-12.0958` edge `-0.0239` maxDD `-1.1161`
- `news_risk_high->commodity_4h` score `-1.8189` n `30` status `ready` deltaP `-13.8821` edge `-0.0531` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.839` n `228` status `ready` deltaP `4.8794` edge `0.0135` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.9481` n `234` status `ready` deltaP `-7.4474` edge `-0.0052` maxDD `-2.2593`
- `market_context_high->crypto_major_4h` score `-2.1699` n `234` status `ready` deltaP `9.4069` edge `0.1937` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.2` n `234` status `ready` deltaP `0.0495` edge `-0.0123` maxDD `-6.3754`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
