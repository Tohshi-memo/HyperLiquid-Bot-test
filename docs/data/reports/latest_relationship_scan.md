# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T17:22:29.307587+00:00`
- Price records: `672`
- Market context records: `7586`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14550`

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

- `market_context_high->commodity_4h` score `0.129` n `156` status `ready` deltaP `9.2331` edge `0.0252` maxDD `-2.4139`
- `market_context_high->index_1h` score `0.0376` n `156` status `ready` deltaP `6.0985` edge `0.013` maxDD `-0.9072`
- `market_context_high->commodity_24h` score `0.0002` n `148` status `ready` deltaP `13.0897` edge `0.0711` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.2086` n `156` status `ready` deltaP `5.4804` edge `0.0033` maxDD `-1.5775`
- `market_context_high->unknown_24h` score `-0.2518` n `149` status `ready` deltaP `10.0403` edge `0.0993` maxDD `-7.881`
- `market_context_high->crypto_alt_1h` score `-0.4318` n `156` status `ready` deltaP `0.833` edge `0.0137` maxDD `-3.6359`
- `market_context_high->crypto_major_1h` score `-0.4471` n `156` status `ready` deltaP `6.4947` edge `0.0146` maxDD `-5.5504`
- `market_context_high->fx_24h` score `-0.5041` n `148` status `ready` deltaP `8.3577` edge `0.0158` maxDD `-3.4152`
- `market_context_high->equity_1h` score `-0.5566` n `156` status `ready` deltaP `5.9078` edge `0.0588` maxDD `-8.8965`
- `market_context_high->index_4h` score `-0.5802` n `156` status `ready` deltaP `9.8624` edge `0.0325` maxDD `-3.4775`
- `market_context_high->fx_1h` score `-0.5869` n `156` status `ready` deltaP `0.2888` edge `-0.0009` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.8743` n `156` status `ready` deltaP `2.0536` edge `0.018` maxDD `-1.0307`
- `market_context_high->unknown_1h` score `-0.9619` n `156` status `ready` deltaP `0.2149` edge `-0.0624` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.1532` n `156` status `ready` deltaP `1.9543` edge `0.0489` maxDD `-10.1158`
- `market_context_high->crypto_major_4h` score `-1.6114` n `156` status `ready` deltaP `6.2579` edge `0.0554` maxDD `-16.63`
- `market_context_high->metal_4h` score `-1.6385` n `156` status `ready` deltaP `-1.3758` edge `0.0473` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.6631` n `156` status `ready` deltaP `2.4759` edge `0.207` maxDD `-21.9375`
- `market_context_high->fx_4h` score `-2.2932` n `156` status `ready` deltaP `-3.0052` edge `-0.0026` maxDD `-2.1439`
- `market_context_high->unknown_4h` score `-2.7974` n `156` status `ready` deltaP `10.0962` edge `-0.1953` maxDD `-5.7848`
- `market_context_high->metal_24h` score `-2.9202` n `149` status `ready` deltaP `-3.8206` edge `0.0899` maxDD `-13.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
