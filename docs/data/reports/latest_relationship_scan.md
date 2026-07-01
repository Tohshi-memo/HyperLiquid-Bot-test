# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T19:07:34.982238+00:00`
- Price records: `672`
- Market context records: `5379`
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

- `market_context_high->unknown_24h` score `7.8442` n `182` status `ready` deltaP `16.785` edge `0.5548` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.4529` n `182` status `ready` deltaP `22.7907` edge `0.7565` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.2168` n `205` status `ready` deltaP `14.1768` edge `0.4028` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.6773` n `205` status `ready` deltaP `11.1585` edge `0.3128` maxDD `-9.46`
- `market_context_high->equity_24h` score `2.5418` n `182` status `ready` deltaP `12.8853` edge `0.6888` maxDD `-40.0306`
- `market_context_high->equity_4h` score `1.8769` n `205` status `ready` deltaP `10.061` edge `0.2532` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.1311` n `205` status `ready` deltaP `6.4123` edge `0.0647` maxDD `-5.0555`
- `market_context_high->index_24h` score `-0.0192` n `182` status `ready` deltaP `16.4797` edge `0.0939` maxDD `-9.0959`
- `market_context_high->index_1h` score `-0.0702` n `205` status `ready` deltaP `4.678` edge `0.0123` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.0983` n `182` status `ready` deltaP `7.4767` edge `0.0315` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `-0.1175` n `205` status `ready` deltaP `1.7796` edge `0.0745` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.1477` n `205` status `ready` deltaP `3.7257` edge `0.0874` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.4322` n `205` status `ready` deltaP `-0.804` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->unknown_4h` score `-0.5393` n `205` status `ready` deltaP `8.4451` edge `0.0172` maxDD `-6.1421`
- `market_context_high->metal_1h` score `-0.567` n `205` status `ready` deltaP `1.3305` edge `0.0114` maxDD `-2.0682`
- `market_context_high->index_4h` score `-1.1737` n `205` status `ready` deltaP `4.878` edge `0.0306` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1803` n `205` status `ready` deltaP `0.5488` edge `0.0009` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.5346` n `205` status `ready` deltaP `-3.9192` edge `-0.0073` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.5258` n `205` status `ready` deltaP `-6.2195` edge `-0.0299` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.228` n `182` status `ready` deltaP `13.4806` edge `0.366` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
