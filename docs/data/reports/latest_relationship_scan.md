# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T09:52:24.143643+00:00`
- Price records: `672`
- Market context records: `1831`
- Flow alert records: `7169`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4488`

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

- `market_context_high->crypto_alt_4h` score `6.9241` n `192` status `ready` deltaP `22.7515` edge `0.5398` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.6532` n `178` status `ready` deltaP `26.3753` edge `0.6212` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.4703` n `192` status `ready` deltaP `26.3847` edge `0.4879` maxDD `-4.9684`
- `news_risk_high->commodity_4h` score `6.3286` n `30` status `ready` deltaP `28.3435` edge `0.4039` maxDD `-3.5713`
- `market_context_high->unknown_4h` score `4.4297` n `192` status `ready` deltaP `17.0604` edge `0.4578` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.5554` n `178` status `ready` deltaP `17.8683` edge `0.3` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2662` n `30` status `ready` deltaP `24.8703` edge `0.1381` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9999` n `192` status `ready` deltaP `16.8064` edge `0.2474` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.7063` n `178` status `ready` deltaP `14.56` edge `0.6605` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.0876` n `178` status `ready` deltaP `15.5411` edge `0.5602` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `0.8924` n `30` status `ready` deltaP `21.4838` edge `-0.0016` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8302` n `192` status `ready` deltaP `12.0427` edge `0.0978` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3894` n `196` status `ready` deltaP `5.8903` edge `0.0918` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.2726` n `196` status `ready` deltaP `6.2233` edge `0.0926` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.1661` n `30` status `ready` deltaP `7.9979` edge `0.0403` maxDD `-2.7857`
- `market_context_high->crypto_major_24h` score `0.0731` n `178` status `ready` deltaP `18.6857` edge `0.7401` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.0651` n `196` status `ready` deltaP `4.5827` edge `0.0434` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.0833` n `178` status `ready` deltaP `12.1294` edge `0.0171` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.4753` n `30` status `ready` deltaP `16.1078` edge `-0.1211` maxDD `-2.1115`
- `news_risk_high->fx_1h` score `-0.513` n `30` status `ready` deltaP `-5.8782` edge `-0.0004` maxDD `-0.0948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
