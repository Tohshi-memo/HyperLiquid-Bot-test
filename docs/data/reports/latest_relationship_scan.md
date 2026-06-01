# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T08:37:21.743052+00:00`
- Price records: `672`
- Market context records: `2545`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->crypto_alt_4h` score `5.4275` n `153` status `ready` deltaP `24.0734` edge `0.5597` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.4155` n `119` status `ready` deltaP `19.548` edge `0.3538` maxDD `-1.626`
- `market_context_high->crypto_major_24h` score `4.7923` n `119` status `ready` deltaP `11.6363` edge `0.5868` maxDD `-16.2014`
- `market_context_high->crypto_major_4h` score `3.7929` n `153` status `ready` deltaP `17.2765` edge `0.3819` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.9043` n `153` status `ready` deltaP `10.87` edge `0.1912` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1717` n `153` status `ready` deltaP `9.7912` edge `0.1511` maxDD `-6.1656`
- `market_context_high->equity_24h` score `0.9019` n `119` status `ready` deltaP `18.2423` edge `0.0206` maxDD `-3.0311`
- `market_context_high->crypto_major_1h` score `0.7122` n `153` status `ready` deltaP `8.3343` edge `0.1232` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.5366` n `119` status `ready` deltaP `5.5191` edge `0.106` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.0767` n `119` status `ready` deltaP `-1.3509` edge `0.6644` maxDD `-41.2179`
- `market_context_high->index_4h` score `-0.1092` n `153` status `ready` deltaP `6.2779` edge `0.0332` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1178` n `153` status `ready` deltaP `3.5547` edge `0.0355` maxDD `-2.8543`
- `market_context_high->index_1h` score `-0.2348` n `153` status `ready` deltaP `3.0801` edge `0.0093` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.3142` n `153` status `ready` deltaP `1.3346` edge `0.0043` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.36` n `153` status `ready` deltaP `2.178` edge `0.0141` maxDD `-2.9823`
- `market_context_high->commodity_1h` score `-0.3799` n `153` status `ready` deltaP `3.814` edge `0.0137` maxDD `-4.3601`
- `market_context_high->equity_1h` score `-0.7539` n `153` status `ready` deltaP `0.3053` edge `0.019` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.7539` n `153` status `ready` deltaP `4.1587` edge `0.0482` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-0.8468` n `153` status `ready` deltaP `0.4354` edge `0.0125` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.9287` n `119` status `ready` deltaP `1.1978` edge `0.0024` maxDD `-2.3556`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
