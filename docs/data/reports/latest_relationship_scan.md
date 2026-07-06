# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T09:52:29.272325+00:00`
- Price records: `672`
- Market context records: `5867`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10176`

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

- `news_risk_high->fx_4h` score `3.7035` n `30` status `ready` deltaP `38.628` edge `0.0557` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.9878` n `30` status `ready` deltaP `24.0818` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9524` n `30` status `ready` deltaP `12.2854` edge `0.0869` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.6364` n `241` status `ready` deltaP `6.7187` edge `0.1527` maxDD `-6.8903`
- `news_risk_high->crypto_alt_1h` score `0.3206` n `30` status `ready` deltaP `6.0679` edge `0.0468` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3873` n `242` status `ready` deltaP `-0.0779` edge `-0.0005` maxDD `-0.5575`
- `market_context_high->metal_1h` score `-0.4152` n `242` status `ready` deltaP `3.9887` edge `0.0059` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4297` n `30` status `ready` deltaP `1.5369` edge `-0.0287` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4687` n `242` status `ready` deltaP `4.2349` edge `0.0334` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.5556` n `242` status `ready` deltaP `-1.737` edge `-0.0025` maxDD `-1.905`
- `market_context_high->index_1h` score `-0.6331` n `242` status `ready` deltaP `-0.0297` edge `0.0038` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.8218` n `242` status `ready` deltaP `3.4976` edge `0.0403` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9487` n `242` status `ready` deltaP `2.2938` edge `0.0391` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2159` n `30` status `ready` deltaP `-12.0958` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.2403` n `241` status `ready` deltaP `-0.3434` edge `0.012` maxDD `-3.165`
- `market_context_high->metal_4h` score `-1.7118` n `241` status `ready` deltaP `-3.0703` edge `-0.0329` maxDD `-5.9542`
- `news_risk_high->commodity_4h` score `-1.8197` n `30` status `ready` deltaP `-13.8821` edge `-0.0532` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8319` n `228` status `ready` deltaP `4.8794` edge `0.0144` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.8941` n `241` status `ready` deltaP `-6.5587` edge `-0.0042` maxDD `-2.2593`
- `market_context_high->equity_24h` score `-2.0293` n `228` status `ready` deltaP `13.5874` edge `0.2482` maxDD `-31.6316`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
