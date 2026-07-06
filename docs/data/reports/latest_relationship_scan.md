# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T14:47:05.430717+00:00`
- Price records: `672`
- Market context records: `5888`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10264`

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

- `news_risk_high->fx_4h` score `3.7241` n `30` status `ready` deltaP `38.7805` edge `0.0564` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0633` n `30` status `ready` deltaP `24.98` edge `0.0193` maxDD `-0.1113`
- `market_context_high->equity_4h` score `0.9607` n `226` status `ready` deltaP `7.3926` edge `0.1408` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9439` n `30` status `ready` deltaP `11.5369` edge `0.0908` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2567` n `30` status `ready` deltaP `5.1697` edge `0.0446` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1947` n `229` status `ready` deltaP `4.9604` edge `0.0346` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.2954` n `229` status `ready` deltaP `3.5124` edge `0.0058` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4352` n `30` status `ready` deltaP `1.3872` edge `-0.0284` maxDD `-1.2643`
- `market_context_high->crypto_major_1h` score `-0.5295` n `229` status `ready` deltaP `3.6621` edge `0.0398` maxDD `-6.2348`
- `market_context_high->commodity_1h` score `-0.5496` n `229` status `ready` deltaP `-1.616` edge `-0.0026` maxDD `-1.9006`
- `market_context_high->index_1h` score `-0.5919` n `229` status `ready` deltaP `0.7178` edge `0.0041` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.6066` n `229` status `ready` deltaP `2.6515` edge `0.038` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.7996` n `229` status `ready` deltaP `-2.5018` edge `-0.0011` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.272` n `30` status `ready` deltaP `-12.994` edge `-0.025` maxDD `-1.1161`
- `market_context_high->crypto_major_4h` score `-1.7052` n `226` status `ready` deltaP `8.9129` edge `0.1592` maxDD `-25.6458`
- `news_risk_high->commodity_4h` score `-1.8102` n `30` status `ready` deltaP `-13.7296` edge `-0.053` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.9442` n `222` status `ready` deltaP `3.3502` edge `0.0102` maxDD `-5.5435`
- `market_context_high->index_4h` score `-1.9814` n `226` status `ready` deltaP `-1.1076` edge `0.011` maxDD `-3.165`
- `news_risk_high->index_4h` score `-2.2954` n `30` status `ready` deltaP `-16.8598` edge `-0.0785` maxDD `-2.9371`
- `market_context_high->commodity_4h` score `-2.4631` n `226` status `ready` deltaP `-2.3432` edge `-0.0183` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
