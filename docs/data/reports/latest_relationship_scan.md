# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T19:07:28.049836+00:00`
- Price records: `672`
- Market context records: `6845`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `1.0208` n `176` status `ready` deltaP `-1.5467` edge `0.5164` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `-0.169` n `176` status `ready` deltaP `7.9704` edge `0.1196` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2482` n `220` status `ready` deltaP `2.2618` edge `0.0016` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5676` n `220` status `ready` deltaP `2.0278` edge `0.0156` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.575` n `220` status `ready` deltaP `3.9957` edge `0.0156` maxDD `-4.2122`
- `market_context_high->commodity_1h` score `-0.673` n `220` status `ready` deltaP `-2.1012` edge `-0.0038` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.9032` n `220` status `ready` deltaP `-3.0267` edge `-0.0045` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9939` n `220` status `ready` deltaP `-6.0806` edge `-0.0101` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0265` n `210` status `ready` deltaP `10.421` edge `0.0053` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.5232` n `210` status `ready` deltaP `-4.4396` edge `-0.0167` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7075` n `220` status `ready` deltaP `-3.6581` edge `-0.0278` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-2.0181` n `220` status `ready` deltaP `-0.5716` edge `-0.0369` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.1961` n `210` status `ready` deltaP `1.2936` edge `-0.0322` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.6519` n `210` status `ready` deltaP `-2.664` edge `-0.0239` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9843` n `210` status `ready` deltaP `-0.1931` edge `-0.0486` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1651` n `210` status `ready` deltaP `-0.4399` edge `-0.0445` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2696` n `210` status `ready` deltaP `-9.6167` edge `0.0282` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4792` n `176` status `ready` deltaP `-9.7853` edge `-0.0044` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.9728` n `210` status `ready` deltaP `-1.8104` edge `-0.2156` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.1872` n `176` status `ready` deltaP `-18.8447` edge `-0.2037` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
