# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T18:37:22.355107+00:00`
- Price records: `478`
- Market context records: `570`
- Flow alert records: `1609`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.8816` n `145` status `ready` deltaP `7.4255` edge `0.3621` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `2.9118` n `145` status `ready` deltaP `9.7869` edge `0.2108` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0059` n `146` status `ready` deltaP `10.1843` edge `0.02` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2927` n `146` status `ready` deltaP `2.3812` edge `0.0044` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5205` n `146` status `ready` deltaP `2.2005` edge `0.0394` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6583` n `146` status `ready` deltaP `0.5334` edge `-0.0026` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1134` n `146` status `ready` deltaP `-3.4275` edge `-0.0096` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2442` n `146` status `ready` deltaP `-1.8071` edge `-0.0106` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3126` n `146` status `ready` deltaP `4.468` edge `-0.0077` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.7441` n `145` status `ready` deltaP `-5.5246` edge `0.091` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.9169` n `146` status `ready` deltaP `4.1038` edge `-0.0148` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.1129` n `146` status `ready` deltaP `1.0947` edge `-0.0311` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.257` n `146` status `ready` deltaP `2.6537` edge `0.0512` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.1351` n `146` status `ready` deltaP `10.4459` edge `0.0397` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.1789` n `146` status `ready` deltaP `-2.8354` edge `-0.0308` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2529` n `146` status `ready` deltaP `-4.2223` edge `-0.047` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5239` n `146` status `ready` deltaP `-5.7097` edge `0.0945` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.5696` n `145` status `ready` deltaP `-9.7482` edge `0.028` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.5892` n `145` status `ready` deltaP `-5.426` edge `-0.0411` maxDD `-20.5533`
- `market_context_high->unknown_4h` score `-5.3196` n `146` status `ready` deltaP `0.0622` edge `-0.2559` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
