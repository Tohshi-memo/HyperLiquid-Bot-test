# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T00:52:34.978916+00:00`
- Price records: `672`
- Market context records: `4990`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `20.8031` n `91` status `ready` deltaP `3.8972` edge `1.7577` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.1932` n `87` status `ready` deltaP `18.0964` edge `0.544` maxDD `-7.8836`
- `market_context_high->unknown_24h` score `5.9671` n `74` status `ready` deltaP `28.7725` edge `0.3397` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.1734` n `87` status `ready` deltaP `12.7366` edge `0.4856` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `1.5317` n `87` status `ready` deltaP `20.8894` edge `0.0906` maxDD `-5.5109`
- `market_context_high->metal_4h` score `1.1097` n `87` status `ready` deltaP `11.0352` edge `0.1268` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.972` n `91` status `ready` deltaP `7.388` edge `0.1235` maxDD `-4.6734`
- `market_context_high->equity_1h` score `0.9467` n `91` status `ready` deltaP `8.6909` edge `0.0783` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.6118` n `87` status `ready` deltaP `5.0077` edge `0.1832` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.4249` n `91` status `ready` deltaP `6.9389` edge `0.0388` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.3734` n `87` status `ready` deltaP `5.4527` edge `0.043` maxDD `-0.8587`
- `market_context_high->crypto_alt_1h` score `0.1886` n `91` status `ready` deltaP `5.0438` edge `0.0928` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2683` n `74` status `ready` deltaP `5.565` edge `0.0047` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3822` n `91` status `ready` deltaP `0.8965` edge `0.011` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5158` n `91` status `ready` deltaP `2.5976` edge `0.0138` maxDD `-0.5946`
- `market_context_high->fx_4h` score `-0.8271` n `87` status `ready` deltaP `-1.1845` edge `-0.0011` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.2738` n `87` status `ready` deltaP `3.5867` edge `-0.0048` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.707` n `91` status `ready` deltaP `-11.3921` edge `-0.0055` maxDD `-0.5308`
- `market_context_high->commodity_24h` score `-3.9426` n `74` status `ready` deltaP `7.8782` edge `-0.0471` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.2911` n `74` status `ready` deltaP `-1.3889` edge `0.0046` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
