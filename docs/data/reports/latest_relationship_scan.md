# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T17:07:28.284850+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10024`

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

- `market_context_high->unknown_1h` score `87.3199` n `47` status `ready` deltaP `10.116` edge `7.2163` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.7261` n `47` status `ready` deltaP `30.4226` edge `3.4803` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.2732` n `47` status `ready` deltaP `24.782` edge `2.3122` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.4434` n `47` status `ready` deltaP `29.2073` edge `1.8778` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8286` n `47` status `ready` deltaP `34.7628` edge `0.4336` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `5.4627` n `93` status `ready` deltaP `1.3217` edge `1.5958` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.7111` n `47` status `ready` deltaP `31.9334` edge `0.1202` maxDD `-0.2401`
- `news_risk_high->crypto_alt_24h` score `3.3675` n `93` status `ready` deltaP `-1.0473` edge `1.14` maxDD `-49.7699`
- `market_context_high->index_4h` score `3.0738` n `47` status `ready` deltaP `35.0934` edge `0.0376` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.8654` n `117` status `ready` deltaP `13.6676` edge `0.1967` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.5613` n `47` status `ready` deltaP `17.6018` edge `0.1379` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.4801` n `117` status `ready` deltaP `16.6181` edge `0.1394` maxDD `-1.8141`
- `news_risk_high->crypto_major_4h` score `2.1335` n `113` status `ready` deltaP `15.6513` edge `0.2866` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `1.9583` n `113` status `ready` deltaP `8.1778` edge `0.3538` maxDD `-15.9436`
- `news_risk_high->fx_4h` score `1.5423` n `113` status `ready` deltaP `22.8335` edge `0.0399` maxDD `-0.421`
- `news_risk_high->metal_24h` score `1.1787` n `93` status `ready` deltaP `25.2072` edge `0.1279` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `1.1471` n `93` status `ready` deltaP `28.1978` edge `0.1222` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9954` n `47` status `ready` deltaP `15.0592` edge `0.0104` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8779` n `47` status `ready` deltaP `11.0173` edge `0.04` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.7728` n `117` status `ready` deltaP `15.1313` edge `0.0212` maxDD `-0.6142`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
