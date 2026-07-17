# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T05:37:25.838780+00:00`
- Price records: `672`
- Market context records: `6997`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11735`

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

- `market_context_high->fx_1h` score `-0.2266` n `237` status `ready` deltaP `2.6333` edge `0.0019` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.2928` n `237` status `ready` deltaP `2.5797` edge `0.0317` maxDD `-4.5815`
- `market_context_high->unknown_24h` score `-0.5684` n `224` status `ready` deltaP `-6.25` edge `0.4238` maxDD `-18.7342`
- `market_context_high->index_1h` score `-0.6305` n `237` status `ready` deltaP `1.2582` edge `0.0019` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.678` n `237` status `ready` deltaP `-1.4913` edge `-0.0002` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9163` n `237` status `ready` deltaP `12.2401` edge `0.0073` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-0.9655` n `237` status `ready` deltaP `3.7773` edge `0.0296` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2155` n `237` status `ready` deltaP `-2.0756` edge `-0.0153` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.3274` n `237` status `ready` deltaP `-1.5318` edge `-0.0103` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6709` n `237` status `ready` deltaP `-4.2805` edge `-0.0367` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7561` n `237` status `ready` deltaP `8.1243` edge `-0.0094` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8042` n `237` status `ready` deltaP `4.0349` edge `-0.0028` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.8871` n `237` status `ready` deltaP `6.8527` edge `0.0107` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.6746` n `237` status `ready` deltaP `-6.124` edge `0.0545` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.7244` n `237` status `ready` deltaP `1.583` edge `0.0187` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.2391` n `237` status `ready` deltaP `1.2427` edge `0.0049` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.8857` n `224` status `ready` deltaP `-6.4485` edge `-0.094` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4485` n `224` status `ready` deltaP `-7.3661` edge `-0.0169` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.3` n `237` status `ready` deltaP `5.6878` edge `-0.0521` maxDD `-66.7371`
- `market_context_high->index_24h` score `-11.7916` n `224` status `ready` deltaP `-1.5377` edge `-0.0945` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
