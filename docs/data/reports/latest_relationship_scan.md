# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T05:07:33.264849+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8902`

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

- `market_context_high->unknown_4h` score `40.3408` n `91` status `ready` deltaP `-3.5965` edge `3.4396` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `12.3604` n `35` status `ready` deltaP `43.4451` edge `0.7404` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `10.8436` n `35` status `ready` deltaP `42.9137` edge `0.6243` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.5555` n `35` status `ready` deltaP `27.8075` edge `0.7042` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.9231` n `90` status `ready` deltaP `22.3611` edge `1.4205` maxDD `-16.7906`
- `market_context_high->equity_24h` score `9.3651` n `90` status `ready` deltaP `30.3472` edge `0.621` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.826` n `35` status `ready` deltaP `51.2153` edge `0.2274` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.1203` n `35` status `ready` deltaP `31.6725` edge `0.3194` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.6144` n `35` status `ready` deltaP `44.5514` edge `0.092` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.5719` n `90` status `ready` deltaP `14.0625` edge `0.958` maxDD `-34.5048`
- `news_risk_high->crypto_major_1h` score `3.1005` n `35` status `ready` deltaP `11.9718` edge `0.2141` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.5385` n `35` status `ready` deltaP `30.6116` edge `0.0164` maxDD `-0.0484`
- `news_risk_high->commodity_24h` score `2.5005` n `35` status `ready` deltaP `27.619` edge `0.0327` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.8433` n `91` status `ready` deltaP `17.8588` edge `0.2503` maxDD `-6.9761`
- `news_risk_high->crypto_alt_1h` score `1.8271` n `35` status `ready` deltaP `-1.7151` edge `0.1954` maxDD `-1.2034`
- `market_context_high->metal_24h` score `1.0555` n `90` status `ready` deltaP `18.8889` edge `0.1579` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `0.5768` n `35` status `ready` deltaP `11.1063` edge `0.0156` maxDD `-0.993`
- `market_context_high->fx_1h` score `0.3889` n `91` status `ready` deltaP `8.1941` edge `0.002` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.3336` n `91` status `ready` deltaP `13.8569` edge `0.0101` maxDD `-0.3077`
- `market_context_high->crypto_major_1h` score `0.2569` n `91` status `ready` deltaP `9.9938` edge `0.0552` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
