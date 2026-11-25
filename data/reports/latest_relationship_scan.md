# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T17:52:29.922255+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3744`

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

- `market_context_high->unknown_1h` score `32182.3381` n `45` status `ready` deltaP `2.1656` edge `2681.8565` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21855.7276` n `45` status `ready` deltaP `2.4154` edge `1821.3084` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `947.3831` n `31` status `ready` deltaP `2.3807` edge `78.9503` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `602.7801` n `31` status `ready` deltaP `3.634` edge `50.2131` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `333.0071` n `31` status `ready` deltaP `5.7292` edge `27.7124` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.3923` n `31` status `ready` deltaP `52.0833` edge `3.5188` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.5082` n `31` status `ready` deltaP `53.9931` edge `3.1824` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.7068` n `31` status `ready` deltaP `55.5556` edge `2.8552` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.0387` n `31` status `ready` deltaP `41.2355` edge `0.7558` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.8793` n `31` status `ready` deltaP `27.3701` edge `0.8945` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `11.5732` n `31` status `ready` deltaP `38.4442` edge `0.7562` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4516` n `31` status `ready` deltaP `53.125` edge `0.2668` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `7.4094` n `31` status `ready` deltaP `18.6074` edge `0.9676` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.4862` n `31` status `ready` deltaP `47.267` edge `0.1549` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.9114` n `31` status `ready` deltaP `20.5862` edge `0.2074` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.485` n `31` status `ready` deltaP `36.9198` edge `0.0703` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6986` n `31` status `ready` deltaP `31.8428` edge `0.0211` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.6247` n `31` status `ready` deltaP `11.3579` edge `0.3069` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4262` n `45` status `ready` deltaP `29.7832` edge `0.0321` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3695` n `31` status `ready` deltaP `13.304` edge `0.2508` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
