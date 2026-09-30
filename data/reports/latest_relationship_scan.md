# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T05:07:35.337678+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7304`

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

- `news_risk_high->unknown_24h` score `1026.4996` n `133` status `ready` deltaP `1.9097` edge `85.5289` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.188` n `133` status `ready` deltaP `29.5726` edge `1.4228` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `8.608` n `133` status `ready` deltaP `29.2384` edge `0.7573` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `8.4234` n `133` status `ready` deltaP `24.7245` edge `0.8525` maxDD `-15.8971`
- `news_risk_high->index_24h` score `4.0072` n `133` status `ready` deltaP `35.5419` edge `0.1448` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.6523` n `133` status `ready` deltaP `27.3391` edge `0.2495` maxDD `-2.192`
- `news_risk_high->equity_4h` score `3.0042` n `135` status `ready` deltaP `30.0858` edge `0.2099` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.9856` n `135` status `ready` deltaP `11.5696` edge `0.3543` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1126` n `135` status `ready` deltaP `9.4012` edge `0.1211` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9248` n `135` status `ready` deltaP `9.5509` edge `0.0757` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.5077` n `135` status `ready` deltaP `8.9676` edge `0.0113` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0335` n `135` status `ready` deltaP `8.016` edge `0.0291` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4808` n `135` status `ready` deltaP `2.7888` edge `0.0696` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4838` n `135` status `ready` deltaP `1.1577` edge `0.0149` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.249` n `135` status `ready` deltaP `-7.2369` edge `0.0289` maxDD `-2.9297`
- `news_risk_high->fx_4h` score `-1.3863` n `135` status `ready` deltaP `7.5328` edge `-0.0066` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.5345` n `135` status `ready` deltaP `-3.5309` edge `0.0983` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-1.8195` n `135` status `ready` deltaP `-8.5185` edge `-0.009` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.9296` n `135` status `ready` deltaP `-10.2528` edge `-0.0044` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2349` n `135` status `ready` deltaP `-8.8449` edge `0.0143` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
