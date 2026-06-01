# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T20:37:20.639076+00:00`
- Price records: `672`
- Market context records: `2595`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->unknown_24h` score `7.7044` n `133` status `ready` deltaP `18.1743` edge `0.5537` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.5393` n `146` status `ready` deltaP `25.5012` edge `0.5595` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8254` n `146` status `ready` deltaP `16.288` edge `0.3912` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.6305` n `133` status `ready` deltaP `3.2111` edge `0.7523` maxDD `-39.0265`
- `market_context_high->crypto_alt_1h` score `1.412` n `146` status `ready` deltaP `11.5803` edge `0.1592` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.9206` n `133` status `ready` deltaP `8.9233` edge `0.1153` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `0.8839` n `146` status `ready` deltaP `7.6846` edge `0.1274` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.8108` n `146` status `ready` deltaP `9.3122` edge `0.1249` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.2268` n `146` status `ready` deltaP `9.1276` edge `0.0422` maxDD `-2.3986`
- `market_context_high->equity_24h` score `0.081` n `133` status `ready` deltaP `16.2098` edge `-0.0343` maxDD `-2.3615`
- `market_context_high->index_1h` score `-0.1299` n `146` status `ready` deltaP `4.0911` edge `0.0113` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3756` n `146` status `ready` deltaP `2.0999` edge `0.021` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4182` n `146` status `ready` deltaP `5.3523` edge `0.0173` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.5985` n `146` status `ready` deltaP `1.4109` edge `0.0155` maxDD `-2.9823`
- `market_context_high->metal_4h` score `-0.6364` n `146` status `ready` deltaP `4.5021` edge `0.0557` maxDD `-4.7664`
- `market_context_high->fx_1h` score `-0.6641` n `146` status `ready` deltaP `-0.8346` edge `0.0037` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7881` n `146` status `ready` deltaP `-0.0779` edge `0.0187` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.9144` n `146` status `ready` deltaP `-0.378` edge `0.0121` maxDD `-0.8621`
- `market_context_high->crypto_major_24h` score `-0.9514` n `133` status `ready` deltaP `4.8285` edge `0.4154` maxDD `-30.15`
- `market_context_high->fx_24h` score `-0.9808` n `133` status `ready` deltaP `2.6891` edge `-0.0003` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
