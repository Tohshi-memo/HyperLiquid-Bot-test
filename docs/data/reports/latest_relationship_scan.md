# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T03:22:28.659212+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2778`

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

- `market_context_high->unknown_1h` score `12002.4332` n `108` status `ready` deltaP `1.1367` edge `1000.215` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7455.1377` n `108` status `ready` deltaP `-0.0903` edge `621.2905` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `20.8461` n `93` status `ready` deltaP `37.696` edge `1.6007` maxDD `-7.1865`
- `market_context_high->crypto_alt_24h` score `10.1556` n `93` status `ready` deltaP `22.1943` edge `1.3585` maxDD `-12.6903`
- `market_context_high->crypto_major_4h` score `1.2704` n `108` status `ready` deltaP `3.7883` edge `0.3625` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.7993` n `108` status `ready` deltaP `5.0079` edge `0.2408` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.7803` n `108` status `ready` deltaP `20.0034` edge `0.0661` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.0595` n `108` status `ready` deltaP `5.988` edge `0.0216` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.2274` n `108` status `ready` deltaP `4.8459` edge `0.0782` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2351` n `108` status `ready` deltaP `3.7148` edge `0.0063` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.6693` n `108` status `ready` deltaP `-1.6356` edge `0.0473` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.0115` n `108` status `ready` deltaP `7.0914` edge `0.0463` maxDD `-10.8962`
- `market_context_high->metal_24h` score `-1.217` n `93` status `ready` deltaP `17.2939` edge `0.1871` maxDD `-22.3047`
- `market_context_high->fx_1h` score `-1.6349` n `108` status `ready` deltaP `-11.6988` edge `-0.0023` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.8308` n `108` status `ready` deltaP `-2.2245` edge `-0.0034` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.4055` n `108` status `ready` deltaP `-9.6696` edge `-0.0278` maxDD `-3.9892`
- `market_context_high->fx_4h` score `-2.4198` n `108` status `ready` deltaP `-15.56` edge `-0.0049` maxDD `-1.794`
- `market_context_high->fx_24h` score `-6.9753` n `93` status `ready` deltaP `-21.6398` edge `-0.0097` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1102` n `108` status `ready` deltaP `-29.1102` edge `-0.1125` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.3343` n `108` status `ready` deltaP `-6.8992` edge `-0.0497` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
