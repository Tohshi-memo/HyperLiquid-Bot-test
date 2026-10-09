# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T03:52:32.330830+00:00`
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

- `market_context_high->unknown_4h` score `40.0192` n `91` status `ready` deltaP `-3.5965` edge `3.4128` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.3192` n `40` status `ready` deltaP `43.4451` edge `0.8203` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `12.2255` n `40` status `ready` deltaP `43.628` edge `0.7347` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.9712` n `40` status `ready` deltaP `28.3681` edge `0.7351` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.7916` n `90` status `ready` deltaP `22.1875` edge `1.4048` maxDD `-16.7906`
- `market_context_high->equity_24h` score `9.0437` n `90` status `ready` deltaP `29.4792` edge `0.6` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.8802` n `40` status `ready` deltaP `50.3472` edge `0.2377` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.1436` n `40` status `ready` deltaP `32.7439` edge `0.3142` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5769` n `40` status `ready` deltaP `44.9085` edge `0.0865` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.639` n `40` status `ready` deltaP `15.9581` edge `0.2324` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `3.506` n `90` status `ready` deltaP `13.8889` edge `0.9507` maxDD `-34.5048`
- `news_risk_high->index_1h` score `2.7243` n `40` status `ready` deltaP `32.7545` edge `0.0176` maxDD `-0.0484`
- `news_risk_high->crypto_alt_1h` score `2.4616` n `40` status `ready` deltaP `4.2066` edge `0.2088` maxDD `-1.2034`
- `news_risk_high->commodity_24h` score `2.2528` n `40` status `ready` deltaP `28.3333` edge `0.0073` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.8051` n `91` status `ready` deltaP `17.8588` edge `0.2454` maxDD `-6.9761`
- `news_risk_high->metal_4h` score `1.4433` n `40` status `ready` deltaP `16.4634` edge `0.0521` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.1147` n `90` status `ready` deltaP `19.7569` edge `0.1597` maxDD `-3.5466`
- `news_risk_high->metal_1h` score `0.8969` n `40` status `ready` deltaP `11.7515` edge `0.0269` maxDD `-0.44`
- `market_context_high->fx_1h` score `0.4128` n `91` status `ready` deltaP `8.4935` edge `0.002` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.3652` n `91` status `ready` deltaP `14.1618` edge `0.0107` maxDD `-0.3077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
