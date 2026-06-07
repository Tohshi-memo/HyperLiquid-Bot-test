# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T19:51:31.510179+00:00`
- Price records: `672`
- Market context records: `3211`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10910`

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

- `market_context_high->commodity_24h` score `13.7969` n `99` status `ready` deltaP `47.6799` edge `0.8747` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `11.4072` n `99` status `ready` deltaP `13.2102` edge `2.372` maxDD `-71.142`
- `market_context_high->index_24h` score `9.2883` n `99` status `ready` deltaP `28.6616` edge `0.8384` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.9984` n `99` status `ready` deltaP `12.8315` edge `1.3969` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.4331` n `125` status `ready` deltaP `22.3037` edge `0.1832` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.6266` n `137` status `ready` deltaP `7.496` edge `0.0445` maxDD `-1.7142`
- `market_context_high->fx_24h` score `0.044` n `99` status `ready` deltaP `8.2071` edge `-0.0058` maxDD `-0.9534`
- `market_context_high->unknown_4h` score `-0.1317` n `125` status `ready` deltaP `9.922` edge `0.1451` maxDD `-14.7778`
- `market_context_high->index_1h` score `-0.9801` n `137` status `ready` deltaP `2.4608` edge `0.0082` maxDD `-4.5023`
- `market_context_high->fx_4h` score `-1.0688` n `125` status `ready` deltaP `-6.5329` edge `-0.005` maxDD `-1.4115`
- `market_context_high->crypto_alt_1h` score `-1.5223` n `137` status `ready` deltaP `3.9206` edge `0.0683` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-1.6183` n `137` status `ready` deltaP `-9.2366` edge `-0.0046` maxDD `-0.8278`
- `market_context_high->index_4h` score `-1.6256` n `125` status `ready` deltaP `14.4951` edge `0.0588` maxDD `-17.6057`
- `market_context_high->equity_1h` score `-1.6915` n `137` status `ready` deltaP `1.5626` edge `-0.0028` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.7692` n `137` status `ready` deltaP `4.0135` edge `0.0521` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.1984` n `137` status `ready` deltaP `-3.8649` edge `-0.0124` maxDD `-7.9361`
- `market_context_high->unknown_1h` score `-2.8615` n `137` status `ready` deltaP `0.7026` edge `-0.1239` maxDD `-17.8119`
- `market_context_high->unknown_24h` score `-4.4127` n `99` status `ready` deltaP `10.6377` edge `0.1026` maxDD `-55.1403`
- `market_context_high->crypto_major_4h` score `-4.7265` n `125` status `ready` deltaP `5.2817` edge `0.1512` maxDD `-54.3896`
- `market_context_high->equity_4h` score `-4.8308` n `125` status `ready` deltaP `12.6293` edge `0.0438` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
