# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T03:52:30.803358+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->equity_24h` score `1.5671` n `80` status `ready` deltaP `2.7391` edge `1.0312` maxDD `-55.843`
- `market_context_high->commodity_24h` score `1.3171` n `80` status `ready` deltaP `14.2065` edge `0.1002` maxDD `-1.8119`
- `market_context_high->crypto_major_24h` score `1.0017` n `80` status `ready` deltaP `4.2014` edge `0.7101` maxDD `-35.1086`
- `risk_on_high->equity_1h` score `0.9384` n `47` status `ready` deltaP `16.4558` edge `0.0284` maxDD `-2.1255`
- `risk_on_and_context->equity_1h` score `0.9384` n `47` status `ready` deltaP `16.4558` edge `0.0284` maxDD `-2.1255`
- `market_context_high->crypto_major_4h` score `0.7286` n `80` status `ready` deltaP `7.1341` edge `0.3863` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.5264` n `81` status `ready` deltaP `5.5925` edge `0.1191` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.5111` n `47` status `ready` deltaP `10.8747` edge `0.0011` maxDD `-0.4804`
- `risk_on_and_context->index_1h` score `0.5111` n `47` status `ready` deltaP `10.8747` edge `0.0011` maxDD `-0.4804`
- `risk_on_high->fx_1h` score `-0.0277` n `47` status `ready` deltaP `4.7185` edge `0.0009` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.0277` n `47` status `ready` deltaP `4.7185` edge `0.0009` maxDD `-0.1065`
- `risk_on_high->commodity_24h` score `-0.164` n `47` status `ready` deltaP `11.0416` edge `-0.0075` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.164` n `47` status `ready` deltaP `11.0416` edge `-0.0075` maxDD `-1.7154`
- `risk_on_high->equity_4h` score `-0.3494` n `47` status `ready` deltaP `4.3269` edge `0.0988` maxDD `-6.5413`
- `risk_on_and_context->equity_4h` score `-0.3494` n `47` status `ready` deltaP `4.3269` edge `0.0988` maxDD `-6.5413`
- `risk_on_high->fx_4h` score `-0.3602` n `47` status `ready` deltaP `-1.0508` edge `0.0038` maxDD `-0.1446`
- `risk_on_and_context->fx_4h` score `-0.3602` n `47` status `ready` deltaP `-1.0508` edge `0.0038` maxDD `-0.1446`
- `market_context_high->fx_1h` score `-0.5436` n `81` status `ready` deltaP `-2.4525` edge `-0.0008` maxDD `-0.537`
- `market_context_high->fx_4h` score `-0.5444` n `80` status `ready` deltaP `-1.6093` edge `0.004` maxDD `-0.7115`
- `risk_on_high->index_4h` score `-0.6025` n `47` status `ready` deltaP `4.6197` edge `0.0086` maxDD `-1.1682`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
