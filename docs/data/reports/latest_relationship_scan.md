# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T18:52:20.301887+00:00`
- Price records: `672`
- Market context records: `1450`
- Flow alert records: `6088`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8808`

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

- `market_context_high->crypto_alt_24h` score `13.1103` n `160` status `ready` deltaP `28.8542` edge `1.1018` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.9873` n `160` status `ready` deltaP `27.5` edge `0.9288` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.7344` n `160` status `ready` deltaP `14.6528` edge `1.0469` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.3818` n `160` status `ready` deltaP `19.7222` edge `0.3423` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.2471` n `160` status `ready` deltaP `12.9167` edge `0.5005` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5958` n `222` status `ready` deltaP `7.4668` edge `0.1662` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.228` n `160` status `ready` deltaP `11.1458` edge `0.0496` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0973` n `228` status `ready` deltaP `3.6743` edge `0.0139` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1094` n `228` status `ready` deltaP `2.1457` edge `0.0366` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.4269` n `222` status `ready` deltaP `10.7216` edge `0.2249` maxDD `-19.5565`
- `market_context_high->fx_1h` score `-0.4677` n `228` status `ready` deltaP `0.8352` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.4754` n `222` status `ready` deltaP `1.0767` edge `0.0621` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.5853` n `228` status `ready` deltaP `1.7991` edge `0.0416` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0312` n `222` status `ready` deltaP `-3.9222` edge `-0.009` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.0825` n `222` status `ready` deltaP `5.6073` edge `0.1433` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.1555` n `228` status `ready` deltaP `4.8587` edge `0.0049` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-1.2021` n `228` status `ready` deltaP `-1.1766` edge `-0.0002` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.6691` n `228` status `ready` deltaP `-1.2606` edge `0.005` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.8703` n `222` status `ready` deltaP `7.7895` edge `0.0614` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-3.3303` n `222` status `ready` deltaP `-11.7049` edge `-0.0585` maxDD `-10.9008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
