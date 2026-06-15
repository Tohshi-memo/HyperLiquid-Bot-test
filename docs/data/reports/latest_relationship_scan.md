# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T21:37:39.331780+00:00`
- Price records: `672`
- Market context records: `4028`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10624`

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

- `risk_on_high->unknown_4h` score `145.9092` n `40` status `ready` deltaP `-6.2195` edge `12.3822` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.9092` n `40` status `ready` deltaP `-6.2195` edge `12.3822` maxDD `-10.864`
- `market_context_high->unknown_24h` score `47.4063` n `134` status `ready` deltaP `-5.8525` edge `4.3924` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `25.5751` n `148` status `ready` deltaP `1.821` edge `2.6614` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `5.5813` n `40` status `ready` deltaP `37.2617` edge `0.2167` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.5813` n `40` status `ready` deltaP `37.2617` edge `0.2167` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.2111` n `40` status `ready` deltaP `35.7622` edge `0.0339` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.2111` n `40` status `ready` deltaP `35.7622` edge `0.0339` maxDD `-0.0446`
- `market_context_high->index_24h` score `3.108` n `134` status `ready` deltaP `24.2104` edge `0.1188` maxDD `-1.3629`
- `market_context_high->equity_4h` score `2.072` n `148` status `ready` deltaP `18.6676` edge `0.1763` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.9052` n `134` status `ready` deltaP `12.221` edge `0.176` maxDD `-4.8962`
- `market_context_high->equity_1h` score `1.1843` n `156` status `ready` deltaP `8.4984` edge `0.098` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.9809` n `40` status `ready` deltaP `18.689` edge `0.0237` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9809` n `40` status `ready` deltaP `18.689` edge `0.0237` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.8143` n `40` status `ready` deltaP `3.8562` edge `0.2703` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.8143` n `40` status `ready` deltaP `3.8562` edge `0.2703` maxDD `-12.9187`
- `risk_on_high->index_24h` score `0.6657` n `40` status `ready` deltaP `24.9567` edge `-0.1109` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.6657` n `40` status `ready` deltaP `24.9567` edge `-0.1109` maxDD `0.0`
- `market_context_high->crypto_major_1h` score `0.5466` n `156` status `ready` deltaP `7.6693` edge `0.0554` maxDD `-2.8785`
- `market_context_high->metal_1h` score `0.4194` n `156` status `ready` deltaP `9.98` edge `0.0498` maxDD `-3.0049`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
