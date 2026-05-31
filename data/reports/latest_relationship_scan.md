# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T22:22:17.902945+00:00`
- Price records: `672`
- Market context records: `2501`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9248`

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

- `market_context_high->unknown_24h` score `5.4715` n `124` status `ready` deltaP `19.8869` edge `0.3562` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.2762` n `149` status `ready` deltaP `21.2023` edge `0.4829` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.64` n `149` status `ready` deltaP `17.4507` edge `0.368` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1586` n `124` status `ready` deltaP `12.78` edge `0.5808` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.585` n `149` status `ready` deltaP `10.5234` edge `0.1669` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.4993` n `156` status `ready` deltaP `6.6214` edge `0.1162` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `0.4707` n `124` status `ready` deltaP `3.0129` edge `0.736` maxDD `-43.6595`
- `market_context_high->crypto_major_1h` score `0.3831` n `156` status `ready` deltaP `6.9208` edge `0.1052` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.1384` n `124` status `ready` deltaP `4.3514` edge `0.0806` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1329` n `124` status `ready` deltaP `18.4084` edge `0.0189` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1484` n `149` status `ready` deltaP `6.7779` edge `0.0266` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.3005` n `156` status `ready` deltaP `1.5815` edge `0.0044` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.4618` n `156` status `ready` deltaP `3.2896` edge `0.0067` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.5537` n `156` status `ready` deltaP `-0.4107` edge `0.006` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.5779` n `156` status `ready` deltaP `-0.2764` edge `0.0037` maxDD `-3.0759`
- `market_context_high->unknown_1h` score `-0.6117` n `156` status `ready` deltaP `1.7081` edge `0.0096` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-0.6558` n `149` status `ready` deltaP `-0.977` edge `0.0084` maxDD `-0.8774`
- `market_context_high->metal_4h` score `-0.6621` n `149` status `ready` deltaP `1.6737` edge `0.0427` maxDD `-4.7664`
- `market_context_high->fx_24h` score `-0.9026` n `124` status `ready` deltaP `2.8506` edge `0.0038` maxDD `-2.7484`
- `market_context_high->equity_1h` score `-0.9153` n `156` status `ready` deltaP `-0.5872` edge `0.0115` maxDD `-2.7085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
