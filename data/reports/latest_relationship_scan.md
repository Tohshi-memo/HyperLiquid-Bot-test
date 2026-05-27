# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T02:22:16.699493+00:00`
- Price records: `672`
- Market context records: `1999`
- Flow alert records: `7646`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7585`

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

- `market_context_high->crypto_major_4h` score `8.6474` n `220` status `ready` deltaP `30.4074` edge `0.5709` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.0256` n `220` status `ready` deltaP `23.9053` edge `0.6239` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.1599` n `220` status `ready` deltaP `17.3864` edge `0.389` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.624` n `220` status `ready` deltaP `15.8121` edge `0.2227` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.4331` n `185` status `ready` deltaP `15.6599` edge `0.6304` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.6456` n `185` status `ready` deltaP `16.7447` edge `0.2681` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `1.3282` n `220` status `ready` deltaP `11.2194` edge `0.1345` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.1368` n `185` status `ready` deltaP `14.4715` edge `0.4881` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `1.0623` n `220` status `ready` deltaP `9.2842` edge `0.138` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.9145` n `220` status `ready` deltaP `9.296` edge `0.0826` maxDD `-1.8022`
- `market_context_high->fx_24h` score `0.7283` n `185` status `ready` deltaP `16.2643` edge `0.0297` maxDD `-1.1952`
- `market_context_high->crypto_major_24h` score `0.5107` n `185` status `ready` deltaP `20.4212` edge `0.765` maxDD `-62.3533`
- `market_context_high->index_24h` score `0.0837` n `185` status `ready` deltaP `2.7472` edge `0.1115` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.0356` n `220` status `ready` deltaP `4.9755` edge `0.0427` maxDD `-2.6402`
- `market_context_high->index_1h` score `-0.5762` n `220` status `ready` deltaP `0.1089` edge `0.0103` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.6139` n `220` status `ready` deltaP `-2.2618` edge `-0.0004` maxDD `-0.3914`
- `market_context_high->unknown_1h` score `-0.8814` n `220` status `ready` deltaP `2.4769` edge `-0.018` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.9476` n `220` status `ready` deltaP `1.6794` edge `0.0009` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.114` n `220` status `ready` deltaP `-7.766` edge `-0.0029` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.8311` n `220` status `ready` deltaP `2.7218` edge `0.0029` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
