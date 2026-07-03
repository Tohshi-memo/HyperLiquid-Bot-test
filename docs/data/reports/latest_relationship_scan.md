# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T09:37:26.831034+00:00`
- Price records: `672`
- Market context records: `5545`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11375`

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

- `market_context_high->equity_24h` score `4.2365` n `192` status `ready` deltaP `14.9306` edge `0.7614` maxDD `-31.6316`
- `market_context_high->crypto_major_24h` score `2.1051` n `192` status `ready` deltaP `16.493` edge `0.5195` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.001` n `192` status `ready` deltaP `11.6997` edge `0.318` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.4892` n `192` status `ready` deltaP `7.1519` edge `0.2405` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.3929` n `192` status `ready` deltaP `7.8506` edge `0.2276` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5311` n `192` status `ready` deltaP `14.9305` edge `0.0421` maxDD `-1.457`
- `market_context_high->equity_1h` score `0.1115` n `195` status `ready` deltaP `6.3627` edge `0.0634` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.1185` n `195` status `ready` deltaP `4.3145` edge `0.0107` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3128` n `195` status `ready` deltaP `1.1961` edge `0.0008` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.4298` n `195` status `ready` deltaP `0.4253` edge `0.0575` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.5198` n `195` status `ready` deltaP `2.4797` edge `0.0647` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6188` n `195` status `ready` deltaP `0.9827` edge `0.0094` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.742` n `192` status `ready` deltaP `3.6713` edge `0.0071` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.5015` n `192` status `ready` deltaP `2.1595` edge `0.0214` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7359` n `195` status `ready` deltaP `-5.4706` edge `-0.0132` maxDD `-3.5988`
- `market_context_high->index_24h` score `-1.9713` n `192` status `ready` deltaP `12.8472` edge `0.0603` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.524` n `192` status `ready` deltaP `-11.3313` edge `-0.049` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7407` n `192` status `ready` deltaP `-10.1372` edge `-0.0613` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.2082` n `192` status `ready` deltaP `7.6389` edge `0.2181` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2935` n `192` status `ready` deltaP `-3.6458` edge `-0.173` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
