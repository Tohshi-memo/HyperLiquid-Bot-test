# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T01:22:26.328444+00:00`
- Price records: `672`
- Market context records: `5407`
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

- `market_context_high->crypto_major_24h` score `4.5528` n `194` status `ready` deltaP `20.6293` edge `0.6959` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.7245` n `205` status `ready` deltaP `16.1585` edge `0.4319` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9913` n `205` status `ready` deltaP `11.7683` edge `0.3349` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.3733` n `205` status `ready` deltaP `11.5854` edge `0.2844` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4368` n `205` status `ready` deltaP `7.7596` edge `0.0812` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.2108` n `205` status `ready` deltaP `5.3724` edge `0.1063` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.1295` n `205` status `ready` deltaP `2.9772` edge `0.0871` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0724` n `205` status `ready` deltaP `5.8756` edge `0.0162` maxDD `-0.9472`
- `market_context_high->equity_24h` score `-0.0128` n `194` status `ready` deltaP `8.0327` edge `0.5291` maxDD `-40.0306`
- `market_context_high->fx_24h` score `-0.1171` n `194` status `ready` deltaP `7.5118` edge `0.0297` maxDD `-0.8294`
- `market_context_high->fx_1h` score `-0.4633` n `205` status `ready` deltaP `-1.4028` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5406` n `205` status `ready` deltaP `1.6299` edge `0.0116` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9361` n `205` status `ready` deltaP `6.7073` edge `0.0382` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2085` n `205` status `ready` deltaP `0.0915` edge `0.0016` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4591` n `205` status `ready` deltaP `-3.021` edge `-0.007` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6175` n `194` status `ready` deltaP `12.8275` edge `0.0783` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.485` n `205` status `ready` deltaP `-5.9147` edge `-0.0267` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3252` n `205` status `ready` deltaP `-7.5914` edge `-0.046` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-5.5395` n `194` status `ready` deltaP `11.8932` edge `0.3288` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-6.9915` n `194` status `ready` deltaP `-4.4226` edge `-0.1291` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
