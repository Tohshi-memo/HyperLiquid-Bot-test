# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T06:07:28.271141+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10659`

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

- `news_risk_high->crypto_alt_24h` score `7.846` n `31` status `ready` deltaP `33.1317` edge `0.4379` maxDD `-0.0621`
- `news_risk_high->crypto_major_4h` score `5.0512` n `31` status `ready` deltaP `25.9442` edge `0.2681` maxDD `-0.6101`
- `news_risk_high->crypto_major_24h` score `4.7472` n `31` status `ready` deltaP `22.0094` edge `0.3759` maxDD `-8.1623`
- `news_risk_high->commodity_24h` score `4.0015` n `31` status `ready` deltaP `20.1389` edge `0.1992` maxDD `0.0`
- `news_risk_high->metal_4h` score `2.5579` n `31` status `ready` deltaP `24.9557` edge `0.0689` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `2.4947` n `31` status `ready` deltaP `14.4621` edge `0.1274` maxDD `-0.2737`
- `risk_on_high->crypto_major_24h` score `2.057` n `90` status `ready` deltaP `13.2639` edge `0.9079` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `2.057` n `90` status `ready` deltaP `13.2639` edge `0.9079` maxDD `-47.9416`
- `news_risk_high->fx_24h` score `1.9334` n `31` status `ready` deltaP `29.1891` edge `0.0412` maxDD `-2.9744`
- `news_risk_high->index_1h` score `1.5406` n `31` status `ready` deltaP `18.1234` edge `0.0168` maxDD `-0.0724`
- `market_context_high->equity_24h` score `1.4106` n `173` status `ready` deltaP `13.3329` edge `0.3825` maxDD `-16.9737`
- `news_risk_high->equity_1h` score `1.3092` n `31` status `ready` deltaP `7.4802` edge `0.0983` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `0.8607` n `31` status `ready` deltaP `9.5615` edge `0.0273` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `0.6039` n `31` status `ready` deltaP `0.9465` edge `0.0623` maxDD `-0.4628`
- `news_risk_high->crypto_alt_4h` score `0.1728` n `31` status `ready` deltaP `2.9799` edge `0.0274` maxDD `-1.296`
- `news_risk_high->crypto_alt_1h` score `-0.0331` n `31` status `ready` deltaP `1.9268` edge `0.0109` maxDD `-0.7867`
- `news_risk_high->commodity_1h` score `-0.0552` n `31` status `ready` deltaP `5.0029` edge `0.0042` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1363` n `145` status `ready` deltaP `8.0487` edge `0.0001` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
