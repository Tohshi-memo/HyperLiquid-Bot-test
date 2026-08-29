# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T05:22:23.286124+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `57.9162` n `50` status `ready` deltaP `21.0069` edge `4.6863` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.6434` n `50` status `ready` deltaP `46.5208` edge `2.5376` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `9.8824` n `50` status `ready` deltaP `27.9236` edge `0.6867` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `7.3636` n `50` status `ready` deltaP `30.0069` edge `0.5064` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `7.2249` n `120` status `ready` deltaP `14.3402` edge `0.5797` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `7.1175` n `77` status `ready` deltaP `12.8306` edge `0.5511` maxDD `-1.4812`
- `news_risk_high->metal_24h` score `4.535` n `50` status `ready` deltaP `43.3125` edge `0.0934` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.3522` n `120` status `ready` deltaP `28.6458` edge `0.1903` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.608` n `80` status `ready` deltaP `5.2246` edge `0.2182` maxDD `-0.8558`
- `news_risk_high->index_24h` score `2.4898` n `50` status `ready` deltaP `26.8889` edge `0.0433` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.4752` n `120` status `ready` deltaP `19.0752` edge `0.1198` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.2858` n `77` status `ready` deltaP `33.4832` edge `0.0222` maxDD `-0.3953`
- `market_context_high->unknown_1h` score `1.1819` n `120` status `ready` deltaP `9.3913` edge `0.0809` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6273` n `80` status `ready` deltaP `12.8443` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4727` n `80` status `ready` deltaP `13.0988` edge `0.0053` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.128` n `120` status `ready` deltaP `9.7967` edge `0.01` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3398` n `120` status `ready` deltaP `4.511` edge `-0.0004` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.398` n `80` status `ready` deltaP `0.1572` edge `-0.0084` maxDD `-0.8275`
- `news_risk_high->commodity_4h` score `-0.5366` n `77` status `ready` deltaP `8.0457` edge `0.0117` maxDD `-2.0635`
- `news_risk_high->index_4h` score `-0.5824` n `77` status `ready` deltaP `1.0335` edge `-0.0174` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
