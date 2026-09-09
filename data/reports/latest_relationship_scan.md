# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T04:37:26.645836+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10200`

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

- `risk_on_high->crypto_alt_24h` score `7.6094` n `117` status `ready` deltaP `18.9904` edge `0.5305` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `7.6094` n `117` status `ready` deltaP `18.9904` edge `0.5305` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `6.0901` n `117` status `ready` deltaP `32.9216` edge `0.3252` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `6.0901` n `117` status `ready` deltaP `32.9216` edge `0.3252` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.1072` n `117` status `ready` deltaP `23.3896` edge `0.2722` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.1072` n `117` status `ready` deltaP `23.3896` edge `0.2722` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.0808` n `117` status `ready` deltaP `17.4546` edge `0.8136` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.0808` n `117` status `ready` deltaP `17.4546` edge `0.8136` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `2.562` n `241` status `ready` deltaP `11.6456` edge `0.2186` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.5729` n `117` status `ready` deltaP `17.4012` edge `0.0193` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.5729` n `117` status `ready` deltaP `17.4012` edge `0.0193` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `1.0472` n `117` status `ready` deltaP `4.6958` edge `0.0912` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0472` n `117` status `ready` deltaP `4.6958` edge `0.0912` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.8515` n `241` status `ready` deltaP `12.4964` edge `0.027` maxDD `-0.1483`
- `risk_on_high->metal_1h` score `0.1897` n `117` status `ready` deltaP `8.6315` edge `-0.0002` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1897` n `117` status `ready` deltaP `8.6315` edge `-0.0002` maxDD `-0.3081`
- `risk_on_high->equity_1h` score `0.144` n `117` status `ready` deltaP `12.2768` edge `-0.0167` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.144` n `117` status `ready` deltaP `12.2768` edge `-0.0167` maxDD `-2.2516`
- `risk_on_high->index_1h` score `0.1367` n `117` status `ready` deltaP `8.8196` edge `-0.0049` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1367` n `117` status `ready` deltaP `8.8196` edge `-0.0049` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
