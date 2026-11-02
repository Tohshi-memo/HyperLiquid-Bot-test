# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T14:37:30.391736+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4879`

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

- `news_risk_high->crypto_alt_4h` score `-0.0145` n `146` status `ready` deltaP `5.3229` edge `0.2263` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.515` n `146` status `ready` deltaP `1.2837` edge `0.0482` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5175` n `146` status `ready` deltaP `0.9208` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8266` n `126` status `ready` deltaP `12.5744` edge `0.1358` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0497` n `146` status `ready` deltaP `-0.2994` edge `-0.0055` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1255` n `146` status `ready` deltaP `-1.2195` edge `-0.011` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2876` n `146` status `ready` deltaP `-4.9483` edge `-0.0099` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-1.9985` n `126` status `ready` deltaP `-13.4921` edge `0.0046` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2086` n `146` status `ready` deltaP `-4.4938` edge `-0.0231` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3301` n `146` status `ready` deltaP `-8.1782` edge `-0.003` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.5632` n `126` status `ready` deltaP `-6.4237` edge `-0.0016` maxDD `-7.402`
- `news_risk_high->crypto_alt_24h` score `-2.5737` n `126` status `ready` deltaP `14.6329` edge `0.523` maxDD `-65.3749`
- `news_risk_high->equity_1h` score `-2.8411` n `146` status `ready` deltaP `-7.2348` edge `-0.0484` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3038` n `146` status `ready` deltaP `-8.6047` edge `-0.0454` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8782` n `146` status `ready` deltaP `-11.4079` edge `-0.0117` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.5658` n `146` status `ready` deltaP `-4.7089` edge `-0.0286` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-4.9997` n `126` status `ready` deltaP `9.0774` edge `0.308` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2048` n `146` status `ready` deltaP `-14.0787` edge `-0.1046` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-12.1333` n `126` status `ready` deltaP `-22.0486` edge `-0.1831` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.3474` n `126` status `ready` deltaP `-26.4881` edge `-0.1635` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
