# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T22:22:29.240382+00:00`
- Price records: `672`
- Market context records: `8240`
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

- `news_risk_high->unknown_24h` score `7957.3289` n `43` status `ready` deltaP `38.5417` edge `662.8538` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.3976` n `54` status `ready` deltaP `27.1454` edge `0.4952` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1037` n `54` status `ready` deltaP `22.128` edge `0.142` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7383` n `54` status `ready` deltaP `23.182` edge `0.0927` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3188` n `54` status `ready` deltaP `11.3934` edge `0.2907` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7548` n `54` status `ready` deltaP `14.2548` edge `0.0946` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6665` n `54` status `ready` deltaP `11.2054` edge `0.1039` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3301` n `54` status `ready` deltaP `16.6215` edge `0.1989` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.9864` n `54` status `ready` deltaP `9.4343` edge `0.0661` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4794` n `54` status `ready` deltaP `7.2023` edge `0.0208` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.151` n `54` status `ready` deltaP `6.6977` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1383` n `54` status `ready` deltaP `2.8055` edge `0.0101` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5086` n `54` status `ready` deltaP `3.698` edge `0.0059` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1432` n `54` status `ready` deltaP `-8.8102` edge `-0.0413` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.0912` n `43` status `ready` deltaP `-18.6491` edge `-0.045` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-5.8854` n `43` status `ready` deltaP `-21.6408` edge `-0.0947` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-8.8951` n `54` status `ready` deltaP `-32.7913` edge `-0.1919` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.6755` n `43` status `ready` deltaP `-23.9624` edge `-0.3554` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-14.3935` n `43` status `ready` deltaP `-20.3488` edge `-0.4807` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.3336` n `43` status `ready` deltaP `-23.4415` edge `-1.2259` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
