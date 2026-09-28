# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T21:37:36.975502+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7310`

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

- `news_risk_high->unknown_24h` score `2669.6616` n `139` status `ready` deltaP `1.2153` edge `222.4637` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `10.5163` n `139` status `ready` deltaP `26.5113` edge `1.0948` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `6.8066` n `139` status `ready` deltaP `26.1091` edge `0.6488` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.3918` n `139` status `ready` deltaP `22.2896` edge `0.8275` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.4246` n `139` status `ready` deltaP `31.7409` edge `0.1433` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `2.6282` n `139` status `ready` deltaP `24.1207` edge `0.2437` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5197` n `139` status `ready` deltaP `26.7163` edge `0.1928` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.8877` n `139` status `ready` deltaP `8.3458` edge `0.2843` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6375` n `139` status `ready` deltaP `6.8679` edge `0.0984` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5392` n `139` status `ready` deltaP `7.554` edge `0.0607` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4695` n `139` status `ready` deltaP `8.9013` edge `0.0088` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1149` n `139` status `ready` deltaP `7.2678` edge `0.0273` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4705` n `139` status `ready` deltaP `1.9396` edge `0.0108` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5373` n `139` status `ready` deltaP `0.7463` edge `0.0544` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1967` n `139` status `ready` deltaP `-9.4172` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.291` n `139` status `ready` deltaP `8.9149` edge `-0.0036` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4043` n `139` status `ready` deltaP `-8.8513` edge `0.0284` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8294` n `139` status `ready` deltaP `-5.2433` edge `0.0719` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0754` n `139` status `ready` deltaP `-12.6147` edge `-0.0145` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7982` n `139` status `ready` deltaP `-11.0173` edge `-0.0012` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
