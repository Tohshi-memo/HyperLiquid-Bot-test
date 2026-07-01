# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T15:07:31.282834+00:00`
- Price records: `672`
- Market context records: `5363`
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

- `market_context_high->unknown_24h` score `11.1395` n `171` status `ready` deltaP `17.087` edge `0.8274` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.0684` n `171` status `ready` deltaP `22.0943` edge `0.7291` maxDD `-29.6555`
- `market_context_high->equity_24h` score `3.5747` n `171` status `ready` deltaP `15.6707` edge `0.7563` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.1081` n `195` status `ready` deltaP `12.6329` edge `0.3207` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.6874` n `195` status `ready` deltaP `9.2097` edge `0.2433` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.4399` n `195` status `ready` deltaP `9.294` edge `0.2219` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.5246` n `171` status `ready` deltaP `18.4028` edge `0.1014` maxDD `-9.0959`
- `market_context_high->equity_1h` score `0.1695` n `205` status `ready` deltaP `6.2626` edge `0.0689` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.1439` n `171` status `ready` deltaP `9.8593` edge `0.0358` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.0262` n `205` status `ready` deltaP `4.3245` edge `0.0979` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.0083` n `205` status `ready` deltaP `1.9293` edge `0.0826` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.0954` n `205` status `ready` deltaP `4.3786` edge `0.0122` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.4493` n `205` status `ready` deltaP `-1.1034` edge `-0.0013` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5658` n `205` status `ready` deltaP `1.1808` edge `0.0125` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.637` n `195` status `ready` deltaP `5.6481` edge `0.0264` maxDD `-2.704`
- `market_context_high->fx_4h` score `-0.6497` n `195` status `ready` deltaP `2.4335` edge `0.0034` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.3748` n `195` status `ready` deltaP `7.4515` edge `-0.0458` maxDD `-6.1421`
- `market_context_high->commodity_1h` score `-1.5358` n `205` status `ready` deltaP `-3.9192` edge `-0.0074` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.8457` n `195` status `ready` deltaP `-8.8915` edge `-0.0531` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.6968` n `171` status `ready` deltaP `12.3538` edge `0.3134` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
