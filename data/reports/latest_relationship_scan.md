# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T04:25:52.159859+00:00`
- Price records: `672`
- Market context records: `6355`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.0124` n `32` status `ready` deltaP `41.6667` edge `0.988` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.184` n `32` status `ready` deltaP `51.2153` edge `0.1739` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4584` n `32` status `ready` deltaP `17.7083` edge `0.5315` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.09` n `32` status `ready` deltaP `42.4543` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.7367` n `32` status `ready` deltaP `32.4653` edge `0.1155` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3512` n `32` status `ready` deltaP `28.2934` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4897` n `32` status `ready` deltaP `14.5771` edge `0.1405` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8769` n `32` status `ready` deltaP `11.1714` edge `0.0841` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.7066` n `200` status `ready` deltaP `14.4207` edge `0.0424` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.0142` n `212` status `ready` deltaP `-7.5161` edge `0.1521` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.0119` n `200` status `ready` deltaP `6.9634` edge `0.0222` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `-0.5743` n `129` status `ready` deltaP `-4.6229` edge `0.1436` maxDD `-6.2457`
- `market_context_high->metal_1h` score `-0.5976` n `212` status `ready` deltaP `3.8047` edge `0.0026` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.6372` n `212` status `ready` deltaP `-1.8416` edge `-0.0011` maxDD `-2.1314`
- `market_context_high->metal_24h` score `-0.6709` n `129` status `ready` deltaP `14.3895` edge `0.0749` maxDD `-11.8809`
- `news_risk_high->unknown_1h` score `-0.7011` n `32` status `ready` deltaP `5.6325` edge `-0.0615` maxDD `-0.7581`
- `news_risk_high->index_24h` score `-0.7027` n `32` status `ready` deltaP `0.5208` edge `-0.0064` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.7408` n `212` status `ready` deltaP `-0.9519` edge `-0.002` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7808` n `32` status `ready` deltaP `-3.7425` edge `-0.0254` maxDD `-1.6464`
- `market_context_high->unknown_4h` score `-0.8754` n `200` status `ready` deltaP `-12.8902` edge `0.2311` maxDD `-11.925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
