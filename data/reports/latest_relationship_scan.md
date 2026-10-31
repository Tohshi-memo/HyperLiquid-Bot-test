# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T07:22:26.111612+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7633`

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

- `market_context_high->unknown_24h` score `1616.0651` n `133` status `ready` deltaP `-4.9695` edge `134.7482` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `112.3841` n `98` status `ready` deltaP `-5.1936` edge `9.4286` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `37.6262` n `133` status `ready` deltaP `2.2063` edge `3.1341` maxDD `-0.3966`
- `market_context_high->equity_24h` score `8.3871` n `133` status `ready` deltaP `20.6754` edge `0.8368` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `7.1721` n `92` status `ready` deltaP `23.3629` edge `0.508` maxDD `-3.6198`
- `market_context_high->index_24h` score `4.195` n `133` status `ready` deltaP `40.1093` edge `0.1005` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.9164` n `98` status `ready` deltaP `8.2457` edge `0.1043` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.4275` n `133` status `ready` deltaP `11.0418` edge `0.0148` maxDD `-0.3549`
- `market_context_high->commodity_4h` score `0.3633` n `133` status `ready` deltaP `14.4084` edge `0.0561` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.3019` n `133` status `ready` deltaP `14.4393` edge `0.0316` maxDD `-1.7988`
- `market_context_high->equity_1h` score `0.1846` n `133` status `ready` deltaP `3.9823` edge `0.0764` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.009` n `133` status `ready` deltaP `7.1429` edge `0.0544` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1031` n `133` status `ready` deltaP `3.5399` edge `-0.001` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.1088` n `133` status `ready` deltaP `1.1072` edge `0.1371` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.213` n `133` status `ready` deltaP `2.7711` edge `0.0152` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.477` n `133` status `ready` deltaP `0.2235` edge `-0.0028` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.4978` n `133` status `ready` deltaP `4.2567` edge `0.1725` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.7251` n `133` status `ready` deltaP `-0.8217` edge `0.0009` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8562` n `98` status `ready` deltaP `1.8636` edge `-0.0038` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.9187` n `98` status `ready` deltaP `-6.4493` edge `-0.0047` maxDD `-0.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
