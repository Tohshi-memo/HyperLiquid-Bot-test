# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T02:22:24.657611+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10973`

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

- `risk_on_high->unknown_4h` score `20.3757` n `143` status `ready` deltaP `-2.8004` edge `1.9172` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `20.3757` n `143` status `ready` deltaP `-2.8004` edge `1.9172` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `7.9995` n `238` status `ready` deltaP `1.0722` edge `0.9063` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `4.9945` n `37` status `ready` deltaP `23.095` edge `0.2892` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9271` n `37` status `ready` deltaP `20.1389` edge `0.193` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2949` n `37` status `ready` deltaP `16.4181` edge `0.2064` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.4125` n `37` status `ready` deltaP `24.6086` edge `0.0591` maxDD `-0.7692`
- `market_context_high->equity_24h` score `2.288` n `158` status `ready` deltaP `14.0713` edge `0.4507` maxDD `-16.9737`
- `news_risk_high->equity_1h` score `1.5739` n `37` status `ready` deltaP `12.935` edge `0.084` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5222` n `37` status `ready` deltaP `7.1605` edge `0.0992` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3556` n `37` status `ready` deltaP `16.2122` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1874` n `37` status `ready` deltaP `14.873` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->fx_24h` score `1.0994` n `37` status `ready` deltaP `21.8656` edge `0.0474` maxDD `-3.1244`
- `news_risk_high->crypto_major_1h` score `1.0971` n `37` status `ready` deltaP `5.717` edge `0.0716` maxDD `-0.4628`
- `risk_on_high->crypto_major_24h` score `0.8482` n `78` status `ready` deltaP `10.0561` edge `0.7743` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `0.8482` n `78` status `ready` deltaP `10.0561` edge `0.7743` maxDD `-47.9416`
- `news_risk_high->crypto_alt_1h` score `0.7882` n `37` status `ready` deltaP `8.4278` edge `0.036` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `-0.0276` n `37` status `ready` deltaP `2.7398` edge `0.0123` maxDD `-1.296`
- `news_risk_high->commodity_1h` score `-0.0371` n `37` status `ready` deltaP `5.5754` edge `0.0027` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.0998` n `145` status `ready` deltaP `5.2364` edge `-0.003` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
