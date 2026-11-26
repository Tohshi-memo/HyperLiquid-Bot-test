# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T14:52:40.311985+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3491`

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

- `news_risk_high->unknown_1h` score `3222.8232` n `31` status `ready` deltaP `1.7819` edge `268.5743` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3219.2611` n `31` status `ready` deltaP `3.4815` edge `268.2542` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `33.6949` n `31` status `ready` deltaP `42.3611` edge `2.5255` maxDD `0.0`
- `news_risk_high->equity_24h` score `32.5322` n `31` status `ready` deltaP `41.4931` edge `2.4344` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `27.6765` n `31` status `ready` deltaP `41.6667` edge `2.0286` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.3843` n `31` status `ready` deltaP `25.6933` edge `0.7811` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.9729` n `31` status `ready` deltaP `37.8344` edge `0.6269` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.9723` n `31` status `ready` deltaP `28.041` edge `0.5049` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.8011` n `31` status `ready` deltaP `18.7598` edge `0.8886` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.509` n `31` status `ready` deltaP `42.8819` edge `0.1732` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.8529` n `31` status `ready` deltaP `40.6698` edge `0.1461` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7014` n `31` status `ready` deltaP `20.5862` edge `0.1899` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3236` n `31` status `ready` deltaP `36.4625` edge `0.0599` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7608` n `31` status `ready` deltaP `32.741` edge `0.0203` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4478` n `31` status `ready` deltaP `9.7112` edge `0.2952` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2105` n `31` status `ready` deltaP `12.5555` edge `0.2354` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4285` n `31` status `ready` deltaP `28.2354` edge `0.0228` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.9568` n `31` status `ready` deltaP `15.2537` edge `0.0767` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.4043` n `31` status `ready` deltaP `12.1804` edge `0.0104` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4239` n `31` status `ready` deltaP `-2.5111` edge `0.0076` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
