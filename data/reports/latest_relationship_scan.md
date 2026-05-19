# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T13:07:23.243740+00:00`
- Price records: `672`
- Market context records: `1222`
- Flow alert records: `5424`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8777`

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

- `market_context_high->crypto_major_24h` score `18.9708` n `128` status `ready` deltaP `44.8784` edge `1.3949` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.7961` n `128` status `ready` deltaP `3.5442` edge `0.7477` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.3885` n `128` status `ready` deltaP `22.6562` edge `0.6663` maxDD `-15.1306`
- `market_context_high->commodity_24h` score `5.3797` n `128` status `ready` deltaP `-3.9931` edge `0.6231` maxDD `-6.8535`
- `market_context_high->metal_24h` score `5.1485` n `128` status `ready` deltaP `-2.2569` edge `0.6108` maxDD `-6.3373`
- `market_context_high->equity_4h` score `3.2333` n `128` status `ready` deltaP `16.33` edge `0.2269` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.726` n `128` status `ready` deltaP `19.9653` edge `0.2027` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4771` n `128` status `ready` deltaP `20.1389` edge `0.416` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.2337` n `128` status `ready` deltaP `12.0617` edge `0.0907` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.8322` n `128` status `ready` deltaP `8.941` edge `0.0562` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.6552` n `128` status `ready` deltaP `9.899` edge `0.0203` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5883` n `128` status `ready` deltaP `5.1599` edge `0.0515` maxDD `-1.2834`
- `market_context_high->unknown_24h` score `0.2623` n `128` status `ready` deltaP `-0.5208` edge `0.2983` maxDD `-10.1706`
- `market_context_high->metal_1h` score `-0.0237` n `128` status `ready` deltaP `9.8194` edge `-0.0064` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.0869` n `128` status `ready` deltaP `5.5998` edge `0.001` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1626` n `128` status `ready` deltaP `5.545` edge `0.1343` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3188` n `128` status `ready` deltaP `0.7953` edge `0.0381` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3895` n `128` status `ready` deltaP `2.8256` edge `0.0078` maxDD `-4.1256`
- `market_context_high->commodity_1h` score `-0.7559` n `128` status `ready` deltaP `-2.1613` edge `0.0129` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.7794` n `128` status `ready` deltaP `12.8621` edge `-0.0076` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
