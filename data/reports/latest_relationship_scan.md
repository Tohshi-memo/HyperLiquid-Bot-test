# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T03:37:37.352336+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8896`

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

- `market_context_high->unknown_4h` score `39.9472` n `91` status `ready` deltaP `-3.5965` edge `3.4068` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.6816` n `41` status `ready` deltaP `43.4451` edge `0.8505` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `12.6397` n `41` status `ready` deltaP `43.75` edge `0.7684` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `11.026` n `41` status `ready` deltaP `28.4383` edge `0.7392` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.7444` n `90` status `ready` deltaP `22.0139` edge `1.3999` maxDD `-16.7906`
- `market_context_high->equity_24h` score `8.9782` n `90` status `ready` deltaP `29.3055` edge `0.5957` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.8891` n `41` status `ready` deltaP `50.1736` edge `0.2396` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.1726` n `41` status `ready` deltaP `32.9268` edge `0.3154` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5806` n `41` status `ready` deltaP `44.9695` edge `0.0864` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.7887` n `41` status `ready` deltaP `16.6898` edge `0.24` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `3.4681` n `90` status `ready` deltaP `13.7153` edge `0.947` maxDD `-34.5048`
- `news_risk_high->index_1h` score `2.7608` n `41` status `ready` deltaP `33.1204` edge `0.0182` maxDD `-0.0484`
- `news_risk_high->crypto_alt_1h` score `2.7017` n `41` status `ready` deltaP `5.2432` edge `0.2219` maxDD `-1.2034`
- `news_risk_high->commodity_24h` score `2.2398` n `41` status `ready` deltaP `28.4553` edge `0.0054` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.7903` n `91` status `ready` deltaP `17.8588` edge `0.2435` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.1261` n `90` status `ready` deltaP `19.9305` edge `0.16` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.0411` n `41` status `ready` deltaP `17.378` edge `0.0592` maxDD `-0.993`
- `news_risk_high->metal_1h` score `0.6415` n `41` status `ready` deltaP `12.6661` edge `0.0283` maxDD `-0.44`
- `market_context_high->fx_1h` score `0.414` n `91` status `ready` deltaP `8.4935` edge `0.0021` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.3786` n `91` status `ready` deltaP `14.3142` edge `0.0108` maxDD `-0.3077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
