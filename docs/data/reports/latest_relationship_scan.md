# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T06:52:25.961870+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10647`

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

- `news_risk_high->crypto_alt_24h` score `8.4787` n `30` status `ready` deltaP `35.7292` edge `0.4728` maxDD `-0.0214`
- `news_risk_high->crypto_major_24h` score `5.8677` n `30` status `ready` deltaP `23.8541` edge `0.4336` maxDD `-6.6257`
- `news_risk_high->crypto_major_4h` score `5.4207` n `30` status `ready` deltaP `28.2826` edge `0.2833` maxDD `-0.6101`
- `news_risk_high->commodity_24h` score `4.0195` n `30` status `ready` deltaP `20.1389` edge `0.2007` maxDD `0.0`
- `news_risk_high->commodity_4h` score `2.7488` n `30` status `ready` deltaP `16.7378` edge `0.1334` maxDD `-0.2737`
- `news_risk_high->metal_4h` score `2.4887` n `30` status `ready` deltaP `23.7906` edge `0.0709` maxDD `-0.7692`
- `risk_on_high->crypto_major_24h` score `2.2673` n `93` status `ready` deltaP `13.9617` edge `0.9302` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `2.2673` n `93` status `ready` deltaP `13.9617` edge `0.9302` maxDD `-47.9416`
- `news_risk_high->fx_24h` score `2.111` n `30` status `ready` deltaP `30.6945` edge `0.0418` maxDD `-2.9744`
- `news_risk_high->index_1h` score `1.4692` n `30` status `ready` deltaP `17.1557` edge `0.0173` maxDD `-0.0724`
- `market_context_high->equity_24h` score `1.2889` n `176` status `ready` deltaP `13.1471` edge `0.3736` maxDD `-16.9737`
- `news_risk_high->equity_1h` score `1.2266` n `30` status `ready` deltaP `5.998` edge `0.1013` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `0.7561` n `30` status `ready` deltaP `8.1637` edge `0.0279` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `0.5171` n `30` status `ready` deltaP `-0.5589` edge `0.0651` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.1794` n `30` status `ready` deltaP `3.8623` edge `0.0157` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.1534` n `30` status `ready` deltaP `2.3171` edge `0.0302` maxDD `-1.296`
- `news_risk_high->commodity_1h` score `0.0402` n `30` status `ready` deltaP `6.7465` edge `0.0048` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1363` n `145` status `ready` deltaP `8.0487` edge `0.0001` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
