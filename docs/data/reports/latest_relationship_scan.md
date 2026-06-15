# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T20:08:25.514521+00:00`
- Price records: `672`
- Market context records: `4022`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10720`

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

- `risk_on_high->unknown_4h` score `146.1082` n `40` status `ready` deltaP `-5.8181` edge `12.3961` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `146.1082` n `40` status `ready` deltaP `-5.8181` edge `12.3961` maxDD `-10.864`
- `market_context_high->unknown_24h` score `48.1195` n `134` status `ready` deltaP `-4.8126` edge `4.4449` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `25.774` n `148` status `ready` deltaP `2.2224` edge `2.6753` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `6.2297` n `40` status `ready` deltaP `38.3016` edge `0.2638` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.2297` n `40` status `ready` deltaP `38.3016` edge `0.2638` maxDD `0.0`
- `market_context_high->index_24h` score `3.4552` n `134` status `ready` deltaP `25.2502` edge `0.1408` maxDD `-1.3629`
- `risk_on_high->equity_4h` score `3.2436` n `40` status `ready` deltaP `35.704` edge `0.037` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.2436` n `40` status `ready` deltaP `35.704` edge `0.037` maxDD `-0.0446`
- `market_context_high->metal_24h` score `2.3916` n `134` status `ready` deltaP `13.2608` edge `0.2096` maxDD `-4.8962`
- `market_context_high->equity_4h` score `2.1045` n `148` status `ready` deltaP `18.6094` edge `0.1794` maxDD `-6.9137`
- `market_context_high->equity_1h` score `1.1593` n `152` status `ready` deltaP `7.946` edge `0.0996` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `1.039` n `40` status `ready` deltaP `18.7709` edge `0.028` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.039` n `40` status `ready` deltaP `18.7709` edge `0.028` maxDD `-2.6576`
- `risk_on_high->index_24h` score `1.0129` n `40` status `ready` deltaP `25.9965` edge `-0.0889` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.0129` n `40` status `ready` deltaP `25.9965` edge `-0.0889` maxDD `0.0`
- `risk_on_high->commodity_24h` score `0.9284` n `40` status `ready` deltaP `4.2028` edge `0.2775` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.9284` n `40` status `ready` deltaP `4.2028` edge `0.2775` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `0.6767` n `152` status `ready` deltaP `8.1311` edge `0.0564` maxDD `-2.3372`
- `market_context_high->metal_1h` score `0.5547` n `152` status `ready` deltaP `10.9163` edge `0.0534` maxDD `-2.4051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
