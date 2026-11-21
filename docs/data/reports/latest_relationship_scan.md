# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T08:37:29.826798+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2674`

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

- `market_context_high->unknown_1h` score `10052.6213` n `126` status `ready` deltaP `1.0146` edge `837.7315` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6135.1785` n `126` status `ready` deltaP `-0.3145` edge `511.2975` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `2.3587` n `109` status `ready` deltaP `26.1739` edge `1.0386` maxDD `-65.8554`
- `market_context_high->metal_1h` score `-0.1641` n `126` status `ready` deltaP `4.5504` edge `0.0151` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3069` n `126` status `ready` deltaP `2.7088` edge `0.0038` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5084` n `126` status `ready` deltaP `11.7958` edge `0.0368` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3771` n `126` status `ready` deltaP `-8.6565` edge `-0.0011` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8` n `126` status `ready` deltaP `6.1377` edge `0.015` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9082` n `126` status `ready` deltaP `-6.7267` edge `0.0018` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1661` n `126` status `ready` deltaP `-6.8744` edge `-0.0215` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.3665` n `126` status `ready` deltaP `-3.0318` edge `-0.0137` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.4692` n `126` status `ready` deltaP `3.0082` edge `0.006` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.1907` n `126` status `ready` deltaP `-3.7449` edge `-0.0132` maxDD `-13.8848`
- `market_context_high->crypto_alt_24h` score `-3.667` n `109` status `ready` deltaP `13.3553` edge `0.6874` maxDD `-79.5618`
- `market_context_high->crypto_major_4h` score `-4.2781` n `126` status `ready` deltaP `-0.9558` edge `0.1508` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.9946` n `109` status `ready` deltaP `12.1958` edge `0.1158` maxDD `-45.7325`
- `market_context_high->fx_24h` score `-6.3726` n `109` status `ready` deltaP `-14.6614` edge `-0.006` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.8054` n `126` status `ready` deltaP `-17.9007` edge `-0.0785` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.4819` n `126` status `ready` deltaP `-1.4131` edge `0.0672` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.7725` n `109` status `ready` deltaP `-26.4398` edge `-0.1133` maxDD `-32.3182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
