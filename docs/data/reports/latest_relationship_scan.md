# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T06:07:32.299486+00:00`
- Price records: `672`
- Market context records: `6999`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11539`

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

- `market_context_high->fx_1h` score `-0.2359` n `237` status `ready` deltaP `2.4836` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.2663` n `237` status `ready` deltaP `2.7294` edge `0.0341` maxDD `-4.5815`
- `market_context_high->unknown_24h` score `-0.4209` n `224` status `ready` deltaP `-5.9028` edge `0.4404` maxDD `-18.7342`
- `market_context_high->index_1h` score `-0.639` n `237` status `ready` deltaP `1.1085` edge `0.0018` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6951` n `237` status `ready` deltaP `-1.7907` edge `-0.0004` maxDD `-2.1427`
- `market_context_high->crypto_major_1h` score `-0.9091` n `237` status `ready` deltaP `4.0767` edge `0.0323` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-0.9265` n `237` status `ready` deltaP `12.0877` edge `0.007` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.2095` n `237` status `ready` deltaP `-2.0756` edge `-0.0148` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.331` n `237` status `ready` deltaP `-1.5318` edge `-0.0106` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6678` n `237` status `ready` deltaP `-4.2805` edge `-0.0363` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7546` n `237` status `ready` deltaP `8.1243` edge `-0.0092` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.7988` n `237` status `ready` deltaP `4.0349` edge `-0.0021` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.891` n `237` status `ready` deltaP `6.8527` edge `0.0102` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.6288` n `237` status `ready` deltaP `-5.9715` edge `0.0573` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.6922` n `237` status `ready` deltaP `1.8878` edge `0.0208` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.1967` n `237` status `ready` deltaP `1.5475` edge `0.0083` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.8905` n `224` status `ready` deltaP `-6.4485` edge `-0.0944` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4497` n `224` status `ready` deltaP `-7.3661` edge `-0.017` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.2883` n `237` status `ready` deltaP `5.6878` edge `-0.0506` maxDD `-66.7371`
- `market_context_high->index_24h` score `-11.7517` n `224` status `ready` deltaP `-1.1904` edge `-0.0917` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
