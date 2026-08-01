# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T16:52:31.719695+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5915`

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

- `news_risk_high->unknown_24h` score `5190.6078` n `60` status `ready` deltaP `34.2345` edge `432.3645` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.8394` n `53` status `ready` deltaP `54.4979` edge `1.0797` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.4664` n `60` status `ready` deltaP `23.4553` edge `0.4422` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.624` n `60` status `ready` deltaP `22.9979` edge `0.0844` maxDD `-0.191`
- `market_context_high->commodity_24h` score `2.1409` n `53` status `ready` deltaP `30.604` edge `0.2563` maxDD `-10.2019`
- `news_risk_high->crypto_major_4h` score `1.3157` n `60` status `ready` deltaP `7.8963` edge `0.1936` maxDD `-3.5385`
- `news_risk_high->equity_1h` score `0.9567` n `65` status `ready` deltaP `10.3155` edge `0.0789` maxDD `-2.7692`
- `news_risk_high->crypto_alt_4h` score `0.5412` n `60` status `ready` deltaP `11.8293` edge `0.1297` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.5266` n `53` status `ready` deltaP `8.4331` edge `0.107` maxDD `-5.323`
- `news_risk_high->crypto_alt_1h` score `0.4921` n `65` status `ready` deltaP `9.0603` edge `0.0579` maxDD `-2.0834`
- `news_risk_high->fx_4h` score `0.2401` n `60` status `ready` deltaP `13.689` edge `0.0245` maxDD `-0.6604`
- `market_context_high->fx_4h` score `0.1971` n `53` status `ready` deltaP `13.406` edge `0.0155` maxDD `-1.3685`
- `news_risk_high->crypto_major_1h` score `0.1895` n `65` status `ready` deltaP `4.2953` edge `0.0504` maxDD `-2.3794`
- `news_risk_high->metal_4h` score `0.1448` n `60` status `ready` deltaP `4.6748` edge `0.035` maxDD `-0.8085`
- `news_risk_high->fx_1h` score `0.0154` n `65` status `ready` deltaP `4.445` edge `0.0046` maxDD `-0.2475`
- `market_context_high->fx_1h` score `-0.0149` n `53` status `ready` deltaP `7.2026` edge `0.001` maxDD `-0.6874`
- `news_risk_high->metal_1h` score `-0.0276` n `65` status `ready` deltaP `4.3782` edge `0.0076` maxDD `-0.5599`
- `news_risk_high->index_1h` score `-0.0701` n `65` status `ready` deltaP `2.2409` edge `0.0082` maxDD `-0.5702`
- `market_context_high->commodity_1h` score `-0.0846` n `53` status `ready` deltaP `4.0278` edge `0.0164` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `-0.1933` n `53` status `ready` deltaP `4.6393` edge `0.0318` maxDD `-3.0005`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
