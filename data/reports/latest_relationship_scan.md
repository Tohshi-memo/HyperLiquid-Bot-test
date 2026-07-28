# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T16:07:33.100412+00:00`
- Price records: `672`
- Market context records: `8212`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5920`

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

- `news_risk_high->unknown_24h` score `8034.4167` n `43` status `ready` deltaP `36.9792` edge `669.2882` maxDD `0.0`
- `market_context_high->equity_24h` score `21.2125` n `31` status `ready` deltaP `38.256` edge `1.6037` maxDD `-4.9489`
- `market_context_high->crypto_major_24h` score `17.3343` n `31` status `ready` deltaP `34.5094` edge `1.3165` maxDD `-5.4964`
- `market_context_high->crypto_alt_24h` score `16.4296` n `31` status `ready` deltaP `35.0302` edge `1.2084` maxDD `-3.1573`
- `market_context_high->equity_4h` score `8.8763` n `31` status `ready` deltaP `47.2315` edge `0.4291` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.029` n `31` status `ready` deltaP `45.2117` edge `0.3778` maxDD `-0.4771`
- `news_risk_high->equity_4h` score `7.3283` n `54` status `ready` deltaP `26.3832` edge `0.4945` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `6.4849` n `31` status `ready` deltaP `27.852` edge `0.379` maxDD `-0.6082`
- `market_context_high->index_24h` score `5.5404` n `31` status `ready` deltaP `35.3774` edge `0.2699` maxDD `-0.857`
- `market_context_high->crypto_alt_4h` score `4.7533` n `31` status `ready` deltaP `21.8578` edge `0.2748` maxDD `-0.6195`
- `market_context_high->index_4h` score `3.6439` n `31` status `ready` deltaP `36.8165` edge `0.0625` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.5637` n `31` status `ready` deltaP `35.1151` edge `0.0807` maxDD `-0.0926`
- `news_risk_high->equity_1h` score `3.1493` n `54` status `ready` deltaP `22.7268` edge `0.1418` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6773` n `54` status `ready` deltaP `22.4198` edge `0.0927` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.5751` n `54` status `ready` deltaP `12.9178` edge `0.3134` maxDD `-2.8833`
- `market_context_high->fx_24h` score `2.5587` n `31` status `ready` deltaP `43.0163` edge `0.0788` maxDD `-0.3364`
- `market_context_high->equity_1h` score `1.8989` n `31` status `ready` deltaP `9.943` edge `0.1066` maxDD `-0.1718`
- `news_risk_high->crypto_major_1h` score `1.857` n `54` status `ready` deltaP `13.0018` edge `0.1078` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.7967` n `54` status `ready` deltaP `14.8536` edge `0.0941` maxDD `-1.1388`
- `market_context_high->crypto_major_1h` score `1.5466` n `31` status `ready` deltaP `15.0328` edge `0.0482` maxDD `-0.5626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
