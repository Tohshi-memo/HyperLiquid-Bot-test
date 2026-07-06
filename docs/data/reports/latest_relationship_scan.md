# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T17:22:27.332347+00:00`
- Price records: `672`
- Market context records: `5899`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11176`

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

- `news_risk_high->fx_4h` score `3.6047` n `30` status `ready` deltaP `37.4085` edge `0.0556` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.9998` n `30` status `ready` deltaP `24.2315` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9346` n `30` status `ready` deltaP `11.3872` edge `0.0906` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.778` n `224` status `ready` deltaP `7.0884` edge `0.1276` maxDD `-4.1352`
- `news_risk_high->crypto_alt_1h` score `0.2356` n `30` status `ready` deltaP `5.1697` edge `0.0419` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2407` n `224` status `ready` deltaP `4.7209` edge `0.0303` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.3295` n `224` status `ready` deltaP `3.1116` edge `0.0041` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4515` n `30` status `ready` deltaP `1.0878` edge `-0.0285` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5298` n `224` status `ready` deltaP `-1.62` edge `-0.0021` maxDD `-1.7349`
- `market_context_high->index_1h` score `-0.6278` n `224` status `ready` deltaP `0.1337` edge `0.0034` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.6282` n `224` status `ready` deltaP `2.9646` edge `0.0318` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.7162` n `224` status `ready` deltaP `2.0744` edge `0.0278` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.8514` n `224` status `ready` deltaP `-3.1197` edge `-0.0013` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2424` n `30` status `ready` deltaP `-12.5449` edge `-0.0242` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6109` n `224` status `ready` deltaP `-2.6241` edge `-0.0177` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.6812` n `224` status `ready` deltaP `-3.1359` edge `-0.0314` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.8829` n `30` status `ready` deltaP `-14.7967` edge `-0.0552` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `-1.8927` n `224` status `ready` deltaP `8.4277` edge `0.1384` maxDD `-25.6458`
- `market_context_high->index_4h` score `-2.0334` n `224` status `ready` deltaP `-1.5027` edge `0.0093` maxDD `-3.165`
- `market_context_high->fx_24h` score `-2.0482` n `217` status `ready` deltaP `2.0113` edge `0.0058` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
