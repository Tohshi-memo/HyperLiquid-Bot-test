# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T23:22:25.765012+00:00`
- Price records: `672`
- Market context records: `5398`
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

- `market_context_high->crypto_major_24h` score `5.0527` n `194` status `ready` deltaP `22.0182` edge `0.7283` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.6039` n `205` status `ready` deltaP `15.7012` edge `0.4249` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9529` n `205` status `ready` deltaP `11.7683` edge `0.3317` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.3247` n `205` status `ready` deltaP `11.1281` edge `0.2834` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.456` n `205` status `ready` deltaP `7.7596` edge `0.0828` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1353` n `205` status `ready` deltaP `5.073` edge `0.102` maxDD `-6.9639`
- `market_context_high->equity_24h` score `0.1084` n `194` status `ready` deltaP `8.0327` edge `0.5392` maxDD `-40.0306`
- `market_context_high->crypto_alt_1h` score `0.0756` n `205` status `ready` deltaP `2.6778` edge `0.0846` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0436` n `205` status `ready` deltaP `5.5762` edge `0.0158` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.1683` n `194` status `ready` deltaP `6.991` edge `0.0289` maxDD `-0.8294`
- `market_context_high->metal_1h` score `-0.4484` n `205` status `ready` deltaP `2.3784` edge `0.0143` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4726` n `205` status `ready` deltaP `-1.5525` edge `-0.0013` maxDD `-0.5823`
- `market_context_high->index_4h` score `-1.0321` n `205` status `ready` deltaP `5.7926` edge `0.0363` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1951` n `205` status `ready` deltaP `0.2439` edge `0.0017` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4783` n `205` status `ready` deltaP `-3.3204` edge `-0.0066` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6835` n `194` status `ready` deltaP `12.8275` edge `0.0728` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.444` n `205` status `ready` deltaP `-5.4573` edge `-0.0245` maxDD `-12.8631`
- `market_context_high->unknown_24h` score `-3.9937` n `194` status `ready` deltaP `17.0569` edge `-0.4335` maxDD `-0.3748`
- `market_context_high->commodity_4h` score `-4.3192` n `205` status `ready` deltaP `-7.5914` edge `-0.0455` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-4.9424` n `194` status `ready` deltaP `13.2821` edge `0.3693` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
