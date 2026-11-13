# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T02:22:39.664954+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `295.3093` n `84` status `ready` deltaP `6.2996` edge `24.5812` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `62.2934` n `94` status `ready` deltaP `7.8004` edge `5.1839` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `30.7287` n `53` status `ready` deltaP `26.7231` edge `2.4532` maxDD `-3.6503`
- `market_context_high->equity_24h` score `22.7113` n `84` status `ready` deltaP `24.4544` edge `1.8002` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.2382` n `53` status `ready` deltaP `38.9184` edge `1.5061` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.4609` n `53` status `ready` deltaP `32.7341` edge `0.6832` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `9.3767` n `84` status `ready` deltaP `45.2133` edge `1.3103` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.0379` n `53` status `ready` deltaP `43.2292` edge `0.2983` maxDD `0.0`
- `market_context_high->metal_24h` score `6.6746` n `84` status `ready` deltaP `40.7738` edge `0.3257` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.4482` n `53` status `ready` deltaP `42.7376` edge `0.1234` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.3562` n `84` status `ready` deltaP `24.6776` edge `0.208` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.9479` n `53` status `ready` deltaP `22.8806` edge `0.2068` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.1165` n `53` status `ready` deltaP `28.3882` edge `0.0958` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.0611` n `53` status `ready` deltaP `16.967` edge `0.205` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.6183` n `53` status `ready` deltaP `19.3713` edge `0.2378` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.0995` n `53` status `ready` deltaP `24.9915` edge `0.0338` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `1.9391` n `53` status `ready` deltaP `15.2941` edge `0.5972` maxDD `-29.0448`
- `news_risk_high->index_4h` score `1.6907` n `53` status `ready` deltaP `18.0022` edge `0.0645` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.4314` n `53` status `ready` deltaP `24.8216` edge `0.1819` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1148` n `53` status `ready` deltaP `15.679` edge `0.0185` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
