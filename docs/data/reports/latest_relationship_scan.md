# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T07:52:23.874288+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10800`

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
- `market_context_high->equity_1h` score `1.5301` n `98` status `ready` deltaP `12.9781` edge `0.0717` maxDD `-0.457`
- `market_context_high->index_1h` score `0.7326` n `98` status `ready` deltaP `13.6319` edge `0.0089` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.3334` n `96` status `ready` deltaP `12.1443` edge `0.0044` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.0423` n `96` status `ready` deltaP `5.9028` edge `0.1494` maxDD `-4.666`
- `market_context_high->index_4h` score `0.0257` n `96` status `ready` deltaP `7.19` edge `0.0197` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0028` n `96` status `ready` deltaP `7.0376` edge `0.0037` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `-0.1918` n `98` status `ready` deltaP `5.93` edge `-0.0328` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.1926` n `98` status `ready` deltaP `1.8911` edge `0.0014` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.2919` n `98` status `ready` deltaP `-0.666` edge `0.0029` maxDD `-0.2043`
- `market_context_high->unknown_24h` score `-0.5781` n `96` status `ready` deltaP `17.7083` edge `-0.1156` maxDD `-1.0505`
- `market_context_high->crypto_alt_1h` score `-0.8378` n `98` status `ready` deltaP `-0.3819` edge `-0.0247` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.8453` n `96` status `ready` deltaP `-3.5315` edge `0.0002` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9015` n `98` status `ready` deltaP `-8.0685` edge `-0.0052` maxDD `-1.1941`
- `market_context_high->crypto_major_1h` score `-0.91` n `98` status `ready` deltaP `1.5917` edge `-0.0428` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.0164` n `96` status `ready` deltaP `4.2683` edge `-0.0695` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.2035` n `96` status `ready` deltaP `6.5803` edge `-0.1254` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.2877` n `96` status `ready` deltaP `-16.8402` edge `-0.0034` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.8115` n `96` status `ready` deltaP `-0.8681` edge `-0.0661` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.4254` n `96` status `ready` deltaP `-16.8403` edge `-0.1243` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
