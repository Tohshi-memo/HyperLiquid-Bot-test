# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T11:07:28.760367+00:00`
- Price records: `672`
- Market context records: `5551`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11377`

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

- `market_context_high->equity_24h` score `4.4357` n `192` status `ready` deltaP `14.9306` edge `0.778` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.0128` n `192` status `ready` deltaP `11.5473` edge `0.32` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.9923` n `192` status `ready` deltaP `16.493` edge `0.5101` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `1.4698` n `192` status `ready` deltaP `6.9995` edge `0.2399` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.4637` n `192` status `ready` deltaP `7.8506` edge `0.2335` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.6276` n `192` status `ready` deltaP `15.9722` edge `0.0432` maxDD `-1.457`
- `market_context_high->equity_1h` score `0.1686` n `201` status `ready` deltaP `7.0464` edge `0.0636` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.077` n `201` status `ready` deltaP `4.8187` edge `0.0108` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.3626` n `201` status `ready` deltaP `0.9355` edge `0.0597` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4275` n `201` status `ready` deltaP `1.8381` edge `0.001` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.472` n `201` status `ready` deltaP `2.6879` edge `0.0673` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6461` n `201` status `ready` deltaP `0.7463` edge `0.0087` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.753` n `192` status `ready` deltaP `3.5188` edge `0.0072` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.5101` n `192` status `ready` deltaP `2.0071` edge `0.0217` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7408` n `201` status `ready` deltaP `-5.5717` edge `-0.0122` maxDD `-3.6579`
- `market_context_high->index_24h` score `-1.9861` n `192` status `ready` deltaP `12.8472` edge `0.0584` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.4794` n `192` status `ready` deltaP `-11.1789` edge `-0.0463` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7371` n `192` status `ready` deltaP `-10.1372` edge `-0.061` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.2214` n `192` status `ready` deltaP `7.6389` edge `0.217` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3598` n `192` status `ready` deltaP `-3.6458` edge `-0.1815` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
