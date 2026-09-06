# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T04:52:25.584170+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10815`

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

- `risk_on_high->unknown_4h` score `21.7803` n `145` status `ready` deltaP `-3.6175` edge `2.0397` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `21.7803` n `145` status `ready` deltaP `-3.6175` edge `2.0397` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.3132` n `245` status `ready` deltaP `0.9427` edge `0.9333` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `4.7597` n `36` status `ready` deltaP `23.6111` edge `0.2643` maxDD `-0.6721`
- `news_risk_high->commodity_24h` score `4.0123` n `36` status `ready` deltaP `20.1389` edge `0.2001` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.1404` n `36` status `ready` deltaP `15.0576` edge `0.2026` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.4996` n `36` status `ready` deltaP `25.4573` edge `0.0607` maxDD `-0.7692`
- `market_context_high->equity_24h` score `1.672` n `168` status `ready` deltaP `13.6161` edge `0.4024` maxDD `-16.9737`
- `news_risk_high->commodity_4h` score `1.5395` n `36` status `ready` deltaP `6.792` edge `0.1031` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5354` n `36` status `ready` deltaP `12.2588` edge `0.0853` maxDD `-0.7924`
- `risk_on_high->crypto_major_24h` score `1.4617` n `85` status `ready` deltaP `11.9097` edge `0.8406` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `1.4617` n `85` status `ready` deltaP `11.9097` edge `0.8406` maxDD `-47.9416`
- `news_risk_high->metal_1h` score `1.2823` n `36` status `ready` deltaP `15.2362` edge `0.0246` maxDD `-0.2118`
- `news_risk_high->fx_24h` score `1.2319` n `36` status `ready` deltaP `22.9167` edge `0.0467` maxDD `-3.0792`
- `news_risk_high->index_1h` score `1.1021` n `36` status `ready` deltaP `13.8224` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `0.9242` n `36` status `ready` deltaP `4.5908` edge `0.0647` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.6033` n `36` status `ready` deltaP `7.6015` edge `0.0261` maxDD `-0.7867`
- `news_risk_high->commodity_1h` score `0.0737` n `36` status `ready` deltaP `7.6015` edge `0.0034` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1076` n `145` status `ready` deltaP `5.0867` edge `-0.003` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1076` n `145` status `ready` deltaP `5.0867` edge `-0.003` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
