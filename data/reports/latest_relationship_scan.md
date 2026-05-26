# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T03:07:17.709004+00:00`
- Price records: `672`
- Market context records: `1906`
- Flow alert records: `7385`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `market_context_high->crypto_alt_4h` score `7.6349` n `199` status `ready` deltaP `23.8808` edge `0.5915` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.0757` n `199` status `ready` deltaP `28.477` edge `0.5244` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.8863` n `199` status `ready` deltaP `17.3482` edge `0.4106` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.4947` n `199` status `ready` deltaP `14.8869` edge `0.2181` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.9871` n `185` status `ready` deltaP `16.9041` edge `0.2955` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.5206` n `185` status `ready` deltaP `13.0292` edge `0.5719` maxDD `-35.8966`
- `market_context_high->index_24h` score `1.2356` n `185` status `ready` deltaP `8.6102` edge `0.1684` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.6741` n `199` status `ready` deltaP `7.3933` edge `0.1055` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4801` n `199` status `ready` deltaP `10.2455` edge `0.0806` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.4751` n `199` status `ready` deltaP `6.805` edge `0.1056` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.2058` n `185` status `ready` deltaP `14.4539` edge `0.0257` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.058` n `199` status `ready` deltaP `5.2862` edge `0.0393` maxDD `-2.6836`
- `market_context_high->equity_24h` score `-0.3211` n `185` status `ready` deltaP `8.7875` edge `0.4045` maxDD `-33.1875`
- `market_context_high->metal_1h` score `-0.5343` n `199` status `ready` deltaP `6.2814` edge `0.0232` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6207` n `199` status `ready` deltaP `-2.6036` edge `0.001` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6637` n `199` status `ready` deltaP `-0.3054` edge `0.0099` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.718` n `199` status `ready` deltaP `11.9331` edge `0.1298` maxDD `-12.5349`
- `market_context_high->crypto_major_24h` score `-0.7427` n `185` status `ready` deltaP `16.9632` edge `0.6836` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-0.8502` n `199` status `ready` deltaP `-3.0572` edge `0.0002` maxDD `-1.1056`
- `market_context_high->unknown_1h` score `-0.8743` n `199` status `ready` deltaP `2.2395` edge `0.0074` maxDD `-3.6151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
