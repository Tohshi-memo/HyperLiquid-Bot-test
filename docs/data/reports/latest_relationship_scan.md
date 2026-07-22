# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T19:23:00.220061+00:00`
- Price records: `672`
- Market context records: `7594`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->commodity_24h` score `0.3294` n `144` status `ready` deltaP `15.2246` edge `0.0843` maxDD `-7.0012`
- `market_context_high->unknown_24h` score `0.305` n `145` status `ready` deltaP `12.1228` edge `0.1113` maxDD `-6.2414`
- `market_context_high->index_1h` score `0.0517` n `150` status `ready` deltaP `6.4865` edge `0.0113` maxDD `-0.8336`
- `market_context_high->commodity_4h` score `-0.03` n `150` status `ready` deltaP `7.9511` edge `0.0205` maxDD `-2.4139`
- `market_context_high->commodity_1h` score `-0.2893` n `150` status `ready` deltaP `4.6967` edge `0.0018` maxDD `-1.5775`
- `market_context_high->fx_24h` score `-0.3082` n `144` status `ready` deltaP `9.5964` edge `0.0191` maxDD `-3.0343`
- `market_context_high->equity_24h` score `-0.3539` n `144` status `ready` deltaP `17.5039` edge `0.5214` maxDD `-49.0105`
- `market_context_high->crypto_major_1h` score `-0.38` n `150` status `ready` deltaP `7.0339` edge `0.0143` maxDD `-5.126`
- `market_context_high->crypto_alt_1h` score `-0.3874` n `150` status `ready` deltaP `1.1158` edge `0.0141` maxDD `-3.3629`
- `market_context_high->equity_1h` score `-0.5479` n `150` status `ready` deltaP `6.1202` edge `0.0518` maxDD `-8.3613`
- `market_context_high->metal_1h` score `-0.648` n `150` status `ready` deltaP `1.2255` edge `0.0133` maxDD `-1.0307`
- `market_context_high->index_4h` score `-0.6695` n `150` status `ready` deltaP `8.6545` edge `0.0291` maxDD `-3.4775`
- `market_context_high->fx_1h` score `-0.6821` n `150` status `ready` deltaP `-0.7807` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->unknown_1h` score `-0.9571` n `150` status `ready` deltaP `-0.0679` edge `-0.0599` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.1336` n `150` status `ready` deltaP `2.0` edge `0.0483` maxDD `-9.8909`
- `market_context_high->crypto_major_4h` score `-1.3707` n `150` status `ready` deltaP `7.5427` edge `0.0578` maxDD `-15.7048`
- `market_context_high->equity_4h` score `-1.6728` n `150` status `ready` deltaP `2.5994` edge `0.2028` maxDD `-21.7674`
- `market_context_high->metal_4h` score `-1.72` n `150` status `ready` deltaP `-2.2845` edge `0.0429` maxDD `-4.8549`
- `market_context_high->metal_24h` score `-2.3033` n `145` status `ready` deltaP `-2.3121` edge `0.1046` maxDD `-10.7584`
- `market_context_high->fx_4h` score `-2.4687` n `150` status `ready` deltaP `-5.0337` edge `-0.0037` maxDD `-2.1439`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
