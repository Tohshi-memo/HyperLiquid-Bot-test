# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T23:22:19.720388+00:00`
- Price records: `672`
- Market context records: `1787`
- Flow alert records: `7041`
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

- `market_context_high->metal_24h` score `7.2337` n `188` status `ready` deltaP `28.487` edge `0.6555` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.1698` n `30` status `ready` deltaP `28.0387` edge `0.3927` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.8224` n `194` status `ready` deltaP `21.7076` edge `0.5171` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.3996` n `194` status `ready` deltaP `22.935` edge `0.4543` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.7563` n `194` status `ready` deltaP `15.9071` edge `0.4341` maxDD `-11.1695`
- `news_risk_high->commodity_1h` score `3.1894` n `30` status `ready` deltaP `24.5709` edge `0.1337` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0419` n `194` status `ready` deltaP `16.6269` edge `0.2521` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.9242` n `188` status `ready` deltaP `15.0636` edge `0.2661` maxDD `-4.1604`
- `market_context_high->equity_24h` score `1.6756` n `188` status `ready` deltaP `15.7912` edge `0.5242` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.124` n `188` status `ready` deltaP `12.9617` edge `0.5393` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.9139` n `194` status `ready` deltaP `12.4591` edge `0.102` maxDD `-3.7119`
- `news_risk_high->fx_4h` score `0.8079` n `30` status `ready` deltaP `20.2643` edge `-0.0043` maxDD `-0.1774`
- `news_risk_high->unknown_4h` score `0.551` n `30` status `ready` deltaP `11.1992` edge `0.0683` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.4194` n `198` status `ready` deltaP `7.0511` edge `0.0991` maxDD `-4.8924`
- `market_context_high->crypto_major_1h` score `0.0726` n `198` status `ready` deltaP `4.4699` edge `0.0836` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0378` n `198` status `ready` deltaP `4.9356` edge `0.0511` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2339` n `198` status `ready` deltaP `3.552` edge `0.02` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.3233` n `194` status `ready` deltaP `12.5597` edge `0.144` maxDD `-12.5349`
- `market_context_high->fx_24h` score `-0.401` n `188` status `ready` deltaP `8.7729` edge `0.013` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.4302` n `30` status `ready` deltaP `17.006` edge `-0.1213` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
