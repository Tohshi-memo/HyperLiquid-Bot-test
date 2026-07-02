# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T02:52:29.909479+00:00`
- Price records: `672`
- Market context records: `5413`
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

- `market_context_high->crypto_major_4h` score `3.9945` n `205` status `ready` deltaP `17.0732` edge `0.4483` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `3.9715` n `194` status `ready` deltaP `19.5876` edge `0.6544` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `3.195` n `205` status `ready` deltaP `12.5305` edge `0.3468` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.4798` n `205` status `ready` deltaP `12.3476` edge `0.2882` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.3817` n `205` status `ready` deltaP `7.4602` edge `0.0786` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0867` n `205` status `ready` deltaP `6.175` edge `0.0154` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `0.0801` n `205` status `ready` deltaP `4.6239` edge `0.1004` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.0024` n `205` status `ready` deltaP `2.2287` edge `0.0815` maxDD `-5.0257`
- `market_context_high->fx_24h` score `-0.0253` n `194` status `ready` deltaP `8.5535` edge `0.0304` maxDD `-0.8294`
- `market_context_high->equity_24h` score `-0.3296` n `194` status `ready` deltaP `8.0327` edge `0.5027` maxDD `-40.0306`
- `market_context_high->fx_1h` score `-0.4555` n `205` status `ready` deltaP `-1.2531` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.573` n `205` status `ready` deltaP `1.3305` edge `0.0109` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9325` n `205` status `ready` deltaP `6.7073` edge `0.0385` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2511` n `205` status `ready` deltaP `-0.3658` edge `0.0011` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4843` n `205` status `ready` deltaP `-3.3204` edge `-0.0071` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6415` n `194` status `ready` deltaP `12.8275` edge `0.0763` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.5283` n `205` status `ready` deltaP `-6.372` edge `-0.0292` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2511` n `205` status `ready` deltaP `-6.8292` edge `-0.0449` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.2228` n `194` status `ready` deltaP `10.8516` edge `0.2788` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.0766` n `194` status `ready` deltaP `-4.7698` edge `-0.1377` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
