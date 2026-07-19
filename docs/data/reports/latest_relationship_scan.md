# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T18:52:21.531940+00:00`
- Price records: `672`
- Market context records: `7280`
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

- `market_context_high->fx_1h` score `-0.1855` n `135` status `ready` deltaP `3.6236` edge `0.001` maxDD `-0.5817`
- `market_context_high->crypto_alt_1h` score `-0.7328` n `135` status `ready` deltaP `-0.6543` edge `0.0143` maxDD `-5.9775`
- `market_context_high->fx_4h` score `-0.9051` n `132` status `ready` deltaP `4.7609` edge `0.0122` maxDD `-1.4649`
- `market_context_high->crypto_major_1h` score `-0.9071` n `135` status `ready` deltaP `1.8519` edge `0.0124` maxDD `-7.6171`
- `market_context_high->unknown_4h` score `-1.105` n `132` status `ready` deltaP `8.398` edge `0.0878` maxDD `-6.2026`
- `market_context_high->commodity_1h` score `-1.1661` n `135` status `ready` deltaP `-2.923` edge `-0.0156` maxDD `-1.9668`
- `market_context_high->unknown_1h` score `-1.2629` n `135` status `ready` deltaP `-0.6387` edge `-0.0953` maxDD `-1.3212`
- `market_context_high->index_1h` score `-1.3967` n `135` status `ready` deltaP `-5.9159` edge `-0.0097` maxDD `-2.3805`
- `market_context_high->commodity_4h` score `-1.5217` n `132` status `ready` deltaP `-0.6742` edge `-0.0196` maxDD `-2.8836`
- `market_context_high->fx_24h` score `-1.7805` n `126` status `ready` deltaP `-3.2836` edge `-0.0037` maxDD `-2.1564`
- `market_context_high->metal_1h` score `-2.235` n `135` status `ready` deltaP `-9.5121` edge `-0.007` maxDD `-1.9334`
- `market_context_high->commodity_24h` score `-2.4936` n `126` status `ready` deltaP `-2.9303` edge `-0.1085` maxDD `-2.3815`
- `market_context_high->metal_4h` score `-4.1517` n `132` status `ready` deltaP `-12.2136` edge `-0.019` maxDD `-4.6441`
- `market_context_high->equity_1h` score `-4.5223` n `135` status `ready` deltaP `-8.5786` edge `-0.067` maxDD `-15.5469`
- `market_context_high->crypto_alt_4h` score `-5.1635` n `132` status `ready` deltaP `-2.379` edge `-0.0529` maxDD `-22.2556`
- `market_context_high->index_4h` score `-5.5369` n `132` status `ready` deltaP `-16.4304` edge `-0.0657` maxDD `-12.5604`
- `market_context_high->crypto_major_4h` score `-5.5851` n `132` status `ready` deltaP `-2.5638` edge `-0.0589` maxDD `-23.4879`
- `market_context_high->unknown_24h` score `-6.3856` n `127` status `ready` deltaP `-13.4323` edge `-0.0639` maxDD `-18.2951`
- `market_context_high->metal_24h` score `-12.5925` n `127` status `ready` deltaP `-32.2056` edge `-0.1544` maxDD `-27.7549`
- `market_context_high->index_24h` score `-15.0665` n `126` status `ready` deltaP `-29.619` edge `-0.1921` maxDD `-41.2788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
