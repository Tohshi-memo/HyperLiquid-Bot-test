# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T21:52:27.115239+00:00`
- Price records: `672`
- Market context records: `8237`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5930`

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

- `news_risk_high->unknown_24h` score `7957.2941` n `43` status `ready` deltaP `38.5417` edge `662.8509` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.447` n `54` status `ready` deltaP `27.2979` edge `0.4983` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1217` n `54` status `ready` deltaP `22.2777` edge `0.1425` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7383` n `54` status `ready` deltaP `23.182` edge `0.0927` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3289` n `54` status `ready` deltaP `11.3934` edge `0.292` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7871` n `54` status `ready` deltaP `14.5542` edge `0.0953` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7012` n `54` status `ready` deltaP `11.5048` edge `0.1048` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3538` n `54` status `ready` deltaP `16.9264` edge `0.1999` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.9465` n `54` status `ready` deltaP `9.1294` edge `0.0648` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.5058` n `54` status `ready` deltaP `7.5017` edge `0.021` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1432` n `54` status `ready` deltaP `6.548` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1515` n `54` status `ready` deltaP `2.6558` edge `0.01` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5078` n `54` status `ready` deltaP `3.698` edge `0.006` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.118` n `54` status `ready` deltaP `-8.6605` edge `-0.0402` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.0936` n `43` status `ready` deltaP `-18.6491` edge `-0.0452` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-5.9444` n `43` status `ready` deltaP `-21.988` edge `-0.0973` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-8.8879` n `54` status `ready` deltaP `-32.7913` edge `-0.1913` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.6827` n `43` status `ready` deltaP `-23.9624` edge `-0.356` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-14.4621` n `43` status `ready` deltaP `-20.696` edge `-0.4841` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.4032` n `43` status `ready` deltaP `-23.4415` edge `-1.2317` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
