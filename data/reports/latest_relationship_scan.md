# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T23:22:21.831091+00:00`
- Price records: `672`
- Market context records: `3226`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->crypto_alt_24h` score `13.9132` n `102` status `ready` deltaP `19.0563` edge `2.6466` maxDD `-70.5257`
- `market_context_high->commodity_24h` score `13.8862` n `102` status `ready` deltaP `49.5609` edge `0.8696` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.7648` n `102` status `ready` deltaP `32.547` edge `0.8522` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.488` n `102` status `ready` deltaP `19.1278` edge `1.5459` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.1043` n `128` status `ready` deltaP `20.9985` edge `0.1645` maxDD `-1.9973`
- `market_context_high->crypto_major_24h` score `1.4423` n `102` status `ready` deltaP `21.4563` edge `2.1521` maxDD `-154.4856`
- `market_context_high->commodity_1h` score `0.2534` n `140` status `ready` deltaP `5.9795` edge `0.0238` maxDD `-1.7371`
- `market_context_high->crypto_alt_1h` score `-0.6841` n `140` status `ready` deltaP `4.3884` edge `0.1085` maxDD `-14.7034`
- `market_context_high->crypto_major_1h` score `-0.7105` n `140` status `ready` deltaP `4.5594` edge `0.1048` maxDD `-15.1032`
- `market_context_high->unknown_4h` score `-0.7417` n `128` status `ready` deltaP `8.2317` edge `0.0766` maxDD `-15.1257`
- `market_context_high->index_1h` score `-0.877` n `140` status `ready` deltaP `3.3747` edge `0.0107` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.9065` n `140` status `ready` deltaP `4.3199` edge `0.0119` maxDD `-8.8863`
- `market_context_high->fx_24h` score `-1.1598` n `102` status `ready` deltaP `-2.5531` edge `-0.0173` maxDD `-1.8164`
- `market_context_high->index_4h` score `-1.4118` n `128` status `ready` deltaP `9.6609` edge `0.0455` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.8442` n `140` status `ready` deltaP `-11.775` edge `-0.0057` maxDD `-0.8922`
- `market_context_high->fx_4h` score `-2.1451` n `128` status `ready` deltaP `-11.6235` edge `-0.0115` maxDD `-1.5151`
- `market_context_high->metal_1h` score `-2.3984` n `140` status `ready` deltaP `-4.5509` edge `-0.02` maxDD `-8.2956`
- `market_context_high->unknown_1h` score `-2.8429` n `140` status `ready` deltaP `2.0873` edge `-0.1305` maxDD `-17.8311`
- `market_context_high->equity_4h` score `-3.4751` n `128` status `ready` deltaP `10.8804` edge `0.0125` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-4.4038` n `128` status `ready` deltaP `7.6792` edge `0.1887` maxDD `-58.6918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
