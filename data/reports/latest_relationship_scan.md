# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T10:07:30.120986+00:00`
- Price records: `672`
- Market context records: `5868`
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

- `news_risk_high->fx_4h` score `3.7047` n `30` status `ready` deltaP `38.628` edge `0.0558` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.001` n `30` status `ready` deltaP `24.2315` edge `0.0191` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9524` n `30` status `ready` deltaP `12.2854` edge `0.0869` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.9024` n `240` status `ready` deltaP `6.8394` edge `0.1569` maxDD `-5.5173`
- `news_risk_high->crypto_alt_1h` score `0.3089` n `30` status `ready` deltaP `5.9182` edge `0.0463` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.4019` n `242` status `ready` deltaP `-0.3415` edge `-0.0005` maxDD `-0.567`
- `news_risk_high->metal_1h` score `-0.4204` n `30` status `ready` deltaP `1.6866` edge `-0.0285` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4399` n `242` status `ready` deltaP `3.7252` edge `0.0056` maxDD `-2.0339`
- `market_context_high->equity_1h` score `-0.4934` n `242` status `ready` deltaP `3.9714` edge `0.0331` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.5387` n `242` status `ready` deltaP `-1.4735` edge `-0.0021` maxDD `-1.905`
- `market_context_high->index_1h` score `-0.6476` n `242` status `ready` deltaP `-0.2932` edge `0.0037` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.8218` n `242` status `ready` deltaP `3.4976` edge `0.0403` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9168` n `242` status `ready` deltaP `2.5573` edge `0.04` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2082` n `30` status `ready` deltaP `-11.9461` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.2323` n `240` status `ready` deltaP `-0.2643` edge `0.0125` maxDD `-3.165`
- `news_risk_high->commodity_4h` score `-1.8205` n `30` status `ready` deltaP `-13.8821` edge `-0.0533` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8327` n `228` status `ready` deltaP `4.8794` edge `0.0143` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.9076` n `240` status `ready` deltaP `-6.7887` edge `-0.0044` maxDD `-2.2593`
- `market_context_high->equity_24h` score `-2.1105` n `228` status `ready` deltaP `13.3224` edge `0.2432` maxDD `-31.6316`
- `news_risk_high->index_4h` score `-2.2534` n `30` status `ready` deltaP `-16.0976` edge `-0.0782` maxDD `-2.9371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
