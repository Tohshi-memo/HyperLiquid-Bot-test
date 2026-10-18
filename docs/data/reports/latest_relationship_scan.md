# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T22:07:23.926697+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8502`

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

- `market_context_high->crypto_major_4h` score `1.936` n `103` status `ready` deltaP `18.5783` edge `0.4648` maxDD `-15.2359`
- `market_context_high->commodity_24h` score `1.9199` n `103` status `ready` deltaP `16.6264` edge `0.1343` maxDD `-1.8119`
- `risk_on_high->crypto_major_4h` score `1.3844` n `70` status `ready` deltaP `18.3841` edge `0.303` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.3844` n `70` status `ready` deltaP `18.3841` edge `0.303` maxDD `-11.1788`
- `risk_on_high->commodity_24h` score `1.0372` n `70` status `ready` deltaP `17.5279` edge `0.0959` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.0372` n `70` status `ready` deltaP `17.5279` edge `0.0959` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.6975` n `103` status `ready` deltaP `8.1027` edge `0.1243` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.176` n `70` status `ready` deltaP `8.4857` edge `0.0044` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.176` n `70` status `ready` deltaP `8.4857` edge `0.0044` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2427` n `70` status `ready` deltaP `1.2784` edge `-0.0024` maxDD `-0.3121`
- `risk_on_and_context->fx_1h` score `-0.2427` n `70` status `ready` deltaP `1.2784` edge `-0.0024` maxDD `-0.3121`
- `market_context_high->crypto_alt_1h` score `-0.2973` n `103` status `ready` deltaP `1.8414` edge `0.0996` maxDD `-7.3329`
- `risk_on_high->crypto_major_1h` score `-0.3469` n `70` status `ready` deltaP `2.7074` edge `0.0294` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.3469` n `70` status `ready` deltaP `2.7074` edge `0.0294` maxDD `-4.6876`
- `market_context_high->index_1h` score `-0.3903` n `103` status `ready` deltaP `3.659` edge `0.0004` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.4254` n `70` status `ready` deltaP `11.1111` edge `0.0201` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4254` n `70` status `ready` deltaP `11.1111` edge `0.0201` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.6169` n `70` status `ready` deltaP `-1.6724` edge `0.0052` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.6169` n `70` status `ready` deltaP `-1.6724` edge `0.0052` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.6964` n `103` status `ready` deltaP `-0.117` edge `0.0452` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
