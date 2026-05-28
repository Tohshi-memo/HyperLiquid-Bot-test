# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T14:52:21.645036+00:00`
- Price records: `672`
- Market context records: `2151`
- Flow alert records: `8089`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `market_context_high->crypto_alt_4h` score `13.6434` n `150` status `ready` deltaP `38.1728` edge `0.9761` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9688` n `150` status `ready` deltaP `42.1341` edge `0.7695` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.4399` n `150` status `ready` deltaP `25.1057` edge `0.4442` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.3225` n `35` status `ready` deltaP `29.4295` edge `0.3978` maxDD `-3.0367`
- `market_context_high->equity_4h` score `4.8023` n `150` status `ready` deltaP `26.0915` edge `0.3357` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.7141` n `150` status `ready` deltaP `14.4514` edge `0.336` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.5463` n `150` status `ready` deltaP `18.8303` edge `0.2177` maxDD `-1.817`
- `market_context_high->index_4h` score `3.3396` n `150` status `ready` deltaP `24.4146` edge `0.1839` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `3.322` n `150` status `ready` deltaP `16.9661` edge `0.2501` maxDD `-4.9097`
- `market_context_high->metal_4h` score `3.1333` n `150` status `ready` deltaP `21.563` edge `0.2561` maxDD `-4.7664`
- `market_context_high->equity_24h` score `3.0762` n `150` status `ready` deltaP `26.1736` edge `0.5717` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.8325` n `150` status `ready` deltaP `27.2222` edge `0.5866` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.4156` n `35` status `ready` deltaP `30.9887` edge `0.0131` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.196` n `150` status `ready` deltaP `21.0486` edge `0.9998` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.1127` n `35` status `ready` deltaP `15.2961` edge `0.113` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0699` n `43` status `ready` deltaP `19.1686` edge `0.0083` maxDD `-1.7548`
- `market_context_high->equity_1h` score `0.8851` n `150` status `ready` deltaP `10.8144` edge `0.0805` maxDD `-2.6402`
- `news_risk_high->commodity_1h` score `0.7978` n `43` status `ready` deltaP `10.6148` edge `0.0995` maxDD `-2.1052`
- `market_context_high->metal_1h` score `0.6705` n `150` status `ready` deltaP `9.5649` edge `0.0591` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.4885` n `43` status `ready` deltaP `8.4389` edge `0.0101` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
