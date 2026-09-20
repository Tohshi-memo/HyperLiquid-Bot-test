# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T22:37:27.319124+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9028`

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

- `news_risk_high->crypto_major_24h` score `24.5753` n `98` status `ready` deltaP `12.7906` edge `2.6485` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2695` n `98` status `ready` deltaP `15.0935` edge `2.0766` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.5752` n `101` status `ready` deltaP `20.5958` edge `0.3649` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.7297` n `101` status `ready` deltaP `20.4434` edge `0.3003` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7042` n `101` status `ready` deltaP `16.2314` edge `0.1637` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.0832` n `101` status `ready` deltaP `18.3272` edge `0.1037` maxDD `-2.8494`
- `market_context_high->commodity_4h` score `1.6999` n `44` status `ready` deltaP `31.8182` edge `0.0361` maxDD `-0.7557`
- `market_context_high->fx_1h` score `1.1866` n `51` status `ready` deltaP `16.2469` edge `0.0085` maxDD `-0.1012`
- `news_risk_high->commodity_24h` score `0.9857` n `98` status `ready` deltaP `22.2541` edge `0.1086` maxDD `-3.4467`
- `news_risk_high->metal_1h` score `0.6341` n `101` status `ready` deltaP `14.7477` edge `0.0147` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.6252` n `101` status `ready` deltaP `17.2512` edge `0.0425` maxDD `-2.0994`
- `market_context_high->fx_4h` score `0.4202` n `44` status `ready` deltaP `11.6408` edge `0.0045` maxDD `-0.2586`
- `news_risk_high->equity_24h` score `0.3542` n `98` status `ready` deltaP `15.8765` edge `0.0646` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.2753` n `51` status `ready` deltaP `6.2639` edge `0.0135` maxDD `-0.2519`
- `news_risk_high->fx_4h` score `0.2395` n `101` status `ready` deltaP `9.098` edge `0.0229` maxDD `-0.421`
- `news_risk_high->equity_1h` score `0.1274` n `101` status `ready` deltaP `4.6155` edge `0.0204` maxDD `-0.9112`
- `market_context_high->commodity_1h` score `0.0987` n `51` status `ready` deltaP `6.1142` edge `0.0053` maxDD `-0.6721`
- `news_risk_high->metal_24h` score `0.0499` n `98` status `ready` deltaP `14.4629` edge `-0.0056` maxDD `-2.4203`
- `market_context_high->index_1h` score `-0.2508` n `51` status `ready` deltaP `-0.3669` edge `0.0012` maxDD `-0.4724`
- `market_context_high->crypto_alt_1h` score `-0.2893` n `51` status `ready` deltaP `-2.1339` edge `0.0687` maxDD `-3.9915`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
