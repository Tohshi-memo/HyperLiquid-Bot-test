# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T10:22:29.745011+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `news_risk_high->crypto_alt_24h` score `3.1226` n `111` status `ready` deltaP `22.2786` edge `0.7427` maxDD `-33.6045`
- `news_risk_high->crypto_alt_4h` score `0.894` n `133` status `ready` deltaP `8.2901` edge `0.2457` maxDD `-10.2419`
- `news_risk_high->fx_1h` score `-0.5068` n `145` status `ready` deltaP `1.1253` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5087` n `145` status `ready` deltaP `1.6333` edge `0.0451` maxDD `-5.6968`
- `news_risk_high->metal_24h` score `-0.8508` n `111` status `ready` deltaP `13.2789` edge `0.128` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.1107` n `145` status `ready` deltaP `-0.8528` edge `-0.0069` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2668` n `145` status `ready` deltaP `-4.6696` edge `-0.0091` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.3503` n `133` status `ready` deltaP `-5.2128` edge `-0.0132` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-2.2747` n `133` status `ready` deltaP `-4.9388` edge `-0.0286` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3855` n `111` status `ready` deltaP `-17.6192` edge `-0.0175` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4461` n `145` status `ready` deltaP `-9.1927` edge `-0.0059` maxDD `-3.2657`
- `news_risk_high->metal_4h` score `-2.8599` n `133` status `ready` deltaP `-2.5593` edge `-0.0291` maxDD `-9.3056`
- `news_risk_high->equity_1h` score `-2.9662` n `145` status `ready` deltaP `-7.8402` edge `-0.0604` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-3.2484` n `111` status `ready` deltaP `-13.9312` edge `-0.0394` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.3291` n `145` status `ready` deltaP `-8.6207` edge `-0.0474` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8736` n `133` status `ready` deltaP `-12.8117` edge `-0.0159` maxDD `-8.386`
- `news_risk_high->equity_24h` score `-6.2292` n `111` status `ready` deltaP `4.0776` edge `0.1837` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2801` n `133` status `ready` deltaP `-14.225` edge `-0.1099` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-8.5548` n `133` status `ready` deltaP `-3.7296` edge `-0.2358` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-10.6264` n `111` status `ready` deltaP `-25.4411` edge `-0.1347` maxDD `-24.1647`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
