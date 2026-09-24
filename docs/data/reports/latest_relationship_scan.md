# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T02:52:27.096359+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.135` n `47` status `ready` deltaP `10.7148` edge `5.9469` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `36.7827` n `46` status `ready` deltaP `24.1244` edge `2.92` maxDD `-0.5817`
- `market_context_high->equity_24h` score `21.3409` n `46` status `ready` deltaP `21.5203` edge `1.645` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `21.1478` n `46` status `ready` deltaP `19.0972` edge `1.635` maxDD `0.0`
- `market_context_high->index_24h` score `7.1633` n `46` status `ready` deltaP `30.548` edge `0.402` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.9755` n `103` status `ready` deltaP `14.6889` edge `0.4165` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.6394` n `103` status `ready` deltaP `17.7377` edge `0.3261` maxDD `-2.619`
- `news_risk_high->crypto_major_24h` score `3.0415` n `103` status `ready` deltaP `-3.5666` edge `1.1815` maxDD `-63.6743`
- `news_risk_high->crypto_alt_1h` score `2.6013` n `103` status `ready` deltaP `13.7565` edge `0.1741` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.5002` n `47` status `ready` deltaP `29.4532` edge `0.0274` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `2.4928` n `103` status `ready` deltaP `23.7476` edge `0.1673` maxDD `-2.431`
- `market_context_high->metal_24h` score `2.1925` n `46` status `ready` deltaP `24.5245` edge `0.0426` maxDD `-0.2042`
- `news_risk_high->crypto_major_1h` score `2.1188` n `103` status `ready` deltaP `16.3014` edge `0.1114` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.5734` n `103` status `ready` deltaP `23.0716` edge `0.0409` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.5043` n `47` status `ready` deltaP `12.114` edge `0.0864` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.2171` n `103` status `ready` deltaP `29.6639` edge `0.1214` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8181` n `47` status `ready` deltaP `13.1131` edge `0.0086` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6673` n `103` status `ready` deltaP `15.502` edge `0.0116` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.6334` n `47` status `ready` deltaP `9.2209` edge `0.0316` maxDD `-1.5564`
- `news_risk_high->metal_4h` score `0.3495` n `103` status `ready` deltaP `14.5749` edge `0.0434` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
