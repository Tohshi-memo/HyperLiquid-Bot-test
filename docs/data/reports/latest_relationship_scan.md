# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T05:07:27.632583+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10755`

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

- `risk_on_high->unknown_4h` score `21.7333` n `145` status `ready` deltaP `-3.77` edge `2.0368` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `21.7333` n `145` status `ready` deltaP `-3.77` edge `2.0368` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.2662` n `245` status `ready` deltaP `0.7902` edge `0.9304` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `5.4349` n `35` status `ready` deltaP `25.8185` edge `0.3023` maxDD `-0.3881`
- `news_risk_high->commodity_24h` score `4.0279` n `35` status `ready` deltaP `20.1389` edge `0.2014` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.469` n `35` status `ready` deltaP `16.9686` edge `0.2121` maxDD `-0.8911`
- `news_risk_high->metal_4h` score `2.4691` n `35` status `ready` deltaP `24.8955` edge `0.0619` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.7498` n `35` status `ready` deltaP `8.7762` edge `0.1074` maxDD `-0.2737`
- `market_context_high->equity_24h` score `1.6125` n `169` status `ready` deltaP `13.5623` edge `0.3978` maxDD `-16.9737`
- `risk_on_high->crypto_major_24h` score `1.5814` n `86` status `ready` deltaP `12.2012` edge `0.854` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `1.5814` n `86` status `ready` deltaP `12.2012` edge `0.854` maxDD `-47.9416`
- `news_risk_high->equity_1h` score `1.5064` n `35` status `ready` deltaP `11.5355` edge `0.0877` maxDD `-0.7924`
- `news_risk_high->fx_24h` score `1.3562` n `35` status `ready` deltaP `24.0278` edge `0.0451` maxDD `-3.0484`
- `news_risk_high->metal_1h` score `1.219` n `35` status `ready` deltaP `14.3541` edge `0.0252` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.09` n `35` status `ready` deltaP `6.1078` edge `0.0684` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.0427` n `35` status `ready` deltaP `13.0197` edge `0.0135` maxDD `-0.0724`
- `news_risk_high->crypto_alt_1h` score `0.5099` n `35` status `ready` deltaP `6.7194` edge `0.0242` maxDD `-0.7867`
- `news_risk_high->commodity_1h` score `0.1733` n `35` status `ready` deltaP `9.4269` edge `0.004` maxDD `-0.9036`
- `news_risk_high->crypto_major_24h` score `0.1298` n `35` status `ready` deltaP `14.5932` edge `0.138` maxDD `-14.1587`
- `risk_on_high->index_1h` score `-0.0998` n `145` status `ready` deltaP `5.2364` edge `-0.003` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
