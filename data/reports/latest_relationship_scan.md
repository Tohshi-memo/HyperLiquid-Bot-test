# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T16:37:28.755510+00:00`
- Price records: `672`
- Market context records: `5369`
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

- `market_context_high->unknown_24h` score `9.2383` n `177` status `ready` deltaP `17.0521` edge `0.6692` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.2791` n `177` status `ready` deltaP `22.2223` edge `0.7458` maxDD `-29.6555`
- `market_context_high->equity_24h` score `2.9699` n `177` status `ready` deltaP `13.8713` edge `0.7179` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.5774` n `201` status `ready` deltaP `13.4002` edge `0.3547` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.9695` n `201` status `ready` deltaP `9.8858` edge `0.2623` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.2226` n `201` status `ready` deltaP `8.4668` edge `0.2093` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.251` n `177` status `ready` deltaP `16.8079` edge `0.0934` maxDD `-9.0959`
- `market_context_high->equity_1h` score `0.0412` n `205` status `ready` deltaP `5.8135` edge `0.0612` maxDD `-5.0555`
- `market_context_high->fx_24h` score `-0.0403` n `177` status `ready` deltaP `8.0067` edge `0.0328` maxDD `-0.8294`
- `market_context_high->index_1h` score `-0.1277` n `205` status `ready` deltaP `4.0792` edge `0.0115` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.2221` n `205` status `ready` deltaP `3.4263` edge `0.0832` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.2854` n `205` status `ready` deltaP `1.1808` edge `0.0645` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4244` n `205` status `ready` deltaP `-0.6543` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5981` n `205` status `ready` deltaP `0.8814` edge `0.0118` maxDD `-2.0682`
- `market_context_high->index_4h` score `-1.0819` n `201` status `ready` deltaP `4.4215` edge `0.0225` maxDD `-2.704`
- `market_context_high->fx_4h` score `-1.1035` n `201` status `ready` deltaP `1.3894` edge `0.0017` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.4859` n `201` status `ready` deltaP `7.5772` edge `-0.0559` maxDD `-6.1421`
- `market_context_high->commodity_1h` score `-1.5034` n `205` status `ready` deltaP `-3.6198` edge `-0.0067` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.7158` n `201` status `ready` deltaP `-7.9845` edge `-0.0425` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.4288` n `177` status `ready` deltaP `12.9179` edge `0.344` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
