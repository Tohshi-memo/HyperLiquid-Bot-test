# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T07:22:27.621656+00:00`
- Price records: `672`
- Market context records: `3260`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10500`

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

- `risk_on_high->crypto_major_4h` score `16.7648` n `31` status `ready` deltaP `31.0041` edge `1.3026` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.7648` n `31` status `ready` deltaP `31.0041` edge `1.3026` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.8148` n `103` status `ready` deltaP `16.0463` edge `2.6483` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `12.8874` n `103` status `ready` deltaP `45.9109` edge `0.8107` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.188` n `103` status `ready` deltaP `29.9268` edge `0.8216` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.244` n `103` status `ready` deltaP `17.6595` edge `1.5244` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `5.128` n `31` status `ready` deltaP `11.9788` edge `0.762` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.128` n `31` status `ready` deltaP `11.9788` edge `0.762` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.2474` n `31` status `ready` deltaP `18.809` edge `0.5326` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.2474` n `31` status `ready` deltaP `18.809` edge `0.5326` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.3928` n `157` status `ready` deltaP `20.2977` edge `0.1599` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.1897` n `32` status `ready` deltaP `8.0651` edge `0.3339` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.1897` n `32` status `ready` deltaP `8.0651` edge `0.3339` maxDD `-5.8885`
- `risk_on_high->index_4h` score `1.5749` n `31` status `ready` deltaP `5.7533` edge `0.2223` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.5749` n `31` status `ready` deltaP `5.7533` edge `0.2223` maxDD `-1.7001`
- `market_context_high->crypto_major_24h` score `1.3647` n `103` status `ready` deltaP `19.4225` edge `2.1154` maxDD `-152.2601`
- `risk_on_high->crypto_alt_1h` score `0.3163` n `32` status `ready` deltaP `1.3473` edge `0.1753` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.3163` n `32` status `ready` deltaP `1.3473` edge `0.1753` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.311` n `32` status `ready` deltaP `6.25` edge `0.0667` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.311` n `32` status `ready` deltaP `6.25` edge `0.0667` maxDD `-1.4793`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
