# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T06:22:28.771258+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8870`

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

- `market_context_high->unknown_4h` score `41.042` n `91` status `ready` deltaP `-3.2917` edge `3.496` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `11.7316` n `30` status `ready` deltaP `43.4451` edge `0.688` maxDD `0.0`
- `news_risk_high->equity_24h` score `10.1498` n `30` status `ready` deltaP `26.7709` edge `0.6773` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `10.0019` n `90` status `ready` deltaP `22.3611` edge `1.4306` maxDD `-16.7906`
- `news_risk_high->crypto_major_4h` score `9.925` n `30` status `ready` deltaP `41.9613` edge `0.5541` maxDD `-0.2073`
- `market_context_high->equity_24h` score `9.6266` n `90` status `ready` deltaP `31.2153` edge `0.637` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.7611` n `30` status `ready` deltaP `52.0833` edge `0.2162` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.2328` n `30` status `ready` deltaP `30.2439` edge `0.3383` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.6651` n `30` status `ready` deltaP `44.0752` edge `0.0994` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.6172` n `90` status `ready` deltaP `14.0625` edge `0.9638` maxDD `-34.5048`
- `news_risk_high->commodity_24h` score `2.7843` n `30` status `ready` deltaP `26.6666` edge `0.0627` maxDD `-0.0096`
- `news_risk_high->index_1h` score `2.3183` n `30` status `ready` deltaP `27.7545` edge `0.0171` maxDD `-0.0484`
- `market_context_high->crypto_major_4h` score `1.8535` n `91` status `ready` deltaP `17.8588` edge `0.2516` maxDD `-6.9761`
- `news_risk_high->crypto_major_1h` score `1.5658` n `30` status `ready` deltaP `6.2575` edge `0.1243` maxDD `-1.5096`
- `market_context_high->metal_24h` score `0.9722` n `90` status `ready` deltaP `18.0208` edge `0.153` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `0.958` n `30` status `ready` deltaP `-3.4431` edge `0.1345` maxDD `-1.2034`
- `market_context_high->fx_1h` score `0.3386` n `91` status `ready` deltaP `7.5953` edge `0.0018` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2897` n `91` status `ready` deltaP `9.9938` edge `0.0594` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.2606` n `91` status `ready` deltaP `13.0947` edge `0.0091` maxDD `-0.3077`
- `news_risk_high->metal_4h` score `-0.1112` n `30` status `ready` deltaP `3.9634` edge `0.0009` maxDD `-0.993`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
