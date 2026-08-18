# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T06:52:25.738736+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11645`

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

- `market_context_high->crypto_major_24h` score `2.2635` n `73` status `ready` deltaP `4.9215` edge `0.2766` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.9663` n `73` status `ready` deltaP `12.6469` edge `0.2229` maxDD `-4.666`
- `market_context_high->equity_1h` score `0.914` n `97` status `ready` deltaP `8.4265` edge `0.0504` maxDD `-0.4329`
- `market_context_high->index_1h` score `0.5716` n `97` status `ready` deltaP `11.9035` edge `0.007` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.5475` n `92` status `ready` deltaP `12.5862` edge `0.0193` maxDD `-1.273`
- `market_context_high->unknown_1h` score `0.5172` n `97` status `ready` deltaP `9.3108` edge `0.0037` maxDD `-0.4807`
- `market_context_high->crypto_major_4h` score `0.262` n `92` status `ready` deltaP `7.6485` edge `0.0847` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `0.2311` n `92` status `ready` deltaP `10.0875` edge `0.0941` maxDD `-5.5373`
- `market_context_high->unknown_24h` score `0.1393` n `73` status `ready` deltaP `14.5841` edge `-0.0668` maxDD `-0.1719`
- `market_context_high->metal_1h` score `-0.1276` n `97` status `ready` deltaP `3.1591` edge `0.007` maxDD `-0.4291`
- `market_context_high->commodity_4h` score `-0.2274` n `92` status `ready` deltaP `5.9518` edge `0.0162` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.2862` n `92` status `ready` deltaP `2.0414` edge `0.0002` maxDD `-0.3734`
- `market_context_high->crypto_alt_1h` score `-0.2894` n `97` status `ready` deltaP `3.0094` edge `0.023` maxDD `-2.413`
- `market_context_high->equity_4h` score `-0.2986` n `92` status `ready` deltaP `0.4905` edge `0.0623` maxDD `-2.5696`
- `market_context_high->index_4h` score `-0.4336` n `92` status `ready` deltaP `2.1076` edge `0.011` maxDD `-0.2281`
- `market_context_high->fx_1h` score `-0.4533` n `97` status `ready` deltaP `-3.4416` edge `0.001` maxDD `-0.2273`
- `market_context_high->crypto_major_1h` score `-0.4959` n `97` status `ready` deltaP `1.0803` edge `0.0137` maxDD `-2.7581`
- `market_context_high->metal_24h` score `-0.6817` n `73` status `ready` deltaP `0.0522` edge `0.0496` maxDD `-3.9881`
- `market_context_high->commodity_1h` score `-0.9502` n `97` status `ready` deltaP `-7.8817` edge `-0.008` maxDD `-1.5684`
- `market_context_high->index_24h` score `-2.6848` n `73` status `ready` deltaP `-7.4334` edge `-0.1303` maxDD `-6.1475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
