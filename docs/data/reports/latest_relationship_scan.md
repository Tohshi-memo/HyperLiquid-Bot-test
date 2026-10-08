# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T06:07:29.749539+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.9201` n `90` status `ready` deltaP `-2.831` edge `3.3161` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.2178` n `62` status `ready` deltaP `39.5763` edge `0.6913` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.3528` n `62` status `ready` deltaP `23.7812` edge `0.5886` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.8854` n `62` status `ready` deltaP `17.5553` edge `0.4667` maxDD `-0.1298`
- `news_risk_high->index_24h` score `5.0652` n `62` status `ready` deltaP `36.9603` edge `0.1757` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.7695` n `90` status `ready` deltaP `12.038` edge `0.8286` maxDD `-16.7906`
- `news_risk_high->index_4h` score `3.1551` n `62` status `ready` deltaP `34.2196` edge `0.061` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.713` n `90` status `ready` deltaP `17.6408` edge `0.2049` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.6042` n `62` status `ready` deltaP `19.3966` edge `0.1475` maxDD `-2.7837`
- `news_risk_high->crypto_major_1h` score `2.5343` n `62` status `ready` deltaP `10.4742` edge `0.1769` maxDD `-1.5096`
- `market_context_high->equity_24h` score `2.3808` n `90` status `ready` deltaP `15.118` edge `0.1405` maxDD `-1.0977`
- `news_risk_high->index_1h` score `2.0403` n `62` status `ready` deltaP `25.4733` edge `0.0152` maxDD `-0.1997`
- `news_risk_high->unknown_4h` score `1.6997` n `62` status `ready` deltaP `-5.806` edge `0.3049` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.4604` n `62` status `ready` deltaP `21.1666` edge `0.0877` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.2455` n `90` status `ready` deltaP `21.5371` edge `0.1646` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.2306` n `62` status `ready` deltaP `3.6073` edge `0.1304` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.0111` n `90` status `ready` deltaP `21.1263` edge `0.0181` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6747` n `90` status `ready` deltaP `11.497` edge `0.0038` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.249` n `90` status `ready` deltaP `7.7145` edge `0.5743` maxDD `-34.5048`
- `market_context_high->crypto_major_1h` score `0.1822` n `90` status `ready` deltaP `10.4025` edge `0.0429` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
