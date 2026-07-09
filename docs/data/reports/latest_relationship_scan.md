# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T19:52:29.326599+00:00`
- Price records: `672`
- Market context records: `6212`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `13.0382` n `32` status `ready` deltaP `42.2194` edge `0.8198` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5922` n `32` status `ready` deltaP `57.1429` edge `0.1684` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.071` n `32` status `ready` deltaP `42.6067` edge `0.0598` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.3798` n `32` status `ready` deltaP `15.625` edge `0.2789` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.2829` n `32` status `ready` deltaP `27.5449` edge `0.0205` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.8417` n `192` status `ready` deltaP `1.3629` edge `0.2452` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.4031` n `32` status `ready` deltaP `14.4274` edge `0.1304` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `0.9506` n `32` status `ready` deltaP `19.7491` edge `-0.0319` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.7335` n `32` status `ready` deltaP `9.6744` edge `0.0757` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.3775` n `192` status `ready` deltaP `-2.1469` edge `0.299` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.0447` n `192` status `ready` deltaP `19.8023` edge `0.1191` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2534` n `32` status `ready` deltaP `8.801` edge `-0.004` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.333` n `192` status `ready` deltaP `0.4616` edge `-0.0012` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5835` n `192` status `ready` deltaP `-0.8982` edge `0.002` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.7481` n `192` status `ready` deltaP `2.2993` edge `0.0075` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.794` n `32` status `ready` deltaP `-3.5928` edge `-0.0281` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8808` n `192` status `ready` deltaP `1.6155` edge `-0.0043` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.8966` n `192` status `ready` deltaP `4.5316` edge `0.0316` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9302` n `192` status `ready` deltaP `3.9452` edge `0.0297` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.1352` n `192` status `ready` deltaP `-3.0127` edge `-0.0139` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
