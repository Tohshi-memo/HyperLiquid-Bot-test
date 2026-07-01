# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T20:22:31.131514+00:00`
- Price records: `672`
- Market context records: `5384`
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

- `market_context_high->unknown_24h` score `6.4328` n `187` status `ready` deltaP `16.9025` edge `0.4364` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.4451` n `187` status `ready` deltaP `22.9631` edge `0.7547` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.478` n `205` status `ready` deltaP `14.7866` edge `0.4205` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9723` n `205` status `ready` deltaP `11.9207` edge `0.3323` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.2355` n `205` status `ready` deltaP `10.8232` edge `0.278` maxDD `-7.4425`
- `market_context_high->equity_24h` score `1.7754` n `187` status `ready` deltaP `10.9849` edge `0.6376` maxDD `-40.0306`
- `market_context_high->equity_1h` score `0.3673` n `205` status `ready` deltaP `7.1608` edge `0.0794` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.0574` n `205` status `ready` deltaP `4.4742` edge `0.0995` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.0492` n `205` status `ready` deltaP `2.3784` edge `0.0844` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0149` n `205` status `ready` deltaP `5.2768` edge `0.0154` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.1919` n `187` status `ready` deltaP `6.561` edge `0.0298` maxDD `-0.8294`
- `market_context_high->unknown_4h` score `-0.3569` n `205` status `ready` deltaP `8.4451` edge `0.0324` maxDD `-6.1421`
- `market_context_high->fx_1h` score `-0.4485` n `205` status `ready` deltaP `-1.1034` edge `-0.0012` maxDD `-0.5823`
- `market_context_high->index_24h` score `-0.4593` n `187` status `ready` deltaP `15.3938` edge `0.0853` maxDD `-9.0959`
- `market_context_high->metal_1h` score `-0.4879` n `205` status `ready` deltaP `1.9293` edge `0.014` maxDD `-2.0682`
- `market_context_high->index_4h` score `-1.0563` n `205` status `ready` deltaP `5.6402` edge `0.0353` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2047` n `205` status `ready` deltaP `0.2439` edge `0.0009` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.5058` n `205` status `ready` deltaP `-3.6198` edge `-0.0069` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.4511` n `205` status `ready` deltaP `-5.4573` edge `-0.0254` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.148` n `187` status `ready` deltaP `13.8026` edge `0.3741` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
