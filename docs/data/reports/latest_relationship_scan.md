# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T11:07:26.065233+00:00`
- Price records: `672`
- Market context records: `5765`
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

- `market_context_high->equity_24h` score `0.7187` n `228` status `ready` deltaP `15.3052` edge `0.498` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1397` n `285` status `ready` deltaP `7.2759` edge `0.127` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2267` n `297` status `ready` deltaP `2.675` edge `0.0012` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4164` n `297` status `ready` deltaP `2.2254` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6522` n `297` status `ready` deltaP `-0.0569` edge `0.0036` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6592` n `297` status `ready` deltaP `2.8595` edge `0.0267` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7867` n `297` status `ready` deltaP `-2.1508` edge `-0.0058` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-0.907` n `228` status `ready` deltaP `14.9488` edge `0.0424` maxDD `-3.6674`
- `market_context_high->crypto_major_1h` score `-0.9423` n `297` status `ready` deltaP `3.1614` edge `0.0325` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.095` n `297` status `ready` deltaP `1.8141` edge `0.0301` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1806` n `285` status `ready` deltaP `0.9863` edge `0.0108` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2358` n `285` status `ready` deltaP `3.014` edge `0.006` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.5922` n `285` status `ready` deltaP `-7.0523` edge `-0.049` maxDD `-11.5722`
- `market_context_high->crypto_major_4h` score `-2.7118` n `285` status `ready` deltaP `7.8198` edge `0.1538` maxDD `-25.2202`
- `market_context_high->index_24h` score `-2.929` n `228` status `ready` deltaP `1.4619` edge `0.0292` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7321` n `285` status `ready` deltaP `-2.3636` edge `-0.0277` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.9219` n `285` status `ready` deltaP `6.3099` edge `0.107` maxDD `-26.7377`
- `market_context_high->crypto_major_24h` score `-5.121` n `228` status `ready` deltaP `5.4368` edge `-0.0173` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.4288` n `228` status `ready` deltaP `-8.9638` edge `-0.2466` maxDD `-29.3511`
- `market_context_high->commodity_24h` score `-11.365` n `228` status `ready` deltaP `-13.0574` edge `-0.0815` maxDD `-42.6163`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
