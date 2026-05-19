# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T22:22:25.537407+00:00`
- Price records: `672`
- Market context records: `1261`
- Flow alert records: `5538`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_major_24h` score `17.9521` n `128` status `ready` deltaP `41.5798` edge `1.332` maxDD `-8.0553`
- `market_context_high->metal_24h` score `9.1603` n `128` status `ready` deltaP `4.1667` edge `0.9023` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `8.1249` n `128` status `ready` deltaP `5.3735` edge `0.7629` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `8.0316` n `128` status `ready` deltaP `23.5243` edge `0.7141` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.5395` n `128` status `ready` deltaP `25.1736` edge `0.3191` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.5614` n `128` status `ready` deltaP `18.6166` edge `0.239` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.4804` n `128` status `ready` deltaP `23.2639` edge `0.5238` maxDD `-14.2815`
- `market_context_high->commodity_24h` score `2.6602` n `128` status `ready` deltaP `-10.4167` edge `0.4393` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `2.265` n `128` status `ready` deltaP `1.5625` edge `0.4513` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.7002` n `128` status `ready` deltaP `14.6532` edge `0.1123` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.8186` n `132` status `ready` deltaP `11.1913` edge `0.0253` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.7951` n `132` status `ready` deltaP `7.4305` edge `0.0536` maxDD `-1.2834`
- `market_context_high->metal_4h` score `0.6461` n `128` status `ready` deltaP `17.4353` edge `0.0807` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.4036` n `132` status `ready` deltaP `12.026` edge `0.0145` maxDD `-2.2164`
- `market_context_high->crypto_major_4h` score `0.1998` n `128` status `ready` deltaP `7.984` edge `0.1645` maxDD `-8.3693`
- `market_context_high->fx_24h` score `0.1572` n `128` status `ready` deltaP `4.2535` edge `0.0312` maxDD `-0.3831`
- `market_context_high->fx_1h` score `-0.2374` n `132` status `ready` deltaP `4.1236` edge `-0.0017` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2982` n `132` status `ready` deltaP `1.1024` edge `0.0387` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.4158` n `128` status `ready` deltaP `9.0129` edge `0.1831` maxDD `-16.7194`
- `market_context_high->crypto_major_1h` score `-0.5043` n `132` status `ready` deltaP `1.2158` edge `0.0052` maxDD `-4.2369`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
