# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T17:22:28.579953+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8829`

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

- `market_context_high->equity_4h` score `2.4101` n `96` status `ready` deltaP `12.3729` edge `0.2072` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8896` n `96` status `ready` deltaP `15.4504` edge `0.0846` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9618` n `96` status `ready` deltaP `16.2113` edge `0.0108` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.7139` n `96` status `ready` deltaP `15.0406` edge `0.0168` maxDD `-1.273`
- `market_context_high->crypto_major_24h` score `0.6143` n `96` status `ready` deltaP `4.1666` edge `0.1442` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.3989` n `96` status `ready` deltaP `7.4653` edge `0.1847` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.3228` n `96` status `ready` deltaP `18.2291` edge `-0.044` maxDD `-1.0505`
- `market_context_high->index_4h` score `0.1932` n `96` status `ready` deltaP `8.7144` edge `0.0235` maxDD `-0.5728`
- `market_context_high->unknown_1h` score `0.1293` n `96` status `ready` deltaP `7.5599` edge `-0.0169` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.0874` n `96` status `ready` deltaP `8.4095` edge `0.0054` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0729` n `96` status `ready` deltaP `4.0232` edge `0.0058` maxDD `-0.4291`
- `market_context_high->crypto_major_4h` score `-0.2996` n `96` status `ready` deltaP `8.1046` edge `0.0231` maxDD `-3.1677`
- `market_context_high->fx_1h` score `-0.3276` n `96` status `ready` deltaP `-1.3224` edge `0.0027` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.6466` n `96` status `ready` deltaP `0.7298` edge `-0.0076` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6489` n `96` status `ready` deltaP `2.233` edge `-0.0136` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.6863` n `96` status `ready` deltaP `-0.7876` edge `0.0023` maxDD `-2.4692`
- `market_context_high->crypto_alt_4h` score `-0.8575` n `96` status `ready` deltaP `5.9451` edge `0.0159` maxDD `-5.4926`
- `market_context_high->commodity_1h` score `-0.9188` n `96` status `ready` deltaP `-8.0402` edge `-0.0076` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.6577` n `96` status `ready` deltaP `-6.7708` edge `0.0352` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.633` n `96` status `ready` deltaP `-19.7916` edge `-0.0125` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
