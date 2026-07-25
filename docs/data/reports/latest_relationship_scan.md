# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T08:52:29.826543+00:00`
- Price records: `672`
- Market context records: `7862`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `11.5024` n `127` status `ready` deltaP `28.9381` edge `0.8998` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.6064` n `128` status `ready` deltaP `5.9776` edge `0.3316` maxDD `-6.5736`
- `market_context_high->metal_24h` score `1.4931` n `128` status `ready` deltaP `10.4324` edge `0.2421` maxDD `-2.3111`
- `market_context_high->commodity_24h` score `1.4111` n `127` status `ready` deltaP `22.1459` edge `0.1283` maxDD `-7.0012`
- `market_context_high->crypto_major_4h` score `1.2946` n `128` status `ready` deltaP `15.3582` edge `0.1773` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.9937` n `128` status `ready` deltaP `12.1679` edge `0.0458` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.9411` n `128` status `ready` deltaP `9.5464` edge `0.1265` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.9328` n `127` status `ready` deltaP `26.9784` edge `0.0485` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.5205` n `128` status `ready` deltaP `7.843` edge `0.0962` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.4906` n `128` status `ready` deltaP `8.8112` edge `0.0415` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3825` n `128` status `ready` deltaP `8.6829` edge `0.017` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2237` n `128` status `ready` deltaP `4.2899` edge `0.0333` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.1487` n `128` status `ready` deltaP `6.6137` edge `0.0142` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1787` n `128` status `ready` deltaP `10.8014` edge `0.0509` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3078` n `128` status `ready` deltaP `-0.0915` edge `-0.0001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.9086` n `128` status `ready` deltaP `0.6175` edge `0.0205` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.1351` n `127` status `ready` deltaP `-4.7312` edge `0.0957` maxDD `-2.1079`
- `market_context_high->metal_4h` score `-1.2288` n `128` status `ready` deltaP `2.7249` edge `0.0807` maxDD `-1.4346`
- `market_context_high->fx_4h` score `-1.4196` n `128` status `ready` deltaP `-3.0032` edge `0.0007` maxDD `-1.6813`
- `market_context_high->crypto_alt_24h` score `-1.5486` n `128` status `ready` deltaP `15.6129` edge `0.2269` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
