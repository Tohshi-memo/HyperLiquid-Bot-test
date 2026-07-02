# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T01:52:31.410240+00:00`
- Price records: `672`
- Market context records: `5409`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11492`

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

- `market_context_high->crypto_major_24h` score `4.3702` n `194` status `ready` deltaP `20.282` edge `0.683` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.8137` n `205` status `ready` deltaP `16.4634` edge `0.4373` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.0685` n `205` status `ready` deltaP `12.0732` edge `0.3393` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.4096` n `205` status `ready` deltaP `11.8903` edge `0.2854` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.3841` n `205` status `ready` deltaP `7.4602` edge `0.0788` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1664` n `205` status `ready` deltaP `5.2227` edge `0.1036` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.0851` n `205` status `ready` deltaP `2.8275` edge `0.0844` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0652` n `205` status `ready` deltaP `5.8756` edge `0.0156` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.0857` n `194` status `ready` deltaP `7.8591` edge `0.03` maxDD `-0.8294`
- `market_context_high->equity_24h` score `-0.0968` n `194` status `ready` deltaP `8.0327` edge `0.5221` maxDD `-40.0306`
- `market_context_high->fx_1h` score `-0.4633` n `205` status `ready` deltaP `-1.4028` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5598` n `205` status `ready` deltaP `1.4802` edge `0.011` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9349` n `205` status `ready` deltaP `6.7073` edge `0.0383` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2365` n `205` status `ready` deltaP `-0.2134` edge `0.0013` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4316` n `205` status `ready` deltaP `-2.7216` edge `-0.0067` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6199` n `194` status `ready` deltaP `12.8275` edge `0.0781` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.4904` n `205` status `ready` deltaP `-5.9147` edge `-0.0274` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2961` n `205` status `ready` deltaP `-7.2866` edge `-0.0456` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-5.7521` n `194` status `ready` deltaP `11.546` edge `0.3134` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.0087` n `194` status `ready` deltaP `-4.4226` edge `-0.1313` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
