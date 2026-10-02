# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T22:52:29.335770+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4790`

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

- `market_context_high->unknown_1h` score `364.0402` n `50` status `ready` deltaP `10.5749` edge `30.2711` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.5585` n `50` status `ready` deltaP `10.6707` edge `24.2254` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.0643` n `71` status `ready` deltaP `42.8428` edge `1.1573` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `10.5591` n `50` status `ready` deltaP `19.6597` edge `0.9192` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.0666` n `50` status `ready` deltaP `31.8264` edge `0.685` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.8319` n `71` status `ready` deltaP `32.5606` edge `0.5674` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.9204` n `50` status `ready` deltaP `19.6768` edge `0.5992` maxDD `-3.294`
- `news_risk_high->crypto_alt_4h` score `6.4842` n `114` status `ready` deltaP `25.0589` edge `0.5077` maxDD `-6.4195`
- `market_context_high->crypto_alt_4h` score `6.4223` n `50` status `ready` deltaP `17.8659` edge `0.545` maxDD `-7.6465`
- `market_context_high->crypto_alt_1h` score `3.3825` n `50` status `ready` deltaP `15.4012` edge `0.2455` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.138` n `50` status `ready` deltaP `14.2994` edge `0.2112` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7653` n `50` status `ready` deltaP `30.8598` edge `0.0382` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.6632` n `114` status `ready` deltaP `22.545` edge `0.1329` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `2.1979` n `71` status `ready` deltaP `7.5729` edge `0.5133` maxDD `-13.8932`
- `news_risk_high->crypto_major_4h` score `1.975` n `114` status `ready` deltaP `17.4663` edge `0.3521` maxDD `-9.894`
- `market_context_high->fx_1h` score `1.4723` n `50` status `ready` deltaP `20.6407` edge `0.0115` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.4589` n `71` status `ready` deltaP `14.0894` edge `0.2199` maxDD `-2.1432`
- `market_context_high->equity_24h` score `1.3416` n `50` status `ready` deltaP `6.1944` edge `0.3169` maxDD `-11.8957`
- `news_risk_high->crypto_alt_1h` score `1.1709` n `114` status `ready` deltaP `5.5416` edge `0.1167` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.9813` n `50` status `ready` deltaP `20.1597` edge `0.0932` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
