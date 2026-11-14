# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T16:52:26.610428+00:00`
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

- `market_context_high->unknown_24h` score `575.1647` n `66` status `ready` deltaP `4.5139` edge `47.9003` maxDD `0.0`
- `news_risk_high->equity_24h` score `39.6618` n `53` status `ready` deltaP `41.3064` edge `3.1004` maxDD `-3.6503`
- `market_context_high->equity_24h` score `35.9081` n `66` status `ready` deltaP `36.3321` edge `2.9043` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `24.2234` n `66` status `ready` deltaP `57.7652` edge `1.7412` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `17.4893` n `53` status `ready` deltaP `42.9114` edge `2.1527` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.4282` n `53` status `ready` deltaP `36.8499` edge `0.8197` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3178` n `53` status `ready` deltaP `50.8681` edge `0.2707` maxDD `0.0`
- `market_context_high->index_24h` score `7.12` n `66` status `ready` deltaP `41.3825` edge `0.3266` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.762` n `53` status `ready` deltaP `37.6375` edge `0.2596` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.2688` n `66` status `ready` deltaP `51.5152` edge `0.4212` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8816` n `53` status `ready` deltaP `45.634` edge `0.1402` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.574` n `53` status `ready` deltaP `21.0481` edge `0.3896` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.7171` n `53` status `ready` deltaP `19.8113` edge `0.2407` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4462` n `53` status `ready` deltaP `31.8943` edge `0.0999` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.904` n `53` status `ready` deltaP `14.4261` edge `0.7267` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `2.5949` n `53` status `ready` deltaP `27.2607` edge `0.3148` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.4342` n `53` status `ready` deltaP `25.1668` edge `0.0787` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2446` n `53` status `ready` deltaP `26.0394` edge `0.0389` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3891` n `53` status `ready` deltaP `18.5233` edge `0.0224` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9394` n `53` status `ready` deltaP `18.6419` edge `0.0941` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
