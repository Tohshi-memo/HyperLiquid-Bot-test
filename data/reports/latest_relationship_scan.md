# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T17:52:27.095087+00:00`
- Price records: `672`
- Market context records: `2888`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `9.5353` n `142` status `ready` deltaP `8.952` edge `1.1266` maxDD `-22.6673`
- `market_context_high->equity_24h` score `5.2389` n `142` status `ready` deltaP `10.2968` edge `0.5683` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.0112` n `142` status `ready` deltaP `10.2406` edge `0.3958` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.2609` n `142` status `ready` deltaP `10.9326` edge `0.2136` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7448` n `142` status `ready` deltaP `15.5516` edge `0.3511` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.6001` n `142` status `ready` deltaP `14.3679` edge `0.0653` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.5134` n `142` status `ready` deltaP `6.0331` edge `0.1079` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.05` n `142` status `ready` deltaP `4.0483` edge `0.016` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.1706` n `142` status `ready` deltaP `4.4014` edge `0.0944` maxDD `-5.7037`
- `market_context_high->unknown_1h` score `-0.2618` n `142` status `ready` deltaP `4.3308` edge `0.0224` maxDD `-3.1801`
- `market_context_high->commodity_1h` score `-0.5867` n `142` status `ready` deltaP `-0.5819` edge `0.004` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.5931` n `142` status `ready` deltaP `5.3956` edge `0.064` maxDD `-10.747`
- `market_context_high->crypto_alt_4h` score `-0.6249` n `142` status `ready` deltaP `14.4903` edge `0.2854` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.6401` n `142` status `ready` deltaP `-1.7352` edge `0.0026` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6894` n `142` status `ready` deltaP `-0.6157` edge `0.0003` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.6949` n `142` status `ready` deltaP `5.423` edge `0.0617` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.7013` n `142` status `ready` deltaP `-1.5518` edge `0.0352` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.0828` n `142` status `ready` deltaP `4.1244` edge `0.0257` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2247` n `142` status `ready` deltaP `-4.3627` edge `0.0049` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3603` n `142` status `ready` deltaP `-1.8852` edge `-0.0136` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
