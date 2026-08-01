# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T20:37:30.577393+00:00`
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

- `news_risk_high->unknown_24h` score `5189.1113` n `60` status `ready` deltaP `32.3281` edge `432.2525` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.5267` n `53` status `ready` deltaP `56.9242` edge `1.1208` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `5.0358` n `67` status `ready` deltaP `17.5578` edge `0.3748` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.8478` n `67` status `ready` deltaP `17.1005` edge `0.0733` maxDD `-0.3321`
- `market_context_high->commodity_24h` score `1.8154` n `53` status `ready` deltaP `28.0043` edge `0.2319` maxDD `-10.2019`
- `market_context_high->crypto_alt_4h` score `0.7082` n `53` status `ready` deltaP `9.1953` edge `0.1252` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6876` n `68` status `ready` deltaP `9.4928` edge `0.0763` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.247` n `53` status `ready` deltaP `14.3207` edge `0.0158` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1911` n `67` status `ready` deltaP `6.1954` edge `0.0308` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1217` n `68` status `ready` deltaP `6.4812` edge `0.0406` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `0.0683` n `67` status `ready` deltaP `11.8425` edge `0.0225` maxDD `-0.6604`
- `market_context_high->fx_1h` score `0.0091` n `53` status `ready` deltaP `7.502` edge `0.001` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0512` n `68` status `ready` deltaP `2.6154` edge `0.0083` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0957` n `68` status `ready` deltaP `2.3688` edge `0.0042` maxDD `-0.2475`
- `market_context_high->fx_24h` score `-0.0959` n `53` status `ready` deltaP `6.54` edge `0.0421` maxDD `-2.506`
- `market_context_high->commodity_1h` score `-0.1064` n `53` status `ready` deltaP `3.7284` edge `0.0156` maxDD `-1.3282`
- `news_risk_high->metal_1h` score `-0.1341` n `68` status `ready` deltaP `2.4657` edge `0.0067` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1812` n `68` status `ready` deltaP `2.2191` edge `0.034` maxDD `-3.762`
- `market_context_high->commodity_4h` score `-0.2928` n `53` status `ready` deltaP `3.1149` edge `0.0292` maxDD `-3.0005`
- `market_context_high->crypto_alt_1h` score `-0.5895` n `53` status `ready` deltaP `-4.1182` edge `0.0146` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
