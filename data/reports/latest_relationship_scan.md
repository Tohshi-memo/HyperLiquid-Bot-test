# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T14:22:30.438960+00:00`
- Price records: `672`
- Market context records: `5565`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11396`

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

- `market_context_high->equity_24h` score `4.4513` n `181` status `ready` deltaP `15.5905` edge `0.7749` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.3412` n `191` status `ready` deltaP `11.3428` edge `0.2654` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.2441` n `181` status `ready` deltaP `14.9104` edge `0.4583` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `0.8266` n `191` status `ready` deltaP `6.7896` edge `0.1877` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.822` n `191` status `ready` deltaP `7.2995` edge `0.1837` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.7488` n `181` status `ready` deltaP `16.6465` edge `0.0488` maxDD `-1.457`
- `market_context_high->index_1h` score `-0.0561` n `201` status `ready` deltaP `5.215` edge `0.0099` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.0743` n `201` status `ready` deltaP `6.3508` edge `0.048` maxDD `-5.0555`
- `market_context_high->fx_4h` score `-0.3033` n `191` status `ready` deltaP `5.9674` edge `0.0093` maxDD `-0.9483`
- `market_context_high->crypto_alt_1h` score `-0.3586` n `201` status `ready` deltaP `1.7808` edge `0.0544` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4163` n `201` status `ready` deltaP `1.6884` edge `0.001` maxDD `-0.4228`
- `market_context_high->crypto_major_1h` score `-0.5064` n `201` status `ready` deltaP `3.6829` edge `0.0578` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5422` n `201` status `ready` deltaP `-0.645` edge `0.0023` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-1.244` n `201` status `ready` deltaP `-2.9873` edge `-0.0072` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5652` n `191` status `ready` deltaP `2.1437` edge `0.0162` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.0145` n `181` status `ready` deltaP `12.5268` edge `0.0569` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.1826` n `191` status `ready` deltaP `-14.1593` edge `-0.0634` maxDD `-12.6856`
- `market_context_high->commodity_4h` score `-4.5713` n `191` status `ready` deltaP `-8.4728` edge `-0.0569` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.7472` n `181` status `ready` deltaP `-6.6854` edge `-0.2109` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-8.3866` n `181` status `ready` deltaP `5.3599` edge `0.1351` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
