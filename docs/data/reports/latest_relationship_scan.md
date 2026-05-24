# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T19:52:15.349795+00:00`
- Price records: `672`
- Market context records: `1770`
- Flow alert records: `6995`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `7.1654` n `177` status `ready` deltaP `28.3222` edge `0.6509` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.1752` n `194` status `ready` deltaP `21.7076` edge `0.5465` maxDD `-9.1295`
- `news_risk_high->commodity_4h` score `5.8458` n `30` status `ready` deltaP `27.124` edge `0.3718` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `4.7332` n `194` status `ready` deltaP `22.935` edge `0.4821` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.8163` n `177` status `ready` deltaP `18.7294` edge `0.316` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.2251` n `194` status `ready` deltaP `17.2366` edge `0.2633` maxDD `-5.0894`
- `market_context_high->unknown_4h` score `3.2056` n `194` status `ready` deltaP `14.0778` edge `0.4004` maxDD `-11.1695`
- `news_risk_high->commodity_1h` score `3.0875` n `30` status `ready` deltaP `24.1218` edge `0.1282` maxDD `-1.2043`
- `market_context_high->equity_24h` score `2.6986` n `177` status `ready` deltaP `17.164` edge `0.6003` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.5654` n `177` status `ready` deltaP `14.5687` edge `0.6487` maxDD `-35.8966`
- `market_context_high->index_4h` score `1.0525` n `194` status `ready` deltaP `12.9165` edge `0.1105` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.8465` n `194` status `ready` deltaP `7.9804` edge `0.1197` maxDD `-4.1892`
- `news_risk_high->fx_4h` score `0.8174` n `30` status `ready` deltaP `20.4167` edge `-0.0041` maxDD `-0.1774`
- `market_context_high->crypto_major_24h` score `0.4378` n `177` status `ready` deltaP `19.1649` edge `0.7673` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2975` n `194` status `ready` deltaP `5.1207` edge `0.098` maxDD `-3.9211`
- `news_risk_high->unknown_4h` score `0.193` n `30` status `ready` deltaP `9.3699` edge `0.0346` maxDD `-2.7857`
- `market_context_high->equity_1h` score `0.1315` n `194` status `ready` deltaP `5.5513` edge `0.0548` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1532` n `194` status `ready` deltaP `4.3213` edge `0.0216` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1796` n `194` status `ready` deltaP `12.8646` edge `0.1604` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4567` n `30` status `ready` deltaP `16.7066` edge `-0.1227` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
