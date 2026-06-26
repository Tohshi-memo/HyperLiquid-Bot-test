# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T12:24:42.494948+00:00`
- Price records: `672`
- Market context records: `4827`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `13.5957` n `110` status `ready` deltaP `12.1394` edge `1.0938` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.0976` n `110` status `ready` deltaP `17.572` edge `0.6787` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.0552` n `103` status `ready` deltaP `15.8324` edge `0.2179` maxDD `-2.8416`
- `market_context_high->index_4h` score `0.8968` n `110` status `ready` deltaP `10.9202` edge `0.0486` maxDD `-0.7334`
- `market_context_high->equity_4h` score `0.8723` n `110` status `ready` deltaP `12.7328` edge `0.1651` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.4769` n `110` status `ready` deltaP `15.8038` edge `0.073` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.23` n `110` status `ready` deltaP `6.3201` edge `0.0252` maxDD `-1.1869`
- `market_context_high->equity_1h` score `-0.0021` n `110` status `ready` deltaP `4.0855` edge `0.0341` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.4908` n `110` status `ready` deltaP `2.2811` edge `-0.0005` maxDD `-1.5439`
- `market_context_high->index_1h` score `-0.5058` n `110` status `ready` deltaP `0.4709` edge `0.0075` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-1.0886` n `110` status `ready` deltaP `-3.2199` edge `-0.0043` maxDD `-0.8626`
- `market_context_high->crypto_alt_1h` score `-1.8801` n `110` status `ready` deltaP `5.2831` edge `-0.0037` maxDD `-12.7225`
- `market_context_high->crypto_major_1h` score `-2.1157` n `110` status `ready` deltaP `3.2825` edge `-0.0356` maxDD `-17.9354`
- `market_context_high->metal_1h` score `-2.124` n `110` status `ready` deltaP `0.4055` edge `-0.0647` maxDD `-13.4916`
- `market_context_high->fx_24h` score `-2.3881` n `103` status `ready` deltaP `-11.5898` edge `-0.0199` maxDD `-2.814`
- `market_context_high->commodity_24h` score `-2.4215` n `103` status `ready` deltaP `17.5247` edge `0.0836` maxDD `-27.5371`
- `market_context_high->crypto_alt_4h` score `-3.7614` n `110` status `ready` deltaP `8.4922` edge `0.0063` maxDD `-38.2779`
- `market_context_high->index_24h` score `-3.9666` n `103` status `ready` deltaP `-2.7878` edge `-0.0991` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-7.2961` n `110` status `ready` deltaP `5.3188` edge `-0.1477` maxDD `-60.5192`
- `market_context_high->metal_4h` score `-8.7392` n `110` status `ready` deltaP `5.6513` edge `-0.3476` maxDD `-60.1721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
