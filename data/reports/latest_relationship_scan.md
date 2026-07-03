# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T06:37:28.488818+00:00`
- Price records: `672`
- Market context records: `5533`
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

- `market_context_high->equity_24h` score `4.0388` n `189` status `ready` deltaP `14.6495` edge `0.7468` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.6079` n `192` status `ready` deltaP `13.3765` edge `0.3574` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `2.4033` n `189` status `ready` deltaP `16.0797` edge `0.5471` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `2.0111` n `192` status `ready` deltaP `8.9812` edge `0.2718` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.7144` n `192` status `ready` deltaP `9.6799` edge `0.2422` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5082` n `189` status `ready` deltaP `14.0212` edge `0.0416` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.2268` n `192` status `ready` deltaP `7.1888` edge `0.0675` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.019` n `192` status `ready` deltaP `5.1241` edge `0.0136` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2697` n `192` status `ready` deltaP `1.4066` edge `0.0643` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.366` n `192` status `ready` deltaP `0.2932` edge `0.0` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.3796` n `192` status `ready` deltaP `2.9878` edge `0.073` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6036` n `192` status `ready` deltaP `1.1134` edge `0.0098` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.9133` n `192` status `ready` deltaP `1.9944` edge `0.004` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.276` n `192` status `ready` deltaP `3.9888` edge `0.028` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7389` n `192` status `ready` deltaP `-5.6574` edge `-0.0124` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.9015` n `189` status `ready` deltaP `13.426` edge `0.0654` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.5856` n `192` status `ready` deltaP `-11.6362` edge `-0.0521` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7773` n `192` status `ready` deltaP `-10.5945` edge `-0.0613` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.1791` n `189` status `ready` deltaP `7.0437` edge `0.2245` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3875` n `189` status `ready` deltaP `-4.5387` edge `-0.1791` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
