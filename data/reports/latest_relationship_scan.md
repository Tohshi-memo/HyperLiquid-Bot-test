# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T05:52:24.347046+00:00`
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

- `news_risk_high->crypto_alt_24h` score `7.0425` n `32` status `ready` deltaP `30.3819` edge `0.3957` maxDD `-0.2431`
- `news_risk_high->crypto_major_4h` score `4.6665` n `32` status `ready` deltaP `23.4756` edge `0.2525` maxDD `-0.6101`
- `news_risk_high->commodity_24h` score `4.0195` n `32` status `ready` deltaP `20.1389` edge `0.2007` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `3.4813` n `32` status `ready` deltaP `19.9653` edge `0.3078` maxDD `-9.7301`
- `news_risk_high->metal_4h` score `2.3606` n `32` status `ready` deltaP `22.7896` edge `0.0669` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `2.2498` n `32` status `ready` deltaP `12.1951` edge `0.1221` maxDD `-0.2737`
- `risk_on_high->crypto_major_24h` score `1.9527` n `89` status `ready` deltaP `13.0131` edge `0.8962` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `1.9527` n `89` status `ready` deltaP `13.0131` edge `0.8962` maxDD `-47.9416`
- `news_risk_high->fx_24h` score `1.7753` n `32` status `ready` deltaP `27.7778` edge `0.0416` maxDD `-2.9744`
- `news_risk_high->index_1h` score `1.606` n `32` status `ready` deltaP `19.0307` edge `0.0162` maxDD `-0.0724`
- `market_context_high->equity_24h` score `1.4573` n `172` status `ready` deltaP `13.3923` edge `0.386` maxDD `-16.9737`
- `news_risk_high->equity_1h` score `1.3667` n `32` status `ready` deltaP `8.5891` edge `0.0957` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `0.9584` n `32` status `ready` deltaP `10.872` edge `0.0267` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `0.7396` n `32` status `ready` deltaP `2.3578` edge `0.0642` maxDD `-0.4628`
- `news_risk_high->crypto_alt_4h` score `0.1876` n `32` status `ready` deltaP `3.7348` edge `0.0236` maxDD `-1.296`
- `news_risk_high->crypto_alt_1h` score `0.0766` n `32` status `ready` deltaP `3.2373` edge `0.0113` maxDD `-0.7867`
- `news_risk_high->commodity_1h` score `0.0093` n `32` status `ready` deltaP `6.2126` edge `0.0044` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1363` n `145` status `ready` deltaP `8.0487` edge `0.0001` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
