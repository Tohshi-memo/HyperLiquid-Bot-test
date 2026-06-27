# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T12:37:26.107970+00:00`
- Price records: `672`
- Market context records: `4934`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9400`

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

- `market_context_high->unknown_1h` score `17.7092` n `100` status `ready` deltaP `10.2036` edge `1.4495` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.6261` n `100` status `ready` deltaP `29.4085` edge `0.8242` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `7.2552` n `100` status `ready` deltaP `23.5244` edge `0.583` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `7.0875` n `100` status `ready` deltaP `21.2012` edge `0.5717` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `6.0444` n `86` status `ready` deltaP `26.5141` edge `0.3612` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7427` n `100` status `ready` deltaP `15.0854` edge `0.1828` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.378` n `100` status `ready` deltaP `10.1646` edge `0.1133` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.8285` n `100` status `ready` deltaP `10.9817` edge `0.042` maxDD `-0.6938`
- `market_context_high->crypto_major_1h` score `0.6211` n `100` status `ready` deltaP `6.6407` edge `0.1392` maxDD `-5.6406`
- `market_context_high->equity_1h` score `0.4356` n `100` status `ready` deltaP `6.2994` edge `0.0712` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.4293` n `100` status `ready` deltaP `7.3473` edge `0.1083` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.0023` n `100` status `ready` deltaP `3.5389` edge `0.0342` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.3415` n `100` status `ready` deltaP `1.8443` edge `0.0099` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4876` n `100` status `ready` deltaP `0.2515` edge `0.0113` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.9053` n `100` status `ready` deltaP `6.6037` edge `-0.0008` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-0.9889` n `100` status `ready` deltaP `-4.0854` edge `-0.0025` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.4401` n `100` status `ready` deltaP `-8.1078` edge `-0.0047` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.8924` n `86` status `ready` deltaP `-6.0401` edge `-0.0164` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-5.1156` n `86` status `ready` deltaP `12.9724` edge `-0.0019` maxDD `-27.5371`
- `market_context_high->index_24h` score `-7.5737` n `86` status `ready` deltaP `-9.9281` edge `-0.1564` maxDD `-24.6845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
