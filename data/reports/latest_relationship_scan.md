# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T16:26:36.013173+00:00`
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

- `news_risk_high->unknown_24h` score `5190.7794` n `60` status `ready` deltaP `34.2345` edge `432.3788` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.801` n `53` status `ready` deltaP `54.4979` edge `1.0765` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.4276` n `60` status `ready` deltaP `23.1504` edge `0.441` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.6106` n `60` status `ready` deltaP `22.8455` edge `0.0843` maxDD `-0.191`
- `market_context_high->commodity_24h` score `2.1901` n `53` status `ready` deltaP `30.9506` edge `0.2603` maxDD `-10.2019`
- `news_risk_high->crypto_major_4h` score `1.2976` n `60` status `ready` deltaP `7.7439` edge `0.1923` maxDD `-3.5385`
- `news_risk_high->equity_1h` score `1.2573` n `63` status `ready` deltaP `12.1163` edge `0.0824` maxDD `-2.6723`
- `news_risk_high->crypto_alt_4h` score `0.5278` n `60` status `ready` deltaP `11.6768` edge `0.129` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.5132` n `53` status `ready` deltaP `8.2806` edge `0.1063` maxDD `-5.323`
- `news_risk_high->crypto_alt_1h` score `0.3931` n `63` status `ready` deltaP `7.7417` edge `0.054` maxDD `-2.0834`
- `news_risk_high->fx_4h` score `0.2657` n `60` status `ready` deltaP `13.9939` edge `0.0246` maxDD `-0.6604`
- `market_context_high->fx_4h` score `0.2137` n `53` status `ready` deltaP `13.7109` edge `0.0156` maxDD `-1.3685`
- `news_risk_high->crypto_major_1h` score `0.1756` n `63` status `ready` deltaP `4.2677` edge `0.0488` maxDD `-2.3794`
- `news_risk_high->metal_4h` score `0.1448` n `60` status `ready` deltaP `4.6748` edge `0.035` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `0.0961` n `63` status `ready` deltaP `6.0356` edge `0.0081` maxDD `-0.5599`
- `news_risk_high->index_1h` score `0.0163` n `63` status `ready` deltaP `3.6998` edge `0.0091` maxDD `-0.5338`
- `market_context_high->fx_1h` score `-0.0149` n `53` status `ready` deltaP `7.2026` edge `0.001` maxDD `-0.6874`
- `news_risk_high->fx_1h` score `-0.0631` n `63` status `ready` deltaP `2.9798` edge `0.0043` maxDD `-0.2475`
- `market_context_high->commodity_1h` score `-0.0667` n `53` status `ready` deltaP `4.3272` edge `0.0167` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `-0.1751` n `53` status `ready` deltaP `4.9442` edge `0.0321` maxDD `-3.0005`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
