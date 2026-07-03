# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T14:07:33.252101+00:00`
- Price records: `672`
- Market context records: `5564`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11380`

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

- `market_context_high->equity_24h` score `4.4085` n `182` status `ready` deltaP `15.5201` edge `0.7718` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.3604` n `191` status `ready` deltaP `11.3428` edge `0.267` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.2575` n `182` status `ready` deltaP `15.0622` edge `0.4584` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `0.8602` n `191` status `ready` deltaP `6.7896` edge `0.1905` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.8244` n `191` status `ready` deltaP `7.2995` edge `0.1839` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.741` n `182` status `ready` deltaP `16.6247` edge `0.0483` maxDD `-1.457`
- `market_context_high->equity_1h` score `-0.0863` n `201` status `ready` deltaP `6.3508` edge `0.047` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0875` n `201` status `ready` deltaP `4.8671` edge `0.0096` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.3092` n `201` status `ready` deltaP `2.1286` edge `0.0562` maxDD `-5.0257`
- `market_context_high->fx_4h` score `-0.3097` n `191` status `ready` deltaP `5.9674` edge `0.0093` maxDD `-0.9913`
- `market_context_high->fx_1h` score `-0.4229` n `201` status `ready` deltaP `1.6884` edge `0.0009` maxDD `-0.4585`
- `market_context_high->crypto_major_1h` score `-0.492` n `201` status `ready` deltaP `3.6829` edge `0.059` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5642` n `201` status `ready` deltaP `-0.9928` edge `0.0018` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-1.2778` n `201` status `ready` deltaP `-3.3351` edge `-0.0077` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5985` n `191` status `ready` deltaP `1.7726` edge `0.0159` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.0286` n `182` status `ready` deltaP `12.3149` edge `0.0565` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.2003` n `191` status `ready` deltaP `-14.1593` edge `-0.0635` maxDD `-12.859`
- `market_context_high->commodity_4h` score `-4.6106` n `191` status `ready` deltaP `-8.8438` edge `-0.0577` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.7428` n `182` status `ready` deltaP `-6.7365` edge `-0.21` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-8.3079` n `182` status `ready` deltaP `5.5785` edge `0.1402` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
