# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T17:07:27.992023+00:00`
- Price records: `672`
- Market context records: `5060`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10292`

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

- `market_context_high->unknown_1h` score `13.1659` n `97` status `ready` deltaP `2.9925` edge `1.1273` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0602` n `97` status `ready` deltaP `20.7207` edge `0.7191` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.2604` n `97` status `ready` deltaP `18.4546` edge `0.5206` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.5574` n `97` status `ready` deltaP `17.0025` edge `0.5082` maxDD `-8.3416`
- `market_context_high->crypto_major_1h` score `1.1419` n `97` status `ready` deltaP `8.3986` edge `0.1208` maxDD `-3.8637`
- `market_context_high->metal_4h` score `0.986` n `97` status `ready` deltaP `10.5843` edge `0.1195` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8759` n `97` status `ready` deltaP `8.6302` edge `0.0728` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.7177` n `97` status `ready` deltaP `6.1636` edge `0.1724` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.6127` n `97` status `ready` deltaP `6.4356` edge `0.1005` maxDD `-4.7207`
- `market_context_high->metal_1h` score `0.4579` n `97` status `ready` deltaP `7.5174` edge `0.0377` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.0222` n `97` status `ready` deltaP `5.8147` edge `0.0392` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.0797` n `73` status `ready` deltaP `8.7115` edge `0.0079` maxDD `-1.7626`
- `market_context_high->index_1h` score `-0.2743` n `97` status `ready` deltaP `1.9955` edge `0.0126` maxDD `-0.552`
- `market_context_high->commodity_1h` score `-0.5941` n `97` status `ready` deltaP `0.3997` edge `0.0138` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.8455` n `97` status `ready` deltaP `7.2951` edge `0.0058` maxDD `-4.9914`
- `market_context_high->fx_4h` score `-0.9401` n `97` status `ready` deltaP `-3.2232` edge `-0.0001` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4819` n `97` status `ready` deltaP `-8.7289` edge `-0.0043` maxDD `-0.5464`
- `market_context_high->metal_24h` score `-3.7427` n `73` status `ready` deltaP `4.9277` edge `0.0328` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.0654` n `73` status `ready` deltaP `1.1843` edge `-0.075` maxDD `-24.3277`
- `market_context_high->unknown_24h` score `-4.7028` n `73` status `ready` deltaP `26.8883` edge `-0.5369` maxDD `-1.4072`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
