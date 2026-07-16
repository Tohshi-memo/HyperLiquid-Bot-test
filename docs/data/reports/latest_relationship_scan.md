# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T16:07:33.060853+00:00`
- Price records: `672`
- Market context records: `6934`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `market_context_high->fx_1h` score `-0.2347` n `231` status `ready` deltaP `2.462` edge `0.002` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4155` n `231` status `ready` deltaP `2.9837` edge `0.0219` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.5717` n `231` status `ready` deltaP `3.716` edge `0.019` maxDD `-4.313`
- `market_context_high->metal_1h` score `-0.6963` n `231` status `ready` deltaP `-1.9034` edge `0.0002` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7067` n `231` status `ready` deltaP `0.0466` edge `0.0002` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.8218` n `224` status `ready` deltaP `13.6978` edge `0.0097` maxDD `-2.1765`
- `market_context_high->unknown_24h` score `-0.9008` n `214` status `ready` deltaP `-7.0652` edge `0.3478` maxDD `-15.6283`
- `market_context_high->commodity_1h` score `-1.1454` n `231` status `ready` deltaP `-1.9805` edge `-0.0134` maxDD `-2.1742`
- `market_context_high->unknown_1h` score `-1.5555` n `231` status `ready` deltaP `-1.9682` edge `-0.0264` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.5986` n `224` status `ready` deltaP `-3.8655` edge `-0.0302` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.6545` n `224` status `ready` deltaP `8.5149` edge `-0.0109` maxDD `-11.3047`
- `market_context_high->equity_1h` score `-1.6924` n `231` status `ready` deltaP `3.0608` edge `-0.0143` maxDD `-13.5134`
- `market_context_high->metal_4h` score `-1.9214` n `224` status `ready` deltaP `5.368` edge `0.0162` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.7601` n `224` status `ready` deltaP `1.753` edge `-0.0072` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7761` n `224` status `ready` deltaP `-0.2396` edge `-0.0216` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9827` n `224` status `ready` deltaP `-7.6655` edge `0.0391` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.2789` n `214` status `ready` deltaP `-3.603` edge `-0.0624` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.1782` n `214` status `ready` deltaP `-5.3629` edge `-0.0088` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.4884` n `224` status `ready` deltaP `6.2173` edge `-0.0788` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.8102` n `214` status `ready` deltaP `-12.9538` edge `-0.1177` maxDD `-33.7026`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
