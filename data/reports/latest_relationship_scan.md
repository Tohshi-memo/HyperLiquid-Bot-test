# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T10:07:30.065611+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3905`

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

- `news_risk_high->equity_4h` score `1.2865` n `62` status `ready` deltaP `12.141` edge `0.1579` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.6641` n `62` status `ready` deltaP `12.318` edge `0.021` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3149` n `62` status `ready` deltaP `9.5822` edge `0.1433` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.0971` n `62` status `ready` deltaP `-2.2234` edge `0.0671` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0544` n `62` status `ready` deltaP `7.3498` edge `0.0033` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0877` n `62` status `ready` deltaP `-0.4491` edge `0.0467` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1402` n `62` status `ready` deltaP `2.7091` edge `0.0025` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2025` n `62` status `ready` deltaP `2.1194` edge `0.0045` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5392` n `62` status `ready` deltaP `-3.9743` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9562` n `62` status `ready` deltaP `1.2687` edge `-0.0405` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.193` n `62` status `ready` deltaP `-2.1441` edge `-0.0231` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2848` n `62` status `ready` deltaP `-3.3143` edge `0.0178` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.6218` n `62` status `ready` deltaP `-11.4738` edge `-0.0027` maxDD `-1.1434`
- `news_risk_high->crypto_major_1h` score `-1.9846` n `62` status `ready` deltaP `-8.0307` edge `-0.0301` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.1853` n `62` status `ready` deltaP `-2.7046` edge `-0.0001` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.791` n `62` status `ready` deltaP `-5.2532` edge `-0.2614` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.5457` n `62` status `ready` deltaP `-31.432` edge `-0.0121` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.8595` n `62` status `ready` deltaP `21.2141` edge `0.3942` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.6461` n `62` status `ready` deltaP `-29.1387` edge `-0.1269` maxDD `-27.9483`
- `news_risk_high->crypto_major_24h` score `-14.4112` n `62` status `ready` deltaP `-30.7964` edge `-0.1453` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
