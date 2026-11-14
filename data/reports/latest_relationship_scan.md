# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T17:22:32.852393+00:00`
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

- `market_context_high->unknown_24h` score `575.3867` n `66` status `ready` deltaP `4.5139` edge `47.9188` maxDD `0.0`
- `news_risk_high->equity_24h` score `39.7555` n `53` status `ready` deltaP `41.6536` edge `3.1059` maxDD `-3.6503`
- `market_context_high->equity_24h` score `36.0019` n `66` status `ready` deltaP `36.6793` edge `2.9098` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `24.4346` n `66` status `ready` deltaP `57.7652` edge `1.7588` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `17.6625` n `53` status `ready` deltaP `42.9114` edge `2.1749` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.4861` n `53` status `ready` deltaP `37.1548` edge `0.8225` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3341` n `53` status `ready` deltaP `51.0417` edge `0.2709` maxDD `0.0`
- `market_context_high->index_24h` score `7.1236` n `66` status `ready` deltaP `41.3825` edge `0.3269` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.7656` n `53` status `ready` deltaP `37.6375` edge `0.2599` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.2766` n `66` status `ready` deltaP `51.5152` edge `0.4222` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.901` n `53` status `ready` deltaP `45.7864` edge `0.1408` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.6928` n `53` status `ready` deltaP `21.0481` edge `0.3995` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.7506` n `53` status `ready` deltaP `20.1107` edge `0.2415` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4754` n `53` status `ready` deltaP `32.1992` edge `0.1003` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `3.0413` n `53` status `ready` deltaP `14.4261` edge `0.7443` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `2.6744` n `53` status `ready` deltaP `27.2607` edge `0.325` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.4622` n `53` status `ready` deltaP `25.4717` edge `0.079` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2446` n `53` status `ready` deltaP `26.0394` edge `0.0389` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4023` n `53` status `ready` deltaP `18.673` edge `0.0225` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9745` n `53` status `ready` deltaP `18.9413` edge `0.0966` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
