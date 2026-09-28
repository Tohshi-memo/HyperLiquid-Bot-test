# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T14:07:33.466726+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7712`

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

- `news_risk_high->unknown_24h` score `1438.5504` n `139` status `ready` deltaP `1.2153` edge `119.8711` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.9498` n `139` status `ready` deltaP `21.6502` edge `0.83` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `4.2941` n `139` status `ready` deltaP `17.4285` edge `0.6851` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `3.8364` n `139` status `ready` deltaP `20.9007` edge `0.436` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.7367` n `139` status `ready` deltaP `26.5325` edge `0.1207` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.89` n `139` status `ready` deltaP `23.2102` edge `0.1637` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.581` n `139` status `ready` deltaP `20.3013` edge `0.1819` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.5943` n `139` status `ready` deltaP `7.0176` edge `0.0938` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.4838` n `139` status `ready` deltaP `6.8214` edge `0.2608` maxDD `-15.9436`
- `news_risk_high->index_1h` score `0.3581` n `139` status `ready` deltaP `7.7037` edge `0.0075` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.3534` n `139` status `ready` deltaP `6.3564` edge `0.0532` maxDD `-1.957`
- `news_risk_high->index_4h` score `-0.3738` n `139` status `ready` deltaP `4.6763` edge `0.023` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5472` n `139` status `ready` deltaP `1.1911` edge `0.0094` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6799` n `139` status `ready` deltaP `-0.1519` edge `0.0421` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1555` n `139` status `ready` deltaP `-8.6687` edge `-0.0023` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1613` n `139` status `ready` deltaP `11.0491` edge `-0.0012` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5811` n `139` status `ready` deltaP `-11.2903` edge `0.022` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0365` n `139` status `ready` deltaP `-11.8662` edge `-0.0145` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.1537` n `139` status `ready` deltaP `-6.9201` edge `0.0415` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0683` n `139` status `ready` deltaP `-12.999` edge `-0.0105` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
