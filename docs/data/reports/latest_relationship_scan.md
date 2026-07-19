# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T19:07:26.573904+00:00`
- Price records: `672`
- Market context records: `7281`
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

- `market_context_high->fx_1h` score `-0.1955` n `134` status `ready` deltaP `3.431` edge `0.001` maxDD `-0.5817`
- `market_context_high->crypto_alt_1h` score `-0.7623` n `134` status `ready` deltaP `-1.0412` edge `0.0131` maxDD `-5.9775`
- `market_context_high->fx_4h` score `-0.891` n `131` status `ready` deltaP `4.9723` edge `0.0126` maxDD `-1.4649`
- `market_context_high->crypto_major_1h` score `-0.9375` n `134` status `ready` deltaP `1.4925` edge `0.0109` maxDD `-7.6171`
- `market_context_high->fx_24h` score `-1.1181` n `126` status `ready` deltaP `-2.664` edge `-0.0028` maxDD `-2.1564`
- `market_context_high->unknown_4h` score `-1.1211` n `131` status `ready` deltaP `8.1514` edge `0.0881` maxDD `-6.2026`
- `market_context_high->commodity_1h` score `-1.1316` n `134` status `ready` deltaP `-2.5526` edge `-0.0152` maxDD `-1.9668`
- `market_context_high->unknown_1h` score `-1.2401` n `134` status `ready` deltaP `-0.2905` edge `-0.0947` maxDD `-1.3212`
- `market_context_high->index_1h` score `-1.3742` n `134` status `ready` deltaP `-5.634` edge `-0.0097` maxDD `-2.3805`
- `market_context_high->commodity_4h` score `-1.453` n `131` status `ready` deltaP `-0.2405` edge `-0.0185` maxDD `-2.7453`
- `market_context_high->metal_1h` score `-2.2265` n `134` status `ready` deltaP `-9.3909` edge `-0.0071` maxDD `-1.9332`
- `market_context_high->commodity_24h` score `-2.6032` n `126` status `ready` deltaP `-3.55` edge `-0.1135` maxDD `-2.3815`
- `market_context_high->metal_4h` score `-2.6884` n `131` status `ready` deltaP `-12.152` edge `-0.0181` maxDD `-4.6441`
- `market_context_high->equity_1h` score `-4.5792` n `134` status `ready` deltaP `-9.065` edge `-0.0685` maxDD `-15.5469`
- `market_context_high->crypto_alt_4h` score `-4.9592` n `131` status `ready` deltaP `-2.0725` edge `-0.0482` maxDD `-21.4334`
- `market_context_high->crypto_major_4h` score `-5.5009` n `131` status `ready` deltaP `-2.2168` edge `-0.0542` maxDD `-23.4879`
- `market_context_high->index_4h` score `-5.5033` n `131` status `ready` deltaP `-16.2453` edge `-0.0655` maxDD `-12.4515`
- `market_context_high->unknown_24h` score `-6.2663` n `127` status `ready` deltaP `-12.8185` edge `-0.0616` maxDD `-18.0109`
- `market_context_high->metal_24h` score `-12.4044` n `127` status `ready` deltaP `-31.5918` edge `-0.1505` maxDD `-27.1402`
- `market_context_high->index_24h` score `-14.8833` n `126` status `ready` deltaP `-29.619` edge `-0.1884` maxDD `-40.6868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
