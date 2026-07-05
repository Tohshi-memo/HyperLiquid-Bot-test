# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T12:07:29.310922+00:00`
- Price records: `672`
- Market context records: `5769`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8674`

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

- `market_context_high->equity_24h` score `0.6929` n `228` status `ready` deltaP `15.3052` edge `0.4947` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1592` n `285` status `ready` deltaP `7.4743` edge `0.1273` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2372` n `297` status `ready` deltaP `2.488` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4059` n `297` status `ready` deltaP `2.4124` edge `-0.0006` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6232` n `297` status `ready` deltaP `3.2335` edge `0.0272` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6417` n `297` status `ready` deltaP `0.1301` edge `0.0037` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.7946` n `297` status `ready` deltaP `-2.3378` edge `-0.0058` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9069` n `297` status `ready` deltaP `3.3484` edge `0.0342` maxDD `-6.2348`
- `market_context_high->fx_24h` score `-0.9109` n `228` status `ready` deltaP `14.9488` edge `0.0419` maxDD `-3.6674`
- `market_context_high->crypto_alt_1h` score `-1.1076` n `297` status `ready` deltaP `1.6271` edge `0.0303` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1917` n `285` status `ready` deltaP `0.7879` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2358` n `285` status `ready` deltaP `3.014` edge `0.006` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.5426` n `285` status `ready` deltaP `-6.2586` edge `-0.0483` maxDD `-11.5426`
- `market_context_high->crypto_major_4h` score `-2.7718` n `285` status `ready` deltaP `7.8198` edge `0.154` maxDD `-25.6362`
- `market_context_high->index_24h` score `-2.9314` n `228` status `ready` deltaP `1.4619` edge `0.0289` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7858` n `285` status `ready` deltaP `-2.959` edge `-0.0282` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-4.291` n `285` status `ready` deltaP `5.5162` edge `0.1016` maxDD `-28.3433`
- `market_context_high->crypto_major_24h` score `-5.2618` n `228` status `ready` deltaP `5.1718` edge `-0.0231` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.0256` n `228` status `ready` deltaP `-7.9039` edge `-0.2411` maxDD `-27.5543`
- `market_context_high->commodity_24h` score `-10.8176` n `228` status `ready` deltaP `-13.0574` edge `-0.0768` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
