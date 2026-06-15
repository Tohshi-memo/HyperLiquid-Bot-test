# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T16:07:31.648663+00:00`
- Price records: `672`
- Market context records: `4006`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10258`

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

- `risk_on_high->unknown_4h` score `147.1846` n `40` status `ready` deltaP `-3.628` edge `12.4712` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `147.1846` n `40` status `ready` deltaP `-3.628` edge `12.4712` maxDD `-10.864`
- `market_context_high->unknown_24h` score `47.8504` n `136` status `ready` deltaP `-3.1352` edge `4.4113` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `26.316` n `147` status `ready` deltaP `2.8176` edge `2.7165` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `8.4486` n `40` status `ready` deltaP `40.9722` edge `0.4309` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.4486` n `40` status `ready` deltaP `40.9722` edge `0.4309` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.8638` n `40` status `ready` deltaP `37.5915` edge `0.0761` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.8638` n `40` status `ready` deltaP `37.5915` edge `0.0761` maxDD `-0.0446`
- `market_context_high->index_24h` score `3.4176` n `136` status `ready` deltaP `26.4399` edge `0.1904` maxDD `-5.5496`
- `market_context_high->metal_24h` score `2.8507` n `136` status `ready` deltaP `14.7978` edge `0.2792` maxDD `-8.2238`
- `risk_on_high->index_24h` score `2.2725` n `40` status `ready` deltaP `28.6458` edge `-0.0016` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.2725` n `40` status `ready` deltaP `28.6458` edge `-0.0016` maxDD `0.0`
- `market_context_high->equity_4h` score `1.9528` n `147` status `ready` deltaP `19.6833` edge `0.1596` maxDD `-6.9137`
- `market_context_high->equity_24h` score `1.6989` n `136` status `ready` deltaP `16.7075` edge `0.33` maxDD `-14.318`
- `risk_on_high->crypto_major_4h` score `1.3522` n `40` status `ready` deltaP `20.061` edge `0.0455` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.3522` n `40` status `ready` deltaP `20.061` edge `0.0455` maxDD `-2.6576`
- `market_context_high->metal_1h` score `1.186` n `147` status `ready` deltaP `12.7215` edge `0.0615` maxDD `-1.7983`
- `risk_on_high->commodity_24h` score `1.0443` n `40` status `ready` deltaP `4.1667` edge `0.2874` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0443` n `40` status `ready` deltaP `4.1667` edge `0.2874` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `0.9034` n `147` status `ready` deltaP `9.6593` edge `0.0651` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
