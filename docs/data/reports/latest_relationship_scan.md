# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T19:22:26.243679+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10053`

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

- `market_context_high->unknown_1h` score `86.9851` n `47` status `ready` deltaP `10.116` edge `7.1884` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `44.6909` n `47` status `ready` deltaP `30.4226` edge `3.5607` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.8036` n `47` status `ready` deltaP `24.782` edge `2.3564` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.8` n `47` status `ready` deltaP `30.7698` edge `1.8971` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8322` n `47` status `ready` deltaP `34.7628` edge `0.4339` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.9189` n `47` status `ready` deltaP `33.4959` edge `0.1271` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.4399` n `111` status `ready` deltaP `16.6937` edge `0.2244` maxDD `-1.5895`
- `news_risk_high->crypto_major_24h` score `3.109` n `85` status `ready` deltaP `-2.0179` edge `1.3163` maxDD `-63.6743`
- `market_context_high->index_4h` score `2.9607` n `47` status `ready` deltaP `33.8739` edge `0.0363` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.8267` n `111` status `ready` deltaP `18.6398` edge `0.1548` maxDD `-1.8141`
- `news_risk_high->crypto_alt_4h` score `2.5417` n `106` status `ready` deltaP `8.8558` edge `0.3979` maxDD `-15.9436`
- `news_risk_high->crypto_major_4h` score `2.4941` n `106` status `ready` deltaP `16.4692` edge `0.3112` maxDD `-13.719`
- `market_context_high->equity_4h` score `2.4239` n `47` status `ready` deltaP `17.1445` edge `0.1295` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.844` n `106` status `ready` deltaP `26.185` edge `0.0427` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.7559` n `85` status `ready` deltaP `19.8918` edge `0.0902` maxDD `-1.7857`
- `news_risk_high->metal_1h` score `1.5379` n `111` status `ready` deltaP `19.511` edge `0.0266` maxDD `-0.6142`
- `news_risk_high->crypto_alt_24h` score `1.1153` n `85` status `ready` deltaP `-3.6785` edge `0.8688` maxDD `-49.7699`
- `market_context_high->index_1h` score `0.999` n `47` status `ready` deltaP `15.0592` edge `0.0107` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.9359` n `85` status `ready` deltaP `23.7337` edge `0.1066` maxDD `-7.2536`
- `market_context_high->equity_1h` score `0.9187` n `47` status `ready` deltaP `11.4664` edge `0.0404` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
