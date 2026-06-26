# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T21:22:29.066544+00:00`
- Price records: `672`
- Market context records: `4867`
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

- `market_context_high->unknown_1h` score `15.3294` n `110` status `ready` deltaP `10.3212` edge `1.2504` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.748` n `110` status `ready` deltaP `23.6197` edge `0.708` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.3554` n `110` status `ready` deltaP `20.7511` edge `0.5265` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.06` n `110` status `ready` deltaP `17.8825` edge `0.5082` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.232` n `91` status `ready` deltaP `25.6429` edge `0.2993` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3034` n `110` status `ready` deltaP `9.8919` edge `0.1089` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.845` n `110` status `ready` deltaP `11.9817` edge `0.1666` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4949` n `110` status `ready` deltaP `10.6208` edge `0.0389` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4749` n `110` status `ready` deltaP `6.6195` edge `0.1206` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4269` n `110` status `ready` deltaP `8.1709` edge `0.1025` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2145` n `110` status `ready` deltaP `4.2352` edge `0.059` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1573` n `110` status `ready` deltaP `0.9934` edge `0.0312` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2043` n `110` status `ready` deltaP `3.5819` edge `0.0159` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4868` n `110` status `ready` deltaP `0.3103` edge `0.011` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6237` n `110` status `ready` deltaP `1.6768` edge `0.0059` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.827` n `110` status `ready` deltaP `6.577` edge `0.0059` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3729` n `110` status `ready` deltaP `-7.3163` edge `-0.0043` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.8639` n `91` status `ready` deltaP `-6.5095` edge `-0.0109` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.7496` n `91` status `ready` deltaP `-7.8393` edge `-0.1481` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.2782` n `91` status `ready` deltaP `11.3743` edge `-0.0048` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
