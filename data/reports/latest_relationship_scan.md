# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T11:22:29.420573+00:00`
- Price records: `672`
- Market context records: `5766`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8670`

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

- `market_context_high->equity_24h` score `0.7163` n `228` status `ready` deltaP `15.3052` edge `0.4977` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.158` n `285` status `ready` deltaP `7.4743` edge `0.1272` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2372` n `297` status `ready` deltaP `2.488` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4164` n `297` status `ready` deltaP `2.2254` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6406` n `297` status `ready` deltaP `3.0465` edge `0.027` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6522` n `297` status `ready` deltaP `-0.0569` edge `0.0036` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.7972` n `297` status `ready` deltaP `-2.3378` edge `-0.0059` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-0.9078` n `228` status `ready` deltaP `14.9488` edge `0.0423` maxDD `-3.6674`
- `market_context_high->crypto_major_1h` score `-0.9213` n `297` status `ready` deltaP `3.3484` edge `0.033` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0938` n `297` status `ready` deltaP `1.8141` edge `0.0302` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1909` n `285` status `ready` deltaP `0.7879` edge `0.0108` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2469` n `285` status `ready` deltaP `2.8156` edge `0.0059` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.5782` n `285` status `ready` deltaP `-6.8539` edge `-0.0489` maxDD `-11.5426`
- `market_context_high->crypto_major_4h` score `-2.7124` n `285` status `ready` deltaP `7.8198` edge `0.1541` maxDD `-25.2477`
- `market_context_high->index_24h` score `-2.929` n `228` status `ready` deltaP `1.4619` edge `0.0292` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7333` n `285` status `ready` deltaP `-2.3636` edge `-0.0278` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.9795` n `285` status `ready` deltaP `6.1115` edge `0.106` maxDD `-26.936`
- `market_context_high->crypto_major_24h` score `-5.127` n `228` status `ready` deltaP `5.4368` edge `-0.0178` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.318` n `228` status `ready` deltaP `-8.6989` edge `-0.2451` maxDD `-28.8087`
- `market_context_high->commodity_24h` score `-11.2456` n `228` status `ready` deltaP `-13.0574` edge `-0.0805` maxDD `-42.2332`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
