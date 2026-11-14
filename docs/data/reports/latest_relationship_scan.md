# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T23:37:26.291982+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_24h` score `572.3294` n `66` status `ready` deltaP `2.7778` edge `47.6756` maxDD `0.0`
- `news_risk_high->equity_24h` score `40.9938` n `53` status `ready` deltaP `44.9522` edge `3.1871` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.2402` n `66` status `ready` deltaP `39.9779` edge `2.991` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `27.6542` n `66` status `ready` deltaP `57.7652` edge `2.0271` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `20.0123` n `53` status `ready` deltaP `43.0851` edge `2.475` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.8231` n `53` status `ready` deltaP `38.8316` edge `0.8394` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3468` n `53` status `ready` deltaP `51.2153` edge `0.2708` maxDD `0.0`
- `market_context_high->index_24h` score `7.2332` n `66` status `ready` deltaP `42.077` edge `0.3314` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.8752` n `53` status `ready` deltaP `38.332` edge `0.2644` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.8684` n `53` status `ready` deltaP `22.5725` edge `0.4873` maxDD `-9.2335`
- `market_context_high->metal_24h` score `5.3943` n `66` status `ready` deltaP `51.5152` edge `0.4373` maxDD `-3.7989`
- `news_risk_high->crypto_alt_24h` score `5.1341` n `53` status `ready` deltaP `14.4261` edge `1.0126` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `5.0593` n `53` status `ready` deltaP `46.701` edge `0.1479` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.8537` n `53` status `ready` deltaP `20.8592` edge `0.2451` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4852` n `53` status `ready` deltaP `32.3516` edge `0.1001` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.4028` n `53` status `ready` deltaP `28.0229` edge `0.4133` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.5474` n `53` status `ready` deltaP `26.3863` edge `0.08` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2626` n `53` status `ready` deltaP `26.0394` edge `0.0404` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4155` n `53` status `ready` deltaP `18.8227` edge `0.0226` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.2075` n `53` status `ready` deltaP `20.2886` edge `0.1175` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
