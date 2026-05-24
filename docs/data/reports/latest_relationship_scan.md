# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T20:22:18.263779+00:00`
- Price records: `672`
- Market context records: `1773`
- Flow alert records: `7002`
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

- `market_context_high->metal_24h` score `7.1574` n `179` status `ready` deltaP `28.4926` edge `0.6491` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.12` n `194` status `ready` deltaP `21.7076` edge `0.5419` maxDD `-9.1295`
- `news_risk_high->commodity_4h` score `5.8422` n `30` status `ready` deltaP `27.124` edge `0.3715` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `4.6948` n `194` status `ready` deltaP `22.935` edge `0.4789` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.7067` n `179` status `ready` deltaP `18.5589` edge `0.308` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.2418` n `194` status `ready` deltaP `14.2302` edge `0.4024` maxDD `-11.1695`
- `market_context_high->equity_4h` score `3.2215` n `194` status `ready` deltaP `17.2366` edge `0.263` maxDD `-5.0894`
- `news_risk_high->commodity_1h` score `3.0875` n `30` status `ready` deltaP `24.1218` edge `0.1282` maxDD `-1.2043`
- `market_context_high->equity_24h` score `2.5922` n `179` status `ready` deltaP `17.0187` edge `0.5924` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.2897` n `179` status `ready` deltaP `14.3476` edge `0.6272` maxDD `-35.8966`
- `market_context_high->index_4h` score `1.0209` n `194` status `ready` deltaP `12.6116` edge `0.1099` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.8692` n `194` status `ready` deltaP `8.1301` edge `0.1206` maxDD `-4.1892`
- `news_risk_high->fx_4h` score `0.8087` n `30` status `ready` deltaP `20.2643` edge `-0.0042` maxDD `-0.1774`
- `market_context_high->crypto_major_1h` score `0.3179` n `194` status `ready` deltaP `5.2704` edge `0.0987` maxDD `-3.9211`
- `market_context_high->crypto_major_24h` score `0.2515` n `179` status `ready` deltaP `18.9818` edge `0.753` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `0.2165` n `30` status `ready` deltaP `9.5223` edge `0.0366` maxDD `-2.7857`
- `market_context_high->equity_1h` score `0.1327` n `194` status `ready` deltaP `5.5513` edge `0.0549` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1268` n `194` status `ready` deltaP `4.6207` edge `0.0218` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1473` n `194` status `ready` deltaP `13.1695` edge `0.1625` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4621` n `30` status `ready` deltaP `16.7066` edge `-0.1234` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
