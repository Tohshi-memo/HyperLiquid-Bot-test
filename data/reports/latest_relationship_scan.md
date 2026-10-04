# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T03:07:30.456089+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4662`

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

- `market_context_high->unknown_4h` score `322.2048` n `50` status `ready` deltaP `13.1098` edge `26.763` maxDD `0.0`
- `market_context_high->unknown_1h` score `306.0196` n `58` status `ready` deltaP `8.6723` edge `25.4555` maxDD `-0.2681`
- `market_context_high->crypto_alt_24h` score `12.9687` n `50` status `ready` deltaP `28.4194` edge `1.0616` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `12.0393` n `59` status `ready` deltaP `31.6952` edge `0.802` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `10.9368` n `65` status `ready` deltaP `40.1736` edge `0.6639` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.8306` n `50` status `ready` deltaP `34.1664` edge `0.8164` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.3329` n `65` status `ready` deltaP `24.2073` edge `0.5841` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0216` n `50` status `ready` deltaP `15.8659` edge `0.5497` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.442` n `50` status `ready` deltaP `14.2073` edge `0.4877` maxDD `-7.6465`
- `news_risk_high->index_24h` score `5.076` n `59` status `ready` deltaP `35.3553` edge `0.1873` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8866` n `65` status `ready` deltaP `26.8269` edge `0.2063` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.0514` n `65` status `ready` deltaP `33.1332` edge `0.0596` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `3.043` n `65` status `ready` deltaP `13.9083` edge `0.1964` maxDD `-1.5096`
- `market_context_high->fx_4h` score `3.0212` n `50` status `ready` deltaP `33.9085` edge `0.0392` maxDD `-0.0791`
- `news_risk_high->metal_4h` score `2.578` n `65` status `ready` deltaP `22.1271` edge `0.1089` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.2963` n `58` status `ready` deltaP `9.8235` edge `0.1709` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0962` n `65` status `ready` deltaP `25.7669` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `1.982` n `58` status `ready` deltaP `7.2011` edge `0.1918` maxDD `-3.6376`
- `news_risk_high->crypto_alt_1h` score `1.5702` n `65` status `ready` deltaP `5.3178` edge `0.1473` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.2509` n `50` status `ready` deltaP `6.4749` edge `0.3034` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
