# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T17:37:27.402779+00:00`
- Price records: `672`
- Market context records: `3201`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10906`

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

- `market_context_high->crypto_alt_24h` score `16.946` n `98` status `ready` deltaP `12.5815` edge `2.3259` maxDD `-71.142`
- `market_context_high->commodity_24h` score `13.5153` n `98` status `ready` deltaP `46.7403` edge `0.8575` maxDD `-2.0927`
- `market_context_high->index_24h` score `6.1464` n `98` status `ready` deltaP `28.373` edge `0.8543` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.4737` n `98` status `ready` deltaP `12.3264` edge `1.333` maxDD `-53.663`
- `market_context_high->unknown_24h` score `4.0441` n `98` status `ready` deltaP `16.8261` edge `0.6496` maxDD `-17.4635`
- `market_context_high->commodity_4h` score `3.4733` n `130` status `ready` deltaP `22.6407` edge `0.1843` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.953` n `98` status `ready` deltaP `14.6223` edge `0.0047` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.6127` n `130` status `ready` deltaP `11.4423` edge `0.197` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3386` n `135` status `ready` deltaP `5.9969` edge `0.0305` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4184` n `135` status `ready` deltaP `5.4214` edge `0.0165` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.6065` n `135` status `ready` deltaP `6.7532` edge `0.1174` maxDD `-14.7034`
- `market_context_high->crypto_major_1h` score `-0.9069` n `135` status `ready` deltaP `4.4278` edge `0.0805` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.1153` n `135` status `ready` deltaP `5.855` edge `0.0166` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.2097` n `130` status `ready` deltaP `-9.0924` edge `-0.006` maxDD `-1.4115`
- `market_context_high->index_4h` score `-1.3932` n `130` status `ready` deltaP `15.856` edge `0.0691` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.7679` n `135` status `ready` deltaP `-11.0169` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-1.9626` n `135` status `ready` deltaP `-2.5926` edge `-0.0069` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.8033` n `130` status `ready` deltaP `14.6834` edge `0.3472` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.451` n `135` status `ready` deltaP `2.3963` edge `-0.0985` maxDD `-14.4044`
- `market_context_high->crypto_major_4h` score `-4.0356` n `130` status `ready` deltaP `8.4874` edge `0.2184` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
