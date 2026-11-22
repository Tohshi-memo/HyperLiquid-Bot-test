# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T09:07:26.462704+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4522`

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

- `market_context_high->unknown_1h` score `11933.3071` n `107` status `ready` deltaP `0.3119` edge `994.46` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7450.0769` n `107` status `ready` deltaP `-2.0287` edge `620.8838` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2947` n `107` status `ready` deltaP `2.9394` edge `0.0091` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3632` n `107` status `ready` deltaP `2.4498` edge `0.0021` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.1438` n `107` status `ready` deltaP `-7.6403` edge `-0.0014` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5323` n `107` status `ready` deltaP `-0.3818` edge `0.0035` maxDD `-1.4588`
- `market_context_high->crypto_major_1h` score `-1.6951` n `107` status `ready` deltaP `3.2346` edge `-0.0279` maxDD `-13.8788`
- `market_context_high->equity_1h` score `-1.8825` n `107` status `ready` deltaP `6.7505` edge `-0.0043` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-2.0176` n `107` status `ready` deltaP `2.0971` edge `-0.0015` maxDD `-10.1161`
- `market_context_high->crypto_alt_1h` score `-2.3239` n `107` status `ready` deltaP `-4.9905` edge `-0.0536` maxDD `-13.8848`
- `market_context_high->commodity_1h` score `-2.5656` n `107` status `ready` deltaP `-11.3059` edge `-0.0267` maxDD `-4.2715`
- `market_context_high->index_4h` score `-3.3657` n `107` status `ready` deltaP `-13.0014` edge `-0.0305` maxDD `-7.0639`
- `market_context_high->fx_24h` score `-4.9197` n `107` status `ready` deltaP `-7.9634` edge `-0.0028` maxDD `-5.9937`
- `market_context_high->commodity_4h` score `-6.7538` n `107` status `ready` deltaP `-17.0318` edge `-0.0893` maxDD `-14.7977`
- `market_context_high->metal_24h` score `-10.1461` n `107` status `ready` deltaP `-8.5361` edge `0.021` maxDD `-52.1012`
- `market_context_high->crypto_major_4h` score `-11.0398` n `107` status `ready` deltaP `-8.3685` edge `-0.1713` maxDD `-47.4317`
- `market_context_high->crypto_alt_4h` score `-11.2803` n `107` status `ready` deltaP `-8.9782` edge `-0.1989` maxDD `-46.5016`
- `market_context_high->commodity_24h` score `-12.7366` n `107` status `ready` deltaP `-27.489` edge `-0.3532` maxDD `-62.7154`
- `market_context_high->crypto_major_24h` score `-15.5486` n `107` status `ready` deltaP `7.5447` edge `0.0163` maxDD `-152.134`
- `market_context_high->index_24h` score `-16.0163` n `107` status `ready` deltaP `-32.3987` edge `-0.1791` maxDD `-39.8349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
