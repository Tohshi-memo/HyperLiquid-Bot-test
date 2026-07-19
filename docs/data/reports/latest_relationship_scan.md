# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T17:22:29.125028+00:00`
- Price records: `672`
- Market context records: `7272`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13791`

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

- `market_context_high->fx_1h` score `-0.2617` n `139` status `ready` deltaP `2.2177` edge `0.0006` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.7068` n `139` status `ready` deltaP `-2.0741` edge `-0.0147` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.7581` n `139` status `ready` deltaP `-0.9004` edge `0.0127` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.9551` n `139` status `ready` deltaP `1.0791` edge `0.0114` maxDD `-7.6171`
- `market_context_high->fx_4h` score `-0.9879` n `138` status `ready` deltaP `3.6033` edge `0.0093` maxDD `-1.4649`
- `market_context_high->unknown_4h` score `-1.291` n `138` status `ready` deltaP `7.0475` edge `0.0813` maxDD `-6.2026`
- `market_context_high->unknown_1h` score `-1.3101` n `139` status `ready` deltaP `-1.2622` edge `-0.0972` maxDD `-1.3212`
- `market_context_high->index_1h` score `-1.4621` n `139` status `ready` deltaP `-6.7028` edge `-0.0097` maxDD `-2.3963`
- `market_context_high->commodity_4h` score `-1.5005` n `138` status `ready` deltaP `-0.2859` edge `-0.0196` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.1793` n `126` status `ready` deltaP `-1.0711` edge `-0.0947` maxDD `-2.3815`
- `market_context_high->metal_1h` score `-2.2969` n `139` status `ready` deltaP `-10.2572` edge `-0.0071` maxDD `-1.9411`
- `market_context_high->fx_24h` score `-2.3024` n `126` status `ready` deltaP `-7.0021` edge `-0.0099` maxDD `-2.1564`
- `market_context_high->metal_4h` score `-4.2338` n `138` status `ready` deltaP `-12.975` edge `-0.0187` maxDD `-4.809`
- `market_context_high->equity_1h` score `-4.5125` n `139` status `ready` deltaP `-8.861` edge `-0.0643` maxDD `-15.5469`
- `market_context_high->index_4h` score `-5.614` n `138` status `ready` deltaP `-17.4844` edge `-0.063` maxDD `-12.7286`
- `market_context_high->crypto_alt_4h` score `-5.8118` n `138` status `ready` deltaP `-3.5525` edge `-0.0609` maxDD `-23.9784`
- `market_context_high->crypto_major_4h` score `-6.2245` n `138` status `ready` deltaP `-4.3876` edge `-0.0675` maxDD `-25.0898`
- `market_context_high->unknown_24h` score `-6.7619` n `127` status `ready` deltaP `-15.2736` edge `-0.0706` maxDD `-19.2854`
- `market_context_high->metal_24h` score `-13.2886` n `127` status `ready` deltaP `-33.4331` edge `-0.175` maxDD `-31.093`
- `market_context_high->index_24h` score `-16.0799` n `126` status `ready` deltaP `-29.619` edge `-0.2118` maxDD `-44.4587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
