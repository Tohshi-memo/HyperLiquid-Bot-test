# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T07:22:37.863592+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10797`

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

- `market_context_high->equity_4h` score `1.7536` n `96` status `ready` deltaP `9.4766` edge `0.1718` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7181` n `96` status `ready` deltaP `14.4025` edge `0.0773` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.854` n `96` status `ready` deltaP `15.0137` edge `0.0098` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.3018` n `96` status `ready` deltaP `11.8394` edge `0.0038` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.0674` n `96` status `ready` deltaP `6.25` edge `0.1503` maxDD `-4.666`
- `market_context_high->index_4h` score `0.0135` n `96` status `ready` deltaP `7.0376` edge `0.0197` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0107` n `96` status `ready` deltaP `7.19` edge `0.0037` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `-0.1415` n `96` status `ready` deltaP `5.4641` edge `-0.0255` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.1867` n `96` status `ready` deltaP `2.9753` edge `0.0033` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3463` n `96` status `ready` deltaP `-1.6218` edge `0.0023` maxDD `-0.2043`
- `market_context_high->unknown_24h` score `-0.5337` n `96` status `ready` deltaP `17.7083` edge `-0.1119` maxDD `-1.0505`
- `market_context_high->commodity_4h` score `-0.8186` n `96` status `ready` deltaP `-3.2266` edge `0.0016` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.829` n `96` status `ready` deltaP `-0.1684` edge `-0.025` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.893` n `96` status `ready` deltaP `1.7839` edge `-0.0419` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9593` n `96` status `ready` deltaP `-8.9384` edge `-0.0068` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.9608` n `96` status `ready` deltaP `4.5732` edge `-0.0669` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.1179` n `96` status `ready` deltaP `6.8851` edge `-0.1203` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.2552` n `96` status `ready` deltaP `-16.493` edge `-0.003` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.8146` n `96` status `ready` deltaP `-0.8681` edge `-0.0665` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.3762` n `96` status `ready` deltaP `-16.4931` edge `-0.1203` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
