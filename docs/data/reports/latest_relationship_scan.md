# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T20:37:25.510077+00:00`
- Price records: `672`
- Market context records: `6427`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `12.1366` n `32` status `ready` deltaP `31.25` edge `0.8178` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.4237` n `146` status `ready` deltaP `19.2851` edge `0.8201` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.5683` n `32` status `ready` deltaP `55.2083` edge `0.1793` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1607` n `32` status `ready` deltaP `43.3689` edge `0.0622` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1125` n `32` status `ready` deltaP `35.2431` edge `0.1283` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.5013` n `32` status `ready` deltaP `12.8472` edge `0.4412` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4721` n `32` status `ready` deltaP `29.7904` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5108` n `32` status `ready` deltaP `14.2777` edge `0.1452` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `0.9546` n `199` status `ready` deltaP `-6.5169` edge `0.2131` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8544` n `32` status `ready` deltaP `9.9738` edge `0.0892` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.2302` n `194` status `ready` deltaP `9.9101` edge `0.0411` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.2057` n `194` status `ready` deltaP `9.2217` edge `0.0233` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.1974` n `32` status `ready` deltaP `7.1295` edge `-0.0295` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.318` n `146` status `ready` deltaP `18.0865` edge `0.0955` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.5518` n `199` status `ready` deltaP `0.7538` edge `0.002` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.5807` n `32` status `ready` deltaP `0.0` edge `-0.0247` maxDD `-1.6464`
- `market_context_high->equity_4h` score `-0.6033` n `194` status `ready` deltaP `6.8613` edge `0.0468` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.6367` n `199` status `ready` deltaP `-1.652` edge `-0.0023` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7079` n `199` status `ready` deltaP `-3.2558` edge `0.0029` maxDD `-0.7564`
- `market_context_high->unknown_4h` score `-0.7142` n `194` status `ready` deltaP `-14.7819` edge `0.2796` maxDD `-10.5788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
