# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T09:07:25.628634+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5116`

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

- `market_context_high->unknown_4h` score `125.2004` n `37` status `ready` deltaP `-4.0911` edge `10.5054` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.2832` n `37` status `ready` deltaP `10.6571` edge `0.2485` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1705` n `37` status `ready` deltaP `34.2287` edge `0.045` maxDD `-0.0521`
- `market_context_high->index_4h` score `2.0304` n `37` status `ready` deltaP `26.5079` edge `0.0395` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.4275` n `44` status `ready` deltaP `7.1338` edge `0.0935` maxDD `-0.1014`
- `news_risk_high->fx_4h` score `0.9947` n `45` status `ready` deltaP `15.1897` edge `0.0117` maxDD `-0.0725`
- `market_context_high->crypto_major_1h` score `0.8083` n `37` status `ready` deltaP `9.9005` edge `0.0599` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.5449` n `37` status `ready` deltaP `12.146` edge `0.0704` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4098` n `37` status `ready` deltaP `6.9227` edge `0.0151` maxDD `-0.1681`
- `news_risk_high->equity_4h` score `0.3554` n `45` status `ready` deltaP `1.4804` edge `0.1096` maxDD `-4.2454`
- `market_context_high->index_1h` score `0.3213` n `37` status `ready` deltaP `2.2496` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_4h` score `0.1873` n `45` status `ready` deltaP `7.649` edge `0.0208` maxDD `-0.4888`
- `market_context_high->commodity_1h` score `0.1335` n `37` status `ready` deltaP `9.3179` edge `0.0096` maxDD `-1.7019`
- `news_risk_high->fx_1h` score `0.058` n `47` status `ready` deltaP `4.335` edge `0.0044` maxDD `-0.0692`
- `news_risk_high->index_1h` score `-0.0092` n `47` status `ready` deltaP `6.2173` edge `0.0027` maxDD `-0.2931`
- `market_context_high->commodity_4h` score `-0.0156` n `37` status `ready` deltaP `2.987` edge `0.0235` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0637` n `37` status `ready` deltaP `1.2017` edge `0.0166` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.225` n `47` status `ready` deltaP `-1.9939` edge `0.0394` maxDD `-1.396`
- `news_risk_high->index_24h` score `-0.3971` n `44` status `ready` deltaP `0.0316` edge `0.1157` maxDD `-6.6786`
- `news_risk_high->metal_1h` score `-0.6218` n `47` status `ready` deltaP `-5.4688` edge `-0.0075` maxDD `-0.5274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
