# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T15:22:30.339505+00:00`
- Price records: `672`
- Market context records: `5569`
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

- `market_context_high->equity_24h` score `4.3868` n `177` status `ready` deltaP `15.3396` edge `0.7712` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.25` n `191` status `ready` deltaP `11.3428` edge `0.2578` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.0166` n `177` status `ready` deltaP `14.2861` edge `0.4435` maxDD `-29.6555`
- `market_context_high->fx_24h` score `0.7748` n `177` status `ready` deltaP `16.7167` edge `0.0505` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.6922` n `191` status `ready` deltaP `6.7896` edge `0.1765` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.6801` n `191` status `ready` deltaP `6.1862` edge `0.1793` maxDD `-7.4425`
- `market_context_high->index_1h` score `-0.1552` n `201` status `ready` deltaP `4.1715` edge `0.0086` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.2519` n `201` status `ready` deltaP `5.6551` edge `0.042` maxDD `-5.0555`
- `market_context_high->fx_4h` score `-0.2893` n `191` status `ready` deltaP `5.9674` edge `0.0095` maxDD `-0.8712`
- `market_context_high->fx_1h` score `-0.3833` n `201` status `ready` deltaP `2.0362` edge `0.0013` maxDD `-0.4122`
- `market_context_high->metal_1h` score `-0.5265` n `201` status `ready` deltaP `-0.2972` edge `0.002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5318` n `201` status `ready` deltaP `1.0852` edge `0.0446` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6532` n `201` status `ready` deltaP `2.9873` edge `0.0502` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.32` n `201` status `ready` deltaP `-3.6829` edge `-0.0089` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5652` n `191` status `ready` deltaP `2.1437` edge `0.0162` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.9971` n `177` status `ready` deltaP `13.0267` edge `0.0558` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.1457` n `191` status `ready` deltaP `-14.1593` edge `-0.0631` maxDD `-12.331`
- `market_context_high->commodity_4h` score `-4.5248` n `191` status `ready` deltaP `-8.1016` edge `-0.0555` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.8385` n `177` status `ready` deltaP `-7.6301` edge `-0.2163` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-8.8137` n `177` status `ready` deltaP `4.4609` edge `0.1055` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
