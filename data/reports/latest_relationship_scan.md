# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T13:38:05.340393+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11258`

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

- `market_context_high->unknown_1h` score `75.8182` n `47` status `ready` deltaP `8.1698` edge `6.2708` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.3677` n `47` status `ready` deltaP `30.9434` edge `4.0303` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.744` n `47` status `ready` deltaP `24.782` edge `2.5181` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2267` n `47` status `ready` deltaP `34.5892` edge `1.9072` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7609` n `47` status `ready` deltaP `34.9364` edge `0.4268` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3033` n `47` status `ready` deltaP `36.6209` edge `0.1383` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.0174` n `57` status `ready` deltaP `26.8001` edge `0.1076` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.5438` n `47` status `ready` deltaP `29.758` edge `0.029` maxDD `-0.2323`
- `news_risk_high->unknown_1h` score `2.4081` n `111` status `ready` deltaP `3.4161` edge `0.1918` maxDD `-0.4452`
- `market_context_high->equity_4h` score `2.0644` n `47` status `ready` deltaP `14.7055` edge `0.1158` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.9192` n `47` status `ready` deltaP `9.5355` edge `0.0798` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.872` n `47` status `ready` deltaP `13.7119` edge `0.0091` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8563` n `47` status `ready` deltaP `11.0173` edge `0.0382` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.7326` n `111` status `ready` deltaP `8.1311` edge `0.0979` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4602` n `47` status `ready` deltaP `9.9598` edge `0.0076` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.0473` n `47` status `ready` deltaP `3.5546` edge `0.062` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.0011` n `111` status `ready` deltaP `3.6104` edge `0.0059` maxDD `-0.3863`
- `market_context_high->metal_1h` score `-0.0053` n `47` status `ready` deltaP `3.1278` edge `0.0101` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `-0.0308` n `111` status `ready` deltaP `8.2457` edge `0.0054` maxDD `-0.7016`
- `news_risk_high->equity_1h` score `-0.0985` n `111` status `ready` deltaP `1.8167` edge `0.026` maxDD `-2.0595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
