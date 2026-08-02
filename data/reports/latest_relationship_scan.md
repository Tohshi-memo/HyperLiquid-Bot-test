# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T01:37:24.193621+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5188.7889` n `60` status `ready` deltaP `33.368` edge `432.2187` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.572` n `53` status `ready` deltaP `60.3904` edge `1.1848` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.8165` n `68` status `ready` deltaP `17.1359` edge `0.3635` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7379` n `68` status `ready` deltaP `16.6786` edge `0.0717` maxDD `-0.3783`
- `market_context_high->commodity_24h` score `1.7072` n `53` status `ready` deltaP `27.4844` edge `0.2215` maxDD `-10.2019`
- `market_context_high->crypto_alt_4h` score `0.7641` n `53` status `ready` deltaP `9.805` edge `0.1283` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.7091` n `68` status `ready` deltaP `10.0916` edge `0.0741` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2517` n `53` status `ready` deltaP `14.3207` edge `0.0164` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1219` n `68` status `ready` deltaP `5.165` edge `0.0288` maxDD `-0.8085`
- `market_context_high->fx_24h` score `0.1132` n `53` status `ready` deltaP `10.0062` edge `0.0458` maxDD `-2.506`
- `news_risk_high->crypto_alt_1h` score `0.0726` n `68` status `ready` deltaP `6.0321` edge `0.0373` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `0.0093` n `68` status `ready` deltaP `11.0743` edge `0.0227` maxDD `-0.6604`
- `market_context_high->commodity_1h` score `-0.0348` n `53` status `ready` deltaP `4.7763` edge `0.0178` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0389` n `53` status `ready` deltaP `6.9032` edge `0.001` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0536` n `68` status `ready` deltaP `2.6154` edge `0.008` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.1217` n `68` status `ready` deltaP `2.7651` edge `0.0063` maxDD `-0.5599`
- `news_risk_high->fx_1h` score `-0.1268` n `68` status `ready` deltaP `1.77` edge `0.0042` maxDD `-0.2475`
- `market_context_high->commodity_4h` score `-0.2403` n `53` status `ready` deltaP `3.4198` edge `0.0339` maxDD `-3.0005`
- `news_risk_high->crypto_major_1h` score `-0.2412` n `68` status `ready` deltaP `1.6203` edge `0.0303` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.6386` n `53` status `ready` deltaP `-4.5673` edge `0.0113` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
