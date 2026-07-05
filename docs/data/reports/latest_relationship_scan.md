# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T10:49:49.349898+00:00`
- Price records: `672`
- Market context records: `5763`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8668`

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

- `market_context_high->equity_24h` score `0.7241` n `228` status `ready` deltaP `15.3052` edge `0.4987` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1409` n `285` status `ready` deltaP `7.2759` edge `0.1271` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.208` n `297` status `ready` deltaP `3.049` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.6568` n `297` status `ready` deltaP `2.0384` edge `-0.0008` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6628` n `297` status `ready` deltaP `2.8595` edge `0.0264` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7859` n `297` status `ready` deltaP `-2.1508` edge `-0.0057` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-0.9055` n `228` status `ready` deltaP `14.9488` edge `0.0426` maxDD `-3.6674`
- `market_context_high->crypto_major_1h` score `-0.9387` n `297` status `ready` deltaP `3.1614` edge `0.0328` maxDD `-6.2348`
- `market_context_high->index_1h` score `-1.0022` n `297` status `ready` deltaP `-0.0569` edge `0.0037` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-1.0926` n `297` status `ready` deltaP `1.8141` edge `0.0303` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1695` n `285` status `ready` deltaP `1.1848` edge `0.0109` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2255` n `285` status `ready` deltaP `3.2124` edge `0.006` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6081` n `285` status `ready` deltaP `-7.2508` edge `-0.0492` maxDD `-11.6132`
- `market_context_high->crypto_major_4h` score `-2.6882` n `285` status `ready` deltaP `8.0183` edge `0.1542` maxDD `-25.2003`
- `market_context_high->index_24h` score `-2.9275` n `228` status `ready` deltaP `1.4619` edge `0.0294` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7297` n `285` status `ready` deltaP `-2.3636` edge `-0.0275` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.8468` n `285` status `ready` deltaP `6.5084` edge `0.1089` maxDD `-26.4952`
- `market_context_high->crypto_major_24h` score `-5.077` n `228` status `ready` deltaP `5.7018` edge `-0.0154` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.5368` n `228` status `ready` deltaP `-9.2288` edge `-0.2482` maxDD `-29.8556`
- `market_context_high->commodity_24h` score `-11.4899` n `228` status `ready` deltaP `-13.0574` edge `-0.0825` maxDD `-43.0353`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
