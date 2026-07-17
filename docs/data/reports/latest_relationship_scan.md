# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T07:37:26.714507+00:00`
- Price records: `672`
- Market context records: `7006`
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

- `market_context_high->unknown_24h` score `-0.1123` n `223` status `ready` deltaP `-5.1133` edge `0.4747` maxDD `-18.7342`
- `market_context_high->fx_1h` score `-0.2579` n `236` status `ready` deltaP `2.1212` edge `0.0013` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4548` n `236` status `ready` deltaP `2.2404` edge `0.0336` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6563` n `236` status `ready` deltaP `0.8525` edge `0.0013` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6852` n `236` status `ready` deltaP `-1.6137` edge `-0.0003` maxDD `-2.1427`
- `market_context_high->crypto_major_1h` score `-0.9155` n `236` status `ready` deltaP `4.0115` edge `0.0322` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-0.939` n `236` status `ready` deltaP `11.8929` edge `0.0067` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.2182` n `236` status `ready` deltaP `-2.1694` edge `-0.0149` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.2862` n `236` status `ready` deltaP `-1.3169` edge `-0.0083` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6534` n `236` status `ready` deltaP `-4.0642` edge `-0.0359` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7354` n `236` status `ready` deltaP `8.3868` edge `-0.0085` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8363` n `236` status `ready` deltaP `3.6435` edge `-0.0043` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.9099` n `236` status `ready` deltaP `6.5652` edge `0.0097` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.4913` n `236` status `ready` deltaP `-5.3483` edge `0.0646` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.641` n `236` status `ready` deltaP `2.2866` edge `0.0247` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.0883` n `236` status `ready` deltaP `2.253` edge `0.0175` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.7763` n `223` status `ready` deltaP `-6.1862` edge `-0.0945` maxDD `-4.9825`
- `market_context_high->fx_24h` score `-4.4237` n `223` status `ready` deltaP `-7.1819` edge `-0.0169` maxDD `-5.6423`
- `market_context_high->equity_4h` score `-7.2588` n `236` status `ready` deltaP `5.7746` edge `-0.0474` maxDD `-66.7371`
- `market_context_high->index_24h` score `-11.6572` n `223` status `ready` deltaP `-0.4671` edge `-0.0844` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
