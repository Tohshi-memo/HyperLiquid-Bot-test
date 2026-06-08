# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T20:07:25.909629+00:00`
- Price records: `672`
- Market context records: `3312`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_4h` score `15.8903` n `32` status `ready` deltaP `30.1829` edge `1.2352` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8903` n `32` status `ready` deltaP `30.1829` edge `1.2352` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `15.0296` n `128` status `ready` deltaP `21.0937` edge `2.7704` maxDD `-70.3986`
- `market_context_high->index_24h` score `10.5507` n `128` status `ready` deltaP `32.7256` edge `0.9165` maxDD `-16.1026`
- `market_context_high->equity_24h` score `8.7915` n `128` status `ready` deltaP `24.7396` edge `1.8038` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.3563` n `32` status `ready` deltaP `9.8323` edge `0.7319` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3563` n `32` status `ready` deltaP `9.8323` edge `0.7319` maxDD `-11.7537`
- `market_context_high->commodity_24h` score `5.8121` n `128` status `ready` deltaP `30.0347` edge `0.5446` maxDD `-14.1725`
- `risk_on_high->equity_4h` score `3.5804` n `32` status `ready` deltaP `13.7957` edge `0.4805` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5804` n `32` status `ready` deltaP `13.7957` edge `0.4805` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.9254` n `128` status `ready` deltaP `22.1355` edge `2.2974` maxDD `-152.2601`
- `risk_on_high->crypto_major_1h` score `2.0743` n `32` status `ready` deltaP `7.1669` edge `0.3251` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0743` n `32` status `ready` deltaP `7.1669` edge `0.3251` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.0052` n `185` status `ready` deltaP `18.6626` edge `0.1385` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.0915` n `32` status `ready` deltaP `0.8384` edge `0.1931` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.0915` n `32` status `ready` deltaP `0.8384` edge `0.1931` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2868` n `32` status `ready` deltaP `6.3997` edge `0.0626` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2868` n `32` status `ready` deltaP `6.3997` edge `0.0626` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2462` n `32` status `ready` deltaP `0.5988` edge `0.1713` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2462` n `32` status `ready` deltaP `0.5988` edge `0.1713` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
