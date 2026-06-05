# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T18:22:32.838089+00:00`
- Price records: `672`
- Market context records: `2993`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `17.3905` n `98` status `ready` deltaP `5.637` edge `1.8033` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.2222` n `98` status `ready` deltaP `42.2938` edge `0.7476` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.5248` n `98` status `ready` deltaP `17.8749` edge `0.8877` maxDD `-1.7175`
- `market_context_high->equity_24h` score `8.1464` n `98` status `ready` deltaP `16.61` edge `0.7685` maxDD `-12.6963`
- `market_context_high->index_24h` score `5.0858` n `98` status `ready` deltaP `16.3939` edge `0.4126` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.0859` n `100` status `ready` deltaP `14.8171` edge `0.2212` maxDD `-2.6927`
- `market_context_high->commodity_4h` score `2.3546` n `100` status `ready` deltaP `17.3598` edge `0.1452` maxDD `-2.8438`
- `market_context_high->index_4h` score `2.3402` n `100` status `ready` deltaP `19.372` edge `0.1447` maxDD `-1.9733`
- `market_context_high->crypto_alt_4h` score `0.9041` n `100` status `ready` deltaP `23.7561` edge `0.4157` maxDD `-30.9862`
- `market_context_high->index_1h` score `-0.0199` n `105` status `ready` deltaP `5.2381` edge `0.0227` maxDD `-2.4087`
- `market_context_high->commodity_1h` score `-0.0489` n `105` status `ready` deltaP `1.0337` edge `0.0198` maxDD `-0.9706`
- `market_context_high->equity_1h` score `-0.3571` n `105` status `ready` deltaP `3.5501` edge `0.0312` maxDD `-5.0523`
- `market_context_high->fx_1h` score `-0.3756` n `105` status `ready` deltaP `-2.4765` edge `0.0006` maxDD `-0.2466`
- `market_context_high->unknown_4h` score `-1.0152` n `100` status `ready` deltaP `0.1707` edge `0.0196` maxDD `-3.7602`
- `market_context_high->fx_4h` score `-1.0598` n `100` status `ready` deltaP `-9.0` edge `0.002` maxDD `-0.5631`
- `market_context_high->crypto_alt_1h` score `-1.0772` n `105` status `ready` deltaP `6.1905` edge `0.0179` maxDD `-13.4485`
- `market_context_high->metal_1h` score `-1.1774` n `105` status `ready` deltaP `-2.448` edge `-0.0113` maxDD `-6.1992`
- `market_context_high->crypto_major_1h` score `-1.5339` n `105` status `ready` deltaP `3.7696` edge `-0.0099` maxDD `-14.2845`
- `market_context_high->unknown_1h` score `-1.876` n `105` status `ready` deltaP `1.0878` edge `-0.0905` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.9478` n `98` status `ready` deltaP `-7.1747` edge `-0.0273` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
