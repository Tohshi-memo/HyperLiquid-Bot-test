# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T12:14:25.826785+00:00`
- Price records: `672`
- Market context records: `2865`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->crypto_alt_24h` score `5.6698` n `142` status `ready` deltaP `4.959` edge `0.8311` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `3.8077` n `142` status `ready` deltaP `6.942` edge `0.3175` maxDD `-1.7175`
- `market_context_high->equity_24h` score `2.7919` n `142` status `ready` deltaP `6.3038` edge `0.391` maxDD `-12.6963`
- `market_context_high->index_24h` score `1.4977` n `142` status `ready` deltaP `8.5021` edge `0.1662` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.4718` n `142` status `ready` deltaP `14.51` edge `0.3353` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.9042` n `142` status `ready` deltaP `5.7282` edge `0.1425` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.5699` n `142` status `ready` deltaP `14.6728` edge `0.0594` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0766` n `142` status `ready` deltaP `4.4805` edge `0.0496` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0251` n `142` status `ready` deltaP `4.7968` edge `0.0142` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.3174` n `142` status `ready` deltaP `4.0965` edge `0.0842` maxDD `-5.7037`
- `market_context_high->crypto_alt_1h` score `-0.5813` n `142` status `ready` deltaP `5.0962` edge `0.0675` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.5976` n `142` status `ready` deltaP `-0.4322` edge `0.0016` maxDD `-4.3601`
- `market_context_high->crypto_alt_4h` score `-0.6011` n `142` status `ready` deltaP `14.3378` edge `0.2884` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.6664` n `142` status `ready` deltaP `-2.0346` edge `0.0024` maxDD `-0.2164`
- `market_context_high->equity_1h` score `-0.7528` n `142` status `ready` deltaP `-1.7015` edge `0.0319` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.765` n `142` status `ready` deltaP `4.6745` edge `0.0577` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.7806` n `142` status `ready` deltaP `-0.7654` edge `-0.0104` maxDD `-3.0996`
- `market_context_high->commodity_4h` score `-1.2046` n `142` status `ready` deltaP `3.0573` edge `0.0172` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2381` n `142` status `ready` deltaP `-4.5152` edge `0.0048` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3879` n `142` status `ready` deltaP `-1.8852` edge `-0.0159` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
