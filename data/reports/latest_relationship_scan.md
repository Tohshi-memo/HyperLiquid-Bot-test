# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T09:22:37.821996+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7653`

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

- `market_context_high->unknown_24h` score `1824.6019` n `126` status `ready` deltaP `-5.6796` edge `152.131` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `97.8211` n `98` status `ready` deltaP `-5.9422` edge `8.22` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `30.4496` n `126` status `ready` deltaP `1.9139` edge `2.538` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `18.6138` n `31` status `ready` deltaP `49.2048` edge `1.2279` maxDD `-0.049`
- `market_context_high->equity_24h` score `9.2368` n `126` status `ready` deltaP `22.8671` edge `0.893` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.2096` n `98` status `ready` deltaP `18.7905` edge `0.4475` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.3716` n `126` status `ready` deltaP `40.997` edge `0.1093` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.9495` n `126` status `ready` deltaP `13.8509` edge `0.0158` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.9056` n `98` status `ready` deltaP `8.096` edge `0.1044` maxDD `-3.9659`
- `market_context_high->equity_1h` score `0.4832` n `126` status `ready` deltaP `6.4989` edge `0.0845` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.4779` n `126` status `ready` deltaP `10.0181` edge `0.0758` maxDD `-5.2213`
- `market_context_high->metal_4h` score `0.4766` n `126` status `ready` deltaP `17.3926` edge `0.0327` maxDD `-1.671`
- `market_context_high->commodity_4h` score `0.2289` n `126` status `ready` deltaP `12.9985` edge `0.0543` maxDD `-1.0837`
- `market_context_high->equity_4h` score `-0.0044` n `126` status `ready` deltaP `2.26` edge `0.1428` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0496` n `126` status `ready` deltaP `4.5528` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2803` n `126` status `ready` deltaP `1.9009` edge `0.0154` maxDD `-0.4475`
- `market_context_high->metal_24h` score `-0.3103` n `126` status `ready` deltaP `6.7212` edge `0.1801` maxDD `-10.5088`
- `market_context_high->fx_4h` score `-0.4859` n `126` status `ready` deltaP `0.0315` edge `-0.0028` maxDD `-0.4433`
- `market_context_high->index_1h` score `-0.5192` n `126` status `ready` deltaP `1.6776` edge `0.0014` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.7502` n `126` status `ready` deltaP `3.7877` edge `0.0561` maxDD `-7.536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
