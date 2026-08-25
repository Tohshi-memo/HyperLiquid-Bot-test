# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T08:37:52.773302+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `43.7361` n `51` status `ready` deltaP `2.9514` edge `3.625` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9061` n `51` status `ready` deltaP `25.0209` edge `0.9133` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.3483` n `51` status `ready` deltaP `37.8064` edge `0.7034` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.8054` n `51` status `ready` deltaP `46.8648` edge `0.1032` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3869` n `51` status `ready` deltaP `16.9337` edge `0.1998` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.1167` n `51` status `ready` deltaP `36.8633` edge `0.0274` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.7007` n `51` status `ready` deltaP `24.0316` edge `0.1419` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.9119` n `133` status `ready` deltaP `19.4629` edge `0.0704` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1428` n `51` status `ready` deltaP `15.7978` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7285` n `51` status `ready` deltaP `16.5463` edge `0.0195` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.5216` n `51` status `ready` deltaP `10.5003` edge `0.0132` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3477` n `51` status `ready` deltaP `9.7364` edge `-0.0051` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.0231` n `51` status `ready` deltaP `5.5301` edge `0.0014` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.0005` n `133` status `ready` deltaP `11.2725` edge `-0.0303` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.2096` n `51` status `ready` deltaP `0.3963` edge `-0.0072` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3055` n `51` status `ready` deltaP `5.8435` edge `-0.0113` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4903` n `133` status `ready` deltaP `1.6006` edge `-0.0003` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.6396` n `51` status `ready` deltaP `21.6503` edge `-0.1934` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.6933` n `133` status `ready` deltaP `6.0941` edge `-0.0347` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1269` n `133` status `ready` deltaP `-5.1731` edge `-0.0056` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
