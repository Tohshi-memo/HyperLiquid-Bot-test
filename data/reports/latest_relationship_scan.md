# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T17:07:27.366466+00:00`
- Price records: `672`
- Market context records: `6200`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `12.761` n `32` status `ready` deltaP `42.2194` edge `0.7967` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.7683` n `32` status `ready` deltaP `59.0136` edge `0.1706` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0502` n `32` status `ready` deltaP `42.3018` edge `0.0601` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3248` n `32` status `ready` deltaP `27.994` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `2.1755` n `32` status `ready` deltaP `15.625` edge `0.2527` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8609` n `192` status `ready` deltaP `1.3629` edge `0.2468` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.421` n `32` status `ready` deltaP `14.5771` edge `0.1317` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7639` n `32` status `ready` deltaP `9.8241` edge `0.0786` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.483` n `32` status `ready` deltaP `17.8784` edge `-0.0584` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `0.2183` n `192` status `ready` deltaP `-2.7566` edge `0.2898` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.0143` n `192` status `ready` deltaP `19.8023` edge `0.123` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2534` n `32` status `ready` deltaP `8.801` edge `-0.004` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3058` n `192` status `ready` deltaP `0.9107` edge `-0.0007` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.6781` n `192` status `ready` deltaP `-1.7964` edge `0.0001` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.7354` n `192` status `ready` deltaP `2.6042` edge `0.0071` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.8166` n `32` status `ready` deltaP `-3.8922` edge `-0.029` maxDD `-1.6464`
- `market_context_high->crypto_major_1h` score `-0.8786` n `192` status `ready` deltaP `4.6813` edge `0.0329` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8998` n `192` status `ready` deltaP `4.0949` edge `0.0326` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.9156` n `192` status `ready` deltaP `1.3161` edge `-0.0052` maxDD `-2.0564`
- `market_context_high->equity_4h` score `-0.9728` n `192` status `ready` deltaP `0.5335` edge `0.0071` maxDD `-2.671`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
