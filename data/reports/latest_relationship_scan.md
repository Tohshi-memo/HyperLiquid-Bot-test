# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T15:22:31.187018+00:00`
- Price records: `672`
- Market context records: `5364`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->unknown_24h` score `10.8174` n `172` status `ready` deltaP `17.1108` edge `0.8004` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.079` n `172` status `ready` deltaP `22.1213` edge `0.7298` maxDD `-29.6555`
- `market_context_high->equity_24h` score `3.4957` n `172` status `ready` deltaP `15.5685` edge `0.7504` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.1318` n `196` status `ready` deltaP `12.6898` edge `0.3223` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.6904` n `196` status `ready` deltaP `9.277` edge `0.2431` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.3565` n `196` status `ready` deltaP `8.9565` edge `0.2172` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.488` n `172` status `ready` deltaP `18.1242` edge `0.1002` maxDD `-9.0959`
- `market_context_high->equity_1h` score `0.1683` n `205` status `ready` deltaP `6.2626` edge `0.0688` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.1109` n `172` status `ready` deltaP `9.5365` edge `0.0352` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `-0.0062` n `205` status `ready` deltaP `4.1748` edge `0.0962` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.0371` n `205` status `ready` deltaP `1.7796` edge `0.0812` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.0822` n `205` status `ready` deltaP `4.5283` edge `0.0123` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.4493` n `205` status `ready` deltaP `-1.1034` edge `-0.0013` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5622` n `205` status `ready` deltaP `1.1808` edge `0.0128` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.661` n `196` status `ready` deltaP `2.2773` edge `0.003` maxDD `-1.567`
- `market_context_high->index_4h` score `-0.7232` n `196` status `ready` deltaP `5.3602` edge `0.0253` maxDD `-2.704`
- `market_context_high->unknown_4h` score `-1.4312` n `196` status `ready` deltaP `7.4509` edge `-0.0505` maxDD `-6.1421`
- `market_context_high->commodity_1h` score `-1.519` n `205` status `ready` deltaP `-3.7695` edge `-0.007` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.8281` n `196` status `ready` deltaP `-8.7326` edge `-0.0519` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.6627` n `172` status `ready` deltaP `12.4556` edge `0.3171` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
