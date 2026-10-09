# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T05:37:28.057489+00:00`
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

- `market_context_high->unknown_4h` score `40.5616` n `91` status `ready` deltaP `-3.5965` edge `3.458` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `12.1852` n `33` status `ready` deltaP `43.4451` edge `0.7258` maxDD `0.0`
- `news_risk_high->equity_24h` score `10.4223` n `33` status `ready` deltaP `27.4621` edge `0.6954` maxDD `-0.1298`
- `news_risk_high->crypto_major_4h` score `10.4151` n `33` status `ready` deltaP `42.5674` edge `0.5909` maxDD `-0.2073`
- `market_context_high->crypto_major_24h` score `9.9574` n `90` status `ready` deltaP `22.3611` edge `1.4249` maxDD `-16.7906`
- `market_context_high->equity_24h` score `9.4817` n `90` status `ready` deltaP `30.6944` edge `0.6284` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.8058` n `33` status `ready` deltaP `51.5625` edge `0.2234` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.2035` n `33` status `ready` deltaP `31.153` edge `0.3298` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.6437` n `33` status `ready` deltaP `44.3782` edge `0.0956` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.5899` n `90` status `ready` deltaP `14.0625` edge `0.9603` maxDD `-34.5048`
- `news_risk_high->crypto_major_1h` score `2.9115` n `33` status `ready` deltaP `9.8939` edge `0.2122` maxDD `-1.5096`
- `news_risk_high->commodity_24h` score `2.6` n `33` status `ready` deltaP `27.2727` edge `0.0433` maxDD `-0.0096`
- `news_risk_high->index_1h` score `2.4602` n `33` status `ready` deltaP `29.5727` edge `0.0168` maxDD `-0.0484`
- `news_risk_high->crypto_alt_1h` score `2.2481` n `33` status `ready` deltaP `1.1024` edge `0.2117` maxDD `-1.2034`
- `market_context_high->crypto_major_4h` score `1.8441` n `91` status `ready` deltaP `17.8588` edge `0.2504` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.025` n `90` status `ready` deltaP `18.5416` edge `0.1563` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.3757` n `91` status `ready` deltaP `8.0444` edge `0.0019` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.3056` n `91` status `ready` deltaP `13.552` edge `0.0098` maxDD `-0.3077`
- `market_context_high->crypto_major_1h` score `0.2569` n `91` status `ready` deltaP `9.9938` edge `0.0552` maxDD `-3.7778`
- `news_risk_high->metal_4h` score `0.1985` n `33` status `ready` deltaP `8.5089` edge `0.0103` maxDD `-0.993`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
