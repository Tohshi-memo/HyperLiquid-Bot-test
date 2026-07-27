# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T00:37:28.454131+00:00`
- Price records: `672`
- Market context records: `8040`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11848`

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

- `market_context_high->equity_24h` score `17.8662` n `81` status `ready` deltaP `29.1418` edge `1.3856` maxDD `-4.9489`
- `market_context_high->metal_24h` score `8.0876` n `81` status `ready` deltaP `35.8752` edge `0.4348` maxDD `0.0`
- `market_context_high->equity_4h` score `7.0126` n `94` status `ready` deltaP `27.6369` edge `0.4801` maxDD `-4.3968`
- `market_context_high->commodity_24h` score `4.2755` n `81` status `ready` deltaP `29.467` edge `0.2753` maxDD `-6.2367`
- `market_context_high->index_4h` score `2.573` n `94` status `ready` deltaP `26.7157` edge `0.0723` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.4944` n `94` status `ready` deltaP `22.4701` edge `0.1203` maxDD `-0.979`
- `market_context_high->index_24h` score `2.0435` n `81` status `ready` deltaP `11.2524` edge `0.1623` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.8547` n `94` status `ready` deltaP `15.2567` edge `0.1346` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.1186` n `81` status `ready` deltaP `26.7647` edge `0.0435` maxDD `-1.2814`
- `market_context_high->index_1h` score `0.8748` n `94` status `ready` deltaP `14.177` edge `0.0214` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.8592` n `94` status `ready` deltaP `11.7499` edge `0.0311` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4694` n `94` status `ready` deltaP `10.1892` edge `0.0333` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.3494` n `94` status `ready` deltaP `8.0436` edge `0.1473` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.3132` n `94` status `ready` deltaP `4.5472` edge `0.1075` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.0161` n `94` status `ready` deltaP `1.6626` edge `0.0301` maxDD `-1.4603`
- `market_context_high->fx_4h` score `-0.1661` n `94` status `ready` deltaP `5.5041` edge `0.0042` maxDD `-0.7123`
- `market_context_high->commodity_1h` score `-0.5249` n `94` status `ready` deltaP `-0.4172` edge `-0.0022` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.6915` n `94` status `ready` deltaP `-3.0896` edge `-0.0003` maxDD `-0.2715`
- `market_context_high->commodity_4h` score `-1.0283` n `94` status `ready` deltaP `2.572` edge `0.0012` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.058` n `94` status `ready` deltaP `6.5008` edge `-0.1725` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
