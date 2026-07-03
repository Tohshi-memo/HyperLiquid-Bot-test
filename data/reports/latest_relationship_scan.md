# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T14:37:27.409586+00:00`
- Price records: `672`
- Market context records: `5566`
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

- `market_context_high->equity_24h` score `4.47` n `180` status `ready` deltaP `15.6597` edge `0.776` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.31` n `191` status `ready` deltaP `11.3428` edge `0.2628` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.1958` n `180` status `ready` deltaP `14.7569` edge `0.4553` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `0.793` n `191` status `ready` deltaP `6.7896` edge `0.1849` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.7827` n `191` status `ready` deltaP `6.9284` edge `0.1829` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.7576` n `180` status `ready` deltaP `16.6666` edge `0.0494` maxDD `-1.457`
- `market_context_high->index_1h` score `-0.0887` n `201` status `ready` deltaP `4.8671` edge `0.0095` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.1273` n `201` status `ready` deltaP `6.0029` edge `0.0459` maxDD `-5.0555`
- `market_context_high->fx_4h` score `-0.2926` n `191` status `ready` deltaP `5.9674` edge `0.0096` maxDD `-0.9016`
- `market_context_high->fx_1h` score `-0.4124` n `201` status `ready` deltaP `1.6884` edge `0.0012` maxDD `-0.4122`
- `market_context_high->crypto_alt_1h` score `-0.4416` n `201` status `ready` deltaP `1.433` edge `0.0498` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.5454` n `201` status `ready` deltaP `-0.645` edge `0.0019` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5894` n `201` status `ready` deltaP `3.3351` edge `0.0532` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.2102` n `201` status `ready` deltaP `-2.6395` edge `-0.0067` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5652` n `191` status `ready` deltaP `2.1437` edge `0.0162` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.0025` n `180` status `ready` deltaP `12.7431` edge `0.057` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.1823` n `191` status `ready` deltaP `-14.1593` edge `-0.0637` maxDD `-12.6577`
- `market_context_high->commodity_4h` score `-4.5296` n `191` status `ready` deltaP `-8.1016` edge `-0.0559` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.7752` n `180` status `ready` deltaP `-7.0138` edge `-0.2123` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-8.4858` n `180` status `ready` deltaP `5.1389` edge `0.1283` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
