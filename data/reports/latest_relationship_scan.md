# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T03:52:39.283430+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_24h` score `37.3875` n `46` status `ready` deltaP `26.2983` edge `2.9446` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `9.8672` n `46` status `ready` deltaP `46.4297` edge `0.5301` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.3273` n `46` status `ready` deltaP `39.1304` edge `0.451` maxDD `-0.434`
- `market_context_high->unknown_4h` score `6.947` n `84` status `ready` deltaP `3.1286` edge `0.6408` maxDD `-2.9526`
- `market_context_high->commodity_4h` score `1.2312` n `84` status `ready` deltaP `15.0189` edge `0.0871` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.5193` n `84` status `ready` deltaP `17.9661` edge `0.0095` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.3008` n `88` status `ready` deltaP `6.2806` edge `0.0248` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.285` n `88` status `ready` deltaP `9.1794` edge `-0.0026` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4102` n `88` status `ready` deltaP `2.4769` edge `-0.0157` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5004` n `88` status `ready` deltaP `-1.0207` edge `-0.0079` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.5766` n `84` status `ready` deltaP `4.5223` edge `0.0194` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-1.2899` n `88` status `ready` deltaP `-3.62` edge `-0.0123` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.4271` n `88` status `ready` deltaP `6.8114` edge `-0.0748` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.4962` n `46` status `ready` deltaP `-2.4909` edge `0.0125` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.7675` n `84` status `ready` deltaP `-8.7543` edge `-0.0428` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.7806` n `84` status `ready` deltaP `1.8003` edge `-0.0214` maxDD `-5.7857`
- `market_context_high->unknown_1h` score `-3.0933` n `88` status `ready` deltaP `3.1982` edge `-0.2344` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6091` n `88` status `ready` deltaP `-12.7994` edge `-0.0781` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.7842` n `46` status `ready` deltaP `-23.4677` edge `-0.1254` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.5353` n `84` status `ready` deltaP `1.5027` edge `-0.3148` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
