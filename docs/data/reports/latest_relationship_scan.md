# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T08:52:29.009511+00:00`
- Price records: `672`
- Market context records: `5755`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8664`

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

- `market_context_high->equity_24h` score `0.8045` n `223` status `ready` deltaP `14.9905` edge `0.5111` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1617` n `285` status `ready` deltaP `7.5204` edge `0.1272` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2033` n `292` status `ready` deltaP `3.1253` edge `0.0012` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4419` n `292` status `ready` deltaP `1.7349` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6049` n `292` status `ready` deltaP `3.3878` edge `0.0277` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6406` n `292` status `ready` deltaP `0.1518` edge `0.0037` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.7328` n `292` status `ready` deltaP `3.7671` edge `0.0373` maxDD `-5.5448`
- `market_context_high->commodity_1h` score `-0.7598` n `292` status `ready` deltaP `-1.6488` edge `-0.0057` maxDD `-3.7906`
- `market_context_high->crypto_alt_1h` score `-0.8168` n `292` status `ready` deltaP `2.4198` edge `0.0362` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-0.9457` n `223` status `ready` deltaP `14.0539` edge `0.0434` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1623` n `285` status `ready` deltaP `1.3227` edge `0.0109` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2199` n `285` status `ready` deltaP `3.3189` edge `0.006` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6044` n `285` status `ready` deltaP `-7.0839` edge `-0.0491` maxDD `-11.6719`
- `market_context_high->crypto_major_4h` score `-2.6393` n `285` status `ready` deltaP `8.3692` edge `0.1548` maxDD `-25.1094`
- `market_context_high->index_24h` score `-2.9823` n `223` status `ready` deltaP `0.4982` edge `0.0288` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7297` n `285` status `ready` deltaP `-2.3636` edge `-0.0275` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.7752` n `285` status `ready` deltaP `6.7067` edge `0.1097` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-4.3616` n `223` status `ready` deltaP `7.7137` edge `0.0308` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.8573` n `223` status `ready` deltaP `-10.1785` edge `-0.251` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.8699` n `223` status `ready` deltaP `-13.3011` edge `-0.0865` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
