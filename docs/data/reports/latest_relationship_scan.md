# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T21:07:33.407871+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8972`

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

- `market_context_high->unknown_24h` score `1380.7809` n `40` status `ready` deltaP `-22.5694` edge `115.2519` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `50.2795` n `93` status `ready` deltaP `-3.493` edge `4.2713` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.7936` n `40` status `ready` deltaP `27.6736` edge `0.5912` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4036` n `40` status `ready` deltaP `52.4306` edge `0.1841` maxDD `0.0`
- `market_context_high->unknown_1h` score `5.2001` n `105` status `ready` deltaP `-3.5457` edge `0.4906` maxDD `-1.0231`
- `market_context_high->fx_24h` score `3.1015` n `40` status `ready` deltaP `35.2083` edge `0.0367` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.3972` n `40` status `ready` deltaP `-21.1111` edge `0.572` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.8428` n `93` status `ready` deltaP `13.6343` edge `0.0077` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.5695` n `93` status `ready` deltaP `12.5836` edge `0.0169` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.326` n `105` status `ready` deltaP `7.2641` edge `0.0071` maxDD `-0.6025`
- `market_context_high->crypto_alt_1h` score `0.2781` n `105` status `ready` deltaP `6.3117` edge `0.097` maxDD `-4.9401`
- `market_context_high->metal_4h` score `0.2054` n `93` status `ready` deltaP `10.079` edge `0.0222` maxDD `-1.1153`
- `market_context_high->crypto_major_4h` score `0.1393` n `93` status `ready` deltaP `1.4277` edge `0.2189` maxDD `-11.1784`
- `market_context_high->fx_1h` score `0.0152` n `105` status `ready` deltaP `3.6584` edge `0.0011` maxDD `-0.271`
- `market_context_high->crypto_alt_4h` score `-0.0465` n `93` status `ready` deltaP `-0.9622` edge `0.2563` maxDD `-13.8008`
- `market_context_high->metal_1h` score `-0.0514` n `105` status `ready` deltaP `7.6048` edge `0.0039` maxDD `-0.7107`
- `market_context_high->crypto_major_1h` score `-0.252` n `105` status `ready` deltaP `0.1768` edge `0.0554` maxDD `-3.7778`
- `market_context_high->index_4h` score `-0.489` n `93` status `ready` deltaP `0.0967` edge `0.0067` maxDD `-0.9364`
- `market_context_high->index_1h` score `-0.7419` n `105` status `ready` deltaP `-4.3271` edge `-0.0012` maxDD `-0.5392`
- `market_context_high->equity_1h` score `-0.9293` n `105` status `ready` deltaP `-5.3079` edge `0.0032` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
