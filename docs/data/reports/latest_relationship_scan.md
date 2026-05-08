# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T22:22:20.846535+00:00`
- Price records: `672`
- Market context records: `801`
- Flow alert records: `2252`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `12.6593` n `149` status `ready` deltaP `29.9905` edge `0.8884` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.6365` n `149` status `ready` deltaP `7.1414` edge `0.4269` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.599` n `33` status `ready` deltaP `10.1903` edge `0.2685` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.599` n `33` status `ready` deltaP `10.1903` edge `0.2685` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.9079` n `33` status `ready` deltaP `18.0802` edge `0.1306` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.9079` n `33` status `ready` deltaP `18.0802` edge `0.1306` maxDD `-0.038`
- `risk_on_high->crypto_alt_4h` score `2.7411` n `33` status `ready` deltaP `20.9396` edge `0.1093` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.7411` n `33` status `ready` deltaP `20.9396` edge `0.1093` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.7368` n `33` status `ready` deltaP `19.66` edge `0.1342` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.7368` n `33` status `ready` deltaP `19.66` edge `0.1342` maxDD `-0.9758`
- `risk_on_high->metal_1h` score `1.1015` n `33` status `ready` deltaP `12.9605` edge `0.0284` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.1015` n `33` status `ready` deltaP `12.9605` edge `0.0284` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.7878` n `33` status `ready` deltaP `5.0582` edge `0.1504` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.7878` n `33` status `ready` deltaP `5.0582` edge `0.1504` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.3195` n `33` status `ready` deltaP `8.4377` edge `0.0223` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.3195` n `33` status `ready` deltaP `8.4377` edge `0.0223` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2532` n `33` status `ready` deltaP `8.0975` edge `0.002` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2532` n `33` status `ready` deltaP `8.0975` edge `0.002` maxDD `-0.2147`
- `market_context_high->index_24h` score `-0.0783` n `149` status `ready` deltaP `1.3026` edge `0.1843` maxDD `-5.9609`
- `risk_on_high->crypto_major_1h` score `-0.1331` n `33` status `ready` deltaP `4.4321` edge `-0.0162` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
