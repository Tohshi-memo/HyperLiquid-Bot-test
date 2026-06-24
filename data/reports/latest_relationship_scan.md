# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T05:07:27.447160+00:00`
- Price records: `672`
- Market context records: `4589`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9937`

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

- `market_context_high->unknown_1h` score `69.6415` n `152` status `ready` deltaP `6.3308` edge `5.8113` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.8366` n `152` status `ready` deltaP `8.0633` edge `0.387` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.528` n `152` status `ready` deltaP `1.7097` edge `0.0242` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.6509` n `152` status `ready` deltaP `3.5542` edge `0.0011` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-0.8389` n `152` status `ready` deltaP `-1.6113` edge `-0.0037` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8524` n `152` status `ready` deltaP `2.0539` edge `-0.0107` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.9403` n `152` status `ready` deltaP `-3.2028` edge `-0.0005` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.163` n `152` status `ready` deltaP `4.0276` edge `0.0348` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.426` n `152` status `ready` deltaP `0.69` edge `-0.0105` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.6609` n `152` status `ready` deltaP `-3.8016` edge `-0.0122` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.6065` n `150` status `ready` deltaP `1.7291` edge `-0.1364` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.9161` n `152` status `ready` deltaP `-3.6756` edge `-0.0842` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.836` n `150` status `ready` deltaP `9.9514` edge `0.0557` maxDD `-29.3365`
- `market_context_high->fx_24h` score `-5.3799` n `150` status `ready` deltaP `-12.9445` edge `-0.0108` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.4265` n `152` status `ready` deltaP `-1.7373` edge `-0.1119` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7353` n `152` status `ready` deltaP `-5.7438` edge `-0.1477` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.2501` n `150` status `ready` deltaP `-7.2639` edge `-0.1016` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.059` n `152` status `ready` deltaP `-3.5542` edge `-0.272` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2178` n `152` status `ready` deltaP `-6.6592` edge `-0.3442` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.0553` n `152` status `ready` deltaP `-3.8511` edge `-0.4255` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
