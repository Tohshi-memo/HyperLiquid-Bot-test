# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T00:52:29.498690+00:00`
- Price records: `672`
- Market context records: `5095`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `20.6874` n `79` status `ready` deltaP `27.7206` edge `1.5734` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.8326` n `114` status `ready` deltaP `4.5147` edge `0.7701` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `8.2422` n `102` status `ready` deltaP `21.461` edge `0.646` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.5467` n `102` status `ready` deltaP `13.6358` edge `0.4479` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.3869` n `102` status `ready` deltaP `12.8078` edge `0.448` maxDD `-13.8566`
- `market_context_high->equity_4h` score `2.1544` n `102` status `ready` deltaP `12.8975` edge `0.2067` maxDD `-6.3852`
- `market_context_high->equity_1h` score `0.5791` n `114` status `ready` deltaP `9.9485` edge `0.0611` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.3994` n `114` status `ready` deltaP `5.904` edge `0.108` maxDD `-5.0257`
- `market_context_high->metal_1h` score `0.3122` n `114` status `ready` deltaP `8.877` edge `0.0305` maxDD `-1.3057`
- `market_context_high->crypto_major_1h` score `0.295` n `114` status `ready` deltaP `6.5658` edge `0.1186` maxDD `-6.9639`
- `market_context_high->index_4h` score `0.2397` n `102` status `ready` deltaP `9.3227` edge `0.0447` maxDD `-1.0893`
- `market_context_high->index_1h` score `0.0124` n `114` status `ready` deltaP `5.4129` edge `0.0113` maxDD `-0.997`
- `market_context_high->metal_4h` score `-0.1513` n `102` status `ready` deltaP `4.899` edge `0.0739` maxDD `-3.4097`
- `market_context_high->commodity_1h` score `-1.0404` n `114` status `ready` deltaP `-1.2633` edge `-0.0025` maxDD `-2.062`
- `market_context_high->fx_1h` score `-1.5505` n `114` status `ready` deltaP `-9.2867` edge `-0.0032` maxDD `-0.7944`
- `market_context_high->fx_24h` score `-1.5606` n `79` status `ready` deltaP `-3.1426` edge `-0.0079` maxDD `-1.7626`
- `market_context_high->commodity_4h` score `-1.6607` n `102` status `ready` deltaP `4.4625` edge `-0.0213` maxDD `-6.7471`
- `market_context_high->commodity_24h` score `-1.6698` n `79` status `ready` deltaP `7.7004` edge `0.0308` maxDD `-15.0303`
- `market_context_high->fx_4h` score `-2.1801` n `102` status `ready` deltaP `-9.7172` edge `-0.0096` maxDD `-1.9169`
- `market_context_high->metal_24h` score `-4.5098` n `79` status `ready` deltaP `-6.5995` edge `0.0113` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
