# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T07:22:27.025120+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `50.3067` n `51` status `ready` deltaP `17.0139` edge `4.0788` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.3107` n `51` status `ready` deltaP `40.237` edge `1.0174` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9401` n `51` status `ready` deltaP `23.4965` edge `0.9263` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.7616` n `51` status `ready` deltaP `48.9481` edge `0.169` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.7546` n `51` status `ready` deltaP `27.0804` edge `0.2094` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6209` n `51` status `ready` deltaP `16.784` edge `0.2203` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.237` n `51` status `ready` deltaP `38.0829` edge `0.0293` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.0962` n `145` status `ready` deltaP `21.3194` edge `0.0589` maxDD `-0.4407`
- `news_risk_high->metal_24h` score `1.7327` n `51` status `ready` deltaP `34.3239` edge `-0.0802` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2434` n `51` status `ready` deltaP `16.9954` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9779` n `51` status `ready` deltaP `18.7918` edge `0.0365` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9593` n `51` status `ready` deltaP `14.0064` edge `0.0263` maxDD `-0.1788`
- `news_risk_high->crypto_alt_24h` score `0.3063` n `51` status `ready` deltaP `23.9583` edge `-0.1342` maxDD `0.0`
- `news_risk_high->index_1h` score `0.2761` n `51` status `ready` deltaP `9.8714` edge `0.0049` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1919` n `51` status `ready` deltaP `8.5388` edge `-0.0101` maxDD `-0.4666`
- `market_context_high->unknown_24h` score `0.1374` n `92` status `ready` deltaP `5.0574` edge `0.0284` maxDD `-1.0533`
- `news_risk_high->metal_1h` score `-0.131` n `51` status `ready` deltaP `1.8933` edge `-0.0071` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1851` n `51` status `ready` deltaP `7.063` edge `-0.0094` maxDD `-0.249`
- `market_context_high->metal_4h` score `-0.1981` n `145` status `ready` deltaP `7.9825` edge `-0.0155` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `-0.2247` n `148` status `ready` deltaP `9.4311` edge `-0.0367` maxDD `-1.5916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
