# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T03:22:24.648836+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10829`

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

- `market_context_high->equity_4h` score `2.0579` n `96` status `ready` deltaP `11.001` edge `0.187` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8152` n `96` status `ready` deltaP `15.0013` edge `0.0814` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9558` n `96` status `ready` deltaP `16.2113` edge `0.0103` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.356` n `96` status `ready` deltaP `11.9918` edge `0.0073` maxDD `-1.273`
- `market_context_high->index_4h` score `0.1996` n `96` status `ready` deltaP `9.0193` edge `0.022` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.1381` n `96` status `ready` deltaP `6.4236` edge `0.1582` maxDD `-4.666`
- `market_context_high->fx_4h` score `-0.0003` n `96` status `ready` deltaP `7.0376` edge `0.0033` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.122` n `96` status `ready` deltaP `3.5741` edge `0.0047` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.1799` n `96` status `ready` deltaP `5.6138` edge `-0.0297` maxDD `-0.4843`
- `market_context_high->unknown_24h` score `-0.2613` n `96` status `ready` deltaP `17.7083` edge `-0.0892` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.3416` n `96` status `ready` deltaP `-1.4721` edge `0.0019` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.7059` n `96` status `ready` deltaP `-1.8546` edge `0.0069` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8049` n `96` status `ready` deltaP `-0.0187` edge `-0.0229` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.8711` n `96` status `ready` deltaP `1.7839` edge `-0.0391` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9499` n `96` status `ready` deltaP `-8.7887` edge `-0.0066` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-2.029` n `96` status `ready` deltaP `3.811` edge `-0.0675` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.1059` n `96` status `ready` deltaP `6.8851` edge `-0.1193` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.0911` n `96` status `ready` deltaP `-14.7569` edge `-0.0009` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.792` n `96` status `ready` deltaP `-0.8681` edge `-0.0636` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-3.8979` n `96` status `ready` deltaP `-13.7153` edge `-0.0775` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
