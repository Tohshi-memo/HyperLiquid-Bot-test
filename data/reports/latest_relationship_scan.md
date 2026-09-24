# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T21:52:31.861975+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10569`

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

- `market_context_high->unknown_1h` score `84.6607` n `47` status `ready` deltaP `10.116` edge `6.9947` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `45.8441` n `47` status `ready` deltaP `30.4226` edge `3.6568` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.3856` n `47` status `ready` deltaP `24.782` edge `2.4049` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2593` n `47` status `ready` deltaP `32.5059` edge `1.9238` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.9722` n `47` status `ready` deltaP `36.1517` edge `0.4363` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `6.2505` n `114` status `ready` deltaP `-4.0498` edge `0.5723` maxDD `-0.9543`
- `market_context_high->metal_24h` score `4.1585` n `47` status `ready` deltaP `35.232` edge `0.1355` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.4624` n `114` status `ready` deltaP `16.8847` edge `0.225` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.8975` n `47` status `ready` deltaP `33.2641` edge `0.0351` maxDD `-0.2323`
- `news_risk_high->crypto_major_4h` score `2.6118` n `102` status `ready` deltaP `17.13` edge `0.3166` maxDD `-13.719`
- `news_risk_high->commodity_24h` score `2.5858` n `78` status `ready` deltaP `25.4407` edge `0.0932` maxDD `-1.7857`
- `news_risk_high->crypto_major_1h` score `2.5723` n `114` status `ready` deltaP `17.5255` edge `0.1452` maxDD `-1.8141`
- `news_risk_high->crypto_alt_4h` score `2.486` n `102` status `ready` deltaP `8.5037` edge `0.3956` maxDD `-15.9436`
- `market_context_high->equity_4h` score `2.3491` n `47` status `ready` deltaP `16.8396` edge `0.1253` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.5871` n `102` status `ready` deltaP `23.2425` edge `0.0409` maxDD `-0.421`
- `news_risk_high->metal_1h` score `1.52` n `114` status `ready` deltaP `19.511` edge `0.0251` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.9858` n `47` status `ready` deltaP `14.9095` edge `0.0106` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9235` n `47` status `ready` deltaP `11.4664` edge `0.0408` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.6704` n `78` status `ready` deltaP `22.3024` edge `0.0821` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `0.6178` n `78` status `ready` deltaP `21.1672` edge `0.1012` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
