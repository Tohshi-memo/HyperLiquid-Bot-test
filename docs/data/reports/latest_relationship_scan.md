# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T10:37:26.029630+00:00`
- Price records: `672`
- Market context records: `5870`
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

- `news_risk_high->fx_4h` score `3.7181` n `30` status `ready` deltaP `38.7805` edge `0.0559` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.013` n `30` status `ready` deltaP `24.3812` edge `0.0191` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.2195` n `238` status `ready` deltaP `7.0878` edge `0.1644` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9166` n `30` status `ready` deltaP `11.986` edge `0.0843` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2754` n `30` status `ready` deltaP `5.6188` edge `0.044` maxDD `-1.6923`
- `market_context_high->metal_1h` score `-0.414` n `242` status `ready` deltaP `3.9887` edge `0.006` maxDD `-2.0339`
- `market_context_high->fx_1h` score `-0.4164` n `242` status `ready` deltaP `-0.605` edge `-0.0005` maxDD `-0.5751`
- `news_risk_high->metal_1h` score `-0.4305` n `30` status `ready` deltaP `1.5369` edge `-0.0288` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4452` n `242` status `ready` deltaP `4.4985` edge `0.0336` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.57` n `242` status `ready` deltaP `-2.0006` edge `-0.0026` maxDD `-1.905`
- `market_context_high->index_1h` score `-0.6339` n `242` status `ready` deltaP `-0.0297` edge `0.0037` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.7245` n `242` status `ready` deltaP `4.0246` edge `0.0449` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.8254` n `242` status `ready` deltaP `3.0843` edge `0.0441` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2159` n `30` status `ready` deltaP `-12.0958` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.216` n `238` status `ready` deltaP `-0.0999` edge `0.0135` maxDD `-3.165`
- `news_risk_high->commodity_4h` score `-1.8189` n `30` status `ready` deltaP `-13.8821` edge `-0.0531` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8351` n `228` status `ready` deltaP `4.8794` edge `0.014` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.9262` n `238` status `ready` deltaP `-7.1019` edge `-0.0047` maxDD `-2.2593`
- `market_context_high->crypto_major_4h` score `-2.2669` n `238` status `ready` deltaP `9.2142` edge `0.1869` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.2677` n `238` status `ready` deltaP `-0.6328` edge `-0.0134` maxDD `-6.3754`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
