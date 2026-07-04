# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T21:22:26.847989+00:00`
- Price records: `672`
- Market context records: `5705`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8874`

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

- `market_context_high->crypto_major_4h` score `2.0348` n `263` status `ready` deltaP `12.1946` edge `0.2254` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.0845` n `213` status `ready` deltaP `16.6251` edge `0.5361` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.8543` n `263` status `ready` deltaP `9.2999` edge `0.1701` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.1981` n `263` status `ready` deltaP `6.7155` edge `0.1356` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.253` n `275` status `ready` deltaP `2.2139` edge `0.0009` maxDD `-0.5144`
- `market_context_high->crypto_major_1h` score `-0.379` n `275` status `ready` deltaP `3.6473` edge `0.0397` maxDD `-3.9811`
- `market_context_high->metal_1h` score `-0.4435` n `275` status `ready` deltaP `1.6581` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5286` n `275` status `ready` deltaP `1.9793` edge `0.0371` maxDD `-3.8812`
- `market_context_high->equity_1h` score `-0.5733` n `275` status `ready` deltaP `3.6484` edge `0.0286` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6299` n `275` status `ready` deltaP `0.2678` edge `0.0043` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-1.0465` n `213` status `ready` deltaP `11.8104` edge `0.0436` maxDD `-3.52`
- `market_context_high->commodity_1h` score `-1.0823` n `275` status `ready` deltaP `-0.8666` edge `-0.0037` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2357` n `263` status `ready` deltaP `2.8517` edge `0.006` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2863` n `263` status `ready` deltaP `-0.7315` edge `0.0087` maxDD `-3.165`
- `market_context_high->metal_4h` score `-2.6843` n `263` status `ready` deltaP `-8.336` edge `-0.051` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8917` n `213` status `ready` deltaP `2.2032` edge `0.0286` maxDD `-18.121`
- `market_context_high->commodity_4h` score `-3.9355` n `263` status `ready` deltaP `-4.3501` edge `-0.0314` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.2035` n `213` status `ready` deltaP `6.2402` edge `0.0538` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.9765` n `213` status `ready` deltaP `-7.8932` edge `-0.2424` maxDD `-32.5421`
- `market_context_high->commodity_24h` score `-12.0882` n `213` status `ready` deltaP `-10.7639` edge `-0.0747` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
