# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T10:22:19.065381+00:00`
- Price records: `672`
- Market context records: `1726`
- Flow alert records: `6875`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8838`

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

- `market_context_high->metal_24h` score `6.7348` n `145` status `ready` deltaP `25.67` edge `0.6327` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.9099` n `196` status `ready` deltaP `20.9713` edge `0.5293` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `5.7587` n `145` status `ready` deltaP `16.8345` edge `0.8997` maxDD `-35.8966`
- `market_context_high->crypto_major_4h` score `4.432` n `196` status `ready` deltaP `23.0245` edge `0.4564` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.0372` n `145` status `ready` deltaP `17.5456` edge `0.3423` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.0665` n `196` status `ready` deltaP `13.7941` edge `0.3907` maxDD `-11.1695`
- `market_context_high->equity_4h` score `3.0201` n `196` status `ready` deltaP `16.2643` edge `0.2527` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8758` n `145` status `ready` deltaP `16.3441` edge `0.5372` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7728` n `196` status `ready` deltaP `7.7203` edge `0.1153` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.5517` n `196` status `ready` deltaP `8.8166` edge `0.0961` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.204` n `196` status `ready` deltaP `4.8974` edge `0.0917` maxDD `-3.9211`
- `market_context_high->crypto_alt_24h` score `0.0856` n `145` status `ready` deltaP `22.5367` edge `1.0378` maxDD `-88.8062`
- `market_context_high->equity_1h` score `0.0251` n `196` status `ready` deltaP `4.6713` edge `0.0518` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.3384` n `196` status `ready` deltaP `11.8343` edge `0.1469` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.3952` n `196` status `ready` deltaP `1.8209` edge `0.0181` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5533` n `196` status `ready` deltaP `5.4962` edge `0.026` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.656` n `196` status `ready` deltaP `-2.9665` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7727` n `145` status `ready` deltaP `5.0722` edge `0.0067` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.8589` n `145` status `ready` deltaP `21.0011` edge `0.647` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-1.4173` n `196` status `ready` deltaP `2.1355` edge `0.0146` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
