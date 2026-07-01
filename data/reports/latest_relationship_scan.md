# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T17:52:29.957245+00:00`
- Price records: `672`
- Market context records: `5374`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11526`

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

- `market_context_high->unknown_24h` score `8.7859` n `179` status `ready` deltaP `17.0963` edge `0.6312` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.3375` n `179` status `ready` deltaP `22.2474` edge `0.7505` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.0596` n `205` status `ready` deltaP `14.1768` edge `0.3897` maxDD `-14.0065`
- `market_context_high->equity_24h` score `2.7999` n `179` status `ready` deltaP `13.4263` edge `0.7067` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `2.4127` n `205` status `ready` deltaP `10.7012` edge `0.2938` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.5291` n `205` status `ready` deltaP `9.2988` edge `0.2293` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.1689` n `179` status `ready` deltaP `16.8364` edge `0.0947` maxDD `-9.0959`
- `market_context_high->equity_1h` score `0.0735` n `205` status `ready` deltaP `6.1129` edge `0.0619` maxDD `-5.0555`
- `market_context_high->fx_24h` score `-0.0506` n `179` status `ready` deltaP `7.9531` edge `0.0323` maxDD `-0.8294`
- `market_context_high->index_1h` score `-0.1026` n `205` status `ready` deltaP `4.3786` edge `0.0116` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.1885` n `205` status `ready` deltaP `3.576` edge `0.085` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.2086` n `205` status `ready` deltaP `1.4802` edge `0.0689` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4322` n `205` status `ready` deltaP `-0.804` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.6173` n `205` status `ready` deltaP `0.8814` edge `0.0102` maxDD `-2.0682`
- `market_context_high->unknown_4h` score `-0.9453` n `205` status `ready` deltaP `8.1402` edge `-0.0146` maxDD `-6.1421`
- `market_context_high->fx_4h` score `-1.1779` n `205` status `ready` deltaP `0.5488` edge `0.0011` maxDD `-1.567`
- `market_context_high->index_4h` score `-1.3054` n `205` status `ready` deltaP `4.1158` edge `0.0247` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.519` n `205` status `ready` deltaP `-3.7695` edge `-0.007` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.6083` n `205` status `ready` deltaP `-6.9817` edge `-0.0354` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.3314` n `179` status `ready` deltaP `13.0819` edge `0.3554` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
