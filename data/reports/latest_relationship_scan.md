# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T01:37:17.147246+00:00`
- Price records: `672`
- Market context records: `2096`
- Flow alert records: `7927`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `10.606` n `185` status `ready` deltaP `30.9146` edge `0.7922` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.4629` n `185` status `ready` deltaP `37.1103` edge `0.6775` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.2712` n `185` status `ready` deltaP `23.7772` edge `0.439` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.122` n `185` status `ready` deltaP `22.2676` edge `0.3045` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.3215` n `184` status `ready` deltaP `22.4744` edge `0.659` maxDD `-35.8966`
- `market_context_high->index_4h` score `2.5233` n `185` status `ready` deltaP `18.6503` edge `0.1543` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.3084` n `185` status `ready` deltaP `16.2122` edge `0.1829` maxDD `-3.2225`
- `market_context_high->index_24h` score `2.1691` n `184` status `ready` deltaP `11.3547` edge `0.2279` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.0898` n `185` status `ready` deltaP `13.3679` edge `0.1964` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.7131` n `184` status `ready` deltaP `22.5008` edge `0.4826` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8219` n `185` status `ready` deltaP `10.7145` edge `0.0759` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.6402` n `185` status `ready` deltaP `5.8667` edge `0.0862` maxDD `-3.0902`
- `market_context_high->index_1h` score `0.1706` n `185` status `ready` deltaP `6.3239` edge `0.0311` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `0.0922` n `184` status `ready` deltaP `21.0998` edge `0.7256` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-0.0807` n `185` status `ready` deltaP `13.3396` edge `0.1546` maxDD `-11.3538`
- `market_context_high->fx_24h` score `-0.1177` n `184` status `ready` deltaP `14.8939` edge `0.0302` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.2477` n `185` status `ready` deltaP `6.6653` edge `0.037` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.7974` n `185` status `ready` deltaP `-0.7776` edge `0.0015` maxDD `-0.3548`
- `market_context_high->metal_24h` score `-1.1943` n `184` status `ready` deltaP `10.5743` edge `0.2201` maxDD `-23.2095`
- `market_context_high->fx_4h` score `-1.4811` n `185` status `ready` deltaP `-5.2175` edge `-0.0005` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
