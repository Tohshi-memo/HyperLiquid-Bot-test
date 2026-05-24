# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T20:52:15.519061+00:00`
- Price records: `672`
- Market context records: `1775`
- Flow alert records: `7008`
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

- `market_context_high->metal_24h` score `7.2169` n `179` status `ready` deltaP `28.6662` edge `0.6529` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.0444` n `194` status `ready` deltaP `21.7076` edge `0.5356` maxDD `-9.1295`
- `news_risk_high->commodity_4h` score `5.8506` n `30` status `ready` deltaP `27.124` edge `0.3722` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `4.6468` n `194` status `ready` deltaP `22.935` edge `0.4749` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.6748` n `179` status `ready` deltaP `18.3853` edge `0.3065` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.3262` n `194` status `ready` deltaP `14.5351` edge `0.4074` maxDD `-11.1695`
- `market_context_high->equity_4h` score `3.1659` n `194` status `ready` deltaP `16.9317` edge `0.2604` maxDD `-5.0894`
- `news_risk_high->commodity_1h` score `3.0563` n `30` status `ready` deltaP `23.8224` edge `0.1276` maxDD `-1.2043`
- `market_context_high->equity_24h` score `2.4876` n `179` status `ready` deltaP `16.6715` edge `0.586` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.2463` n `179` status `ready` deltaP `14.0004` edge `0.6259` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.9871` n `194` status `ready` deltaP `12.4591` edge `0.1081` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.8968` n `194` status `ready` deltaP `8.2798` edge `0.1219` maxDD `-4.1892`
- `news_risk_high->fx_4h` score `0.8079` n `30` status `ready` deltaP `20.2643` edge `-0.0043` maxDD `-0.1774`
- `market_context_high->crypto_major_1h` score `0.3454` n `194` status `ready` deltaP `5.4201` edge `0.1` maxDD `-3.9211`
- `news_risk_high->unknown_4h` score `0.2714` n `30` status `ready` deltaP `9.8272` edge `0.0416` maxDD `-2.7857`
- `market_context_high->crypto_major_24h` score `0.1525` n `179` status `ready` deltaP `18.8082` edge `0.7459` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.1315` n `194` status `ready` deltaP `5.5513` edge `0.0548` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1124` n `194` status `ready` deltaP `4.7704` edge `0.022` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1221` n `194` status `ready` deltaP `13.4743` edge `0.1637` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4614` n `30` status `ready` deltaP `16.7066` edge `-0.1233` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
