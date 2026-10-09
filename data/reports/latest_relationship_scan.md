# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T05:22:29.914865+00:00`
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

- `market_context_high->unknown_4h` score `40.4548` n `91` status `ready` deltaP `-3.5965` edge `3.4491` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `12.2608` n `34` status `ready` deltaP `43.4451` edge `0.7321` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `10.6166` n `34` status `ready` deltaP `42.7456` edge `0.6065` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.4813` n `34` status `ready` deltaP `27.645` edge `0.6991` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.9434` n `90` status `ready` deltaP `22.3611` edge `1.4231` maxDD `-16.7906`
- `market_context_high->equity_24h` score `9.427` n `90` status `ready` deltaP `30.5208` edge `0.625` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.8159` n `34` status `ready` deltaP `51.3889` edge `0.2254` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.1697` n `34` status `ready` deltaP `31.4204` edge `0.3252` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.6328` n `34` status `ready` deltaP `44.4673` edge `0.0941` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.5813` n `90` status `ready` deltaP `14.0625` edge `0.9592` maxDD `-34.5048`
- `news_risk_high->crypto_major_1h` score `3.0258` n `34` status `ready` deltaP `10.9634` edge `0.2146` maxDD `-1.5096`
- `news_risk_high->commodity_24h` score `2.5554` n `34` status `ready` deltaP `27.4509` edge `0.0384` maxDD `-0.0096`
- `news_risk_high->index_1h` score `2.5017` n `34` status `ready` deltaP `30.1074` edge `0.0167` maxDD `-0.0484`
- `news_risk_high->crypto_alt_1h` score `2.0429` n `34` status `ready` deltaP `-0.3522` edge `0.2043` maxDD `-1.2034`
- `market_context_high->crypto_major_4h` score `1.8449` n `91` status `ready` deltaP `17.8588` edge `0.2505` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.0411` n `90` status `ready` deltaP `18.7152` edge `0.1572` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `0.4375` n `34` status `ready` deltaP `9.8458` edge `0.0124` maxDD `-0.993`
- `market_context_high->fx_1h` score `0.3889` n `91` status `ready` deltaP `8.1941` edge `0.002` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.3202` n `91` status `ready` deltaP `13.7045` edge `0.01` maxDD `-0.3077`
- `market_context_high->crypto_major_1h` score `0.2585` n `91` status `ready` deltaP `9.9938` edge `0.0554` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
