# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T20:22:33.819734+00:00`
- Price records: `672`
- Market context records: `2797`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `2.9168` n `142` status `ready` deltaP `4.685` edge `0.2583` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `1.646` n `142` status `ready` deltaP `2.1812` edge `0.5143` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.9704` n `142` status `ready` deltaP `6.7953` edge `0.1409` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.5869` n `142` status `ready` deltaP `11.0377` edge `0.2847` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3184` n `142` status `ready` deltaP `13.3009` edge `0.0363` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0538` n `142` status `ready` deltaP `4.7799` edge `0.0457` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0696` n `142` status `ready` deltaP `4.4974` edge `0.0105` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5514` n `142` status `ready` deltaP `-0.6873` edge `0.003` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6006` n `142` status `ready` deltaP `0.8813` edge `0.0017` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.6773` n `142` status `ready` deltaP `5.0962` edge `0.0552` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6927` n `142` status `ready` deltaP `-0.8813` edge `-0.0076` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.8679` n `142` status `ready` deltaP `4.2254` edge `0.0475` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.9279` n `142` status `ready` deltaP `-2.3003` edge `0.0213` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1581` n `142` status `ready` deltaP `-3.9054` edge `0.0074` maxDD `-0.5631`
- `market_context_high->equity_4h` score `-1.1934` n `142` status `ready` deltaP `2.2673` edge `0.0234` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-1.5063` n `142` status `ready` deltaP `14.0329` edge `0.215` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.5806` n `142` status `ready` deltaP `-3.2741` edge `-0.0227` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6514` n `142` status `ready` deltaP `-0.6012` edge `-0.0157` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.0507` n `142` status `ready` deltaP `-0.0086` edge `-0.0078` maxDD `-11.4038`
- `market_context_high->index_24h` score `-2.4073` n `142` status `ready` deltaP `-2.4354` edge `-0.0863` maxDD `-2.5127`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
