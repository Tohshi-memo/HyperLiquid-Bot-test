# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T00:37:29.364179+00:00`
- Price records: `672`
- Market context records: `7306`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14793`

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

- `market_context_high->fx_1h` score `-0.1389` n `126` status `ready` deltaP `4.5045` edge `0.0011` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6797` n `126` status `ready` deltaP `-2.4024` edge `-0.0139` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.6917` n `126` status `ready` deltaP `-1.1382` edge `0.0228` maxDD `-5.9775`
- `market_context_high->index_1h` score `-0.7277` n `126` status `ready` deltaP `-3.9254` edge `-0.0053` maxDD `-1.9459`
- `market_context_high->crypto_major_1h` score `-0.7674` n `126` status `ready` deltaP `3.4146` edge `0.0199` maxDD `-7.6171`
- `market_context_high->commodity_4h` score `-0.776` n `118` status `ready` deltaP `1.5238` edge `-0.0128` maxDD `-2.4139`
- `market_context_high->fx_24h` score `-0.7846` n `112` status `ready` deltaP `2.8354` edge `0.0033` maxDD `-2.1564`
- `market_context_high->fx_4h` score `-1.0327` n `118` status `ready` deltaP `2.7264` edge `0.0094` maxDD `-1.4649`
- `market_context_high->metal_1h` score `-1.3672` n `126` status `ready` deltaP `-9.4502` edge `-0.0019` maxDD `-1.4971`
- `market_context_high->crypto_alt_4h` score `-1.7094` n `118` status `ready` deltaP `3.488` edge `0.0319` maxDD `-15.2776`
- `market_context_high->unknown_1h` score `-1.7432` n `126` status `ready` deltaP `0.8079` edge `-0.0883` maxDD `-1.3217`
- `market_context_high->unknown_4h` score `-1.789` n `118` status `ready` deltaP `3.9583` edge `0.0604` maxDD `-6.2031`
- `market_context_high->metal_4h` score `-2.3382` n `118` status `ready` deltaP `-8.0224` edge `0.0019` maxDD `-4.8549`
- `market_context_high->equity_1h` score `-2.6215` n `126` status `ready` deltaP `-7.8936` edge `-0.0532` maxDD `-13.7551`
- `market_context_high->crypto_major_4h` score `-2.6636` n `118` status `ready` deltaP `4.2373` edge `0.0197` maxDD `-23.4879`
- `market_context_high->unknown_24h` score `-2.919` n `113` status `ready` deltaP `-7.1242` edge `-0.0314` maxDD `-11.627`
- `market_context_high->commodity_24h` score `-3.7384` n `112` status `ready` deltaP `-7.3897` edge `-0.1825` maxDD `-2.3815`
- `market_context_high->index_4h` score `-4.242` n `118` status `ready` deltaP `-12.9166` edge `-0.043` maxDD `-7.6178`
- `market_context_high->crypto_alt_24h` score `-8.2645` n `113` status `ready` deltaP `3.7964` edge `-0.2347` maxDD `-58.0124`
- `market_context_high->metal_24h` score `-10.5873` n `113` status `ready` deltaP `-28.1511` edge `-0.1218` maxDD `-19.1572`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
