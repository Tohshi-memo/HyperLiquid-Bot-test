# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T16:37:24.601651+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9384`

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

- `market_context_high->unknown_24h` score `575.0243` n `66` status `ready` deltaP `4.5139` edge `47.8886` maxDD `0.0`
- `news_risk_high->equity_24h` score `39.6227` n `53` status `ready` deltaP `41.1328` edge `3.0983` maxDD `-3.6503`
- `market_context_high->equity_24h` score `35.869` n `66` status `ready` deltaP `36.1585` edge `2.9022` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `24.1106` n `66` status `ready` deltaP `57.7652` edge `1.7318` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `17.3976` n `53` status `ready` deltaP `42.7378` edge `2.1421` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3956` n `53` status `ready` deltaP `36.6975` edge `0.818` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3166` n `53` status `ready` deltaP `50.8681` edge `0.2706` maxDD `0.0`
- `market_context_high->index_24h` score `7.12` n `66` status `ready` deltaP `41.3825` edge `0.3266` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.762` n `53` status `ready` deltaP `37.6375` edge `0.2596` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.2664` n `66` status `ready` deltaP `51.5152` edge `0.4209` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.878` n `53` status `ready` deltaP `45.634` edge `0.1399` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.5006` n `53` status `ready` deltaP `20.8957` edge `0.3845` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6979` n `53` status `ready` deltaP `19.6616` edge `0.2401` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4316` n `53` status `ready` deltaP `31.7419` edge `0.0997` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.8307` n `53` status `ready` deltaP `14.4261` edge `0.7173` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `2.5433` n `53` status `ready` deltaP `27.1082` edge `0.3092` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.4196` n `53` status `ready` deltaP `25.0144` edge `0.0785` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2577` n `53` status `ready` deltaP `26.1891` edge `0.039` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3891` n `53` status `ready` deltaP `18.5233` edge `0.0224` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9145` n `53` status `ready` deltaP `18.4922` edge `0.0919` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
