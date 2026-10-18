# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T08:22:29.282373+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10390`

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

- `market_context_high->commodity_24h` score `2.8454` n `116` status `ready` deltaP `20.0499` edge `0.1886` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `2.4052` n `75` status `ready` deltaP `19.4866` edge `0.1503` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `2.4052` n `75` status `ready` deltaP `19.4866` edge `0.1503` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `2.1046` n `143` status `ready` deltaP `17.5103` edge `0.3991` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.7417` n `143` status `ready` deltaP `5.5955` edge `0.1134` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.2207` n `91` status `ready` deltaP `13.9139` edge `0.1836` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.2207` n `91` status `ready` deltaP `13.9139` edge `0.1836` maxDD `-11.1788`
- `market_context_high->crypto_alt_1h` score `0.2041` n `143` status `ready` deltaP `6.9899` edge `0.1204` maxDD `-7.3329`
- `risk_on_high->index_1h` score `-0.0521` n `91` status `ready` deltaP `4.2553` edge `0.0057` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0521` n `91` status `ready` deltaP `4.2553` edge `0.0057` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2718` n `91` status `ready` deltaP `0.8976` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2718` n `91` status `ready` deltaP `0.8976` edge `-0.0028` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.2876` n `143` status `ready` deltaP `6.1901` edge `0.0088` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.3804` n `143` status `ready` deltaP `5.8538` edge `0.0041` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.456` n `91` status `ready` deltaP `9.2582` edge `0.0299` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.456` n `91` status `ready` deltaP `9.2582` edge `0.0299` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4852` n `91` status `ready` deltaP `0.9952` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4852` n `91` status `ready` deltaP `0.9952` edge `0.0043` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5456` n `143` status `ready` deltaP `6.5006` edge `0.0449` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.7363` n `143` status `ready` deltaP `-1.1005` edge `-0.0019` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
