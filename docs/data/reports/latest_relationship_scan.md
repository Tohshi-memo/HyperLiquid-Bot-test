# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T12:37:26.305882+00:00`
- Price records: `672`
- Market context records: `3178`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8856`

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

- `market_context_high->commodity_24h` score `13.9363` n `101` status `ready` deltaP `47.2171` edge `0.8894` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.3673` n `101` status `ready` deltaP `20.6116` edge `0.942` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.3251` n `101` status `ready` deltaP `13.717` edge `2.3581` maxDD `-71.142`
- `market_context_high->index_24h` score `6.1742` n `101` status `ready` deltaP `29.2216` edge `0.8522` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.2967` n `101` status `ready` deltaP `12.2817` edge `1.3106` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.121` n `134` status `ready` deltaP `19.8125` edge `0.1738` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.7222` n `101` status `ready` deltaP `12.0067` edge `0.0029` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.5756` n `134` status `ready` deltaP `11.2031` edge `0.1955` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3516` n `140` status `ready` deltaP `5.9795` edge `0.0317` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3509` n `140` status `ready` deltaP `6.1634` edge `0.0202` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.4361` n `140` status `ready` deltaP `6.2318` edge `0.1155` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.8734` n `134` status `ready` deltaP `16.2336` edge `0.0707` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0446` n `140` status `ready` deltaP `3.4303` edge `0.0695` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2562` n `140` status `ready` deltaP `4.3199` edge `0.0151` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3378` n `134` status `ready` deltaP `-11.4352` edge `-0.0068` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.5749` n `140` status `ready` deltaP `-8.6185` edge `-0.0051` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.0786` n `140` status `ready` deltaP `-3.8024` edge `-0.0085` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.2321` n `134` status `ready` deltaP `17.5078` edge `0.4016` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.0572` n `140` status `ready` deltaP `2.9513` edge `-0.0718` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.66` n `134` status `ready` deltaP `10.4455` edge `0.2535` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
