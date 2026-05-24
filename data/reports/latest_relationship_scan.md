# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T21:52:15.952092+00:00`
- Price records: `672`
- Market context records: `1780`
- Flow alert records: `7021`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8882`

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

- `market_context_high->metal_24h` score `7.0813` n `182` status `ready` deltaP `27.9609` edge `0.6463` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.9592` n `194` status `ready` deltaP `21.7076` edge `0.5285` maxDD `-9.1295`
- `news_risk_high->commodity_4h` score `5.907` n `30` status `ready` deltaP `27.124` edge `0.3769` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `4.5748` n `194` status `ready` deltaP `22.935` edge `0.4689` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.555` n `194` status `ready` deltaP `15.1449` edge `0.4224` maxDD `-11.1695`
- `market_context_high->index_24h` score `3.3727` n `182` status `ready` deltaP `16.9948` edge `0.2906` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.0827` n `194` status `ready` deltaP `16.6269` edge `0.2555` maxDD `-5.0894`
- `news_risk_high->commodity_1h` score `3.0372` n `30` status `ready` deltaP `23.6727` edge `0.127` maxDD `-1.2043`
- `market_context_high->equity_24h` score `2.182` n `182` status `ready` deltaP `16.2718` edge `0.5632` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.8005` n `182` status `ready` deltaP `13.2879` edge `0.5935` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.9535` n `194` status `ready` deltaP `12.4591` edge `0.1053` maxDD `-3.7119`
- `news_risk_high->fx_4h` score `0.8071` n `30` status `ready` deltaP `20.2643` edge `-0.0044` maxDD `-0.1774`
- `market_context_high->crypto_alt_1h` score `0.7569` n `196` status `ready` deltaP `8.1083` edge `0.1137` maxDD `-4.3742`
- `news_risk_high->unknown_4h` score `0.4201` n `30` status `ready` deltaP `10.437` edge `0.0566` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `0.2723` n `196` status `ready` deltaP `5.2854` edge `0.0948` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0837` n `196` status `ready` deltaP `5.209` edge `0.0531` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.115` n `196` status `ready` deltaP `4.7538` edge `0.0219` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1486` n `194` status `ready` deltaP `13.4743` edge `0.1603` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4255` n `30` status `ready` deltaP `17.1557` edge `-0.1217` maxDD `-2.1115`
- `market_context_high->fx_24h` score `-0.4501` n `182` status `ready` deltaP `8.3695` edge `0.0116` maxDD `-1.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
