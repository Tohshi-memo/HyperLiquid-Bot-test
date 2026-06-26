# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T22:07:30.720435+00:00`
- Price records: `672`
- Market context records: `4870`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7626`

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

- `market_context_high->unknown_1h` score `15.3318` n `110` status `ready` deltaP `10.3212` edge `1.2506` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.7504` n `110` status `ready` deltaP `23.6197` edge `0.7082` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.4388` n `110` status `ready` deltaP `21.2084` edge `0.5304` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.1446` n `110` status `ready` deltaP `18.3398` edge `0.5122` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.2909` n `91` status `ready` deltaP `25.9902` edge `0.3019` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.2912` n `110` status `ready` deltaP `9.7395` edge `0.1089` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8812` n `110` status `ready` deltaP `12.439` edge `0.1682` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5265` n `110` status `ready` deltaP `11.0781` edge `0.0399` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4796` n `110` status `ready` deltaP `6.6195` edge `0.1212` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4316` n `110` status `ready` deltaP `8.1709` edge `0.1031` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2145` n `110` status `ready` deltaP `4.2352` edge `0.059` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1503` n `110` status `ready` deltaP `1.1431` edge `0.0311` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2067` n `110` status `ready` deltaP `3.5819` edge `0.0156` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4876` n `110` status `ready` deltaP `0.3103` edge `0.0109` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6245` n `110` status `ready` deltaP `1.6768` edge `0.0058` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.878` n `110` status `ready` deltaP `6.1197` edge `0.0047` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3741` n `110` status `ready` deltaP `-7.3163` edge `-0.0044` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.8579` n `91` status `ready` deltaP `-6.5095` edge `-0.0104` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.7053` n `91` status `ready` deltaP `-7.3184` edge `-0.1459` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.2125` n `91` status `ready` deltaP `11.8952` edge `-0.0028` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
