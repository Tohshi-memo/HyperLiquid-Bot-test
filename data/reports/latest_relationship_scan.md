# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T20:52:29.084329+00:00`
- Price records: `672`
- Market context records: `5702`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8856`

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

- `market_context_high->crypto_major_4h` score `2.1258` n `261` status `ready` deltaP `12.4766` edge `0.2311` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.1112` n `211` status `ready` deltaP `16.4783` edge `0.5405` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.9513` n `261` status `ready` deltaP `9.8069` edge `0.1748` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.2166` n `261` status `ready` deltaP `6.7376` edge `0.137` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2641` n `273` status `ready` deltaP `2.0147` edge `0.0008` maxDD `-0.5144`
- `market_context_high->crypto_major_1h` score `-0.2891` n `273` status `ready` deltaP `3.8303` edge `0.0418` maxDD `-3.9811`
- `market_context_high->crypto_alt_1h` score `-0.4432` n `273` status `ready` deltaP `2.1677` edge `0.0388` maxDD `-3.8812`
- `market_context_high->metal_1h` score `-0.4457` n `273` status `ready` deltaP `1.6166` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5508` n `273` status `ready` deltaP `3.8687` edge `0.029` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6084` n `273` status `ready` deltaP `0.6515` edge `0.0045` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-1.005` n `211` status `ready` deltaP `12.3667` edge `0.0445` maxDD `-3.4629`
- `market_context_high->commodity_1h` score `-1.0844` n `273` status `ready` deltaP `-0.8171` edge `-0.0042` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2123` n `261` status `ready` deltaP `3.2567` edge `0.0063` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.3119` n `261` status `ready` deltaP `-1.0898` edge `0.0078` maxDD `-3.165`
- `market_context_high->metal_4h` score `-2.7091` n `261` status `ready` deltaP `-8.7527` edge `-0.0514` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8856` n `211` status `ready` deltaP `2.3721` edge `0.0275` maxDD `-18.0608`
- `market_context_high->commodity_4h` score `-3.9571` n `261` status `ready` deltaP `-4.381` edge `-0.033` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.0209` n `211` status `ready` deltaP `6.4228` edge `0.0678` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.009` n `211` status `ready` deltaP `-8.3827` edge `-0.2433` maxDD `-32.5421`
- `market_context_high->commodity_24h` score `-12.17` n `211` status `ready` deltaP `-11.3958` edge `-0.0773` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
