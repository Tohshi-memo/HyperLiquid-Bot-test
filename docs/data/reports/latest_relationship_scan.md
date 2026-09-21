# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T05:07:30.117135+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9296`

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

- `market_context_high->unknown_4h` score `37.5961` n `58` status `ready` deltaP `1.23` edge `3.1398` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `24.3728` n `98` status `ready` deltaP `12.2697` edge `2.6351` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `19.1668` n `98` status `ready` deltaP `13.0102` edge `1.9986` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.6408` n `101` status `ready` deltaP `20.291` edge `0.3724` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.9803` n `101` status `ready` deltaP `21.2056` edge `0.3161` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7582` n `101` status `ready` deltaP `16.3811` edge `0.1672` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1623` n `101` status `ready` deltaP `18.4769` edge `0.1093` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.1635` n `98` status `ready` deltaP `23.1222` edge `0.1256` maxDD `-3.4467`
- `market_context_high->equity_1h` score `1.0488` n `58` status `ready` deltaP `7.8051` edge `0.0607` maxDD `-0.36`
- `market_context_high->index_1h` score `0.8418` n `58` status `ready` deltaP `12.0741` edge `0.0152` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6197` n `101` status `ready` deltaP `14.598` edge `0.0145` maxDD `-0.8144`
- `market_context_high->index_4h` score `0.4497` n `58` status `ready` deltaP `16.6106` edge `0.0106` maxDD `-1.0949`
- `news_risk_high->metal_4h` score `0.4224` n `101` status `ready` deltaP `15.422` edge `0.0378` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.3417` n `58` status `ready` deltaP `6.1481` edge `0.0183` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.2816` n `58` status `ready` deltaP `8.0271` edge `0.0056` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.1785` n `101` status `ready` deltaP `8.3358` edge `0.0229` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.026` n `101` status `ready` deltaP `3.4179` edge `0.0156` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.1226` n `58` status `ready` deltaP `-1.3421` edge `0.0706` maxDD `-2.7494`
- `news_risk_high->fx_1h` score `-0.2675` n `101` status `ready` deltaP `2.3937` edge `0.0061` maxDD `-0.2147`
- `news_risk_high->metal_24h` score `-0.2994` n `98` status `ready` deltaP `10.2962` edge `-0.0226` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
