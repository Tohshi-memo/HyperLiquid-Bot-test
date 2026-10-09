# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T05:52:27.551784+00:00`
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

- `market_context_high->unknown_4h` score `40.6732` n `91` status `ready` deltaP `-3.5965` edge `3.4673` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `12.0808` n `32` status `ready` deltaP `43.4451` edge `0.7171` maxDD `0.0`
- `news_risk_high->equity_24h` score `10.3543` n `32` status `ready` deltaP `27.2569` edge `0.6911` maxDD `-0.1298`
- `news_risk_high->crypto_major_4h` score `10.2535` n `32` status `ready` deltaP `42.378` edge `0.5787` maxDD `-0.2073`
- `market_context_high->crypto_major_24h` score `9.973` n `90` status `ready` deltaP `22.3611` edge `1.4269` maxDD `-16.7906`
- `market_context_high->equity_24h` score `9.5328` n `90` status `ready` deltaP `30.868` edge `0.6315` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.7945` n `32` status `ready` deltaP `51.7361` edge `0.2213` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.2348` n `32` status `ready` deltaP `30.8689` edge `0.3343` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.6541` n `32` status `ready` deltaP `44.2835` edge `0.0971` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.5985` n `90` status `ready` deltaP `14.0625` edge `0.9614` maxDD `-34.5048`
- `news_risk_high->commodity_24h` score `2.6472` n `32` status `ready` deltaP `27.0833` edge `0.0485` maxDD `-0.0096`
- `news_risk_high->crypto_major_1h` score `2.6214` n `32` status `ready` deltaP `8.7575` edge `0.1956` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.4171` n `32` status `ready` deltaP `29.0045` edge `0.017` maxDD `-0.0484`
- `news_risk_high->crypto_alt_1h` score `2.0324` n `32` status `ready` deltaP `-0.3181` edge `0.2032` maxDD `-1.2034`
- `market_context_high->crypto_major_4h` score `1.848` n `91` status `ready` deltaP `17.8588` edge `0.2509` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.0074` n `90` status `ready` deltaP `18.368` edge `0.1552` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.3637` n `91` status `ready` deltaP `7.8947` edge `0.0019` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.291` n `91` status `ready` deltaP `13.3996` edge `0.0096` maxDD `-0.3077`
- `market_context_high->crypto_major_1h` score `0.2631` n `91` status `ready` deltaP `9.9938` edge `0.056` maxDD `-3.7778`
- `news_risk_high->metal_4h` score `0.0989` n `32` status `ready` deltaP `7.0884` edge `0.007` maxDD `-0.993`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
