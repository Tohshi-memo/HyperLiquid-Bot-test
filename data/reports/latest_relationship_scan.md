# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T08:52:25.355258+00:00`
- Price records: `672`
- Market context records: `2647`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9223`

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

- `market_context_high->unknown_24h` score `7.6394` n `130` status `ready` deltaP `17.7057` edge `0.5514` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.7296` n `130` status `ready` deltaP `26.4094` edge `0.5693` maxDD `-15.4319`
- `market_context_high->crypto_alt_24h` score `5.4881` n `130` status `ready` deltaP `8.2131` edge `0.8078` maxDD `-24.4167`
- `market_context_high->crypto_major_4h` score `4.3141` n `130` status `ready` deltaP `17.2209` edge `0.4257` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.3668` n `130` status `ready` deltaP `7.7064` edge `0.1675` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1358` n `133` status `ready` deltaP `10.3035` edge `0.1447` maxDD `-6.1656`
- `market_context_high->index_24h` score `1.0079` n `130` status `ready` deltaP `11.0496` edge `0.1084` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.5056` n `133` status `ready` deltaP `6.8468` edge `0.1159` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.3872` n `130` status `ready` deltaP `10.1877` edge `0.0485` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0616` n `133` status `ready` deltaP `2.3423` edge `0.0334` maxDD `-1.665`
- `market_context_high->index_1h` score `-0.1178` n `133` status `ready` deltaP `3.8528` edge `0.0139` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.1692` n `130` status `ready` deltaP `5.5089` edge `0.0308` maxDD `-2.5301`
- `market_context_high->fx_1h` score `-0.4073` n `133` status `ready` deltaP `0.9883` edge `0.0041` maxDD `-0.2373`
- `market_context_high->commodity_1h` score `-0.4423` n `133` status `ready` deltaP `5.3363` edge `0.0154` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.5669` n `130` status `ready` deltaP `6.1085` edge `-0.0001` maxDD `-0.6957`
- `market_context_high->metal_1h` score `-0.7203` n `133` status `ready` deltaP `-0.6787` edge `0.0054` maxDD `-1.8722`
- `market_context_high->equity_1h` score `-0.8815` n `133` status `ready` deltaP `-1.3799` edge `0.0196` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-1.043` n `130` status `ready` deltaP `-2.1341` edge `0.0104` maxDD `-0.6474`
- `market_context_high->commodity_4h` score `-1.2577` n `130` status `ready` deltaP `3.2434` edge `0.0114` maxDD `-10.2078`
- `market_context_high->equity_24h` score `-1.3009` n `130` status `ready` deltaP `8.5711` edge `-0.0678` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
