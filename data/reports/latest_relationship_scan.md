# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T20:37:26.276525+00:00`
- Price records: `672`
- Market context records: `5701`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8856`

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

- `market_context_high->crypto_major_4h` score `2.1848` n `260` status `ready` deltaP `12.7345` edge `0.2343` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.1245` n `210` status `ready` deltaP `16.4038` edge `0.5427` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `1.0006` n `260` status `ready` deltaP `10.0633` edge `0.1772` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.2234` n `260` status `ready` deltaP `6.7472` edge `0.1375` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `-0.2087` n `272` status `ready` deltaP `4.0309` edge `0.043` maxDD `-3.9811`
- `market_context_high->fx_1h` score `-0.2733` n `272` status `ready` deltaP `1.8382` edge `0.0008` maxDD `-0.5144`
- `market_context_high->crypto_alt_1h` score `-0.3601` n `272` status `ready` deltaP `2.371` edge `0.0402` maxDD `-3.8812`
- `market_context_high->metal_1h` score `-0.4469` n `272` status `ready` deltaP `1.5939` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5495` n `272` status `ready` deltaP `3.8702` edge `0.0291` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.5975` n `272` status `ready` deltaP `0.8454` edge `0.0046` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.9843` n `210` status `ready` deltaP `12.6488` edge `0.045` maxDD `-3.4411`
- `market_context_high->commodity_1h` score `-1.0834` n `272` status `ready` deltaP `-0.7903` edge `-0.0043` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2009` n `260` status `ready` deltaP `3.4615` edge `0.0064` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.3245` n `260` status `ready` deltaP `-1.2711` edge `0.0074` maxDD `-3.165`
- `market_context_high->metal_4h` score `-2.7224` n `260` status `ready` deltaP `-8.9634` edge `-0.0517` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8835` n `210` status `ready` deltaP `2.4603` edge `0.027` maxDD `-18.0462`
- `market_context_high->crypto_major_24h` score `-3.9249` n `210` status `ready` deltaP `6.5129` edge `0.0752` maxDD `-29.6555`
- `market_context_high->commodity_4h` score `-3.9654` n `260` status `ready` deltaP `-4.395` edge `-0.0336` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.0258` n `210` status `ready` deltaP `-8.631` edge `-0.2438` maxDD `-32.5421`
- `market_context_high->commodity_24h` score `-12.2088` n `210` status `ready` deltaP `-11.7162` edge `-0.0784` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
