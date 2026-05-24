# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T11:52:15.256978+00:00`
- Price records: `672`
- Market context records: `1733`
- Flow alert records: `6894`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8838`

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

- `market_context_high->metal_24h` score `6.8952` n `151` status `ready` deltaP `25.5448` edge `0.6469` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.7929` n `196` status `ready` deltaP `20.514` edge `0.5226` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `5.1143` n `151` status `ready` deltaP `16.3994` edge `0.8489` maxDD `-35.8966`
- `market_context_high->index_24h` score `4.2571` n `151` status `ready` deltaP `18.1948` edge `0.3563` maxDD `-4.1604`
- `market_context_high->crypto_major_4h` score `4.2532` n `196` status `ready` deltaP `22.1099` edge `0.4476` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.0845` n `196` status `ready` deltaP `13.7941` edge `0.3922` maxDD `-11.1695`
- `market_context_high->equity_4h` score `2.9753` n `196` status `ready` deltaP `15.9594` edge `0.251` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.3894` n `151` status `ready` deltaP `16.5837` edge `0.5784` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7189` n `196` status `ready` deltaP `7.2712` edge `0.1138` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.6125` n `196` status `ready` deltaP `9.4264` edge `0.0971` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `0.2986` n `151` status `ready` deltaP `22.0193` edge `1.059` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.1693` n `196` status `ready` deltaP `4.598` edge `0.0908` maxDD `-3.9211`
- `market_context_high->crypto_major_24h` score `0.0398` n `151` status `ready` deltaP `20.7304` edge `0.7237` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.0323` n `196` status `ready` deltaP `4.821` edge `0.0514` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.3437` n `196` status `ready` deltaP `2.4197` edge `0.0184` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.3661` n `196` status `ready` deltaP `11.3769` edge `0.1464` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5619` n `196` status `ready` deltaP `5.3465` edge `0.0259` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.649` n `196` status `ready` deltaP `-2.8168` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7259` n `151` status `ready` deltaP `5.7025` edge `0.0064` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-1.5132` n `196` status `ready` deltaP `1.387` edge `0.0116` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
