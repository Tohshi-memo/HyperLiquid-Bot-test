# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T08:37:29.088848+00:00`
- Price records: `672`
- Market context records: `3265`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10503`

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

- `risk_on_high->crypto_major_4h` score `16.6271` n `32` status `ready` deltaP `32.0122` edge `1.2844` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.6271` n `32` status `ready` deltaP `32.0122` edge `1.2844` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.7886` n `103` status `ready` deltaP `15.8727` edge `2.6461` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `12.6055` n `103` status `ready` deltaP `45.0429` edge `0.793` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.1031` n `103` status `ready` deltaP `29.406` edge `0.818` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.9388` n `32` status `ready` deltaP `13.0335` edge `0.7591` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.9388` n `32` status `ready` deltaP `13.0335` edge `0.7591` maxDD `-11.7537`
- `market_context_high->equity_24h` score `6.2416` n `103` status `ready` deltaP `17.6595` edge `1.5241` maxDD `-53.663`
- `risk_on_high->equity_4h` score `4.0232` n `32` status `ready` deltaP `16.3872` edge `0.52` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.0232` n `32` status `ready` deltaP `16.3872` edge `0.52` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.269` n `162` status `ready` deltaP `19.9356` edge `0.152` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.2006` n `32` status `ready` deltaP `8.0651` edge `0.3353` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.2006` n `32` status `ready` deltaP `8.0651` edge `0.3353` maxDD `-5.8885`
- `risk_on_high->index_4h` score `1.4153` n `32` status `ready` deltaP `3.7348` edge `0.2153` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.4153` n `32` status `ready` deltaP `3.7348` edge `0.2153` maxDD `-1.7001`
- `market_context_high->crypto_major_24h` score `1.1269` n `103` status `ready` deltaP `18.5545` edge `2.0907` maxDD `-152.2601`
- `risk_on_high->metal_1h` score `0.3336` n `32` status `ready` deltaP `6.5494` edge `0.0676` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3336` n `32` status `ready` deltaP `6.5494` edge `0.0676` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.3085` n `32` status `ready` deltaP `1.3473` edge `0.1743` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.3085` n `32` status `ready` deltaP `1.3473` edge `0.1743` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
