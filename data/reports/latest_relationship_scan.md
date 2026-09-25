# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T10:52:31.194762+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11286`

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

- `market_context_high->unknown_1h` score `84.7474` n `47` status `ready` deltaP `8.1698` edge `7.0149` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.2357` n `47` status `ready` deltaP `30.9434` edge `4.0193` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.9804` n `47` status `ready` deltaP `24.782` edge `2.5378` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.4895` n `47` status `ready` deltaP `34.5892` edge `1.9291` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.3373` n `111` status `ready` deltaP `3.4161` edge `0.9359` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.8439` n `47` status `ready` deltaP `35.2837` edge `0.4314` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.5141` n `47` status `ready` deltaP `38.357` edge `0.1443` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.6977` n `48` status `ready` deltaP `30.7292` edge `0.1381` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.6544` n `47` status `ready` deltaP `30.8251` edge `0.0311` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.0762` n `47` status `ready` deltaP `14.553` edge `0.1178` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.9228` n `47` status `ready` deltaP `9.5355` edge `0.0801` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.914` n `47` status `ready` deltaP `14.161` edge `0.0096` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8851` n `47` status `ready` deltaP `11.167` edge `0.0396` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.6438` n `111` status `ready` deltaP `7.5323` edge `0.0945` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.459` n `47` status `ready` deltaP `9.9598` edge `0.0075` maxDD `-0.1854`
- `news_risk_high->index_1h` score `0.0283` n `111` status `ready` deltaP `4.0595` edge `0.0064` maxDD `-0.3863`
- `market_context_high->metal_1h` score `0.0188` n `47` status `ready` deltaP `3.4272` edge `0.0112` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0064` n `111` status `ready` deltaP `8.5451` edge `0.0065` maxDD `-0.7016`
- `news_risk_high->equity_1h` score `-0.0798` n `111` status `ready` deltaP `1.9664` edge `0.0274` maxDD `-2.0595`
- `market_context_high->crypto_major_1h` score `-0.111` n `47` status `ready` deltaP `2.9558` edge `0.0528` maxDD `-4.5405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
