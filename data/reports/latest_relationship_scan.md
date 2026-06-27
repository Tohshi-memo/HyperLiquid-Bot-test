# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T14:52:29.064744+00:00`
- Price records: `672`
- Market context records: `4944`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9456`

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

- `market_context_high->unknown_1h` score `19.1844` n `96` status `ready` deltaP `10.4042` edge `1.5711` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.1966` n `94` status `ready` deltaP `28.2596` edge `0.8794` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.2655` n `94` status `ready` deltaP `20.9814` edge `0.588` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.0317` n `94` status `ready` deltaP `21.5848` edge `0.5773` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8471` n `89` status `ready` deltaP `26.8668` edge `0.3424` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7749` n `94` status `ready` deltaP `14.7379` edge `0.1878` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.6487` n `94` status `ready` deltaP `12.633` edge `0.1194` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.9859` n `94` status `ready` deltaP `12.62` edge `0.0442` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.7988` n `96` status `ready` deltaP `7.142` edge `0.0763` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.7986` n `96` status `ready` deltaP `8.2086` edge `0.1515` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.6108` n `96` status `ready` deltaP `9.0818` edge `0.12` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.1206` n `96` status `ready` deltaP `4.7904` edge `0.0361` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.3803` n `96` status `ready` deltaP `1.5032` edge `0.0072` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4382` n `96` status `ready` deltaP `1.0354` edge `0.0124` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.9531` n `94` status `ready` deltaP `6.5613` edge `-0.0045` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.1207` n `94` status `ready` deltaP `-6.3797` edge `-0.0041` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.4997` n `89` status `ready` deltaP `-1.5215` edge `-0.0138` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.6349` n `96` status `ready` deltaP `-10.3917` edge `-0.0057` maxDD `-0.5675`
- `market_context_high->commodity_24h` score `-4.2815` n `89` status `ready` deltaP `18.4632` edge `0.031` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-7.0308` n `89` status `ready` deltaP `-9.6325` edge `0.0238` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
