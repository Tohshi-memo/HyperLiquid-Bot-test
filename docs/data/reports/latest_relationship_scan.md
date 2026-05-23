# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T20:07:19.165844+00:00`
- Price records: `672`
- Market context records: `1664`
- Flow alert records: `6696`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8844`

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

- `market_context_high->metal_24h` score `10.1723` n `169` status `ready` deltaP `28.9337` edge `0.8974` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.5718` n `195` status `ready` deltaP `22.8901` edge `0.4948` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.7923` n `169` status `ready` deltaP `20.5841` edge `0.3166` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.6598` n `195` status `ready` deltaP `18.9955` edge `0.3659` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.994` n `195` status `ready` deltaP `13.2028` edge `0.1876` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.7537` n `169` status `ready` deltaP `19.9473` edge `0.503` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `1.0195` n `169` status `ready` deltaP `25.7468` edge `0.7719` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.7355` n `169` status `ready` deltaP `26.401` edge `1.0662` maxDD `-88.8062`
- `market_context_high->crypto_alt_1h` score `0.6186` n `207` status `ready` deltaP `6.9774` edge `0.1074` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.268` n `207` status `ready` deltaP `2.5681` edge `0.0414` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3196` n `195` status `ready` deltaP `2.0732` edge `0.0541` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.36` n `207` status `ready` deltaP `3.2761` edge `0.0594` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.3673` n `169` status `ready` deltaP `7.0791` edge `0.0271` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.4315` n `207` status `ready` deltaP `-0.4122` edge `0.0106` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7103` n `207` status `ready` deltaP `5.3581` edge `0.0068` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.84` n `207` status `ready` deltaP `-0.5207` edge `-0.0033` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-1.2155` n `195` status `ready` deltaP `9.764` edge `0.1028` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.4268` n `207` status `ready` deltaP `-0.6227` edge `-0.0182` maxDD `-9.8461`
- `market_context_high->fx_4h` score `-1.9125` n `195` status `ready` deltaP `-7.9621` edge `-0.0134` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-4.6177` n `195` status `ready` deltaP `11.5666` edge `-0.2348` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
