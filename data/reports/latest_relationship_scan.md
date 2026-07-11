# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T15:37:29.724472+00:00`
- Price records: `672`
- Market context records: `6405`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11093`

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

- `news_risk_high->crypto_alt_24h` score `13.3864` n `32` status `ready` deltaP `34.7222` edge `0.8988` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6871` n `32` status `ready` deltaP `56.4236` edge `0.1811` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.2862` n `32` status `ready` deltaP `36.9792` edge `0.1312` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1132` n `32` status `ready` deltaP `42.7591` edge `0.0623` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0547` n `32` status `ready` deltaP `16.3194` edge `0.489` maxDD `-4.2368`
- `market_context_high->unknown_24h` score `2.7957` n `146` status `ready` deltaP `9.57` edge `0.4992` maxDD `-15.0689`
- `news_risk_high->fx_1h` score `2.4458` n `32` status `ready` deltaP `29.491` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.439` n `32` status `ready` deltaP `13.8286` edge `0.139` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8247` n `32` status `ready` deltaP `10.1235` edge `0.0844` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.4966` n `213` status `ready` deltaP `-5.8959` edge `0.1815` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3864` n `213` status `ready` deltaP `11.2826` edge `0.0408` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0336` n `213` status `ready` deltaP `7.3557` edge `0.0214` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2489` n `32` status `ready` deltaP `6.5307` edge `-0.0298` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3329` n `146` status `ready` deltaP `19.6205` edge `0.0983` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4751` n `213` status `ready` deltaP `2.1534` edge `0.0025` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5186` n `213` status `ready` deltaP `8.0084` edge `0.05` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.629` n `32` status `ready` deltaP `-0.8982` edge `-0.0249` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.6961` n `213` status `ready` deltaP `-0.4386` edge `-0.0017` maxDD `-0.9376`
- `market_context_high->index_1h` score `-0.7123` n `213` status `ready` deltaP `-3.3103` edge `0.0027` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.7305` n `213` status `ready` deltaP `-3.351` edge `-0.003` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
