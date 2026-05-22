# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T14:22:17.110471+00:00`
- Price records: `672`
- Market context records: `1534`
- Flow alert records: `6329`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8802`

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

- `market_context_high->metal_24h` score `13.0646` n `174` status `ready` deltaP `23.635` edge `1.0312` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.7885` n `174` status `ready` deltaP `28.8315` edge `0.9918` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.2447` n `174` status `ready` deltaP `28.4423` edge `0.7773` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.9857` n `174` status `ready` deltaP `20.4262` edge `0.3046` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7287` n `174` status `ready` deltaP `13.7213` edge `0.3686` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.8334` n `174` status `ready` deltaP `17.858` edge `0.0553` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1665` n `199` status `ready` deltaP `4.0239` edge `0.0965` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.5712` n `199` status `ready` deltaP `10.9679` edge `0.1856` maxDD `-19.5565`
- `market_context_high->crypto_alt_1h` score `-0.5819` n `199` status `ready` deltaP `-0.3799` edge `0.0303` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.5907` n `199` status `ready` deltaP `-1.3954` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_major_4h` score `-0.612` n `199` status `ready` deltaP `6.993` edge `0.1458` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-0.7594` n `199` status `ready` deltaP `4.8484` edge `0.0039` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7644` n `199` status `ready` deltaP `-0.1241` edge `0.0003` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.771` n `199` status `ready` deltaP `-0.7966` edge `-0.0014` maxDD `-4.7041`
- `market_context_high->equity_1h` score `-0.9015` n `199` status `ready` deltaP `-1.7813` edge `0.0176` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.0953` n `199` status `ready` deltaP `-1.7911` edge `0.0072` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.2771` n `199` status `ready` deltaP `-8.7204` edge `-0.0127` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.3802` n `199` status `ready` deltaP `-4.5923` edge `0.0245` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.6065` n `199` status `ready` deltaP `8.6867` edge `0.0774` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.3804` n `199` status `ready` deltaP `-16.5293` edge `-0.1169` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
