# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T13:37:24.260715+00:00`
- Price records: `672`
- Market context records: `1943`
- Flow alert records: `7488`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7547`

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

- `market_context_high->crypto_alt_4h` score `7.0863` n `228` status `ready` deltaP `22.1835` edge `0.5571` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.455` n `228` status `ready` deltaP `25.8032` edge `0.4905` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.549` n `228` status `ready` deltaP `14.1909` edge `0.3202` maxDD `-9.8581`
- `market_context_high->equity_4h` score `1.9811` n `228` status `ready` deltaP `13.7762` edge `0.1827` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.7081` n `199` status `ready` deltaP `14.7079` edge `0.493` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.6846` n `232` status `ready` deltaP `7.7044` edge `0.1043` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.5184` n `232` status `ready` deltaP `7.0153` edge `0.1078` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.2174` n `199` status `ready` deltaP `11.9871` edge `0.1808` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1501` n `199` status `ready` deltaP `4.1922` edge `0.1074` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1223` n `228` status `ready` deltaP `8.4284` edge `0.0629` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.171` n `232` status `ready` deltaP `4.9247` edge `0.0323` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2759` n `199` status `ready` deltaP `9.9323` edge `0.0157` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6174` n `232` status `ready` deltaP `0.573` edge `0.0079` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6356` n `232` status `ready` deltaP `-2.754` edge `0.0001` maxDD `-0.3914`
- `market_context_high->equity_24h` score `-0.7915` n `199` status `ready` deltaP `8.9532` edge `0.3642` maxDD `-33.1875`
- `market_context_high->fx_4h` score `-0.9924` n `228` status `ready` deltaP `-5.5063` edge `-0.0017` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.1582` n `232` status `ready` deltaP `3.5799` edge `0.0132` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4676` n `232` status `ready` deltaP `0.5678` edge `-0.0309` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.6639` n `228` status `ready` deltaP `6.9198` edge `0.0844` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.9927` n `232` status `ready` deltaP `0.9937` edge `-0.0063` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
