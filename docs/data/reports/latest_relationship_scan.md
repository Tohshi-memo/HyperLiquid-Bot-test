# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T20:37:20.609669+00:00`
- Price records: `672`
- Market context records: `1774`
- Flow alert records: `7005`
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

- `market_context_high->metal_24h` score `7.1766` n `179` status `ready` deltaP `28.4926` edge `0.6507` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.0756` n `194` status `ready` deltaP `21.7076` edge `0.5382` maxDD `-9.1295`
- `news_risk_high->commodity_4h` score `5.8458` n `30` status `ready` deltaP `27.124` edge `0.3718` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `4.6648` n `194` status `ready` deltaP `22.935` edge `0.4764` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.6832` n `179` status `ready` deltaP `18.3853` edge `0.3072` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.2816` n `194` status `ready` deltaP `14.3827` edge `0.4047` maxDD `-11.1695`
- `market_context_high->equity_4h` score `3.1925` n `194` status `ready` deltaP `17.0842` edge `0.2616` maxDD `-5.0894`
- `news_risk_high->commodity_1h` score `3.0719` n `30` status `ready` deltaP `23.9721` edge `0.1279` maxDD `-1.2043`
- `market_context_high->equity_24h` score `2.5363` n `179` status `ready` deltaP `16.8451` edge `0.5889` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.265` n `179` status `ready` deltaP `14.174` edge `0.6263` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.9967` n `194` status `ready` deltaP `12.4591` edge `0.1089` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.8704` n `194` status `ready` deltaP `8.1301` edge `0.1207` maxDD `-4.1892`
- `news_risk_high->fx_4h` score `0.8079` n `30` status `ready` deltaP `20.2643` edge `-0.0043` maxDD `-0.1774`
- `market_context_high->crypto_major_1h` score `0.3191` n `194` status `ready` deltaP `5.2704` edge `0.0988` maxDD `-3.9211`
- `news_risk_high->unknown_4h` score `0.2424` n `30` status `ready` deltaP `9.6748` edge `0.0389` maxDD `-2.7857`
- `market_context_high->crypto_major_24h` score `0.1825` n `179` status `ready` deltaP `18.8082` edge `0.7484` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.1183` n `194` status `ready` deltaP `5.4016` edge `0.0547` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1256` n `194` status `ready` deltaP `4.6207` edge `0.0219` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1332` n `194` status `ready` deltaP `13.3219` edge `0.1633` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4731` n `30` status `ready` deltaP `16.5569` edge `-0.1238` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
