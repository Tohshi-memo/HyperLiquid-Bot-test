# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T08:45:26.540923+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4814`

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

- `market_context_high->unknown_1h` score `340.8179` n `50` status `ready` deltaP `10.2754` edge `28.3379` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.4701` n `50` status `ready` deltaP `8.8415` edge `23.8969` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.615` n `67` status `ready` deltaP `39.5496` edge `0.9752` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.8539` n `50` status `ready` deltaP `36.1667` edge `0.805` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `9.9103` n `67` status `ready` deltaP `36.5309` edge `0.6308` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `8.9817` n `50` status `ready` deltaP `16.5347` edge `0.8092` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9709` n `50` status `ready` deltaP `17.5427` edge `0.5343` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9409` n `50` status `ready` deltaP `15.5793` edge `0.4372` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.3483` n `96` status `ready` deltaP `16.4126` edge `0.3873` maxDD `-6.4152`
- `market_context_high->fx_4h` score `2.9347` n `50` status `ready` deltaP `32.8415` edge `0.0391` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8965` n `50` status `ready` deltaP `13.9042` edge `0.215` maxDD `-3.6387`
- `market_context_high->equity_24h` score `2.8674` n `50` status `ready` deltaP `13.4861` edge `0.4639` maxDD `-11.8957`
- `market_context_high->crypto_major_1h` score `2.862` n `50` status `ready` deltaP `14.0` edge `0.1902` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `2.3644` n `96` status `ready` deltaP `23.4502` edge `0.1103` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.4651` n `50` status `ready` deltaP `20.491` edge `0.0119` maxDD `-0.113`
- `news_risk_high->crypto_major_24h` score `1.2466` n `67` status `ready` deltaP `6.4055` edge `0.4325` maxDD `-15.8971`
- `news_risk_high->crypto_alt_1h` score `1.0228` n `108` status `ready` deltaP `6.2375` edge `0.0999` maxDD `-2.4998`
- `market_context_high->index_24h` score `0.9908` n `50` status `ready` deltaP `16.0069` edge `0.0774` maxDD `-1.2338`
- `news_risk_high->metal_24h` score `0.9379` n `67` status `ready` deltaP `7.8358` edge `0.1954` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.6699` n `96` status `ready` deltaP `8.9177` edge `0.2574` maxDD `-10.477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
