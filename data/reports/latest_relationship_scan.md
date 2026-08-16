# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T06:52:25.931434+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `184.4559` n `88` status `ready` deltaP `-22.7923` edge `24.0685` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.3504` n `36` status `ready` deltaP `21.9815` edge `0.9206` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.5526` n `36` status `ready` deltaP `38.2622` edge `0.3743` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4149` n `88` status `ready` deltaP `41.2282` edge `0.3488` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.663` n `36` status `ready` deltaP `30.5026` edge `0.1019` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.1484` n `102` status `ready` deltaP `19.3269` edge `0.0973` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7743` n `36` status `ready` deltaP `20.376` edge `0.0252` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6999` n `36` status `ready` deltaP `7.8344` edge `0.1213` maxDD `-0.5496`
- `market_context_high->commodity_1h` score `0.0755` n `109` status `ready` deltaP `3.4376` edge `0.0238` maxDD `-0.5677`
- `market_context_high->fx_4h` score `0.0072` n `102` status `ready` deltaP `7.6937` edge `0.0101` maxDD `-0.504`
- `news_risk_high->fx_4h` score `-0.0108` n `36` status `ready` deltaP `4.0989` edge `-0.0068` maxDD `-0.0863`
- `market_context_high->fx_1h` score `-0.0428` n `109` status `ready` deltaP `3.0998` edge `0.002` maxDD `-0.2527`
- `news_risk_high->index_1h` score `-0.1401` n `36` status `ready` deltaP `-0.4324` edge `0.0138` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2113` n `36` status `ready` deltaP `0.8317` edge `-0.0017` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.5728` n `109` status `ready` deltaP `0.8158` edge `-0.0073` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.708` n `36` status `ready` deltaP `-7.9508` edge `-0.0109` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.8116` n `109` status `ready` deltaP `-7.3641` edge `-0.0028` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.0015` n `36` status `ready` deltaP `-1.6768` edge `-0.0279` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.1225` n `36` status `ready` deltaP `-6.2209` edge `-0.0213` maxDD `-0.7946`
- `market_context_high->metal_4h` score `-1.3069` n `102` status `ready` deltaP `1.2644` edge `-0.0186` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
