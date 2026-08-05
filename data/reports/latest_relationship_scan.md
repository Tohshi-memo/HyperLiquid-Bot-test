# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T00:37:25.788840+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11823`

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

- `market_context_high->unknown_24h` score `15.8348` n `87` status `ready` deltaP `17.0798` edge `1.21` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.5621` n `90` status `ready` deltaP `1.7479` edge `0.5514` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.649` n `90` status `ready` deltaP `17.8422` edge `0.1031` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.4174` n `87` status `ready` deltaP `3.0831` edge `0.278` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.0666` n `87` status `ready` deltaP `25.8321` edge `0.0851` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3109` n `90` status `ready` deltaP `5.9414` edge `0.0279` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1135` n `90` status `ready` deltaP `7.1557` edge `-0.0034` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0601` n `90` status `ready` deltaP `13.0048` edge `0.007` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.541` n `90` status `ready` deltaP `-1.6068` edge `-0.0092` maxDD `-1.6224`
- `market_context_high->crypto_alt_24h` score `-0.5459` n `87` status `ready` deltaP `7.142` edge `0.0267` maxDD `-4.5445`
- `market_context_high->index_1h` score `-0.5853` n `90` status `ready` deltaP `-0.4557` edge `-0.0186` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.6863` n `90` status `ready` deltaP `3.6416` edge `0.0112` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.7047` n `90` status `ready` deltaP `-2.0093` edge `-0.0059` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.0889` n `90` status `ready` deltaP `3.0284` edge `-0.0208` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.6133` n `87` status `ready` deltaP `-4.8372` edge `0.0449` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.6993` n `90` status `ready` deltaP `4.0519` edge `-0.0913` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0827` n `90` status `ready` deltaP `-12.1307` edge `-0.0607` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.3241` n `90` status `ready` deltaP `-10.9614` edge `-0.0666` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4108` n `90` status `ready` deltaP `2.0492` edge `-0.2532` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-7.0699` n `87` status `ready` deltaP `3.8972` edge `-0.1577` maxDD `-48.3072`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
