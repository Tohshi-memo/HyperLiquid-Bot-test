# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T19:07:44.352897+00:00`
- Price records: `672`
- Market context records: `4018`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10566`

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

- `risk_on_high->unknown_4h` score `146.4569` n `40` status `ready` deltaP `-5.2093` edge `12.4211` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `146.4569` n `40` status `ready` deltaP `-5.2093` edge `12.4211` maxDD `-10.864`
- `market_context_high->unknown_24h` score `48.7209` n `134` status `ready` deltaP `-4.1194` edge `4.4904` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `26.4568` n `145` status `ready` deltaP `2.1183` edge `2.7329` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `6.7016` n `40` status `ready` deltaP `38.9948` edge `0.2985` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.7016` n `40` status `ready` deltaP `38.9948` edge `0.2985` maxDD `0.0`
- `market_context_high->index_24h` score `3.7266` n `134` status `ready` deltaP `25.9435` edge `0.1588` maxDD `-1.3629`
- `risk_on_high->equity_4h` score `3.4118` n `40` status `ready` deltaP `35.8562` edge `0.05` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.4118` n `40` status `ready` deltaP `35.8562` edge `0.05` maxDD `-0.0446`
- `market_context_high->metal_24h` score `2.7399` n `134` status `ready` deltaP `13.9541` edge `0.234` maxDD `-4.8962`
- `market_context_high->equity_4h` score `1.7122` n `145` status `ready` deltaP `19.0459` edge `0.1438` maxDD `-6.9137`
- `market_context_high->equity_1h` score `1.3073` n `148` status `ready` deltaP `8.8809` edge `0.1057` maxDD `-2.144`
- `risk_on_high->index_24h` score `1.2844` n `40` status `ready` deltaP `26.6898` edge `-0.0709` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.2844` n `40` status `ready` deltaP `26.6898` edge `-0.0709` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.0694` n `40` status `ready` deltaP `19.0753` edge `0.0285` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0694` n `40` status `ready` deltaP `19.0753` edge `0.0285` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `0.9984` n `148` status `ready` deltaP `9.767` edge `0.0723` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `0.9656` n `40` status `ready` deltaP `4.2028` edge `0.2806` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.9656` n `40` status `ready` deltaP `4.2028` edge `0.2806` maxDD `-12.9187`
- `market_context_high->equity_24h` score `0.7515` n `134` status `ready` deltaP `15.8605` edge `0.2567` maxDD `-14.318`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
