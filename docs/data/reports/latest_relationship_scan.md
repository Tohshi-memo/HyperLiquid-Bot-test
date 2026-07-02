# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T21:07:29.715355+00:00`
- Price records: `672`
- Market context records: `5493`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->crypto_major_24h` score `3.2508` n `190` status `ready` deltaP `16.2189` edge `0.6168` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.9284` n `193` status `ready` deltaP `13.3641` edge `0.3188` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `2.6843` n `193` status `ready` deltaP `14.646` edge `0.3553` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.3279` n `193` status `ready` deltaP `11.1707` edge `0.2836` maxDD `-9.46`
- `market_context_high->equity_24h` score `1.9917` n `190` status `ready` deltaP `10.7511` edge `0.6022` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.5855` n `193` status `ready` deltaP `9.0325` edge `0.0851` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2367` n `190` status `ready` deltaP `11.5424` edge `0.0355` maxDD `-1.0847`
- `market_context_high->index_1h` score `0.2194` n `193` status `ready` deltaP `7.4439` edge `0.018` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2448` n `193` status `ready` deltaP `1.5831` edge `0.0652` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3626` n `193` status `ready` deltaP `0.3281` edge `0.0002` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.402` n `193` status `ready` deltaP `3.0227` edge `0.0709` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.4445` n `193` status `ready` deltaP `2.562` edge `0.0134` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.6738` n `193` status `ready` deltaP `8.276` edge `0.0496` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.8054` n `193` status `ready` deltaP `3.6712` edge `0.0065` maxDD `-1.5143`
- `market_context_high->commodity_1h` score `-1.5482` n `193` status `ready` deltaP `-3.7247` edge `-0.0094` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.7702` n `190` status `ready` deltaP `14.2708` edge `0.0766` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.7222` n `193` status `ready` deltaP `-9.0365` edge `-0.0363` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3924` n `193` status `ready` deltaP `-7.2665` edge `-0.0503` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.1558` n `190` status `ready` deltaP `7.2442` edge `0.2251` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2424` n `190` status `ready` deltaP `-4.2379` edge `-0.1625` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
