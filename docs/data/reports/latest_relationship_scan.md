# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T20:52:17.632685+00:00`
- Price records: `672`
- Market context records: `1667`
- Flow alert records: `6706`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `9.8747` n `166` status `ready` deltaP `28.6342` edge `0.8746` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.741` n `195` status `ready` deltaP `22.8901` edge `0.5089` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8162` n `166` status `ready` deltaP `20.2526` edge `0.3208` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.8458` n `195` status `ready` deltaP `18.9955` edge `0.3814` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.0888` n `195` status `ready` deltaP `13.2028` edge `0.1955` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8017` n `166` status `ready` deltaP `19.5731` edge `0.5095` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.8351` n `166` status `ready` deltaP `25.4367` edge `0.7586` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.674` n `166` status `ready` deltaP `26.1871` edge `1.0625` maxDD `-88.8062`
- `market_context_high->crypto_alt_1h` score `0.6519` n `207` status `ready` deltaP `6.644` edge `0.1124` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.2476` n `207` status `ready` deltaP `2.5681` edge `0.0431` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3657` n `195` status `ready` deltaP `2.7939` edge `0.0598` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.3794` n `166` status `ready` deltaP `7.1685` edge `0.0255` maxDD `-1.3925`
- `market_context_high->crypto_major_1h` score `-0.414` n `207` status `ready` deltaP `3.9428` edge `0.0666` maxDD `-5.5244`
- `market_context_high->index_1h` score `-0.6447` n `207` status `ready` deltaP `-0.4122` edge `0.0122` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8376` n `207` status `ready` deltaP `-0.5207` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-1.0711` n `207` status `ready` deltaP `5.3581` edge `0.0086` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.1663` n `195` status `ready` deltaP `9.764` edge `0.1069` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.2611` n `195` status `ready` deltaP `-8.3224` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.849` n `207` status `ready` deltaP `-1.2894` edge `-0.026` maxDD `-12.1961`
- `market_context_high->unknown_24h` score `-3.9952` n `166` status `ready` deltaP `9.2362` edge `0.1667` maxDD `-35.8966`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
