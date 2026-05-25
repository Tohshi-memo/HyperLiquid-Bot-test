# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T07:07:16.922046+00:00`
- Price records: `672`
- Market context records: `1820`
- Flow alert records: `7136`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4474`

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

- `market_context_high->crypto_alt_4h` score `6.9032` n `185` status `ready` deltaP `22.4745` edge `0.5399` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8728` n `178` status `ready` deltaP `27.5905` edge `0.6314` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.5653` n `30` status `ready` deltaP `29.563` edge `0.4155` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `6.4954` n `185` status `ready` deltaP `26.3834` edge `0.49` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.6657` n `185` status `ready` deltaP `17.2355` edge `0.4763` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6346` n `178` status `ready` deltaP `17.8683` edge `0.3066` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2674` n `30` status `ready` deltaP `24.8703` edge `0.1382` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0082` n `185` status `ready` deltaP `15.9196` edge `0.254` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.5943` n `178` status `ready` deltaP `17.4508` edge `0.5897` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.4905` n `178` status `ready` deltaP `13.6919` edge `0.6483` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9058` n `30` status `ready` deltaP `21.6362` edge `-0.0009` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8369` n `185` status `ready` deltaP `11.7057` edge `0.1006` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4398` n `192` status `ready` deltaP `6.1596` edge `0.0942` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.3543` n `192` status `ready` deltaP `6.5245` edge `0.0974` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.3044` n `30` status `ready` deltaP `9.2174` edge `0.0499` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.1132` n `192` status `ready` deltaP `4.2665` edge `0.0415` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.1853` n `178` status `ready` deltaP `17.9912` edge `0.7232` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.2351` n `178` status `ready` deltaP `11.0877` edge `0.0114` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.3978` n `192` status `ready` deltaP `0.0406` edge `0.0119` maxDD `-1.7205`
- `news_risk_high->unknown_1h` score `-0.4115` n `30` status `ready` deltaP `16.8563` edge `-0.1179` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
