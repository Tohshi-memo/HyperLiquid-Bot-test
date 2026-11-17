# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T19:07:26.835359+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4053`

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

- `market_context_high->unknown_24h` score `1492.7269` n `98` status `ready` deltaP `3.4662` edge `124.3708` maxDD `0.0`
- `news_risk_high->equity_24h` score `59.5935` n `41` status `ready` deltaP `67.6883` edge `4.5855` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `20.1912` n `41` status `ready` deltaP `55.3354` edge `1.3137` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `17.7249` n `41` status `ready` deltaP `34.6451` edge `2.1558` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `15.2003` n `98` status `ready` deltaP `45.7203` edge `1.971` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.4044` n `98` status `ready` deltaP `31.7812` edge `1.8472` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.4228` n `41` status `ready` deltaP `59.0227` edge `0.4221` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.1301` n `41` status `ready` deltaP `54.766` edge `0.3124` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.0104` n `41` status `ready` deltaP `33.2318` edge `0.5227` maxDD `-4.137`
- `news_risk_high->crypto_alt_24h` score `7.6089` n `41` status `ready` deltaP `17.9186` edge `1.3066` maxDD `-29.0448`
- `news_risk_high->crypto_major_4h` score `6.8458` n `41` status `ready` deltaP `26.0671` edge `0.4394` maxDD `-1.7491`
- `news_risk_high->metal_4h` score `6.6914` n `41` status `ready` deltaP `55.183` edge `0.1942` maxDD `-0.0246`
- `news_risk_high->equity_1h` score `5.9602` n `41` status `ready` deltaP `28.005` edge `0.3318` maxDD `-0.4122`
- `news_risk_high->index_4h` score `4.4138` n `41` status `ready` deltaP `38.4147` edge `0.1342` maxDD `-0.1319`
- `news_risk_high->crypto_major_1h` score `3.4475` n `41` status `ready` deltaP `20.0891` edge `0.1885` maxDD `-1.4777`
- `news_risk_high->metal_1h` score `2.8021` n `41` status `ready` deltaP `29.8452` edge `0.0563` maxDD `-0.0743`
- `news_risk_high->commodity_4h` score `2.8001` n `41` status `ready` deltaP `29.8781` edge `0.0595` maxDD `-0.3611`
- `news_risk_high->crypto_alt_1h` score `2.7754` n `41` status `ready` deltaP `18.9974` edge `0.1573` maxDD `-2.5469`
- `news_risk_high->index_1h` score `2.2112` n `41` status `ready` deltaP `25.8653` edge `0.0336` maxDD `-0.0751`
- `news_risk_high->metal_24h` score `-0.0663` n `41` status `ready` deltaP `9.3122` edge `0.1467` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
