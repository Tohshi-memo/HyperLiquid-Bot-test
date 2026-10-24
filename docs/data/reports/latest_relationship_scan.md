# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T20:07:36.508056+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7806`

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

- `market_context_high->unknown_4h` score `17.0758` n `102` status `ready` deltaP `-2.1431` edge `1.4708` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.2195` n `74` status `ready` deltaP `18.8438` edge `0.0669` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `1.0807` n `30` status `ready` deltaP `20.5555` edge `0.0419` maxDD `-0.8976`
- `risk_on_and_context->commodity_24h` score `1.0807` n `30` status `ready` deltaP `20.5555` edge `0.0419` maxDD `-0.8976`
- `market_context_high->commodity_4h` score `0.831` n `102` status `ready` deltaP `12.1174` edge `0.0447` maxDD `-1.165`
- `risk_on_high->fx_1h` score `0.7636` n `30` status `ready` deltaP `16.7764` edge `0.0036` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.7636` n `30` status `ready` deltaP `16.7764` edge `0.0036` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `0.3414` n `30` status `ready` deltaP `8.8211` edge `0.0072` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.3414` n `30` status `ready` deltaP `8.8211` edge `0.0072` maxDD `-0.1126`
- `risk_on_high->index_1h` score `0.3031` n `30` status `ready` deltaP `9.9601` edge `-0.0005` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.3031` n `30` status `ready` deltaP `9.9601` edge `-0.0005` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.2128` n `30` status `ready` deltaP `11.7565` edge `-0.0088` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.2128` n `30` status `ready` deltaP `11.7565` edge `-0.0088` maxDD `-0.7172`
- `market_context_high->fx_1h` score `-0.1476` n `111` status `ready` deltaP `2.0917` edge `0.0026` maxDD `-0.1712`
- `risk_on_high->metal_1h` score `-0.1681` n `30` status `ready` deltaP `-0.529` edge `0.0077` maxDD `-0.058`
- `risk_on_and_context->metal_1h` score `-0.1681` n `30` status `ready` deltaP `-0.529` edge `0.0077` maxDD `-0.058`
- `market_context_high->commodity_1h` score `-0.2913` n `111` status `ready` deltaP `3.0143` edge `0.0057` maxDD `-1.0053`
- `risk_on_high->commodity_4h` score `-0.3607` n `30` status `ready` deltaP `0.5488` edge `-0.0073` maxDD `-1.0752`
- `risk_on_and_context->commodity_4h` score `-0.3607` n `30` status `ready` deltaP `0.5488` edge `-0.0073` maxDD `-1.0752`
- `market_context_high->fx_4h` score `-0.3995` n `102` status `ready` deltaP `0.5858` edge `0.0055` maxDD `-0.5168`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
