# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T01:07:31.512729+00:00`
- Price records: `672`
- Market context records: `5096`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `20.3622` n `79` status `ready` deltaP `27.7206` edge `1.5463` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.5913` n `115` status `ready` deltaP `4.9037` edge `0.7474` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `8.2679` n `103` status `ready` deltaP `21.5561` edge `0.6475` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.5566` n `103` status `ready` deltaP `14.0451` edge `0.446` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.3875` n `103` status `ready` deltaP `13.0743` edge `0.4463` maxDD `-13.8566`
- `market_context_high->equity_4h` score `2.0627` n `103` status `ready` deltaP `12.4408` edge `0.2021` maxDD `-6.3852`
- `market_context_high->equity_1h` score `0.5407` n `115` status `ready` deltaP `9.5795` edge `0.0596` maxDD `-2.6644`
- `market_context_high->crypto_alt_1h` score `0.4516` n `115` status `ready` deltaP `6.3082` edge `0.112` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.3516` n `115` status `ready` deltaP `6.9929` edge `0.123` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.3258` n `115` status `ready` deltaP `9.1239` edge `0.0306` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.2019` n `103` status `ready` deltaP `8.7896` edge `0.0434` maxDD `-1.0893`
- `market_context_high->index_1h` score `-0.042` n `115` status `ready` deltaP `5.082` edge `0.0111` maxDD `-1.0296`
- `market_context_high->metal_4h` score `-0.2054` n `103` status `ready` deltaP `4.4326` edge `0.0718` maxDD `-3.5485`
- `market_context_high->commodity_1h` score `-1.0067` n `115` status `ready` deltaP `-0.9477` edge `-0.0018` maxDD `-2.062`
- `market_context_high->fx_1h` score `-1.5036` n `115` status `ready` deltaP `-8.7451` edge `-0.0029` maxDD `-0.7944`
- `market_context_high->fx_24h` score `-1.5455` n `79` status `ready` deltaP `-2.9689` edge `-0.0078` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.6737` n `79` status `ready` deltaP `7.7004` edge `0.0303` maxDD `-15.0303`
- `market_context_high->commodity_4h` score `-1.7801` n `103` status `ready` deltaP `4.0152` edge `-0.0223` maxDD `-6.8914`
- `market_context_high->fx_4h` score `-2.1293` n `103` status `ready` deltaP `-9.1271` edge `-0.0093` maxDD `-1.9169`
- `market_context_high->metal_24h` score `-4.5168` n `79` status `ready` deltaP `-6.5995` edge `0.0104` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
