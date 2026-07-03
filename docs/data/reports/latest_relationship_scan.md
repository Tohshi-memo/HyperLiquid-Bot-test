# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T20:07:26.298048+00:00`
- Price records: `672`
- Market context records: `5591`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11423`

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

- `market_context_high->equity_24h` score `3.7915` n `174` status `ready` deltaP `15.0084` edge `0.7238` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.199` n `205` status `ready` deltaP `11.8902` edge `0.2499` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.0489` n `174` status `ready` deltaP `19.5283` edge `0.0546` maxDD `-1.457`
- `market_context_high->equity_4h` score `0.6187` n `205` status `ready` deltaP `6.7682` edge `0.1703` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.5275` n `205` status `ready` deltaP `6.9207` edge `0.1619` maxDD `-9.46`
- `market_context_high->crypto_major_24h` score `-0.0234` n `174` status `ready` deltaP `12.2366` edge `0.3705` maxDD `-29.6555`
- `market_context_high->equity_1h` score `-0.2051` n `217` status `ready` deltaP `5.7749` edge `0.0359` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.281` n `217` status `ready` deltaP `1.4984` edge `0.0008` maxDD `-0.4122`
- `market_context_high->index_1h` score `-0.3368` n `217` status `ready` deltaP `2.1558` edge `0.0069` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.4137` n `217` status `ready` deltaP `3.7674` edge `0.0464` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6012` n `217` status `ready` deltaP `-1.4632` edge `0.0002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6326` n `217` status `ready` deltaP `0.7851` edge `0.0382` maxDD `-5.0257`
- `market_context_high->fx_4h` score `-0.8757` n `205` status `ready` deltaP `3.811` edge `0.0087` maxDD `-0.9001`
- `market_context_high->commodity_1h` score `-1.1735` n `217` status `ready` deltaP `-2.062` edge `-0.0075` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.4986` n `205` status `ready` deltaP `3.2012` edge `0.0147` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.2479` n `174` status `ready` deltaP `11.1291` edge `0.0363` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9663` n `205` status `ready` deltaP `-12.5` edge `-0.0586` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1494` n `205` status `ready` deltaP `-4.9695` edge `-0.0451` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.013` n `174` status `ready` deltaP `-8.3273` edge `-0.2357` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-10.1223` n `174` status `ready` deltaP `2.0235` edge `0.0127` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
