# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T08:52:25.165724+00:00`
- Price records: `672`
- Market context records: `7011`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11541`

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

- `market_context_high->fx_1h` score `-0.279` n `231` status `ready` deltaP `1.7458` edge `0.0011` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.2859` n `218` status `ready` deltaP `-5.5413` edge `0.4553` maxDD `-18.7342`
- `market_context_high->crypto_alt_1h` score `-0.4859` n `231` status `ready` deltaP `2.0168` edge `0.0325` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6226` n `231` status `ready` deltaP `1.4101` edge `0.0019` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6426` n `231` status `ready` deltaP `-1.0052` edge `0.0011` maxDD `-2.1427`
- `market_context_high->crypto_major_1h` score `-0.9604` n `231` status `ready` deltaP `3.9305` edge `0.029` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-0.9949` n `231` status `ready` deltaP `10.8932` edge `0.0062` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.1995` n `231` status `ready` deltaP `-1.9805` edge `-0.0146` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.3368` n `231` status `ready` deltaP `-2.219` edge `-0.0065` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6634` n `231` status `ready` deltaP `-4.0762` edge `-0.0371` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7548` n `231` status `ready` deltaP `8.1493` edge `-0.0094` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.7668` n `231` status `ready` deltaP `4.4242` edge `-0.0006` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.8584` n `231` status `ready` deltaP `7.284` edge `0.0115` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.5152` n `231` status `ready` deltaP `-6.0811` edge `0.0675` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.6787` n `231` status `ready` deltaP `1.9665` edge `0.022` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.2577` n `218` status `ready` deltaP `-4.8389` edge `-0.0875` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.2801` n `218` status `ready` deltaP `-6.2357` edge `-0.016` maxDD `-5.2614`
- `market_context_high->crypto_major_4h` score `-4.8252` n `231` status `ready` deltaP `1.9421` edge `0.0134` maxDD `-24.6094`
- `market_context_high->equity_4h` score `-11.2595` n `231` status `ready` deltaP `5.4178` edge `-0.0527` maxDD `-66.7371`
- `market_context_high->metal_24h` score `-13.3531` n `218` status `ready` deltaP `-9.109` edge `-0.0551` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
