# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T09:52:23.629601+00:00`
- Price records: `672`
- Market context records: `2130`
- Flow alert records: `8028`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9158`

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

- `market_context_high->crypto_alt_4h` score `13.2881` n `158` status `ready` deltaP `37.226` edge `0.9528` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9298` n `158` status `ready` deltaP `41.5271` edge `0.7703` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.1711` n `158` status `ready` deltaP `24.3555` edge `0.4268` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.0372` n `158` status `ready` deltaP `26.7771` edge `0.3507` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.2417` n `157` status `ready` deltaP `13.5125` edge `0.3029` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.1534` n `158` status `ready` deltaP `17.4354` edge `0.1987` maxDD `-2.1721`
- `market_context_high->metal_4h` score `3.1233` n `158` status `ready` deltaP `21.7081` edge `0.2543` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.0631` n `158` status `ready` deltaP `22.2175` edge `0.1755` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9268` n `158` status `ready` deltaP `15.0402` edge `0.23` maxDD `-4.9097`
- `news_risk_high->unknown_1h` score `2.7153` n `33` status `ready` deltaP `29.8721` edge `0.0574` maxDD `-1.7548`
- `market_context_high->equity_24h` score `2.405` n `157` status `ready` deltaP `24.9388` edge `0.524` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.029` n `157` status `ready` deltaP `25.4733` edge `0.5313` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `1.5456` n `157` status `ready` deltaP `21.2913` edge `0.9148` maxDD `-62.3533`
- `news_risk_high->commodity_1h` score `0.8833` n `33` status `ready` deltaP `8.474` edge `0.0851` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.6944` n `158` status `ready` deltaP `9.2701` edge `0.0749` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.466` n `158` status `ready` deltaP `8.044` edge `0.0522` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.2311` n `157` status `ready` deltaP `11.4065` edge `0.3437` maxDD `-23.2095`
- `market_context_high->unknown_1h` score `0.1077` n `158` status `ready` deltaP `5.0159` edge `0.0475` maxDD `-3.0902`
- `market_context_high->fx_24h` score `-0.0292` n `157` status `ready` deltaP `15.3693` edge `0.0331` maxDD `-2.811`
- `market_context_high->index_1h` score `-0.0472` n `158` status `ready` deltaP `3.8865` edge `0.0292` maxDD `-1.3898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
