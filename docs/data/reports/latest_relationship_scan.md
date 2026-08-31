# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T06:07:27.203627+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11588`

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

- `risk_on_high->crypto_alt_24h` score `21.6619` n `55` status `ready` deltaP `47.9261` edge `1.5337` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.6619` n `55` status `ready` deltaP `47.9261` edge `1.5337` maxDD `-3.1772`
- `risk_on_high->crypto_major_24h` score `9.7892` n `55` status `ready` deltaP `29.214` edge `0.7628` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `9.7892` n `55` status `ready` deltaP `29.214` edge `0.7628` maxDD `-9.0103`
- `risk_on_high->unknown_4h` score `8.3428` n `101` status `ready` deltaP `24.4038` edge `0.5942` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.3428` n `101` status `ready` deltaP `24.4038` edge `0.5942` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.6457` n `153` status `ready` deltaP `21.3106` edge `0.4811` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `6.2917` n `55` status `ready` deltaP `70.4861` edge `0.0544` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.2917` n `55` status `ready` deltaP `70.4861` edge `0.0544` maxDD `0.0`
- `market_context_high->metal_24h` score `5.2312` n `96` status `ready` deltaP `37.1527` edge `0.2491` maxDD `-1.8678`
- `risk_on_high->metal_24h` score `4.4116` n `55` status `ready` deltaP `40.5808` edge `0.1443` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.4116` n `55` status `ready` deltaP `40.5808` edge `0.1443` maxDD `-0.7767`
- `market_context_high->crypto_alt_24h` score `4.3699` n `96` status `ready` deltaP `22.3958` edge `0.8299` maxDD `-27.517`
- `market_context_high->crypto_major_24h` score `3.8499` n `96` status `ready` deltaP `20.3125` edge `0.4345` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `2.6193` n `107` status `ready` deltaP `7.7131` edge `0.2245` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.6193` n `107` status `ready` deltaP `7.7131` edge `0.2245` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.3966` n `159` status `ready` deltaP `7.0548` edge `0.2157` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.0321` n `96` status `ready` deltaP `37.1528` edge `0.0305` maxDD `-1.6688`
- `risk_on_high->equity_24h` score `0.8123` n `55` status `ready` deltaP `18.7153` edge `0.0237` maxDD `-3.7955`
- `risk_on_and_context->equity_24h` score `0.8123` n `55` status `ready` deltaP `18.7153` edge `0.0237` maxDD `-3.7955`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
