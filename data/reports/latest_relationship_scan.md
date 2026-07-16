# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T14:52:27.050338+00:00`
- Price records: `672`
- Market context records: `6928`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->fx_1h` score `-0.1886` n `226` status `ready` deltaP `3.2735` edge `0.0025` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3814` n `226` status `ready` deltaP `3.2007` edge `0.0233` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4818` n `226` status `ready` deltaP `4.3718` edge `0.0211` maxDD `-4.2314`
- `market_context_high->unknown_24h` score `-0.5314` n `209` status `ready` deltaP `-5.9696` edge `0.3733` maxDD `-14.4643`
- `market_context_high->index_1h` score `-0.7017` n `226` status `ready` deltaP `0.1894` edge `-0.0001` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7508` n `226` status `ready` deltaP `-2.7251` edge `-0.0013` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.7972` n `224` status `ready` deltaP `14.1551` edge `0.0098` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.0273` n `226` status `ready` deltaP `-1.191` edge `-0.0092` maxDD `-2.1443`
- `market_context_high->unknown_1h` score `-1.5047` n `226` status `ready` deltaP `-1.8733` edge `-0.0228` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.5869` n `224` status `ready` deltaP `-3.8655` edge `-0.0287` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.6107` n `226` status `ready` deltaP `3.5729` edge `-0.0123` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.6876` n `224` status `ready` deltaP `8.0575` edge `-0.0121` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-1.9356` n `224` status `ready` deltaP `5.2156` edge `0.0154` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.7453` n `224` status `ready` deltaP `1.753` edge `-0.0053` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7752` n `224` status `ready` deltaP `-0.0871` edge `-0.0225` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9719` n `224` status `ready` deltaP `-7.6655` edge `0.04` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.0906` n `209` status `ready` deltaP `-2.7489` edge `-0.0524` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.0743` n `209` status `ready` deltaP `-4.3345` edge `-0.007` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.6294` n `224` status `ready` deltaP `5.4552` edge `-0.0918` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.6421` n `209` status `ready` deltaP `-12.4004` edge `-0.1158` maxDD `-32.4262`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
