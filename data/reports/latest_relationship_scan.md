# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T23:07:26.611510+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `risk_on_high->crypto_alt_24h` score `23.2432` n `52` status `ready` deltaP `48.7847` edge `1.6117` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `23.2432` n `52` status `ready` deltaP `48.7847` edge `1.6117` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `10.6975` n `52` status `ready` deltaP `30.4621` edge `0.7474` maxDD `-3.3886`
- `risk_on_and_context->crypto_major_24h` score `10.6975` n `52` status `ready` deltaP `30.4621` edge `0.7474` maxDD `-3.3886`
- `risk_on_high->unknown_4h` score `8.8355` n `82` status `ready` deltaP `30.3354` edge `0.5769` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.8355` n `82` status `ready` deltaP `30.3354` edge `0.5769` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.1801` n `52` status `ready` deltaP `69.2708` edge `0.0532` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.1801` n `52` status `ready` deltaP `69.2708` edge `0.0532` maxDD `0.0`
- `market_context_high->unknown_4h` score `5.0909` n `149` status `ready` deltaP `21.054` edge `0.3309` maxDD `-1.0945`
- `risk_on_high->metal_24h` score `4.7039` n `52` status `ready` deltaP `42.8018` edge `0.1372` maxDD `-0.4443`
- `risk_on_and_context->metal_24h` score `4.7039` n `52` status `ready` deltaP `42.8018` edge `0.1372` maxDD `-0.4443`
- `risk_on_high->unknown_1h` score `4.4249` n `92` status `ready` deltaP `11.7418` edge `0.3149` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `4.4249` n `92` status `ready` deltaP `11.7418` edge `0.3149` maxDD `-0.2885`
- `market_context_high->crypto_major_24h` score `4.3691` n `117` status `ready` deltaP `17.4279` edge `0.497` maxDD `-17.2607`
- `market_context_high->metal_24h` score `4.134` n `117` status `ready` deltaP `32.9728` edge `0.2266` maxDD `-3.1535`
- `market_context_high->crypto_alt_24h` score `3.7233` n `117` status `ready` deltaP `18.0155` edge `0.7762` maxDD `-27.517`
- `market_context_high->unknown_1h` score `2.9962` n `161` status `ready` deltaP `10.3442` edge `0.2216` maxDD `-0.9372`
- `risk_on_high->equity_24h` score `2.8543` n `52` status `ready` deltaP `23.3307` edge `0.1184` maxDD `-1.2199`
- `risk_on_and_context->equity_24h` score `2.8543` n `52` status `ready` deltaP `23.3307` edge `0.1184` maxDD `-1.2199`
- `risk_on_high->index_24h` score `1.5152` n `52` status `ready` deltaP `21.9818` edge `0.0048` maxDD `-0.3393`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
