# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T01:07:23.131650+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3540`

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

- `news_risk_high->unknown_1h` score `3208.0716` n `31` status `ready` deltaP `1.7819` edge `267.345` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3172.1874` n `31` status `ready` deltaP `4.3962` edge `264.3253` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `26.5093` n `31` status `ready` deltaP `35.4167` edge `1.973` maxDD `0.0`
- `news_risk_high->equity_24h` score `23.6429` n `31` status `ready` deltaP `34.8958` edge `1.7376` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3859` n `31` status `ready` deltaP `34.5486` edge `1.4685` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.543` n `31` status `ready` deltaP `23.7116` edge `0.7242` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.2893` n `31` status `ready` deltaP `35.0905` edge `0.5049` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.2465` n `31` status `ready` deltaP `16.7781` edge `0.8307` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `6.2336` n `31` status `ready` deltaP `22.3119` edge `0.3982` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.9592` n `31` status `ready` deltaP `42.0587` edge `0.1457` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.1983` n `31` status `ready` deltaP `36.4583` edge `0.1068` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.073` n `31` status `ready` deltaP `18.0413` edge `0.1545` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9329` n `31` status `ready` deltaP `33.1088` edge `0.0497` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5668` n `31` status `ready` deltaP `30.7949` edge `0.0171` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2421` n `31` status `ready` deltaP `7.7651` edge `0.2818` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0094` n `31` status `ready` deltaP `10.7591` edge `0.2216` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.3046` n `31` status `ready` deltaP `26.8881` edge `0.0159` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.6124` n `31` status `ready` deltaP `12.9671` edge `0.0478` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2028` n `31` status `ready` deltaP `9.1316` edge `0.0049` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5125` n `31` status `ready` deltaP `-3.4093` edge `0.0062` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
