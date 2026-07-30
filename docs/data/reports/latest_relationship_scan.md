# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T15:22:37.428762+00:00`
- Price records: `672`
- Market context records: `8422`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5742`

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

- `news_risk_high->unknown_24h` score `6253.0042` n `52` status `ready` deltaP `41.4396` edge `520.8495` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8216` n `52` status `ready` deltaP `23.7805` edge `0.3863` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.2875` n `52` status `ready` deltaP `19.1847` edge `0.0936` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1811` n `52` status `ready` deltaP `18.9024` edge `0.0748` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5536` n `52` status `ready` deltaP `12.31` edge `0.0908` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.3641` n `52` status `ready` deltaP `5.5582` edge `0.2072` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.3592` n `52` status `ready` deltaP `9.9148` edge `0.0869` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.0933` n `52` status `ready` deltaP `14.5873` edge `0.1821` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.2033` n `52` status `ready` deltaP `3.3654` edge `0.0413` maxDD `-0.7433`
- `news_risk_high->fx_1h` score `0.1335` n `52` status `ready` deltaP `6.0917` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0347` n `52` status `ready` deltaP `2.7983` edge `0.0131` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.3978` n `52` status `ready` deltaP `0.7025` edge `0.0025` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4292` n `52` status `ready` deltaP `4.6553` edge `0.0097` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9333` n `52` status `ready` deltaP `-6.322` edge `-0.0404` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7421` n `52` status `ready` deltaP `-27.7244` edge `-0.0615` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.3099` n `52` status `ready` deltaP `-25.4456` edge `-0.1921` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.5779` n `52` status `ready` deltaP `-34.3616` edge `-0.2087` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.4866` n `52` status `ready` deltaP `-12.086` edge `-0.366` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.5663` n `52` status `ready` deltaP `-26.5091` edge `-0.3202` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.5842` n `52` status `ready` deltaP `-24.5994` edge `-1.0138` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
