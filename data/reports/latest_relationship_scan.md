# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T03:22:24.609187+00:00`
- Price records: `672`
- Market context records: `5840`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10126`

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

- `news_risk_high->fx_1h` score `1.9148` n `30` status `ready` deltaP `23.1836` edge `0.0189` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8277` n `30` status `ready` deltaP `11.2375` edge `0.0779` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7072` n `264` status `ready` deltaP `7.742` edge `0.1531` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.1819` n `30` status `ready` deltaP `4.5709` edge `0.039` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3289` n `264` status `ready` deltaP `0.9867` edge `-0.0002` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.3538` n `264` status `ready` deltaP `4.6362` edge `0.0403` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4219` n `30` status `ready` deltaP `1.3872` edge `-0.0267` maxDD `-1.2643`
- `market_context_high->index_1h` score `-0.5335` n `264` status `ready` deltaP `1.5424` edge `0.0061` maxDD `-0.7819`
- `market_context_high->commodity_1h` score `-0.5373` n `264` status `ready` deltaP `-1.023` edge `-0.0018` maxDD `-2.1545`
- `market_context_high->metal_1h` score `-0.5731` n `264` status `ready` deltaP `2.5994` edge `0.002` maxDD `-2.0339`
- `market_context_high->equity_24h` score `-0.5985` n `236` status `ready` deltaP `16.1282` edge `0.3505` maxDD `-31.6316`
- `market_context_high->crypto_major_1h` score `-0.9497` n `264` status `ready` deltaP `2.8284` edge `0.0341` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1435` n `264` status `ready` deltaP `1.3133` edge `0.0294` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1727` n `264` status `ready` deltaP `0.5682` edge `0.0146` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2253` n `30` status `ready` deltaP `-12.2455` edge `-0.024` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.6768` n `264` status `ready` deltaP `-2.7393` edge `-0.0018` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.6901` n `236` status `ready` deltaP `6.7973` edge `0.0198` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.1455` n `264` status `ready` deltaP `-4.8134` edge `-0.0426` maxDD `-8.6964`
- `market_context_high->commodity_4h` score `-2.5072` n `264` status `ready` deltaP `-0.6144` edge `-0.0144` maxDD `-7.9015`
- `market_context_high->index_24h` score `-2.9087` n `236` status `ready` deltaP `2.919` edge `0.0221` maxDD `-18.1572`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
