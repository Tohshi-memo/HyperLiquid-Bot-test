# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T10:07:26.941484+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9564`

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

- `market_context_high->unknown_24h` score `481.9116` n `74` status `ready` deltaP `2.1584` edge `40.159` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `37.9411` n `53` status `ready` deltaP `36.7925` edge `2.9871` maxDD `-3.6503`
- `market_context_high->equity_24h` score `30.2705` n `74` status `ready` deltaP `32.4324` edge `2.4605` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.6508` n `74` status `ready` deltaP `48.5924` edge `1.3695` maxDD `-14.4708`
- `news_risk_high->crypto_major_24h` score `15.8748` n `53` status `ready` deltaP `42.0434` edge `1.9515` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2352` n `53` status `ready` deltaP `36.0877` edge `0.8087` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.8043` n `53` status `ready` deltaP `46.3542` edge `0.258` maxDD `0.0`
- `market_context_high->index_24h` score `6.2207` n `74` status `ready` deltaP `37.5516` edge `0.2772` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.3853` n `53` status `ready` deltaP `34.3389` edge `0.2502` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `4.9343` n `53` status `ready` deltaP `46.5486` edge `0.1385` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.4462` n `74` status `ready` deltaP `42.3424` edge `0.3769` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.0882` n `53` status `ready` deltaP `21.2006` edge `0.3481` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5541` n `53` status `ready` deltaP `18.464` edge `0.2361` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1261` n `53` status `ready` deltaP `28.3882` edge `0.0966` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.1823` n `53` status `ready` deltaP `25.4406` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1297` n `53` status `ready` deltaP `21.6607` edge `0.0767` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1057` n `53` status `ready` deltaP `26.1936` edge `0.2592` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7356` n `53` status `ready` deltaP `14.4261` edge `0.5769` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2382` n `53` status `ready` deltaP `16.7269` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7341` n `53` status `ready` deltaP `18.0431` edge `0.079` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
