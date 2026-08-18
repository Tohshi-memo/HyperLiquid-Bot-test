# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T14:07:37.269233+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11630`

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

- `market_context_high->crypto_major_24h` score `2.3266` n `89` status `ready` deltaP `8.9206` edge `0.2552` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.7034` n `89` status `ready` deltaP `18.6318` edge `0.2775` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.148` n `96` status `ready` deltaP `10.0612` edge `0.059` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.7031` n `96` status `ready` deltaP `14.126` edge `0.022` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6743` n `96` status `ready` deltaP `13.0676` edge `0.0078` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5568` n `96` status `ready` deltaP `9.506` edge `0.0057` maxDD `-0.4807`
- `market_context_high->crypto_major_4h` score `0.5318` n `96` status `ready` deltaP `8.8668` edge `0.0873` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `0.1886` n `96` status `ready` deltaP `9.4512` edge `0.0797` maxDD `-5.4926`
- `market_context_high->equity_4h` score `0.0999` n `96` status `ready` deltaP `2.9217` edge `0.0793` maxDD `-2.5696`
- `market_context_high->metal_1h` score `-0.0561` n `96` status `ready` deltaP `3.8735` edge `0.0082` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.2068` n `96` status `ready` deltaP `3.5315` edge `0.0002` maxDD `-0.3539`
- `market_context_high->commodity_4h` score `-0.3774` n `96` status `ready` deltaP `3.938` edge `0.0104` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.3792` n `96` status `ready` deltaP `2.0771` edge `0.0177` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4709` n `96` status `ready` deltaP `-3.8673` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4873` n `96` status `ready` deltaP `1.1851` edge `0.0141` maxDD `-2.7581`
- `market_context_high->unknown_24h` score `-0.4883` n `89` status `ready` deltaP `10.4454` edge `-0.0888` maxDD `-0.3891`
- `market_context_high->index_4h` score `-0.6383` n `96` status `ready` deltaP `0.3303` edge `0.0101` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8845` n `96` status `ready` deltaP `-7.5911` edge `-0.0062` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.299` n `89` status `ready` deltaP `-8.1125` edge `0.0163` maxDD `-7.8901`
- `market_context_high->fx_24h` score `-4.6127` n `89` status `ready` deltaP `-30.7402` edge `-0.0302` maxDD `-1.2737`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
