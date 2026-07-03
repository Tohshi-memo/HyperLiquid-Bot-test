# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T09:52:29.478156+00:00`
- Price records: `672`
- Market context records: `5546`
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

- `market_context_high->equity_24h` score `4.2713` n `192` status `ready` deltaP `14.9306` edge `0.7643` maxDD `-31.6316`
- `market_context_high->crypto_major_24h` score `2.0823` n `192` status `ready` deltaP `16.493` edge `0.5176` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `1.984` n `192` status `ready` deltaP `11.5473` edge `0.3176` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.4674` n `192` status `ready` deltaP `6.9995` edge `0.2397` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.3893` n `192` status `ready` deltaP `7.8506` edge `0.2273` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5462` n `192` status `ready` deltaP `15.1041` edge `0.0422` maxDD `-1.457`
- `market_context_high->equity_1h` score `0.1102` n `196` status `ready` deltaP `6.4066` edge `0.063` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.1428` n `196` status `ready` deltaP `4.0266` edge `0.0106` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.2993` n `196` status `ready` deltaP `1.442` edge `0.0009` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.4286` n `196` status `ready` deltaP `0.5163` edge `0.057` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.5191` n `196` status `ready` deltaP `2.5785` edge `0.0641` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6302` n `196` status `ready` deltaP `0.8707` edge `0.0092` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7274` n `192` status `ready` deltaP `3.8237` edge `0.0073` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.5173` n `192` status `ready` deltaP `2.0071` edge `0.0211` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7411` n `196` status `ready` deltaP `-5.5511` edge `-0.0131` maxDD `-3.5988`
- `market_context_high->index_24h` score `-1.9737` n `192` status `ready` deltaP `12.8472` edge `0.06` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.5228` n `192` status `ready` deltaP `-11.3313` edge `-0.0489` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7395` n `192` status `ready` deltaP `-10.1372` edge `-0.0612` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.2082` n `192` status `ready` deltaP `7.6389` edge `0.2181` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3037` n `192` status `ready` deltaP `-3.6458` edge `-0.1743` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
