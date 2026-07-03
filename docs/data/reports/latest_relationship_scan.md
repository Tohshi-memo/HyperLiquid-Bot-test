# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T05:37:26.825509+00:00`
- Price records: `672`
- Market context records: `5529`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11432`

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

- `market_context_high->equity_24h` score `3.8941` n `189` status `ready` deltaP `14.4759` edge `0.7359` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.6659` n `192` status `ready` deltaP `13.6814` edge `0.3602` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `2.5581` n `189` status `ready` deltaP `16.0797` edge `0.56` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `2.0209` n `192` status `ready` deltaP `9.1336` edge `0.2716` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.7784` n `192` status `ready` deltaP `9.9848` edge `0.2455` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.4521` n `189` status `ready` deltaP `13.5004` edge `0.0404` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.186` n `192` status `ready` deltaP `7.0391` edge `0.0651` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0345` n `192` status `ready` deltaP `4.9744` edge `0.0133` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.3201` n `192` status `ready` deltaP `1.4066` edge `0.0601` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3777` n `192` status `ready` deltaP `0.1435` edge `-0.0005` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.4443` n `192` status `ready` deltaP `2.8381` edge `0.0686` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6791` n `192` status `ready` deltaP `0.5146` edge `0.0075` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.9291` n `192` status `ready` deltaP `1.842` edge `0.0037` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.19` n `192` status `ready` deltaP `4.5985` edge `0.0311` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.6814` n `192` status `ready` deltaP `-5.0586` edge `-0.0116` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8419` n `189` status `ready` deltaP `14.1204` edge `0.0684` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.6665` n `192` status `ready` deltaP `-12.0935` edge `-0.0558` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.6961` n `192` status `ready` deltaP `-9.9848` edge `-0.0586` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.1455` n `189` status `ready` deltaP `7.0437` edge `0.2273` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3813` n `189` status `ready` deltaP `-4.5387` edge `-0.1783` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
