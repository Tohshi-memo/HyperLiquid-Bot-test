# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T15:37:29.696098+00:00`
- Price records: `672`
- Market context records: `4841`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7616`

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

- `market_context_high->unknown_1h` score `13.7449` n `109` status `ready` deltaP `10.2703` edge `1.1187` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.7072` n `97` status `ready` deltaP `24.0382` edge `0.8201` maxDD `-3.0471`
- `market_context_high->unknown_24h` score `4.5844` n `93` status `ready` deltaP `22.2391` edge `0.2722` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `2.9046` n `97` status `ready` deltaP `15.1009` edge `0.2766` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `1.7772` n `97` status `ready` deltaP `11.3182` edge `0.2748` maxDD `-7.1265`
- `market_context_high->metal_4h` score `0.2812` n `97` status `ready` deltaP `10.2794` edge `0.0684` maxDD `-4.7365`
- `market_context_high->index_4h` score `0.1675` n `97` status `ready` deltaP `6.3521` edge `0.0258` maxDD `-0.7334`
- `market_context_high->equity_1h` score `0.063` n `109` status `ready` deltaP `3.0421` edge `0.0494` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.0335` n `97` status `ready` deltaP `8.1893` edge `0.0108` maxDD `-0.788`
- `market_context_high->crypto_alt_1h` score `-0.1285` n `109` status `ready` deltaP `5.6254` edge `0.0551` maxDD `-6.0592`
- `market_context_high->commodity_4h` score `-0.1776` n `97` status `ready` deltaP `11.5712` edge `0.0173` maxDD `-4.377`
- `market_context_high->equity_4h` score `-0.2738` n `97` status `ready` deltaP `8.3778` edge `0.0472` maxDD `-6.3852`
- `market_context_high->commodity_1h` score `-0.3389` n `109` status `ready` deltaP `1.4297` edge `0.013` maxDD `-1.278`
- `market_context_high->crypto_major_1h` score `-0.3612` n `109` status `ready` deltaP `3.5832` edge `0.0688` maxDD `-8.4525`
- `market_context_high->index_1h` score `-0.6298` n `109` status `ready` deltaP `-2.1246` edge `0.0089` maxDD `-0.7054`
- `market_context_high->metal_1h` score `-0.7072` n `109` status `ready` deltaP `0.8309` edge `0.0044` maxDD `-4.7154`
- `market_context_high->fx_1h` score `-1.2649` n `109` status `ready` deltaP `-5.8905` edge `-0.0041` maxDD `-0.6295`
- `market_context_high->fx_24h` score `-1.8494` n `93` status `ready` deltaP `-6.3732` edge `-0.0106` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-3.3539` n `93` status `ready` deltaP `11.7888` edge `0.0023` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.6966` n `93` status `ready` deltaP `-8.3501` edge `-0.1454` maxDD `-24.085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
