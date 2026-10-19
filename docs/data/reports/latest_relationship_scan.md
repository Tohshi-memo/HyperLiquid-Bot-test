# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T15:52:38.770316+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8252`

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

- `market_context_high->commodity_24h` score `2.1012` n `76` status `ready` deltaP `19.0424` edge `0.1333` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.5031` n `43` status `ready` deltaP `14.0475` edge `0.0061` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5031` n `43` status `ready` deltaP `14.0475` edge `0.0061` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4399` n `43` status `ready` deltaP `10.1553` edge `-0.0007` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4399` n `43` status `ready` deltaP `10.1553` edge `-0.0007` maxDD `-0.4273`
- `risk_on_high->commodity_24h` score `0.2504` n `43` status `ready` deltaP `14.4219` edge `0.0045` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2504` n `43` status `ready` deltaP `14.4219` edge `0.0045` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `-0.0281` n `78` status `ready` deltaP `2.3139` edge `0.3225` maxDD `-15.3224`
- `market_context_high->crypto_major_1h` score `-0.1315` n `88` status `ready` deltaP `2.5381` edge `0.0679` maxDD `-4.8007`
- `risk_on_high->fx_4h` score `-0.1531` n `43` status `ready` deltaP `1.1628` edge `0.0059` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1531` n `43` status `ready` deltaP `1.1628` edge `0.0059` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2566` n `43` status `ready` deltaP `0.4143` edge `-0.001` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2566` n `43` status `ready` deltaP `0.4143` edge `-0.001` maxDD `-0.1065`
- `market_context_high->index_1h` score `-0.2965` n `88` status `ready` deltaP `4.3413` edge `-0.0002` maxDD `-1.0073`
- `market_context_high->crypto_major_24h` score `-0.334` n `76` status `ready` deltaP `-2.0742` edge `0.5807` maxDD `-35.1086`
- `market_context_high->metal_1h` score `-0.4182` n `88` status `ready` deltaP `-2.6878` edge `0.0018` maxDD `-0.6669`
- `market_context_high->fx_4h` score `-0.5355` n `78` status `ready` deltaP `-1.2821` edge `0.0036` maxDD `-0.7635`
- `market_context_high->metal_4h` score `-0.6312` n `78` status `ready` deltaP `-0.9499` edge `0.0484` maxDD `-0.8388`
- `risk_on_high->index_4h` score `-0.651` n `43` status `ready` deltaP `4.4774` edge `0.0026` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.651` n `43` status `ready` deltaP `4.4774` edge `0.0026` maxDD `-0.9359`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
