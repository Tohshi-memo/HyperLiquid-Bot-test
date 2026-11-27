# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T02:37:26.268101+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3552`

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

- `news_risk_high->unknown_1h` score `3216.9852` n `31` status `ready` deltaP `1.7819` edge `268.0878` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3186.1446` n `31` status `ready` deltaP `4.3962` edge `265.4884` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `25.6856` n `31` status `ready` deltaP `34.375` edge `1.9113` maxDD `0.0`
- `news_risk_high->equity_24h` score `22.8191` n `31` status `ready` deltaP `33.8542` edge `1.6759` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.6618` n `31` status `ready` deltaP `33.5069` edge `1.4151` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.4422` n `31` status `ready` deltaP `23.7116` edge `0.7158` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.035` n `31` status `ready` deltaP `34.1759` edge `0.4898` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.2107` n `31` status `ready` deltaP `16.9305` edge `0.8251` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `6.077` n `31` status `ready` deltaP `21.2702` edge `0.3921` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.9139` n `31` status `ready` deltaP `41.5379` edge `0.1454` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.0333` n `31` status `ready` deltaP `35.4167` edge `0.1` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.9135` n `31` status `ready` deltaP `17.5922` edge `0.1442` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.8381` n `31` status `ready` deltaP `32.1942` edge `0.0479` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4937` n `31` status `ready` deltaP `30.0464` edge `0.016` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.1602` n `31` status `ready` deltaP `7.316` edge `0.2743` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9221` n `31` status `ready` deltaP `10.31` edge `0.2134` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.2259` n `31` status `ready` deltaP `26.1396` edge `0.0108` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.5489` n `31` status `ready` deltaP `12.5098` edge `0.0427` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.1476` n `31` status `ready` deltaP `8.3694` edge `0.0029` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5677` n `31` status `ready` deltaP `-4.0081` edge `0.0056` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
