# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T09:07:26.643288+00:00`
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

- `market_context_high->equity_4h` score `1.8429` n `96` status `ready` deltaP `9.9339` edge `0.1762` maxDD `-2.4411`
- `market_context_high->equity_1h` score `0.6134` n `103` status `ready` deltaP `9.809` edge `0.0507` maxDD `-2.5318`
- `market_context_high->metal_4h` score `0.4148` n `96` status `ready` deltaP `12.9065` edge `0.0061` maxDD `-1.273`
- `market_context_high->index_1h` score `0.3865` n `103` status `ready` deltaP `10.5619` edge `0.0052` maxDD `-0.4726`
- `market_context_high->index_4h` score `0.0975` n `96` status `ready` deltaP `7.9522` edge `0.0206` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.0134` n `96` status `ready` deltaP `5.5556` edge `0.148` maxDD `-4.666`
- `market_context_high->fx_4h` score `-0.0328` n `96` status `ready` deltaP `6.4278` edge `0.0032` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1813` n `103` status `ready` deltaP `1.311` edge `0.0039` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.1853` n `103` status `ready` deltaP `3.0987` edge `0.0026` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.2544` n `103` status `ready` deltaP `7.5635` edge `-0.0489` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.4166` n `103` status `ready` deltaP `1.4476` edge `0.0171` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.441` n `103` status `ready` deltaP `3.1713` edge `0.0068` maxDD `-2.7581`
- `market_context_high->unknown_24h` score `-0.6981` n `96` status `ready` deltaP `17.7083` edge `-0.1256` maxDD `-1.0505`
- `market_context_high->commodity_1h` score `-0.8158` n `103` status `ready` deltaP `-6.9138` edge `-0.0019` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.9052` n `96` status `ready` deltaP `-4.2937` edge `-0.0024` maxDD `-2.4692`
- `market_context_high->crypto_alt_4h` score `-2.2102` n `96` status `ready` deltaP `3.811` edge `-0.0826` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.5105` n `96` status `ready` deltaP `5.8181` edge `-0.1459` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.3788` n `96` status `ready` deltaP `-17.7083` edge `-0.0052` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7739` n `96` status `ready` deltaP `-0.5209` edge `-0.0636` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.5415` n `96` status `ready` deltaP `-17.7083` edge `-0.1334` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
