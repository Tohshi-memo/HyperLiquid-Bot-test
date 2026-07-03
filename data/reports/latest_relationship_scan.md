# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T10:37:27.051768+00:00`
- Price records: `672`
- Market context records: `5549`
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

- `market_context_high->equity_24h` score `4.3709` n `192` status `ready` deltaP `14.9306` edge `0.7726` maxDD `-31.6316`
- `market_context_high->crypto_major_24h` score `2.0283` n `192` status `ready` deltaP `16.493` edge `0.5131` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.0116` n `192` status `ready` deltaP `11.5473` edge `0.3199` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.4722` n `192` status `ready` deltaP `6.9995` edge `0.2401` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.4445` n `192` status `ready` deltaP `7.8506` edge `0.2319` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.595` n `192` status `ready` deltaP `15.625` edge `0.0428` maxDD `-1.457`
- `market_context_high->equity_1h` score `0.1593` n `199` status `ready` deltaP `6.9758` edge `0.0633` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0874` n `199` status `ready` deltaP `4.6881` edge `0.0108` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.4103` n `199` status `ready` deltaP `0.7748` edge `0.0568` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4415` n `199` status `ready` deltaP `1.6625` edge `0.001` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.532` n `199` status `ready` deltaP `2.5073` edge `0.0635` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5957` n `199` status `ready` deltaP `1.2563` edge `0.0095` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7262` n `192` status `ready` deltaP `3.8237` edge `0.0074` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.5113` n `192` status `ready` deltaP `2.0071` edge `0.0216` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7606` n `199` status `ready` deltaP `-5.7789` edge `-0.0127` maxDD `-3.6391`
- `market_context_high->index_24h` score `-1.9815` n `192` status `ready` deltaP `12.8472` edge `0.059` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.5036` n `192` status `ready` deltaP `-11.3313` edge `-0.0473` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7347` n `192` status `ready` deltaP `-10.1372` edge `-0.0608` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.2118` n `192` status `ready` deltaP `7.6389` edge `0.2178` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3349` n `192` status `ready` deltaP `-3.6458` edge `-0.1783` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
