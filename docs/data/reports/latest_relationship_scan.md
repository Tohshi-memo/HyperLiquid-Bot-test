# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T01:52:34.193498+00:00`
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

- `news_risk_high->unknown_24h` score `5188.8039` n `60` status `ready` deltaP `33.5413` edge `432.2188` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.6231` n `53` status `ready` deltaP `60.5637` edge `1.1879` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.8165` n `68` status `ready` deltaP `17.1359` edge `0.3635` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7379` n `68` status `ready` deltaP `16.6786` edge `0.0717` maxDD `-0.3783`
- `market_context_high->commodity_24h` score `1.7064` n `53` status `ready` deltaP `27.4844` edge `0.2214` maxDD `-10.2019`
- `market_context_high->crypto_alt_4h` score `0.7649` n `53` status `ready` deltaP `9.805` edge `0.1284` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.7235` n `68` status `ready` deltaP `10.2413` edge `0.0743` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2604` n `53` status `ready` deltaP `14.4731` edge `0.0165` maxDD `-1.3685`
- `market_context_high->fx_24h` score `0.1246` n `53` status `ready` deltaP `10.1795` edge `0.0461` maxDD `-2.506`
- `news_risk_high->metal_4h` score `0.1219` n `68` status `ready` deltaP `5.165` edge `0.0288` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0695` n `68` status `ready` deltaP `6.0321` edge `0.0369` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `0.0227` n `68` status `ready` deltaP `11.2267` edge `0.0228` maxDD `-0.6604`
- `market_context_high->commodity_1h` score `-0.0239` n `53` status `ready` deltaP `4.926` edge `0.0182` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0269` n `53` status `ready` deltaP `7.0529` edge `0.001` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0536` n `68` status `ready` deltaP `2.6154` edge `0.008` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.119` n `68` status `ready` deltaP `1.9197` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1217` n `68` status `ready` deltaP `2.7651` edge `0.0063` maxDD `-0.5599`
- `market_context_high->commodity_4h` score `-0.238` n `53` status `ready` deltaP `3.4198` edge `0.0342` maxDD `-3.0005`
- `news_risk_high->crypto_major_1h` score `-0.2435` n `68` status `ready` deltaP `1.6203` edge `0.03` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.6417` n `53` status `ready` deltaP `-4.5673` edge `0.0109` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
