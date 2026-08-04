# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T11:37:24.218148+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9833`

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

- `market_context_high->unknown_24h` score `36.6256` n `46` status `ready` deltaP `22.9997` edge `2.9031` maxDD `-0.0103`
- `market_context_high->commodity_24h` score `7.9584` n `46` status `ready` deltaP `36.8735` edge `0.4353` maxDD `-0.434`
- `market_context_high->crypto_alt_24h` score `7.8407` n `46` status `ready` deltaP `41.0477` edge `0.3971` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `5.4933` n `88` status `ready` deltaP `1.0532` edge `0.5503` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1786` n `88` status `ready` deltaP `15.2162` edge `0.0814` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.2369` n `88` status `ready` deltaP `16.2555` edge `0.008` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2171` n `89` status `ready` deltaP `5.8047` edge `0.021` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1362` n `89` status `ready` deltaP `7.4548` edge `-0.0035` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4605` n `89` status `ready` deltaP `1.6148` edge `-0.0164` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5254` n `89` status `ready` deltaP `-1.3826` edge `-0.0087` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6238` n `88` status `ready` deltaP `3.8249` edge `0.018` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9662` n `88` status `ready` deltaP `3.2567` edge `-0.0066` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2141` n `89` status `ready` deltaP `-2.883` edge `-0.0109` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5937` n `89` status `ready` deltaP `4.9872` edge `-0.084` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9028` n `88` status `ready` deltaP `-10.7262` edge `-0.047` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-2.0503` n `46` status `ready` deltaP `-7.8729` edge `0.0022` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.5093` n `89` status `ready` deltaP `1.9125` edge `-0.2605` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5841` n `89` status `ready` deltaP `-12.696` edge `-0.0767` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-5.0275` n `46` status `ready` deltaP `-25.2038` edge `-0.1341` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-7.0423` n `88` status `ready` deltaP `-1.4967` edge `-0.3598` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
