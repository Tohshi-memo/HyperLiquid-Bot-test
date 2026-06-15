# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T19:52:47.573744+00:00`
- Price records: `672`
- Market context records: `4021`
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

- `risk_on_high->unknown_4h` score `146.1995` n `40` status `ready` deltaP `-5.6659` edge `12.4027` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `146.1995` n `40` status `ready` deltaP `-5.6659` edge `12.4027` maxDD `-10.864`
- `market_context_high->unknown_24h` score `48.2617` n `134` status `ready` deltaP `-4.6393` edge `4.4556` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `25.9438` n `147` status `ready` deltaP `2.1402` edge `2.69` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `6.348` n `40` status `ready` deltaP `38.4749` edge `0.2725` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.348` n `40` status `ready` deltaP `38.4749` edge `0.2725` maxDD `0.0`
- `market_context_high->index_24h` score `3.523` n `134` status `ready` deltaP `25.4235` edge `0.1453` maxDD `-1.3629`
- `risk_on_high->equity_4h` score `3.2267` n `40` status `ready` deltaP `35.5518` edge `0.0366` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.2267` n `40` status `ready` deltaP `35.5518` edge `0.0366` maxDD `-0.0446`
- `market_context_high->metal_24h` score `2.4811` n `134` status `ready` deltaP `13.4342` edge `0.2159` maxDD `-4.8962`
- `market_context_high->equity_4h` score `2.1601` n `147` status `ready` deltaP `19.0042` edge `0.1814` maxDD `-6.9137`
- `market_context_high->equity_1h` score `1.1408` n `151` status `ready` deltaP `7.7151` edge `0.0996` maxDD `-2.144`
- `risk_on_high->index_24h` score `1.0808` n `40` status `ready` deltaP `26.1698` edge `-0.0844` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.0808` n `40` status `ready` deltaP `26.1698` edge `-0.0844` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.0402` n `40` status `ready` deltaP `18.7709` edge `0.0281` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0402` n `40` status `ready` deltaP `18.7709` edge `0.0281` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.9404` n `40` status `ready` deltaP `4.2028` edge `0.2785` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.9404` n `40` status `ready` deltaP `4.2028` edge `0.2785` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `0.7556` n `151` status `ready` deltaP `8.532` edge `0.0603` maxDD `-2.3372`
- `market_context_high->metal_1h` score `0.5518` n `151` status `ready` deltaP `10.8002` edge `0.0538` maxDD `-2.4051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
