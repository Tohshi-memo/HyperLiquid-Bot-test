# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T11:37:26.861022+00:00`
- Price records: `672`
- Market context records: `5553`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11378`

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

- `market_context_high->equity_24h` score `4.5029` n `192` status `ready` deltaP `14.9306` edge `0.7836` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.0842` n `193` status `ready` deltaP `11.7497` edge `0.3246` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.9671` n `192` status `ready` deltaP `16.493` edge `0.508` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `1.5428` n `193` status `ready` deltaP `7.2073` edge `0.2446` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.5091` n `193` status `ready` deltaP `8.0287` edge `0.2361` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.659` n `192` status `ready` deltaP `16.3194` edge `0.0435` maxDD `-1.457`
- `market_context_high->equity_1h` score `0.1677` n `203` status `ready` deltaP `7.1097` edge `0.0631` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0684` n `203` status `ready` deltaP `4.9409` edge `0.0107` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2893` n `203` status `ready` deltaP `1.3864` edge `0.0628` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4031` n `203` status `ready` deltaP `3.1585` edge `0.0699` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.4142` n `203` status `ready` deltaP `2.0044` edge `0.001` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.6647` n `203` status `ready` deltaP `0.5892` edge `0.0082` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7615` n `193` status `ready` deltaP `3.4272` edge `0.0071` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.4904` n `193` status `ready` deltaP `2.2392` edge `0.0218` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7339` n `203` status `ready` deltaP `-5.5153` edge `-0.012` maxDD `-3.6579`
- `market_context_high->index_24h` score `-1.9916` n `192` status `ready` deltaP `12.8472` edge `0.0577` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.4752` n `193` status `ready` deltaP `-11.2316` edge `-0.0456` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7585` n `193` status `ready` deltaP `-10.3153` edge `-0.0616` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.231` n `192` status `ready` deltaP `7.6389` edge `0.2162` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.384` n `192` status `ready` deltaP `-3.6458` edge `-0.1846` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
