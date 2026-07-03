# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T10:52:30.264475+00:00`
- Price records: `672`
- Market context records: `5550`
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

- `market_context_high->equity_24h` score `4.4033` n `192` status `ready` deltaP `14.9306` edge `0.7753` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.014` n `192` status `ready` deltaP `11.5473` edge `0.3201` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `2.0127` n `192` status `ready` deltaP `16.493` edge `0.5118` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `1.4722` n `192` status `ready` deltaP `6.9995` edge `0.2401` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.4577` n `192` status `ready` deltaP `7.8506` edge `0.233` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.6113` n `192` status `ready` deltaP `15.7986` edge `0.043` maxDD `-1.457`
- `market_context_high->equity_1h` score `0.1658` n `200` status `ready` deltaP `7.012` edge `0.0636` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0821` n `200` status `ready` deltaP `4.7545` edge `0.0108` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.387` n `200` status `ready` deltaP `0.8563` edge `0.0582` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4344` n `200` status `ready` deltaP `1.7515` edge `0.001` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.5007` n `200` status `ready` deltaP `2.5988` edge `0.0655` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.621` n `200` status `ready` deltaP `1.0` edge `0.0091` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7396` n `192` status `ready` deltaP `3.6713` edge `0.0073` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.5113` n `192` status `ready` deltaP `2.0071` edge `0.0216` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7655` n `200` status `ready` deltaP `-5.8503` edge `-0.0124` maxDD `-3.6579`
- `market_context_high->index_24h` score `-1.9838` n `192` status `ready` deltaP `12.8472` edge `0.0587` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.4964` n `192` status `ready` deltaP `-11.3313` edge `-0.0467` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7347` n `192` status `ready` deltaP `-10.1372` edge `-0.0608` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.213` n `192` status `ready` deltaP `7.6389` edge `0.2177` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3466` n `192` status `ready` deltaP `-3.6458` edge `-0.1798` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
