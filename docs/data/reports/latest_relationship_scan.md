# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T22:07:29.178632+00:00`
- Price records: `672`
- Market context records: `5392`
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

- `market_context_high->crypto_major_24h` score `5.3328` n `193` status `ready` deltaP `22.7287` edge `0.7469` maxDD `-29.6555`
- `market_context_high->unknown_24h` score `4.959` n `193` status `ready` deltaP `17.0355` edge `0.3127` maxDD `-0.3748`
- `market_context_high->crypto_major_4h` score `3.5637` n `205` status `ready` deltaP `15.2439` edge `0.4246` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.0484` n `205` status `ready` deltaP `12.3781` edge `0.3356` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.3415` n `205` status `ready` deltaP `11.1281` edge `0.2848` maxDD `-7.4425`
- `market_context_high->equity_24h` score `0.4239` n `193` status `ready` deltaP `8.4413` edge `0.5586` maxDD `-40.0306`
- `market_context_high->equity_1h` score `0.4129` n `205` status `ready` deltaP `7.4602` edge `0.0812` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.046` n `205` status `ready` deltaP `5.5762` edge `0.016` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `0.0322` n `205` status `ready` deltaP `4.4742` edge `0.0974` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.0012` n `205` status `ready` deltaP `2.2287` edge `0.0814` maxDD `-5.0257`
- `market_context_high->fx_24h` score `-0.1795` n `193` status `ready` deltaP `6.8815` edge `0.0287` maxDD `-0.8294`
- `market_context_high->metal_1h` score `-0.4484` n `205` status `ready` deltaP `2.3784` edge `0.0143` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4828` n `205` status `ready` deltaP `-1.7022` edge `-0.0016` maxDD `-0.5823`
- `market_context_high->unknown_4h` score `-0.5825` n `205` status `ready` deltaP `7.5305` edge `0.0197` maxDD `-6.1421`
- `market_context_high->index_4h` score `-1.0333` n `205` status `ready` deltaP `5.7926` edge `0.0362` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1987` n `205` status `ready` deltaP `0.2439` edge `0.0014` maxDD `-1.567`
- `market_context_high->index_24h` score `-1.5305` n `193` status `ready` deltaP `13.1827` edge `0.0728` maxDD `-12.0582`
- `market_context_high->commodity_1h` score `-1.5322` n `205` status `ready` deltaP `-3.9192` edge `-0.0071` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.4386` n `205` status `ready` deltaP `-5.4573` edge `-0.0238` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3204` n `205` status `ready` deltaP `-7.5914` edge `-0.0456` maxDD `-14.1062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
