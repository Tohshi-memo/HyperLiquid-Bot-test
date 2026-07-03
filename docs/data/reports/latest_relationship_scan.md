# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T06:22:26.835722+00:00`
- Price records: `672`
- Market context records: `5532`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11416`

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

- `market_context_high->equity_24h` score `4.0112` n `189` status `ready` deltaP `14.6495` edge `0.7445` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.6417` n `192` status `ready` deltaP `13.529` edge `0.3592` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `2.4441` n `189` status `ready` deltaP `16.0797` edge `0.5505` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `2.0317` n `192` status `ready` deltaP `9.1336` edge `0.2725` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.7434` n `192` status `ready` deltaP `9.8323` edge `0.2436` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.4883` n `189` status `ready` deltaP `13.8476` edge `0.0411` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.222` n `192` status `ready` deltaP `7.1888` edge `0.0671` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.019` n `192` status `ready` deltaP `5.1241` edge `0.0136` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2877` n `192` status `ready` deltaP `1.4066` edge `0.0628` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3761` n `192` status `ready` deltaP `0.1435` edge `-0.0003` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.4143` n `192` status `ready` deltaP `2.8381` edge `0.0711` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6203` n `192` status `ready` deltaP `0.9637` edge `0.0094` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.9279` n `192` status `ready` deltaP `1.842` edge `0.0038` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.253` n `192` status `ready` deltaP `4.1412` edge `0.0289` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7245` n `192` status `ready` deltaP `-5.5077` edge `-0.0122` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8854` n `189` status `ready` deltaP `13.5996` edge `0.0663` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.6074` n `192` status `ready` deltaP `-11.7887` edge `-0.0529` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7591` n `192` status `ready` deltaP `-10.4421` edge `-0.0608` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.1647` n `189` status `ready` deltaP `7.0437` edge `0.2257` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3836` n `189` status `ready` deltaP `-4.5387` edge `-0.1786` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
